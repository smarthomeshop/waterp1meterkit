# Changelog

All notable customer-facing firmware changes for WaterP1MeterKit are tracked in this file.

This changelog starts on 2026-04-14. Earlier firmware versions existed before that date, but they were not tracked in a customer-facing changelog.

## [Unreleased]

- Add customer-facing firmware notes here before merging a PR.
- Updated LAN8720 Ethernet clock configuration for ESPHome 2026.7 compatibility.

## [WaterP1MeterKit V4 1.10] - 2026-06-26


- Fixed WaterP1MeterKit V4 default gas MBus ID back to 1.


## [WaterP1MeterKit V1 1.11] - 2026-06-26


- Fixed cloud firmware variant selector defaults to match the published SmartHomeShop App option names.


## [WaterP1MeterKit V2 1.12] - 2026-06-26


- Fixed cloud firmware variant selector defaults to match the published SmartHomeShop App option names.


## [WaterP1MeterKit V3 1.11] - 2026-06-26


- Fixed cloud firmware variant selector defaults to match the published SmartHomeShop App option names.


## [WaterP1MeterKit V1 1.10] - 2026-06-26


- Fixed WaterP1MeterKit V4 expansion port leak/door input pin mapping from GPIO2 to GPIO5.
- Added SmartHomeShop App (cloud) firmware variants where available.


## [WaterP1MeterKit V2 1.11] - 2026-06-26


- Fixed WaterP1MeterKit V4 expansion port leak/door input pin mapping from GPIO2 to GPIO5.
- Added SmartHomeShop App (cloud) firmware variants where available.


## [WaterP1MeterKit V3 1.10] - 2026-06-26


- Fixed WaterP1MeterKit V4 expansion port leak/door input pin mapping from GPIO2 to GPIO5.
- Added SmartHomeShop App (cloud) firmware variants where available.


## [WaterP1MeterKit V4 1.9] - 2026-06-26


- Fixed WaterP1MeterKit V4 expansion port leak/door input pin mapping from GPIO2 to GPIO5.
- Added SmartHomeShop App (cloud) firmware variants where available.


## [WaterP1MeterKit V4 1.8] - 2026-05-27


- Set WaterP1MeterKit V4 to target the ESP32-C6-WROOM-1-N8 8 MB flash module used in production hardware.


## [WaterP1MeterKit V4 1.7] - 2026-05-27


- Fixed USB/serial provisioning for WaterP1MeterKit V4 by using the ESP32-C6 UART0 USB-UART bridge on GPIO16/GPIO17.


## [WaterP1MeterKit V4 1.6] - 2026-05-26


- Added WaterP1MeterKit V4 WiFi and Ethernet firmware for ESP32-C6 based hardware with updated pin mapping.


## [WaterP1MeterKit V1 1.9] - 2026-04-17

- Water Meter Initial Value is now saved immediately when entered, so a sudden power loss right after manual input no longer resets the stored meter reading.
- Improved onboarding and adoption defaults for the public WiFi and Ethernet builds so WaterP1MeterKit fits the Made for ESPHome flow better.
- Renamed the firmware selector labels to clearly distinguish fully local variants from SmartHomeShop App (cloud) variants.
- Marked the live water flow sensor as a proper volume flow rate measurement so Home Assistant accepts it cleanly in water dashboards.


## [WaterP1MeterKit V2 1.10] - 2026-04-17


- Water Meter Initial Value is now saved immediately when entered, so a sudden power loss right after manual input no longer resets the stored meter reading.
- Improved onboarding and adoption defaults for the public WiFi and Ethernet builds so WaterP1MeterKit fits the Made for ESPHome flow better.
- Renamed the firmware selector labels to clearly distinguish fully local variants from SmartHomeShop App (cloud) variants.
- Marked the live water flow sensor as a proper volume flow rate measurement so Home Assistant accepts it cleanly in water dashboards.


## [WaterP1MeterKit V3 1.9] - 2026-04-17


- Water Meter Initial Value is now saved immediately when entered, so a sudden power loss right after manual input no longer resets the stored meter reading.
- Improved onboarding and adoption defaults for the public WiFi and Ethernet builds so WaterP1MeterKit fits the Made for ESPHome flow better.
- Renamed the firmware selector labels to clearly distinguish fully local variants from SmartHomeShop App (cloud) variants.
- Marked the live water flow sensor as a proper volume flow rate measurement so Home Assistant accepts it cleanly in water dashboards.


## [WaterP1MeterKit V1 1.7] - 2026-04-15

### Changed

- OTA behavior was adjusted to disable automatic rollback after an OTA update.

## [WaterP1MeterKit V2 1.8] - 2026-04-15

### Changed

- OTA behavior was adjusted to disable automatic rollback after an OTA update.

## [WaterP1MeterKit V3 1.7] - 2026-04-15

### Changed

- OTA behavior was adjusted to disable automatic rollback after an OTA update.

## [WaterP1MeterKit V1 1.6] - 2026-04-15

### Added

- New "Water Meter Total" sensor keeps the absolute water meter reading after reboots and OTA updates.
- New "Water Meter Initial Value" setting lets you match the kit to the physical meter reading.

### Changed

- Water total persistence now batches writes to reduce flash wear while still saving recent usage during clean restarts.

## [WaterP1MeterKit V2 1.7] - 2026-04-15

### Added

- New "Water Meter Total" sensor keeps the absolute water meter reading after reboots and OTA updates.
- New "Water Meter Initial Value" setting lets you match the kit to the physical meter reading.

### Changed

- Water total persistence now batches writes to reduce flash wear while still saving recent usage during clean restarts.

## [WaterP1MeterKit V3 1.6] - 2026-04-15

### Added

- New "Water Meter Total" sensor keeps the absolute water meter reading after reboots and OTA updates.
- New "Water Meter Initial Value" setting lets you match the kit to the physical meter reading.

### Changed

- Water total persistence now batches writes to reduce flash wear while still saving recent usage during clean restarts.

## [WaterP1MeterKit V1 1.5] - 2026-04-14

### Added

- Customer-facing version history now lives in this repository.
- GitHub Releases will now be published for future firmware versions.

### Changed

- This file is now the public place for customer-facing firmware notes.

## [WaterP1MeterKit V2 1.5] - 2026-04-14

### Added

- Customer-facing version history now lives in this repository.
- GitHub Releases will now be published for future firmware versions.

### Changed

- This file is now the public place for customer-facing firmware notes.

## [WaterP1MeterKit V3 1.5] - 2026-04-14

### Added

- Customer-facing version history now lives in this repository.
- GitHub Releases will now be published for future firmware versions.

### Changed

- This file is now the public place for customer-facing firmware notes.
