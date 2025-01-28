import serial
import time
from ezslib import *

def hw_output(data):
    bytes_written = ser.write(data)
    return (bytes_written, API.EZS_OUTPUT_RESULT_DATA_WRITTEN)

def hw_input(timeout=None):
    if timeout is not None:
        ser.timeout = timeout
    try:
        byte = ser.read(1)
        if len(byte) == 0:
            return (None, API.EZS_INPUT_RESULT_NO_DATA)
        return (int.from_bytes(byte, 'big'), API.EZS_INPUT_RESULT_BYTE_READ)
    except:
        return (None, API.EZS_INPUT_RESULT_NO_DATA)

def packet_handler(packet):
    print(f"Received packet: {packet}")

def change_device_name(api, new_name):
    print("Getting current name...")
    api.sendAndWait("gap_get_device_name")

    print(f"Setting new name to: {new_name}")
    name_bytes = bytearray(new_name.encode())
    api.sendCommand("gap_set_device_name", name=name_bytes)
    time.sleep(0.1)

    print("Verifying new name...")
    api.sendAndWait("gap_get_device_name")
    
def set_adv_payload(api, adv_string):
    if len(adv_string) > 29:
        print("Warning: String too long, truncating to 29 characters")
        adv_string = adv_string[:29]
        
    name_ad = bytearray([len(adv_string) + 1, 0x09]) + bytearray(adv_string.encode())
    
    print(f"Setting advertising payload to: {adv_string}")
    api.sendCommand("gap_set_adv_data", data=name_ad)
    time.sleep(0.1)
    
    print("Verifying advertising payload...")
    api.sendAndWait("gap_get_adv_data")
    
def set_extended_adv_payload(api, adv_string):
    print("Setting up extended advertising parameters...")
    api.sendCommand("gap_set_adv_parameters",
        mode=2,
        type=0,
        interval=160,
        channels=7,
        filter=0,
        timeout=0,
        flags=1
    )

    name_ad = bytearray([len(adv_string) + 1, 0x09]) + bytearray(adv_string.encode())
    print(f"Setting advertising payload to: {adv_string}")
    api.sendCommand("gap_set_adv_data", data=name_ad)
    
    print("Starting advertising...")
    api.sendCommand("gap_start_adv",
        mode=2,
        type=0,
        interval=160,
        channels=7,
        filter=0,
        timeout=0
    )

    print("\nVerifying settings...")
    api.sendAndWait("gap_get_adv_parameters")
    api.sendAndWait("gap_get_adv_data")
    
def get_device_status(api):
    print("\nGetting current device name...")
    api.sendAndWait("gap_get_device_name")

    print("\nChecking advertising parameters...")
    api.sendAndWait("gap_get_adv_parameters")

    print("\nChecking current advertising data...")
    api.sendAndWait("gap_get_adv_data")

def main():
    global ser
    ser = serial.Serial(port='COM13', baudrate=115200)
    api = API(rxPacketHandler=packet_handler, hardwareOutput=hw_output, hardwareInput=hw_input)

    try:
        change_device_name(api, "NathanBLE01")
        set_adv_payload(api, "This is legacy")
        # set_extended_adv_payload(api, "This is extended advertising packet. This is extended advertising packet. This is extended advertising packet. This is extended advertising packet. This is extended advertising packet.")
        get_device_status(api)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ser.close()

if __name__ == "__main__":
    main()