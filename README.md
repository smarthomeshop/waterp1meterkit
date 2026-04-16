# WaterP1MeterKit for Home Assistant / ESPHome

![WaterP1MeterKit Logo](images/waterp1meterkit-logo.png)

WaterP1MeterKit combines P1 smart meter reading and water meter monitoring in a single ESPHome-based device for Home Assistant. It supports local operation, multiple hardware revisions, and WiFi or Ethernet connectivity depending on the hardware version.

Product page: https://waterp1meterkit.nl/en

## How It Works

The WaterP1MeterKit reads DSMR telegrams from the P1 port of your smart meter and pulse signals from a water meter sensor. That lets you track electricity, gas, and water with one device in Home Assistant.

## Key Features

- Combined P1 energy and water monitoring in one device
- Support for energy, gas, and water usage tracking
- Temperature and humidity monitoring with HDC1080
- WiFi and Ethernet firmware variants for all hardware revisions
- PoE support on V2 and V3
- Fully local operation with ESPHome and Home Assistant
- V3 expansion support for add-ons such as a water leak sensor or door sensor

## Hardware Versions

We publish firmware for three hardware revisions.

| Version | Chip | Connectivity | Description |
|---------|------|--------------|-------------|
| V1 | ESP32 | WiFi and Ethernet | Original combined P1 and water monitor with fixed water sensor |
| V2 | ESP32 | WiFi, Ethernet, and PoE | Updated hardware with PoE support |
| V3 | ESP32 | WiFi, Ethernet, and PoE | Detachable water sensor, expansion support, and improved precision |

See the README in each version folder for hardware-specific details.

## Variants

We publish customer-facing WiFi and Ethernet firmware for each hardware revision.

| Hardware | Variant | Description |
|----------|---------|-------------|
| V1 (ESP32) | WiFi | Standard WiFi connectivity |
| V1 (ESP32) | Ethernet | Wired Ethernet connectivity |
| V2 (ESP32) | WiFi | WiFi firmware for PoE-capable V2 hardware |
| V2 (ESP32) | Ethernet | Wired Ethernet firmware for PoE-capable V2 hardware |
| V3 (ESP32) | WiFi | WiFi firmware for detachable-sensor V3 hardware |
| V3 (ESP32) | Ethernet | Wired Ethernet firmware for detachable-sensor V3 hardware |

## Water Meter Total

WaterP1MeterKit stores an absolute water meter total so the reading survives reboots and firmware updates.

### Sensors

| Sensor | Description |
|--------|-------------|
| Water Total Consumption | Raw pulses since boot; suitable for Home Assistant Energy Dashboard |
| Water Meter Initial Value | Input value that matches the physical water meter reading |
| Water Meter Total | Initial value plus measured usage; represents the actual meter reading |

### First-Time Setup

1. Read the current value on your physical water meter.
2. Enter that value in `Water Meter Initial Value` in Home Assistant.
3. Use `Water Meter Total` as the absolute meter reading going forward.

### Save Behavior

The device batches writes to reduce flash wear while keeping the reading reliable.

| Trigger | When | Save behavior |
|---------|------|---------------|
| Interval check | Every 5 minutes | Saves only if at least 50 liters changed |
| Shutdown | OTA, restart, factory reset | Always saves |

| Scenario | Water Meter Total | Maximum loss |
|----------|-------------------|--------------|
| OTA firmware update | Saved before reboot | 0 L |
| Manual restart | Saved before reboot | 0 L |
| Factory reset | Saved before reset | 0 L |
| Sudden power loss | Unsaved recent usage may be lost | About 50 L |

## Getting Started

1. Connect power with USB-C, or use PoE on V2 and V3 where applicable.
2. Devices ship pre-flashed with WiFi firmware by default.
3. Complete onboarding through captive portal in the WiFi build.
4. If you want Ethernet, switch firmware later from Home Assistant.

Quick start guide: https://smarthomeshop.io/quick-start-waterp1meterkit

## Version History

- Customer-facing release notes: [CHANGELOG.md](CHANGELOG.md)
- GitHub Releases: https://github.com/smarthomeshop/waterp1meterkit/releases

## Repository Layout

```text
waterp1meterkit/
├── waterp1meterkit-v1/     # V1 ESPHome configurations
│   ├── base.yaml           # Shared configuration
│   ├── waterp1meterkit-wifi.yaml
│   └── waterp1meterkit-ethernet.yaml
├── waterp1meterkit-v2/     # V2 ESPHome configurations
│   ├── base.yaml
│   ├── waterp1meterkit-wifi.yaml
│   └── waterp1meterkit-ethernet.yaml
├── waterp1meterkit-v3/     # V3 ESPHome configurations
│   ├── base.yaml
│   ├── waterp1meterkit-wifi.yaml
│   └── waterp1meterkit-ethernet.yaml
├── .github/workflows/      # Build and release automation
├── CHANGELOG.md            # Customer-facing firmware notes
└── images/
```

## Firmware Downloads

Pre-built firmware manifests are published on the `gh-pages` branch.

- V1 WiFi: `waterp1meterkit-v1-wifi-manifest.json`
- V1 Ethernet: `waterp1meterkit-v1-ethernet-manifest.json`
- V2 WiFi: `waterp1meterkit-v2-wifi-manifest.json`
- V2 Ethernet: `waterp1meterkit-v2-ethernet-manifest.json`
- V3 WiFi: `waterp1meterkit-v3-wifi-manifest.json`
- V3 Ethernet: `waterp1meterkit-v3-ethernet-manifest.json`

## Contributing

PRs and issues are welcome. Please keep changes modular and follow ESPHome best practices.

## Support

- Product info and guides: https://waterp1meterkit.nl/en
- Store: https://smarthomeshop.io
- Community and support: https://smarthomeshop.io/discord

## License

This project is released under the MIT License. See [LICENSE](LICENSE).
