# WaterP1MeterKit V2

## Overview

The WaterP1MeterKit V2 builds upon V1 functionality and introduces Power over Ethernet (PoE) support, allowing for simplified installation with power and data over a single cable.

## Features

- **Flexible monitoring**: Choose to monitor **only energy**, **only water**, or **both** with a single kit
- **Energy monitoring**: Reads data via the P1 port of DSMR-compatible energy meters
- **Water monitoring**: Detects water consumption via a fixed (non-detachable) water sensor
- **Connectivity**: WiFi, Ethernet, and **Power over Ethernet (PoE)** support
- **Temperature & Humidity**: Built-in HDC1080 sensor
- **Integration**: Fully integrated with Home Assistant via ESPHome

## Hardware Specifications

| Component | Specification |
|-----------|---------------|
| MCU | ESP32 |
| P1 Port | DSMR 2.2 - 5.0 compatible |
| Water Sensor | Fixed, non-detachable |
| Network | WiFi, Ethernet (LAN8720), or PoE |
| PoE | ✅ Supported |
| Power | USB-C or PoE powered |
| LEDs | RGB status indication |

## Pin Configuration

- **UART RX (P1)**: GPIO16 (inverted)
- **P1 Request**: GPIO12
- **Water Pulse**: GPIO32
- **I²C SDA**: GPIO15
- **I²C SCL**: GPIO4
- **Ethernet Power**: GPIO33

## What's New in V2 (compared to V1)

- ✅ **Power over Ethernet (PoE) support** - Power and data via single cable
- ✅ Improved UART configuration with inverted RX pin
- ✅ Gas MBus ID support for better gas meter compatibility
- ✅ Internal hardware improvements

## Installation

1. **Mounting**: Attach the water sensor to the water meter using the included holder
2. **Power**: Connect via USB-C or PoE
3. **Connect**: Device comes **pre-flashed with WiFi firmware** - use captive portal to connect
4. **Add to Home Assistant**: The device will be automatically discovered

## Switching to Ethernet/PoE

After connecting to Home Assistant via WiFi, you can easily switch to Ethernet firmware using a simple switch in the device settings. No manual flashing required!

For detailed instructions: https://smarthomeshop.io/quick-start-waterp1meterkit

## Firmware Files

- `waterp1meterkit-wifi.yaml` - WiFi connection (pre-installed)
- `waterp1meterkit-ethernet.yaml` - Ethernet or PoE connection

## Notes

- The water sensor is fixed and not detachable
- PoE support provides both power and data via a single cable
- Consider upgrading to V3 for detachable water sensor and expansion port

## More Information

Visit [waterp1meterkit.nl](https://waterp1meterkit.nl/en/) for detailed instructions and compatibility information.
