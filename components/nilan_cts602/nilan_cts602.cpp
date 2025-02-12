#include "nilan_cts602.h"
#include "esphome/core/log.h"

namespace esphome {
namespace nilan {

static const char *const TAG = "nilan.cts602";

void NilanCTS602::setup() {
    ESP_LOGD(TAG, "Setting up Modbus communication");
}

void NilanCTS602::loop() {
    uint8_t request[] = { 0x01, 0x03, 0x00, 0x64, 0x00, 0x01, 0x85, 0xDB }; // Example read request for register 100
    write_array(request, sizeof(request));
    flush();
    
    delay(200); // Wait for response

    if (available() >= 7) {
        uint8_t response[7];
        read_array(response, 7);
        
        if (validate_crc(response, 7)) {
            int16_t value = (response[3] << 8) | response[4];
            ESP_LOGD(TAG, "Read value: %d", value);
        } else {
            ESP_LOGE(TAG, "CRC check failed");
        }
    } else {
        ESP_LOGW(TAG, "No response from Nilan CTS602");
    }
}

bool NilanCTS602::validate_crc(uint8_t *data, size_t len) {
    uint16_t crc = 0xFFFF;
    for (size_t i = 0; i < len - 2; i++) {
        crc ^= data[i];
        for (int j = 0; j < 8; j++) {
            if (crc & 1) {
                crc = (crc >> 1) ^ 0xA001;
            } else {
                crc >>= 1;
            }
        }
    }
    return ((crc & 0xFF) == data[len - 2]) && ((crc >> 8) == data[len - 1]);
}

}  // namespace nilan
}  // namespace esphome

