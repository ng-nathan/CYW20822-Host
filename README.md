# CYW20822 Host

This repository contains scripts and resources for developing and debugging BLE functionality using the [CYW20822 module](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-bluetooth-le-bluetooth-multiprotocol/airoc-bluetooth-modules/cyw20822-p4tai040/). 

## Scripts

- `cyw20822term.py`: a terminal script that I personally made to replace Teraterm because of the regular console has echo and is much easier to copy/paste hex string

- `encoder.py`: a script that encodes regular string (ASCII) to hex string to set custom ble advertising data

- `decoder.py`: a script that decodes hex string into regular string. I used this when I haven't implemented a decoder on our mobile apps, [Android](https://github.com/ng-nathan/BLE-tester) & [iOS](https://github.com/ng-nathan/ScoutStream)

## Usage

### `cyw20822term.py`

- Run `python cyw20822term.py COM14` or `python cyw20822term.py 14` _(change your COM port)_
- Use commands as you do when you use other consoles
    - e.g., `sacp,p=1,t=6,f=2` is setting the advertising parameter to extended advertising mode and allow you to set custom advertising data. `gacp` is getting all the advertising parameter
- `Ctrl + C` to exit

```
python cyw20822term.py 13
sacp,p=1,t=6,f=2
sacp,p=1,t=6,f=2
@R,000A,SACP,0000
gacp
gacp
@R,0065,GACP,0000,P=01,M=01,T=06,H=00,I=0020,C=07,L=00,O=0000,F=02,A=000000000000,Y=00,E=00,S=00,D=00,N=0018

Exiting...
Port closed
```
- If you want to know how to set a custom advertisement data, please refer to [example.md](/example.md)
- For more commands related to advertising, please refers to [cyw20822 documentation](https://www.infineon.com/dgdl/Infineon-EZ-Serial_firmware_platform_user_guide_for_CYW20822_module-UserManual-v02_00-EN.pdf?fileId=8ac78c8c8d2fe47b018e17ad650a6ea6) on page 6

### `encoder.py`
- Run `encoder.py`
- Type your custom regular string (ASCII)
- The byte count in the output is to help you format a custom advertising data
- e.g., Converting "This is encoder" to hex string
```
Enter ASCII text to convert: This is encoder          

Results:
Original text: This is encoder
Pure hex value: 5468697320697320656e636f646572
Byte count: 15
Byte count in hex: 0F
```


### `decoder.py`
- Run `python decoder.py`
- Paste in the hex string you want to decode
- e.g., Decoding "5468697320697320656e636f646572" to ASCII
```
Enter hex string to decode: 5468697320697320656e636f646572

Results:
Original hex: 5468697320697320656e636f646572
Decoded ASCII text: This is encoder
Byte count: 15
```