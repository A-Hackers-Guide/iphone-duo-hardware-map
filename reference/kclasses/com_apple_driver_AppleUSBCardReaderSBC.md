# `com_apple_driver_AppleUSBCardReaderSBC`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleUSBCardReader`](../kexts/com.apple.driver.AppleUSBCardReader.md)
- Object size: `0x180` (384 bytes)
- Metaclass: `0xfffffe000b9a5680`; metaclass vtable `0xfffffe0008239848`; class vtable `0xfffffe0008238fe8`
- Registration (init): `0xfffffe000978393c`
- Superclasses: [`IOSCSIPeripheralDeviceType00`](IOSCSIPeripheralDeviceType00.md) → [`IOSCSIBlockCommandsDevice`](IOSCSIBlockCommandsDevice.md) → [`IOSCSIPrimaryCommandsDevice`](IOSCSIPrimaryCommandsDevice.md) → [`IOSCSIProtocolInterface`](IOSCSIProtocolInterface.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSDCardReader` in [`com.apple.driver.AppleUSBCardReader`](../kexts/com.apple.driver.AppleUSBCardReader.md): `IOProviderClass` = `IOSCSILogicalUnitNub`

## Strings in its kext that name it (2)

- `site.com_apple_driver_AppleUSBCardReaderSBC`
- `com_apple_driver_AppleUSBCardReaderSBC`
