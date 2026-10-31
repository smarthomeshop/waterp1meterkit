"""The firmware selector must start on the variant that is actually running.

Its on_value runs on every boot and moves the update source to that variant,
so a wrong start value makes Home Assistant offer the wrong firmware.

Run with: python3 -m unittest discover -s tests
"""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "waterp1meterkit-wifi.yaml": "WiFi (local)",
    "waterp1meterkit-wifi-cloud.yaml": "WiFi + SmartHomeShop App (cloud)",
    "waterp1meterkit-ethernet.yaml": "Ethernet (local)",
    "waterp1meterkit-ethernet-cloud.yaml": "Ethernet + SmartHomeShop App (cloud)",
}


class FirmwareVariantTests(unittest.TestCase):
    def test_every_variant_starts_on_its_own_selector_option(self):
        for folder in sorted(ROOT.glob("waterp1meterkit-v*")):
            for name, option in EXPECTED.items():
                with self.subTest(firmware=f"{folder.name}/{name}"):
                    source = (folder / name).read_text()
                    self.assertEqual(re.findall(r'^  default_network: "(.+)"$', source, re.M), [option])


    def test_v4_ignores_stale_saved_variant_on_boot(self):
        source = (ROOT / "waterp1meterkit-v4/base.yaml").read_text()
        selector = source.split("select:\n", 1)[1].split("\nweb_server:", 1)[0]
        self.assertIn("id: firmware_selector", selector)
        self.assertRegex(selector, r"(?m)^    restore_value: false$")
        self.assertIn("initial_option: ${default_network}", selector)


if __name__ == "__main__":
    unittest.main()
