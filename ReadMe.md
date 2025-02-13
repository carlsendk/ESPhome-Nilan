# ESPHome Nilan CTS602 Integration

## Overview

This ESPHome external component integrates with the **Nilan CTS602** ventilation system using **Modbus RTU over RS485**. The integration provides access to temperature readings, fan speed control, and system monitoring.

## Features

✅ **Read Room Temperature** (and other sensors from Modbus)  
✅ **Control Fan Speed** via Modbus write registers  
✅ **Integrate with Home Assistant** for easy monitoring  
✅ **Fully ESPHome-compatible** using `modbus_controller`  
✅ **Minimal configuration required**

## Installation

### 1️⃣ Add External Component

Include this repository in your `esphome` configuration:

```yaml
external_components:
  - source: github://your_repo/ESPhome-Nilan
```

### 2️⃣ Configure Modbus UART

Make sure the **Wemos D1 Mini (ESP8266)** is wired correctly to the RS485 adapter.

```yaml
uart:
  id: uart_bus
  tx_pin: D1
  rx_pin: D2
  baud_rate: 19200
  stop_bits: 1
  parity: NONE
```

### 3️⃣ Setup Modbus Controller

```yaml
modbus:
  send_wait_time: 200ms
  id: modbus_nilan

modbus_controller:
  - id: nilan_controller
    address: 30  # Default Modbus ID for CTS602
    modbus_id: modbus_nilan
    update_interval: 5s
```

### 4️⃣ Add Sensors

```yaml
sensor:
  - platform: modbus_controller
    modbus_controller_id: nilan_controller
    name: "Nilan Room Temperature"
    register_type: input
    address: 0  # 30001 in documentation
    unit_of_measurement: "°C"
    value_type: U_WORD
```

### 5️⃣ Compile & Upload

Run the following command:

```sh
esphome compile nilan.yaml && esphome upload nilan.yaml
```

## Supported Sensors & Controls

| **Sensor/Control** | **Modbus Address** | **Type** |
|--------------------|-------------------|----------|
| Room Temperature  | 30001              | Input Register |
| Fan Speed        | 40101              | Holding Register |
| Supply Air Temp  | 30002              | Input Register |

## Troubleshooting

- **No data received?** Check RS485 wiring and Modbus ID settings.
- **Incorrect readings?** Ensure correct register types and scaling.
- **Timeouts?** Try adjusting `send_wait_time` to `300ms`.

## Contributing

Feel free to contribute by submitting pull requests or opening issues for bugs and feature requests.

## License

MIT License - Open for community use!
