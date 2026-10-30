# `AppleT8160MemCacheController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleT8160MCC`](../kexts/com.apple.driver.AppleT8160MCC.md)
- Object size: `0x5d0` (1,488 bytes)
- Metaclass: `0xfffffe000b9d0a48`; metaclass vtable `0xfffffe00082633c8`; class vtable `0xfffffe0008262ba8`
- Registration (init): `0xfffffe0009889e88`
- Superclasses: [`MemCacheCIP`](MemCacheCIP.md) → [`AppleMemCacheControllerV2`](AppleMemCacheControllerV2.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleMemCacheController` in [`com.apple.driver.AppleT8160MCC`](../kexts/com.apple.driver.AppleT8160MCC.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `mcc,t8160`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) on `mcc,t8160`

## Strings in its kext that name it (3)

- `AppleT8160MemCacheController.cpp`
- `AppleT8160MemCacheController`
- `site.AppleT8160MemCacheController`
