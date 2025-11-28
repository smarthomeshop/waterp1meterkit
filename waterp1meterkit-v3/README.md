# WaterP1MeterKit V3

## Overview

The WaterP1MeterKit V3 is the most flexible and comprehensive version to date. It features a **detachable water sensor** with improved precision and a **new expansion port** for optional sensors like a water leak sensor or door sensor.

> 🎉 As the very first water meter kit ever made for Home Assistant, we are still the best choice for measuring your water meter and/or energy meter. Always focused on staying true to what the community values most: 100% local, open-source, and built for Home Assistant users!

## Features

- **Energy monitoring**: Reads data via the P1 port of DSMR-compatible energy meters
- **Water monitoring**: **Detachable water sensor with cable** for flexible installation and improved precision
- **Flexible setup**: Choose to monitor only energy, only water, or both with a single kit
- **Expansion Port**: Extra port for add-ons like a **water leak sensor** or **door sensor**
- **Connectivity**: WiFi, Ethernet, and Power over Ethernet (PoE) support
- **Temperature & Humidity**: Built-in HDC1080 sensor
- **Integration**: Fully integrated with Home Assistant via ESPHome

## Hardware Specifications

| Component | Specification |
|-----------|---------------|
| MCU | ESP32 |
| P1 Port | DSMR 2.2 - 5.0 compatible |
| Water Sensor | **Detachable with cable** |
| Expansion Port | For water leak sensor or door sensor |
| Network | WiFi, Ethernet (LAN8720), or PoE |
| PoE | ✅ Supported |
| Power | USB-C, P1 port, or PoE powered |
| LEDs | RGB status indication |

## Pin Configuration

- **UART RX (P1)**: GPIO16 (inverted)
- **P1 Request**: GPIO12
- **Water Pulse**: GPIO32
- **Expansion Port (Leak/Door)**: GPIO2
- **I²C SDA**: GPIO15
- **I²C SCL**: GPIO4
- **Ethernet Power**: GPIO33

## What's New in V3

- ✅ **Detachable water sensor with cable** - Easier placement and slightly improved precision
- ✅ **New expansion port** - Connect a water leak sensor or door sensor
- ✅ **Flexible monitoring** - Choose energy only, water only, or both
- ✅ Minor internal hardware refinements for smoother and more stable readings
- ✅ All V2 features included (WiFi, Ethernet, PoE)

## Installation

1. **Mounting**: Attach the universal holder to the water meter and connect the detachable water sensor
2. **Power**: Connect via USB-C or PoE
3. **Connect**: Device comes **pre-flashed with WiFi firmware** - use captive portal to connect
4. **Add to Home Assistant**: The device will be automatically discovered
5. **Optional**: Connect a water leak sensor or door sensor to the expansion port

📺 **Installation videos** available on YouTube for popular meters: Sensus, Itron, Actaris, Schlumberger, Elster, and Honeywell.

## Switching to Ethernet/PoE

After connecting to Home Assistant via WiFi, you can easily switch to Ethernet firmware using a simple switch in the device settings. No manual flashing required!

For detailed instructions: https://smarthomeshop.io/quick-start-waterp1meterkit

## Firmware Files

- `waterp1meterkit-wifi.yaml` - WiFi connection (pre-installed)
- `waterp1meterkit-ethernet.yaml` - Ethernet or PoE connection

## Sensors Included

| Sensor | Description |
|--------|-------------|
| Energy (P1) | All DSMR data (consumption, production, voltage, current, gas) |
| Water | Current usage (L/min) and total consumption (m³) |
| Expansion Port | Water leak sensor or door sensor (optional) |
| Temperature | Ambient temperature (°C) |
| Humidity | Relative humidity (%) |

## Version Comparison

| Feature | V1 | V2 | V3 |
|---------|----|----|-----|
| WiFi | ✅ | ✅ | ✅ |
| Ethernet | ✅ | ✅ | ✅ |
| PoE | ❌ | ✅ | ✅ |
| Detachable Water Sensor | ❌ | ❌ | ✅ |
| Expansion Port | ❌ | ❌ | ✅ |
| Improved Precision | - | - | ✅ |

## More Information

- 🌐 Website: [waterp1meterkit.nl](https://waterp1meterkit.nl/en/)
- 🛒 Order: [smarthomeshop.io/en/order](https://smarthomeshop.io/en/order)
