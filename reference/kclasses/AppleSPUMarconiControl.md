# `AppleSPUMarconiControl`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md)
- Object size: `0xa8` (168 bytes)
- Metaclass: `0xfffffe000b99cd60`; metaclass vtable `0xfffffe0008212be0`; class vtable `0xfffffe0008212688`
- Registration (init): `0xfffffe00096ccac4`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSPUMarconiControl` in [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md): `IOProviderClass` = `AppleSPUAppInterface`, `IONameMatch` = `['aop-marconi-bt-control']`, `IOMatchCategory` = `AppleSPUMarconiControl`

## Strings in its kext that name it (6)

- `AppleSPUMarconiControl`
- `com.apple.drivers.AppleSPUMarconiControl`
- `site.AppleSPUMarconiControl`
- `AppleSPUMarconiControl Failed setPowerEnable %d, %d`
- `AppleSPUMarconiControl setPowerEnable %d time %lldus (%lld)\n`
- `AppleSPUMarconiControl setPowerEnable [Caching State] %d, %d time %lldus (%lld)`
