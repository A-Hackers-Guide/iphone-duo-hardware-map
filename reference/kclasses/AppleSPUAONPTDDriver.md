# `AppleSPUAONPTDDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md)
- Object size: `0xa0` (160 bytes)
- Metaclass: `0xfffffe000b99cea0`; metaclass vtable `0xfffffe0008215a50`; class vtable `0xfffffe00082154f8`
- Registration (init): `0xfffffe00096d0bb0`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSPUAONPTDDriver` in [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md): `IOProviderClass` = `AppleSPUAppInterface`, `IONameMatch` = `['aon-ptd']`, `IOMatchCategory` = `AppleSPUAONPTDDriver`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) on `aon-ptd`

## Strings in its kext that name it (2)

- `site.AppleSPUAONPTDDriver`
- `AppleSPUAONPTDDriver`
