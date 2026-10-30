# `AppleC26HID`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleC26Charger`](../kexts/com.apple.driver.AppleC26Charger.md)
- Object size: `0x120` (288 bytes)
- Metaclass: `0xfffffe000b938458`; metaclass vtable `0xfffffe0008003738`; class vtable `0xfffffe0008003180`
- Registration (init): `0xfffffe0008a267b4`
- Superclasses: [`IOAccessoryHIDDeviceInterface`](IOAccessoryHIDDeviceInterface.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleC26HID` in [`com.apple.driver.AppleC26Charger`](../kexts/com.apple.driver.AppleC26Charger.md): `IOProviderClass` = `AppleC26DeviceStream`, `IOMatchCategory` = `AppleC26HID`

## Strings in its kext that name it (8)

- `virtual IOReturn AppleC26HIDWatch::sendOutData(const void *, IOByteCount)`
- `site.AppleC26HIDWatch`
- `AppleC26HIDWatch`
- `AppleC26HIDWatch::%s: received HID telegram:%s\n`
- `AppleC26HID`
- `site.AppleC26HID`
- `AppleC26HIDWatch::%s: sending HID telegram:%s\n`
- `void AppleC26HIDWatch::_receiveData(AppleC26DataStream *, const void *, size_t)`
