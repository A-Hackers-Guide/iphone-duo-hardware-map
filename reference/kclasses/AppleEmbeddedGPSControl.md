# `AppleEmbeddedGPSControl`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedGPS`](../kexts/com.apple.driver.AppleEmbeddedGPS.md)
- Object size: `0x100` (256 bytes)
- Metaclass: `0xfffffe000b942d58`; metaclass vtable `0xfffffe00080815a0`; class vtable `0xfffffe0008081048`
- Registration (init): `0xfffffe0008c3056c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleEmbeddedGPSControl` in [`com.apple.driver.AppleEmbeddedGPS`](../kexts/com.apple.driver.AppleEmbeddedGPS.md): `IOProviderClass` = `IOService`, `IONameMatch` = `['gps,bcm4750', 'gps,bcm4773']`, `IOMatchCategory` = `AppleEmbeddedGPSControl`

## Strings in its kext that name it (5)

- `site.AppleEmbeddedGPSControlUserClient`
- `AppleEmbeddedGPSControlUserClient`
- `AppleEmbeddedGPSControl`
- `site.AppleEmbeddedGPSControl`
- `AppleEmbeddedGPSControl.cpp`
