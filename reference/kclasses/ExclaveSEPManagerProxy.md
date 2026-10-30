# `ExclaveSEPManagerProxy`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.ExclaveSEPManagerProxy`](../kexts/com.apple.driver.ExclaveSEPManagerProxy.md)
- Object size: `0xd0` (208 bytes)
- Metaclass: `0xfffffe000b9e0490`; metaclass vtable `0xfffffe00082e0610`; class vtable `0xfffffe00082e00b8`
- Registration (init): `0xfffffe0009c61ac8`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `ExclaveSEPManagerProxy` in [`com.apple.driver.ExclaveSEPManagerProxy`](../kexts/com.apple.driver.ExclaveSEPManagerProxy.md): `IOProviderClass` = `IOService`, `IONameMatch` = `iop,exclave-sep-manager`, `IOProbeScore` = `10000`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/esm`](../devicetree/root__arm-io__esm.md) on `iop,exclave-sep-manager`

## Strings in its kext that name it (4)

- `ExclaveSEPManagerProxy`
- `ExclaveSEPManagerProxy.cpp`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/ExclaveSEPManager/Sources/ExclaveSEPManagerProxy/ExclaveSEPManagerProxy.cpp`
- `site.ExclaveSEPManagerProxy`
