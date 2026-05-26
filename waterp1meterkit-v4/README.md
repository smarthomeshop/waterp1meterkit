# WaterP1MeterKit V4

## Overview

The WaterP1MeterKit V4 is the ESP32-C6 based hardware revision. It keeps the combined P1 smart meter and water meter monitoring flow from V3, with updated GPIO mapping for the C6 board and ESP-IDF as the firmware framework.

## Features

- **Energy monitoring**: Reads DSMR telegrams from the P1 port of compatible smart meters
- **Water monitoring**: Tracks current water usage and total consumption from the pulse input
- **Expansion port**: Supports a water leak sensor or door sensor input
- **Connectivity**: WiFi or W5500 Ethernet firmware for Home Assistant / ESPHome
- **Temperature & humidity**: Built-in HDC1080 sensor
- **Integration**: Fully local Home Assistant integration through ESPHome

## Hardware Specifications

| Component | Specification |
|-----------|---------------|
| MCU | ESP32-C6 |
| Framework | ESP-IDF |
| P1 Port | DSMR 2.2 - 5.0 compatible |
| Water Sensor | Pulse input |
| Expansion Port | For water leak sensor or door sensor |
| Network | WiFi or W5500 SPI Ethernet |
| Power | USB-C or P1 port powered |
| LEDs | RGB status indication |

## Pin Configuration

- **UART RX (P1)**: GPIO1 (inverted)
- **P1 Request**: GPIO10
- **Water Pulse**: GPIO0
- **Expansion Port (Leak/Door)**: GPIO2
- **I2C SDA**: GPIO6
- **I2C SCL**: GPIO7
- **LED Green**: GPIO12
- **LED Red / Status**: GPIO13
- **LED Blue**: GPIO11
- **Ethernet Power Enable**: GPIO18 (active-low, LOW = on)
- **Ethernet SPI SCLK**: GPIO23
- **Ethernet SPI MISO**: GPIO22
- **Ethernet SPI MOSI**: GPIO21
- **Ethernet CS**: GPIO15
- **Ethernet INT**: GPIO20
- **Ethernet Reset**: GPIO19

## What's New in V4

- ESP32-C6 based hardware platform
- ESP-IDF firmware framework
- Updated GPIO mapping for P1, water pulse, I2C, and RGB status LEDs
- WiFi and W5500 Ethernet public firmware variants

## Installation

1. Connect the P1 and water sensor inputs.
2. Power the device through USB-C or the P1 port.
3. Use the pre-flashed WiFi firmware and complete onboarding through the captive portal or Improv.
4. Add the device to Home Assistant when it is discovered through ESPHome.
5. Optional: connect a water leak sensor or door sensor to the expansion port.
6. Optional: switch to Ethernet firmware from Home Assistant if wired networking is preferred.

For detailed instructions: https://smarthomeshop.io/quick-start-waterp1meterkit

## Firmware Files

- `waterp1meterkit-wifi.yaml` - WiFi connection (pre-installed)
- `waterp1meterkit-ethernet.yaml` - W5500 Ethernet connection

## Sensors Included

| Sensor | Description |
|--------|-------------|
| Energy (P1) | DSMR data such as consumption, production, voltage, current, and gas |
| Water | Current usage (L/min), total consumption (m3), and absolute meter total |
| Expansion Port | Water leak sensor or door sensor input |
| Temperature | Ambient temperature |
| Humidity | Relative humidity |

## Version Comparison

| Feature | V1 | V2 | V3 | V4 |
|---------|----|----|----|----|
| MCU | ESP32 | ESP32 | ESP32 | ESP32-C6 |
| WiFi | Yes | Yes | Yes | Yes |
| Ethernet | Yes | Yes | Yes | Yes |
| PoE | No | Yes | Yes | No |
| Detachable Water Sensor | No | No | Yes | Yes |
| Expansion Port | No | No | Yes | Yes |
| ESP-IDF Framework | No | No | No | Yes |

## More Information

- Website: [waterp1meterkit.nl](https://waterp1meterkit.nl/en/)
- Order: [smarthomeshop.io/en/order](https://smarthomeshop.io/en/order)
