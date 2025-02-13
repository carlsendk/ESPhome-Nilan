"""Nilan CTS602 sensor implementation."""

from typing import Any  # Add this import for type annotation

import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import modbus_controller, sensor
from esphome.const import (
    CONF_ID,
    DEVICE_CLASS_TEMPERATURE,
    STATE_CLASS_MEASUREMENT,
    UNIT_CELSIUS,
)

from . import const

DEPENDENCIES = ["modbus_controller"]

# Configuration schema for each sensor
SENSOR_SCHEMA = cv.Schema(
    {
        cv.Required(CONF_ID): cv.declare_id(sensor.Sensor),
        cv.Optional("name", default=""): cv.string,
    }
)

# Configuration schema for the component
CONFIG_SCHEMA = cv.Schema(
    {
        cv.Optional(sensor_id): SENSOR_SCHEMA
        for sensor_id in const.TEMPERATURE_SENSORS.keys()
    }
)


async def to_code(config: dict[str, dict[str, Any]]) -> None:
    """Generate code for sensors."""
    for sensor_id, sensor_config in config.items():
        if sensor_id not in const.TEMPERATURE_SENSORS:
            continue

        reg_info = const.TEMPERATURE_SENSORS[sensor_id]
        name = sensor_config.get("name", reg_info["name"])

        var = cg.new_Pvariable(sensor_config[CONF_ID])
        await sensor.register_sensor(
            var,
            {
                "name": name,
                "device_class": DEVICE_CLASS_TEMPERATURE,
                "state_class": STATE_CLASS_MEASUREMENT,
                "unit_of_measurement": UNIT_CELSIUS,
            },
        )

        cg.add(
            modbus_controller.register_sensor(
                var,
                reg_info["type"],
                reg_info["register"],
                value_type="U_WORD",
                scale=0.1,  # Nilan uses 0.1°C resolution
            )
        )
