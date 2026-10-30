# `AppleUSBLightningAdapterBOS`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleUSBLightningAdapter`](../kexts/com.apple.driver.AppleUSBLightningAdapter.md)
- Object size: `0x88` (136 bytes)
- Metaclass: `0xfffffe000b9d58b8`; metaclass vtable `0xfffffe00082b2ca8`; class vtable `0xfffffe00082b2750`
- Registration (init): `0xfffffe0009b4df74`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (3)

- `A2868-EmbeddedUSB` in [`com.apple.driver.AppleUSBLightningAdapter`](../kexts/com.apple.driver.AppleUSBLightningAdapter.md): `IOProviderClass` = `AppleEmbeddedUSBDevice`
- `A2868-USB` in [`com.apple.driver.AppleUSBLightningAdapter`](../kexts/com.apple.driver.AppleUSBLightningAdapter.md): `IOProviderClass` = `IOUSBHostDevice`
- `A2869-USB` in [`com.apple.driver.AppleUSBLightningAdapter`](../kexts/com.apple.driver.AppleUSBLightningAdapter.md): `IOProviderClass` = `IOUSBHostDevice`

## Strings in its kext that name it (2)

- `site.AppleUSBLightningAdapterBOS`
- `AppleUSBLightningAdapterBOS`
