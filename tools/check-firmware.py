#!/usr/bin/env python3
"""Run regression tests and ESPHome builds in Docker with dummy credentials."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
IMAGE = "ghcr.io/esphome/esphome:2026.7.3"
CACHE = "water-kits-esphome-2026-7-3-platformio"
THREAD_DATASET = (
    "0e080000000000010000000300000f35060004001fffe002081122334455667788"
    "0708fd123456789abcde051000112233445566778899aabbccddeeff"
    "030e5761746572436865636b706f696e7401021234"
    "0410112233445566778899aabbccddeeff00"
)
SECRETS = """# Dummy credentials: generated only for local checks; do not flash.
wifi_ssid: DUMMY
wifi_password: DUMMYPASS
api_encryption_key: MDEyMzQ1Njc4OWFiY2RlZjAxMjM0NTY3ODlhYmNkZWY=
ota_password: DUMMYOTAPASS
fallback_ap_password: DUMMYFALLBACK
"""


def configuration_files(root):
    files = set(root.glob("*.yaml")) | set((root / "packages").glob("*.yaml"))
    for hardware in root.glob("*-v[0-9]*"):
        if hardware.is_dir():
            for directory, children, names in os.walk(hardware):
                children[:] = [name for name in children if name not in {".esphome", "__pycache__"}]
                files.update(Path(directory) / name for name in names if name.endswith(".yaml"))
    return sorted(p for p in files if p.name != "secrets.yaml"
                  and ".esphome" not in p.parts)


def stage_sources(root, stage):
    """Copy current YAML and tests, without reading developers' secrets."""
    sources = configuration_files(root)
    expected = {source.relative_to(root) for source in sources}
    # Keep compiler caches, but never let deleted YAML hide a broken include.
    for old in configuration_files(stage):
        if old.relative_to(stage) not in expected:
            old.unlink()
    for source in sources:
        if os.environ.get("SMK_BUILD_VERBOSE"):
            print(f"Copying {source}", flush=True)
        target = stage / source.relative_to(root)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(source.read_text().replace(
            "PASTE_YOUR_THREAD_DATASET_TLVS_HERE", THREAD_DATASET))
        # !secret is resolved beside the entrypoint, including nested tests.
        (target.parent / "secrets.yaml").write_text(SECRETS)
    test_sources = list((root / "tests").glob("*.py"))
    for old in (stage / "tests").glob("*.py"):
        if old.name not in {source.name for source in test_sources}:
            old.unlink()
    for source in test_sources:
        target = stage / "tests" / source.name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)


def entrypoints(root):
    product = "waterp1meterkit" if (root / "waterp1meterkit-v1").is_dir() else "watermeterkit"
    return [p.relative_to(root) for p in configuration_files(root)
            if p.name.startswith(product) or p.name == "api-encryption-size.yaml"]


def run_docker(stage, arguments, log, entrypoint=None):
    command = ["docker", "run", "--rm",
               "--mount", f"type=bind,source={stage},target=/config",
               "--mount", f"type=volume,source={CACHE},target=/root/.platformio",
               "--env", "PYTHONDONTWRITEBYTECODE=1",
               "--workdir", "/config"]
    if entrypoint:
        command.extend(["--entrypoint", entrypoint])
    command.extend([IMAGE, *arguments])
    print(f"Running {' '.join(arguments)} (log: {log})", flush=True)
    with log.open("w") as stream:
        result = subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT)
    if result.returncode:
        # Remove terminal escapes and download progress for a readable failure.
        output = re.sub(r"\x1b\[[0-?]*[ -/]*[@-~]", "", log.read_text(errors="replace"))
        print("\n".join(output.splitlines()[-35:]), file=sys.stderr)
    return result.returncode == 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("test", "validate", "build"), nargs="?", default="validate")
    parser.add_argument("configs", nargs="*", help="Repository-relative entrypoint YAMLs; default: all for validate, latest local variant for build")
    args = parser.parse_args()
    if args.action == "test" and args.configs:
        parser.error("test does not take configurations")
    available = entrypoints(ROOT)
    if args.configs:
        configs = []
        for name in args.configs:
            resolved = (ROOT / name).resolve()
            if resolved not in [(ROOT / p).resolve() for p in available]:
                parser.error(f"Unknown entrypoint: {name}")
            configs.append(resolved.relative_to(ROOT))
    elif args.action == "build":
        configs = [Path("waterp1meterkit-v4/waterp1meterkit-ethernet.yaml")
                   if (ROOT / "waterp1meterkit-v4").is_dir()
                   else Path("watermeterkit-v3/watermeterkit.yaml")]
    else:
        configs = available

    if not shutil.which("docker"):
        parser.exit(1, "Docker is required. Install/start Docker Desktop, then retry.\n")
    daemon = subprocess.run(["docker", "info"], capture_output=True)
    if daemon.returncode:
        parser.exit(1, "Docker is not running. Start Docker Desktop, then retry.\n")
    output = ROOT / ".local-build"
    # Docker's shared Documents filesystem can return EDEADLK while comparing
    # generated files. Keep the toolchain/build tree on the local temp volume.
    cache_key = hashlib.sha256(str(ROOT).encode()).hexdigest()[:12]
    stage = Path(tempfile.gettempdir()).resolve() / "smarthomeshop-firmware" / f"{ROOT.name}-{cache_key}"
    logs = output / "logs"
    logs.mkdir(parents=True, exist_ok=True)
    stage_sources(ROOT, stage)
    print(f"Using {IMAGE}; sources staged with dummy credentials in {stage}", flush=True)
    report = [{"check": "water persistence", "ok": run_docker(
        stage, ["-m", "unittest", "discover", "-s", "tests", "-v"],
        logs / "water-persistence.log", entrypoint="python3")}]
    if report[0]["ok"] and args.action != "test":
        # Hardware variants share build directories. Run them sequentially,
        # and copy each binary before the next variant overwrites it.
        for config in configs:
            key = str(config.with_suffix("")).replace("/", "__")
            command = ["compile"]
            if args.action == "validate":
                command.append("--only-generate")
            command.append(f"/config/{config.as_posix()}")
            ok = run_docker(stage, command, logs / f"{key}.log")
            artifacts = []
            if ok and args.action == "build":
                destination = output / "firmware" / key
                destination.mkdir(parents=True, exist_ok=True)
                for binary in (stage / config.parent / ".esphome" / "build").rglob("firmware*.bin"):
                    target = destination / binary.name
                    shutil.copyfile(binary, target)
                    artifacts.append(str(target.relative_to(ROOT)))
                if not artifacts:
                    ok = False
                    print(f"No firmware binary found for {config}", file=sys.stderr)
            report.append({"check": str(config), "ok": ok, "artifacts": artifacts})
            print(f"{'PASS' if ok else 'FAIL'} {config}", flush=True)
    report_json = json.dumps(report, indent=2) + "\n"
    (output / "report.json").write_text(report_json)
    (output / f"{args.action}-report.json").write_text(report_json)
    passed = sum(item["ok"] for item in report)
    print(f"{passed}/{len(report)} checks passed. Report: {output / 'report.json'}", flush=True)
    if args.action == "build":
        print("Test binaries contain dummy credentials; they are not deployment firmware.", flush=True)
    return 0 if all(item["ok"] for item in report) else 1


if __name__ == "__main__":
    sys.exit(main())
