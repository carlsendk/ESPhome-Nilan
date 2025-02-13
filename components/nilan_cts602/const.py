"""Constants for Nilan CTS602 component."""

from enum import IntEnum

# Modbus register types
REGISTER_TYPE_HOLDING = "holding"
REGISTER_TYPE_INPUT = "input"

# Default values
DEFAULT_MODBUS_ADDRESS = 30  # Default Modbus address for CTS602
DEFAULT_UPDATE_INTERVAL = 5  # seconds


# Register blocks
class RegisterBlocks(IntEnum):
    """Register blocks in the Nilan CTS602."""

    TEMPERATURES = 200  # Temperature sensors block
    ALARMS = 400  # Alarm status block
    CONTROL = 1000  # Control parameters block
    FAN_SPEED = 200  # Fan speed control block
    AIR_TEMP = 1200  # Air temperature block


# Register sizes (number of registers in each block)
REGISTER_SIZES = {
    RegisterBlocks.TEMPERATURES: 23,
    RegisterBlocks.ALARMS: 10,
    RegisterBlocks.CONTROL: 8,
    RegisterBlocks.FAN_SPEED: 2,
    RegisterBlocks.AIR_TEMP: 6,
}

# Sensor definitions
TEMPERATURE_SENSORS = {
    "T0_Controller": {
        "register": 200,
        "name": "Controller Temperature",
        "type": REGISTER_TYPE_INPUT,
    },
    "T1_Intake": {
        "register": 201,
        "name": "Intake Temperature",
        "type": REGISTER_TYPE_INPUT,
    },
    "T2_Inlet": {
        "register": 202,
        "name": "Inlet Temperature",
        "type": REGISTER_TYPE_INPUT,
    },
    "T3_Exhaust": {
        "register": 203,
        "name": "Exhaust Temperature",
        "type": REGISTER_TYPE_INPUT,
    },
    "T4_Outlet": {
        "register": 204,
        "name": "Outlet Temperature",
        "type": REGISTER_TYPE_INPUT,
    },
    "T7_Inlet": {
        "register": 207,
        "name": "Inlet After Heating",
        "type": REGISTER_TYPE_INPUT,
    },
    "T8_Outdoor": {
        "register": 208,
        "name": "Outdoor Temperature",
        "type": REGISTER_TYPE_INPUT,
    },
    "T9_Heater": {
        "register": 209,
        "name": "Heater Temperature",
        "type": REGISTER_TYPE_INPUT,
    },
}

# Control registers
CONTROL_REGISTERS = {
    "fan_speed": {"register": 200, "name": "Fan Speed", "type": REGISTER_TYPE_HOLDING},
    "mode": {"register": 1000, "name": "Operation Mode", "type": REGISTER_TYPE_HOLDING},
    "target_temp": {
        "register": 1001,
        "name": "Target Temperature",
        "type": REGISTER_TYPE_HOLDING,
    },
}

# Stores register names, addresses, sizes
#
