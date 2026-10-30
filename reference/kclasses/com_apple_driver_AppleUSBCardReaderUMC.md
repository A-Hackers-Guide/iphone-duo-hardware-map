# `com_apple_driver_AppleUSBCardReaderUMC`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleUSBCardReader`](../kexts/com.apple.driver.AppleUSBCardReader.md)
- Object size: `0x1f0` (496 bytes)
- Metaclass: `0xfffffe000b9a56d8`; metaclass vtable `0xfffffe000823a588`; class vtable `0xfffffe0008239ee0`
- Registration (init): `0xfffffe00097855a0`
- Superclasses: [`IOUSBMassStorageDriver`](IOUSBMassStorageDriver.md) → [`IOSCSIProtocolServices`](IOSCSIProtocolServices.md) → [`IOSCSIProtocolInterface`](IOSCSIProtocolInterface.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `Apple_Internal_SD_Card_Reader_4_00` in [`com.apple.driver.AppleUSBCardReader`](../kexts/com.apple.driver.AppleUSBCardReader.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`
- `Apple_Internal_SD_Card_Reader_6_00` in [`com.apple.driver.AppleUSBCardReader`](../kexts/com.apple.driver.AppleUSBCardReader.md): `IOProviderClass` = `IOUSBMassStorageDriverNub`

## Strings in its kext that name it (2)

- `com_apple_driver_AppleUSBCardReaderUMC`
- `site.com_apple_driver_AppleUSBCardReaderUMC`
