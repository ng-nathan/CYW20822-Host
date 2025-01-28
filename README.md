# CYW20822 Host

## Overview
This repository contains scripts and resources for developing and debugging BLE functionality using the [CYW20822 module](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-bluetooth-le-bluetooth-multiprotocol/airoc-bluetooth-modules/cyw20822-p4tai040/). The primary focus is on:

- Customizing BLE advertising and payload data.

- Interfacing with the module via UART using EZ-Serial firmware.

## Contents
- CYW20822 Scripts:

    - Custom Python scripts for interacting with the CYW20822 module.

    - Utilities for sending/receiving BLE payloads, configuring settings, and troubleshooting.

- EZ-Serial Library:

    - Official EZ-Serial firmware library obtained from [Infineon's official website](https://www.infineon.com/cms/en/design-support/software/device-driver-libraries/airoc-wi-fi-bluetooth-ez-serial-module-firmware-platform/?tab=~%27all#!designsupport).

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run examples:
   ```bash
   python cyw20822host.py
   ```

## Acknowledgments
Infineon Technologies for EZ-Serial firmware library.

