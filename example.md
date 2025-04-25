# Example

This is a quick explanation on how to set a custom advertisement data. For more details, please refer to [cyw20822 documentation](https://www.infineon.com/dgdl/Infineon-EZ-Serial_firmware_platform_user_guide_for_CYW20822_module-UserManual-v02_00-EN.pdf?fileId=8ac78c8c8d2fe47b018e17ad650a6ea6) on page 49

## How to format a custom advertising data
We use this hex string as an example `050846325A310B0953636F75745F46325A3112FF310132342e302c35302c312e382c373532`

This can be broken down into 3 pieces:
1. `050846325A31`
2. `B0953636F75745F46325A31`
3. `12FF310132342e302c35302c312e382c373532`

Each of these follow the format of `[byte_length]` + `[advertisement_type]` + `[advertisement_data]`

Let's look at the 1st one, `050846325A31`. The data we want to set is `46325A31`, which has 4 bytes. `08` is the advertisement type we want to set, which sets the shortened local name of the dev kit and it has 1 byte. Hence, the total number of bytes for this data is `05` bytes. This is how we get `05 08 46325A31`.

The 2nd one is the same as the 1st. It sets the complete local name.

Now, look at the 3rd one, setting manufacture data. This one is different. The data we want to set is `32342e302c35302c312e382c373532`, which has 15 bytes. `FF` is the advertisement type (manufacture data in this case) and it has 1 byte. But we need to put a company identifier, `3101`, in front of our custom data, which has 2 bytes. So now we have `FF 3101 32342e302c35302c312e382c373532`, which has 18 bytes or `12` bytes in hex. This is how we get `12 FF 3101 32342e302c35302c312e382c373532`.

_Note: Company identifier is an assigned number by bluetooth. Check more about assigned numbers [here](https://www.bluetooth.com/wp-content/uploads/Files/Specification/Assigned_Numbers.pdf?v=1703431207015)_


## How to set a custom advertising data
- `sacp,p=1,t=6,f=2`
    - `p=1` is to set advertising mode to extended
    - `t=6` is to set advertisement type to extended: undirected connectable
    - `f=2` is to allow to use custom advertment data
- `sead,t=0,d=` 
    - `t=0` is to erase all
- `sead,t=1,d=050846325A310B0953636F75745F46325A3112FF310132342e302c35302c312e382c373532`
    - `t=1` is to append advertisement data
    - `d=...` is to set the advertisement data