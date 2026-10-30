# `AppleC26HIDWatch`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleC26Charger`](../kexts/com.apple.driver.AppleC26Charger.md)
- Object size: `0x120` (288 bytes)
- Metaclass: `0xfffffe000b938480`; metaclass vtable `0xfffffe0008003d88`; class vtable `0xfffffe00080037d0`
- Registration (init): `0xfffffe0008a267ec`
- Superclasses: [`IOAccessoryHIDDeviceInterface`](IOAccessoryHIDDeviceInterface.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleC26HIDWatch` in [`com.apple.driver.AppleC26Charger`](../kexts/com.apple.driver.AppleC26Charger.md): `IOProviderClass` = `AppleC26DeviceStream`, `IOMatchCategory` = `AppleC26HIDWatch`

## Strings in its kext that name it (6)

- `virtual IOReturn AppleC26HIDWatch::sendOutData(const void *, IOByteCount)`
- `site.AppleC26HIDWatch`
- `AppleC26HIDWatch`
- `AppleC26HIDWatch::%s: received HID telegram:%s\n`
- `AppleC26HIDWatch::%s: sending HID telegram:%s\n`
- `void AppleC26HIDWatch::_receiveData(AppleC26DataStream *, const void *, size_t)`
