# `AppleSPUDCPDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md)
- Object size: `0xc0` (192 bytes)
- Metaclass: `0xfffffe000b99ce50`; metaclass vtable `0xfffffe0008214b20`; class vtable `0xfffffe00082145c8`
- Registration (init): `0xfffffe00096ceb90`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSPUDCPDriver` in [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md): `IOProviderClass` = `AppleSPUAppInterface`, `IONameMatch` = `['dcp-control']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/aop/iop-aop-nub/dcp-control`](../devicetree/root__arm-io__aop__iop-aop-nub__dcp-control.md) on `dcp-control`

## Strings in its kext that name it (2)

- `AppleSPUDCPDriver`
- `site.AppleSPUDCPDriver`
