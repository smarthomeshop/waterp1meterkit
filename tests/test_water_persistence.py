"""Execute the firmware's actual lambdas against buffered preferences.

Run with: python3 -m unittest discover -s tests
Requires a C++17 compiler, but no ESPHome installation or connected hardware.
"""

from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import textwrap
import unittest


ROOT = Path(__file__).resolve().parents[1]


def lambdas(source, spaces, list_item=True):
    prefix = "- " if list_item else ""
    body_spaces = spaces + (4 if list_item else 2)
    pattern = rf"^{' ' * spaces}{prefix}lambda: \|-\n((?:{' ' * body_spaces}[^\n]*\n|\n)+)"
    return [textwrap.dedent(body) for body in re.findall(pattern, source, re.M)]


class WaterPersistenceTests(unittest.TestCase):
    def test_checkpoint_calibration_and_reboot_for_every_hardware(self):
        compiler = shutil.which("clang++") or shutil.which("g++")
        self.assertIsNotNone(compiler, "Install a C++17 compiler to run these checks")
        package = (ROOT / "packages/water-persistence.yaml").read_text()
        checkpoint, = lambdas(package, 6)
        self.assertEqual(package.count("- script.execute: save_water_checkpoint"), 2)

        for base in sorted(ROOT.glob("*-v*/base.yaml")):
            with self.subTest(hardware=base.parent.name):
                source = base.read_text()
                self.assertIn("water_persistence: !include ../packages/water-persistence.yaml", source)
                expected = "30min" if "\nesp8266:\n" in source else "5min"
                self.assertIn(f'water_checkpoint_interval: "{expected}"', source)
                self.assertRegex(source, r"id: water_total_persistent\n\s+type: float\n\s+restore_value: true")
                self.assertNotIn("pulses_since_offset >= 0.05", source)
                self.assertIn("      on_value:\n        then:\n          - component.update: sensor_water_meter_total", source)
                calibration, = [body for body in lambdas(source, 8)
                                if "id(water_total_persistent) = x;" in body]
                reading, = [body for body in lambdas(source, 4, list_item=False)
                            if "float current_delta" in body]
                cpp = HARNESS.replace("CHECKPOINT_BODY", checkpoint)
                cpp = cpp.replace("CALIBRATION_BODY", calibration).replace("READING_BODY", reading)
                with tempfile.TemporaryDirectory() as directory:
                    path = Path(directory)
                    (path / "probe.cpp").write_text(cpp)
                    subprocess.run([compiler, "-std=c++17", "-Wall", "-Wextra", "-Werror",
                                    str(path / "probe.cpp"), "-o", str(path / "probe")], check=True)
                    subprocess.run([str(path / "probe")], check=True)


HARNESS = r"""
#include <cassert>
#include <cmath>
#include <limits>
using std::isnan;
#define ESP_LOGW(...) ((void)0)
#define ESP_LOGI(...) ((void)0)
#define ESP_LOGE(...) ((void)0)

struct Preferences {
  float disk = 0, buffer = 0;
  bool pending = false, fail = false;
  int calls = 0, writes = 0;
  bool sync() {
    ++calls;
    if (fail) return false;
    if (pending && buffer != disk) { disk = buffer; ++writes; }
    pending = false;
    return true;
  }
} prefs;
Preferences *global_preferences = &prefs;

struct RestoringGlobal {
  float value = 0, last = 0;
  void update() {
    if (value != last) {
      prefs.buffer = value; prefs.pending = true; last = value;
    }
  }
} persistent;
RestoringGlobal *water_total_persistent = &persistent;
struct Sensor {
  float state = 0;
  bool available = true;
  bool has_state() const { return available; }
  void update() {}
} pulses, meter;
float offset = 0;
float &test_id_water_total_persistent() { return persistent.value; }
float &test_id_water_pulse_offset() { return offset; }
Sensor &test_id_sensor_pulse_meter_total() { return pulses; }
Sensor &test_id_sensor_water_meter_total() { return meter; }
#define id(name) test_id_##name()

void checkpoint() { CHECKPOINT_BODY }
void calibrate(float x) { CALIBRATION_BODY }
float reading() { READING_BODY }
void reset(float stored) {
  prefs = {}; prefs.disk = stored;
  persistent = {stored, stored}; pulses = {}; meter = {}; offset = 0;
}
void close(float actual, float expected) {
  assert(std::fabs(actual - expected) < 0.00025f);
}

int main() {
  reset(1625.0f);
  pulses.state = 0.018f;
  close(reading(), 1625.018f); // first total update does not require flow
  checkpoint();
  close(prefs.disk, 1625.018f); // below the former 50-litre threshold
  assert(prefs.writes == 1);
  close(reading(), prefs.disk);
  const int calls = prefs.calls;
  checkpoint();
  assert(prefs.calls == calls && prefs.writes == 1); // idle saves nothing
  pulses.state = 0.022f;
  checkpoint();
  close(prefs.disk, 1625.022f); // only the four new litres, no double count
  assert(prefs.writes == 2);

  const float saved = prefs.disk;
  reset(saved); // unexpected reboot after successful checkpoint
  close(reading(), saved); // raw pulses start at zero, absolute total survives
  pulses.state = 0.004f;
  checkpoint(); // the clean-shutdown hook invokes this same synchronous code
  close(prefs.disk, saved + 0.004f);

  reset(1625.0f);
  pulses.state = 0.018f;
  calibrate(1700.0f);
  close(prefs.disk, 1700.0f); // flush the new global, not the old buffer
  close(reading(), 1700.0f);
  assert(prefs.writes == 1);
  checkpoint(); assert(prefs.writes == 1);
  pulses.state = 0.019f;
  checkpoint(); close(prefs.disk, 1700.001f);

  reset(1625.0f);
  pulses.available = false; calibrate(1700.0f);
  close(prefs.disk, 1700.0f); // calibration also works before the first pulse
  pulses.available = true; pulses.state = 0.001f;
  checkpoint(); close(prefs.disk, 1700.001f);

  reset(1625.0f);
  pulses.available = false; checkpoint(); assert(prefs.calls == 0);
  pulses.available = true;
  pulses.state = std::numeric_limits<float>::quiet_NaN();
  checkpoint(); assert(prefs.calls == 0);
  pulses.state = std::numeric_limits<float>::infinity();
  checkpoint(); assert(prefs.calls == 0);
  pulses.state = -1; checkpoint(); assert(prefs.calls == 0);

  reset(1625.0f); // interruption before a checkpoint still loses unsaved usage
  pulses.state = 0.018f;
  reset(prefs.disk); close(reading(), 1625.0f);
  pulses.state = 0.001f; prefs.fail = true;
  checkpoint(); close(prefs.disk, 1625.0f); // no false durability guarantee
}
"""


if __name__ == "__main__":
    unittest.main()
