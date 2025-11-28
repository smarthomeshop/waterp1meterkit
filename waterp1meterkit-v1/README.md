# WaterP1MeterKit V1

## Overview

The WaterP1MeterKit V1 is the original version, designed for real-time monitoring of energy and water consumption within Home Assistant. This version offers basic functionality for reading both energy and water meters.

## Features

- **Flexible monitoring**: Choose to monitor **only energy**, **only water**, or **both** with a single kit
- **Energy monitoring**: Reads data via the P1 port of DSMR-compatible energy meters
- **Water monitoring**: Detects water consumption via a fixed (non-detachable) water sensor
- **Connectivity**: WiFi or Ethernet support (no PoE)
- **Temperature & Humidity**: Built-in HDC1080 sensor
- **Integration**: Fully integrated with Home Assistant via ESPHome

## Hardware Specifications

| Component | Specification |
|-----------|---------------|
| MCU | ESP32 |
| P1 Port | DSMR 2.2 - 5.0 compatible |
| Water Sensor | Fixed, non-detachable |
| Network | WiFi or Ethernet (LAN8720) |
| PoE | ❌ Not supported |
| Power | USB-C |
| LEDs | RGB status indication |

## Pin Configuration

- **UART RX (P1)**: GPIO33
- **P1 Request**: GPIO12
- **Water Pulse**: GPIO32
- **I²C SDA**: GPIO15
- **I²C SCL**: GPIO4
- **Ethernet Power**: GPIO16

## Installation

1. **Mounting**: Attach the water sensor to the water meter using the included holder
2. **Power**: Connect power via USB-C
3. **Connect**: Device comes **pre-flashed with WiFi firmware** - use captive portal to connect
4. **Add to Home Assistant**: The device will be automatically discovered

## Switching to Ethernet

After connecting to Home Assistant via WiFi, you can easily switch to Ethernet firmware using a simple switch in the device settings. No manual flashing required!

For detailed instructions: https://smarthomeshop.io/quick-start-waterp1meterkit

## Firmware Files

- `waterp1meterkit-wifi.yaml` - WiFi connection (pre-installed)
- `waterp1meterkit-ethernet.yaml` - Ethernet connection

## Notes

- The water sensor is fixed and not detachable
- No PoE support - use USB-C for power
- Consider upgrading to V2 (adds PoE) or V3 (adds detachable sensor + expansion port)

## More Information

Visit [waterp1meterkit.nl](https://waterp1meterkit.nl/en/) for detailed instructions and compatibility information.
