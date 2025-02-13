"""ESPHome Nilan CTS602 Component."""

from typing import Any

import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import modbus_controller
from esphome.const import CONF_ID

CODEOWNERS = ["@joncarlsen"]
DEPENDENCIES = ["modbus_controller"]
AUTO_LOAD = ["sensor", "climate"]

# Component namespace
CONF_NILAN_ID = "nilan_id"


# Configuration schema
CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(modbus_controller.ModbusController),
}).extend(modbus_controller.validate_modbus_controller_config({}))


async def to_code(config: dict[str, Any]) -> None:
    """Generate code for Nilan component."""
    var = await modbus_controller.register_modbus_controller(config)
    # Set default Modbus settings for Nilan
    cg.add(var.set_send_wait_time(200))  # 200ms between requests
    cg.add(var.set_update_interval(5000))  # 5s update interval
