# `com_apple_driver_AppleUSBCardReaderDriverNub`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleUSBCardReader`](../kexts/com.apple.driver.AppleUSBCardReader.md)
- Object size: `0x6c0` (1,728 bytes)
- Metaclass: `0xfffffe000b9a5630`; metaclass vtable `0xfffffe00082388a0`; class vtable `0xfffffe0008238318`
- Registration (init): `0xfffffe000978043c`
- Superclasses: [`IOUSBMassStorageDriverNub`](IOUSBMassStorageDriverNub.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `Apple_Internal_SD_Card_Reader_4_00_Driver_Nub` in [`com.apple.driver.AppleUSBCardReader`](../kexts/com.apple.driver.AppleUSBCardReader.md): `IOProviderClass` = `com_apple_driver_AppleUSBCardReaderInterfaceNub`
- `Apple_Internal_SD_Card_Reader_6_00_Driver_Nub` in [`com.apple.driver.AppleUSBCardReader`](../kexts/com.apple.driver.AppleUSBCardReader.md): `IOProviderClass` = `com_apple_driver_AppleUSBCardReaderInterfaceNub`

## Strings in its kext that name it (2)

- `site.com_apple_driver_AppleUSBCardReaderDriverNub`
- `com_apple_driver_AppleUSBCardReaderDriverNub`
