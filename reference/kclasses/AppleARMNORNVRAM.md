# `AppleARMNORNVRAM`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md)
- Object size: `0xa0` (160 bytes)
- Metaclass: `0xfffffe000b934ad8`; metaclass vtable `0xfffffe0007fc56f8`; class vtable `0xfffffe0007fc5178`
- Registration (init): `0xfffffe0008732160`
- Superclasses: [`IONVRAMController`](IONVRAMController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `AppleARMNORNVRAM1` in [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md): `IOProviderClass` = `AppleARMNORFlashDevice`, `IONameMatch` = `nvram,chrp`
- `AppleARMNORNVRAM2` in [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md): `IOProviderClass` = `AppleARMNORFlashDevice`, `IONameMatch` = `nvram,nor`

## Strings in its kext that name it (3)

- `site.AppleARMNORNVRAM`
- `AppleARMNORNVRAM`
- `AppleARMNORNVRAM.cpp`
