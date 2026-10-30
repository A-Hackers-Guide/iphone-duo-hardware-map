# `IOUSBMassStorageDriverNub`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOUSBMassStorageDriver`](../kexts/com.apple.iokit.IOUSBMassStorageDriver.md)
- Object size: `0x688` (1,672 bytes)
- Metaclass: `0xfffffe000ba20c10`; metaclass vtable `0xfffffe00084765b0`; class vtable `0xfffffe0008476028`
- Registration (init): `0xfffffe000a8686e0`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`com_apple_driver_AppleUSBCardReaderDriverNub`](com_apple_driver_AppleUSBCardReaderDriverNub.md) — `com.apple.driver.AppleUSBCardReader`

## IOKit personalities that instantiate it (1)

- `IOUSBMassStorageDriverNub` in [`com.apple.iokit.IOUSBMassStorageDriver`](../kexts/com.apple.iokit.IOUSBMassStorageDriver.md): `IOProviderClass` = `IOUSBMassStorageInterfaceNub`

## Strings in its kext that name it (4)

- `site.IOUSBMassStorageDriverNubExpansionData`
- `site.IOUSBMassStorageDriverNub`
- `IOUSBMassStorageDriverNub`
- `USB device %016llX - fIOUSBMassStorageDriverNub->terminate().\n`
