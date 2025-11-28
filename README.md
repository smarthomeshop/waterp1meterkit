# WaterP1MeterKit for Home Assistant / ESPHome

![WaterP1MeterKit Logo](images/waterp1meterkit-logo.png)

## 🌟 The Ultimate All-in-One Energy & Water Monitor

**WaterP1MeterKit** is the first and only solution that combines **P1 energy meter reading** and **water meter monitoring** in a single device — with support for **WiFi, Ethernet, and PoE**!

> 🎉 As the very first water meter kit ever made for Home Assistant, we are the best choice for measuring your water meter and/or energy meter. 100% local, open-source, and built for Home Assistant users!

### ⚡ What Makes Us Unique

| Feature | WaterP1MeterKit |
|---------|-----------------|
| 📊 **Dual Monitoring** | Measure **both P1 energy AND water** simultaneously — or choose just one |
| 🌐 **Triple Connectivity** | **WiFi**, **Ethernet**, and **PoE** support (V2+) |
| 🏠 **100% Local** | No cloud, no subscriptions — runs entirely on your Home Assistant |
| 🔌 **Single Device** | No need for separate energy and water monitors |

---

## Key Features

- **🔄 Flexible monitoring**: Choose to monitor **only energy**, **only water**, or **both at the same time** with a single kit!
- **⚡ P1 Energy monitoring**: Full DSMR support (2.2 - 5.0) — consumption, production, voltage, current, gas
- **💧 Water monitoring**: Real-time water flow (L/min) and total consumption (m³)
- **🌡️ Environment sensors**: Temperature and humidity monitoring (HDC1080)
- **🌐 WiFi + Ethernet + PoE**: Choose your preferred connectivity (PoE on V2+)
- **🔒 Fully local**: No cloud required — works offline with Home Assistant
- **📦 Pre-flashed**: Comes ready to use with WiFi firmware out of the box
- **🔧 Expansion port**: V3 supports water leak sensor or door sensor add-ons

Learn more on our website: https://waterp1meterkit.nl/en

---

## Hardware Versions

We have 3 hardware versions, each with WiFi and Ethernet firmware variants:

| Feature | V1 | V2 | V3 |
|---------|----|----|-----|
| WiFi | ✅ | ✅ | ✅ |
| Ethernet | ✅ | ✅ | ✅ |
| **PoE** | ❌ | ✅ | ✅ |
| Water Sensor | Fixed | Fixed | **Detachable** |
| Expansion Port | ❌ | ❌ | ✅ |
| Improved Precision | - | - | ✅ |

See the README in each version folder for detailed specifications.

---

## Getting Started

1. **Hardware**: Connect power (USB-C or PoE for V2/V3)
2. **Connect**: All devices come **pre-flashed with WiFi firmware** out of the box
3. **Onboarding**: WiFi builds support captive portal for easy setup
4. **Switch to Ethernet**: After connecting to Home Assistant, you can easily switch to Ethernet firmware using a simple switch in the device settings

📺 **Installation videos** available on YouTube for popular water meters: Sensus, Itron, Actaris, Schlumberger, Elster, and Honeywell.

For full documentation see our quick start guide: https://smarthomeshop.io/quick-start-waterp1meterkit

---

## Repository Layout

```
waterp1meterkit/
├── waterp1meterkit-v1/     # V1 ESPHome configurations
│   ├── base.yaml           # Shared configuration
│   ├── waterp1meterkit-wifi.yaml
│   └── waterp1meterkit-ethernet.yaml
├── waterp1meterkit-v2/     # V2 ESPHome configurations (+ PoE)
│   ├── base.yaml
│   ├── waterp1meterkit-wifi.yaml
│   └── waterp1meterkit-ethernet.yaml
├── waterp1meterkit-v3/     # V3 ESPHome configurations (+ detachable sensor)
│   ├── base.yaml
│   ├── waterp1meterkit-wifi.yaml
│   └── waterp1meterkit-ethernet.yaml
├── .github/workflows/      # CI to build and publish firmware to gh-pages
└── images/
```

## Firmware Downloads

Pre-built firmware is available on the `gh-pages` branch:
- V1 WiFi: `waterp1meterkit-v1-wifi-manifest.json`
- V1 Ethernet: `waterp1meterkit-v1-ethernet-manifest.json`
- V2 WiFi: `waterp1meterkit-v2-wifi-manifest.json`
- V2 Ethernet: `waterp1meterkit-v2-ethernet-manifest.json`
- V3 WiFi: `waterp1meterkit-v3-wifi-manifest.json`
- V3 Ethernet: `waterp1meterkit-v3-ethernet-manifest.json`

## Contributing

PRs and issues are welcome. Please keep changes modular and follow ESPHome best practices.

## Support

- 🌐 Product info and guides: https://waterp1meterkit.nl/en
- 🛒 Store: https://smarthomeshop.io
- 💬 Community & support (Discord): https://smarthomeshop.io/discord

## License

This project is released under the MIT License (see `LICENSE`).
