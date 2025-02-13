"""Nilan CTS602 Modbus register definitions."""

from typing import Any

from . import const

# Main register blocks with their base addresses and sizes
NILAN_REGISTERS = {
    "temperatures": {
        "address": const.RegisterBlocks.TEMPERATURES,
        "size": const.REGISTER_SIZES[const.RegisterBlocks.TEMPERATURES],
        "type": const.REGISTER_TYPE_INPUT,
    },
    "alarms": {
        "address": const.RegisterBlocks.ALARMS,
        "size": const.REGISTER_SIZES[const.RegisterBlocks.ALARMS],
        "type": const.REGISTER_TYPE_HOLDING,
    },
    "control": {
        "address": const.RegisterBlocks.CONTROL,
        "size": const.REGISTER_SIZES[const.RegisterBlocks.CONTROL],
        "type": const.REGISTER_TYPE_HOLDING,
    },
    "fan_speed": {
        "address": const.RegisterBlocks.FAN_SPEED,
        "size": const.REGISTER_SIZES[const.RegisterBlocks.FAN_SPEED],
        "type": const.REGISTER_TYPE_HOLDING,
    },
    "air_temp": {
        "address": const.RegisterBlocks.AIR_TEMP,
        "size": const.REGISTER_SIZES[const.RegisterBlocks.AIR_TEMP],
        "type": const.REGISTER_TYPE_INPUT,
    },
}

# Mapping of sensor names to their register offsets
SENSOR_MAPPING = {
    "temperatures": list(const.TEMPERATURE_SENSORS.keys()),
    "control": list(const.CONTROL_REGISTERS.keys()),
}


def get_nilan_registers() -> dict[str, dict[str, Any]]:
    """Return the complete register map."""
    return NILAN_REGISTERS
