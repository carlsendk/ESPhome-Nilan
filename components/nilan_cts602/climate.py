"""Nilan CTS602 climate implementation."""

import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import climate, modbus_controller
from esphome.const import CONF_ID, CONF_NAME

from . import const

DEPENDENCIES = ["modbus_controller"]

# Climate modes mapping
CLIMATE_MODES = {
    0: climate.ClimateMode.OFF,
    1: climate.ClimateMode.HEAT_COOL,  # Auto mode
    2: climate.ClimateMode.COOL,
    3: climate.ClimateMode.HEAT,
}

# Configuration schema
CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(climate.Climate),
        cv.Optional(CONF_NAME, default="Nilan Climate"): cv.string,
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config: dict) -> None:
    """Generate code for climate control."""
    var = cg.new_Pvariable(config[CONF_ID])
    await climate.register_climate(
        var,
        {
            "name": config[CONF_NAME],
            "supports_target_temperature": True,
            "supports_mode": True,
            "supported_modes": list(CLIMATE_MODES.values()),
            "visual_min_temperature": 5,
            "visual_max_temperature": 30,
            "visual_temperature_step": 0.5,
        },
    )

    # Register temperature sensors
    cg.add(
        modbus_controller.register_sensor(
            var,
            const.CONTROL_REGISTERS["target_temp"]["type"],
            const.CONTROL_REGISTERS["target_temp"]["register"],
            value_type="U_WORD",
            scale=0.1,
            write_lambda=lambda value: int(value * 10),
        )
    )

    # Register mode control
    cg.add(
        modbus_controller.register_sensor(
            var,
            const.CONTROL_REGISTERS["mode"]["type"],
            const.CONTROL_REGISTERS["mode"]["register"],
            value_type="U_WORD",
            write_lambda=lambda value: list(CLIMATE_MODES.keys())[
                list(CLIMATE_MODES.values()).index(value)
            ],
        )
    )

    # Register fan speed control
    cg.add(
        modbus_controller.register_sensor(
            var,
            const.CONTROL_REGISTERS["fan_speed"]["type"],
            const.CONTROL_REGISTERS["fan_speed"]["register"],
            value_type="U_WORD",
        )
    )
