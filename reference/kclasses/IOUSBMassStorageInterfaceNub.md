# `IOUSBMassStorageInterfaceNub`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOUSBMassStorageDriver`](../kexts/com.apple.iokit.IOUSBMassStorageDriver.md)
- Object size: `0x4f8` (1,272 bytes)
- Metaclass: `0xfffffe000ba20c38`; metaclass vtable `0xfffffe0008476bb0`; class vtable `0xfffffe0008476648`
- Registration (init): `0xfffffe000a86b0e4`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 2 in total)

- [`com_apple_driver_AppleUSBCardReaderInterfaceNub`](com_apple_driver_AppleUSBCardReaderInterfaceNub.md) — `com.apple.driver.AppleUSBCardReader`
- [`com_apple_driver_AppleUSBMassStorageInterfaceNub`](com_apple_driver_AppleUSBMassStorageInterfaceNub.md) — `com.apple.driver.AppleUSBMassStorageInterfaceNub`

## IOKit personalities that instantiate it (14)

- `IOUSBMassStorageInterfaceNubMMC` in [`com.apple.iokit.IOUSBMassStorageDriver`](../kexts/com.apple.iokit.IOUSBMassStorageDriver.md): `IOProviderClass` = `IOUSBHostInterface`
- `IOUSBMassStorageInterfaceNubQIC-157` in [`com.apple.iokit.IOUSBMassStorageDriver`](../kexts/com.apple.iokit.IOUSBMassStorageDriver.md): `IOProviderClass` = `IOUSBHostInterface`
- `IOUSBMassStorageInterfaceNubRBC` in [`com.apple.iokit.IOUSBMassStorageDriver`](../kexts/com.apple.iokit.IOUSBMassStorageDriver.md): `IOProviderClass` = `IOUSBHostInterface`
- `IOUSBMassStorageInterfaceNubSCSI` in [`com.apple.iokit.IOUSBMassStorageDriver`](../kexts/com.apple.iokit.IOUSBMassStorageDriver.md): `IOProviderClass` = `IOUSBHostInterface`
- `IOUSBMassStorageInterfaceNubSFF-8070i` in [`com.apple.iokit.IOUSBMassStorageDriver`](../kexts/com.apple.iokit.IOUSBMassStorageDriver.md): `IOProviderClass` = `IOUSBHostInterface`
- `IOUSBMassStorageInterfaceNubUFI` in [`com.apple.iokit.IOUSBMassStorageDriver`](../kexts/com.apple.iokit.IOUSBMassStorageDriver.md): `IOProviderClass` = `IOUSBHostInterface`
- `AppleSonyDSCDriver` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBHostInterface`
- `Buffalo_1041_566` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBHostInterface`
- `VIA_1356_3182` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBHostInterface`
- `VIA_16700_45154` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBHostInterface`
- `VIA_4703_42538` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBHostInterface`
- `VIA_4703_42826` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBHostInterface`
- `VIA_8457_1813` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBHostInterface`
- `VIA_8457_1814` in [`com.apple.driver.USBStorageDeviceSpecifics`](../kexts/com.apple.driver.USBStorageDeviceSpecifics.md): `IOProviderClass` = `IOUSBHostInterface`

## Strings in its kext that name it (2)

- `IOUSBMassStorageInterfaceNub`
- `site.IOUSBMassStorageInterfaceNub`
