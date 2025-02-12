#pragma once

#include "esphome/core/component.h"
#include "esphome/components/uart/uart.h"

namespace esphome {
namespace nilan {

class NilanCTS602 : public Component, public uart::UARTDevice {
public:
    NilanCTS602() = default;
    
    void setup() override;
    void loop() override;

protected:
    bool validate_crc(uint8_t *data, size_t len);
};

}  // namespace nilan
}  // namespace esphome
