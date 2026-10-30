# `AppleUSBHubIICDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedUSBHost`](../kexts/com.apple.driver.AppleEmbeddedUSBHost.md)
- Object size: `0xb8` (184 bytes)
- Metaclass: `0xfffffe000b944b48`; metaclass vtable `0xfffffe0008097de8`; class vtable `0xfffffe0008097858`
- Registration (init): `0xfffffe0008c9f714`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleUSBHubIICDevice` in [`com.apple.driver.AppleEmbeddedUSBHost`](../kexts/com.apple.driver.AppleEmbeddedUSBHost.md): `IOProviderClass` = `AppleARMIICDevice`, `IONameMatch` = `usb-hub-i2c`

## Strings in its kext that name it (5)

- `AppleUSBHubIICDeviceTunables`
- `site.AppleUSBHubIICDevice`
- `AppleUSBHubIICDevice`
- `AppleUSBHubIICDeviceVendor`
- `AppleUSBHubIICDeviceResetFunction`
