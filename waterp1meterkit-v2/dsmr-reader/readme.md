# DSMR Configuration for Watermeter P1 Kit  

This guide explains how to configure the Watermeter P1 Kit to send data to a DSMR-Reader instance.  

## What is DSMR-Reader?  

[DSMR-Reader](https://dsmr-reader.readthedocs.io/) is an open-source application for collecting, monitoring, and analyzing smart meter data based on the **Dutch Smart Meter Requirements (DSMR)** protocol. It provides a web-based dashboard to visualize electricity and gas usage, track costs, and set alerts for unusual consumption patterns.  

## Prerequisites  

1. **DSMR-Reader Instance**: Ensure you have DSMR-Reader installed and running. Refer to the [DSMR-Reader installation guide](https://dsmr-reader.readthedocs.io/en/latest/installation.html).  
2. **API Token**: Generate an API token for secure data transmission.  
3. **API Endpoint**: Ensure the API feature is enabled in DSMR-Reader (disabled by default).  

## Enabling the API in DSMR-Reader  

Follow these steps to enable the API in DSMR-Reader:  

1. Log in to the DSMR-Reader admin interface.  
2. Navigate to **API Settings** under the _Configuration_ menu.  
3. Enable the API by toggling the "Enable API" setting.  
4. Save the changes.  

## Generating an API Token  

1. Go to **API Settings** in DSMR-Reader.  
2. Copy the generated token for later use.  

## Configuration  

Update the `interval` block in your Watermeter P1 Kit's configuration file with your DSMR-Reader **authorization token** and **URL**.  

### Example Configuration  

```yaml
interval:
  - interval: 15sec
    then:
      - http_request.post:
          url: http://<your-dsmr-reader-instance>/api/v2/datalogger/dsmrreading
          headers:
            Authorization: Token <your-api-token>
            Content-Type: application/json
          verify_ssl: false
          json: |-
            root["electricity_currently_delivered"] = id(dsmr_electricity_currently_delivered).state;
            root["electricity_currently_returned"] = id(dsmr_electricity_currently_returned).state;
            root["electricity_delivered_1"] = id(dsmr_electricity_delivered_1).state;
            root["electricity_delivered_2"] = id(dsmr_electricity_delivered_2).state;
            root["electricity_returned_1"] = id(dsmr_electricity_returned_1).state;
            root["electricity_returned_2"] = id(dsmr_electricity_returned_2).state;
            root["extra_device_delivered"] = id(dsmr_extra_device_delivered).state;
            root["extra_device_timestamp"] = id(dsmr_timestamp_formatted).state;
            root["phase_currently_delivered_l1"] = id(dsmr_phase_currently_delivered_l1).state;
            root["phase_currently_delivered_l2"] = id(dsmr_phase_currently_delivered_l2).state;
            root["phase_currently_delivered_l3"] = id(dsmr_phase_currently_delivered_l3).state;
            root["phase_currently_returned_l1"] = id(dsmr_phase_currently_returned_l1).state;
            root["phase_currently_returned_l2"] = id(dsmr_phase_currently_returned_l2).state;
            root["phase_currently_returned_l3"] = id(dsmr_phase_currently_returned_l3).state;
            root["phase_power_current_l1"] = id(dsmr_phase_power_current_l1).state;
            root["phase_power_current_l2"] = id(dsmr_phase_power_current_l2).state;
            root["phase_power_current_l3"] = id(dsmr_phase_power_current_l3).state;
            root["phase_voltage_l1"] = id(dsmr_phase_voltage_l1).state;
            root["phase_voltage_l2"] = id(dsmr_phase_voltage_l2).state;
            root["phase_voltage_l3"] = id(dsmr_phase_voltage_l3).state;
            root["timestamp"] = id(dsmr_timestamp_formatted).state;
