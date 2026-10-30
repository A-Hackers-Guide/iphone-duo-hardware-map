# `AppleSPUBasebandDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md)
- Object size: `0xc0` (192 bytes)
- Metaclass: `0xfffffe000b99ccc0`; metaclass vtable `0xfffffe0008211070`; class vtable `0xfffffe0008210b18`
- Registration (init): `0xfffffe00096ca9d8`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSPUBasebandDriver` in [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md): `IOProviderClass` = `AppleSPUAppInterface`, `IONameMatch` = `['AOP_baseband']`

## Strings in its kext that name it (4)

- `AppleSPUBasebandDriver`
- `AppleSPUBasebandDriver BB-Uart quiescing: %s\n`
- `site.AppleSPUBasebandDriver`
- `AppleSPUBasebandDriver BB-Gyro coex: %s\n`
