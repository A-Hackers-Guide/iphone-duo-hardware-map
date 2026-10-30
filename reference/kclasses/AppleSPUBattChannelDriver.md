# `AppleSPUBattChannelDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md)
- Object size: `0xb0` (176 bytes)
- Metaclass: `0xfffffe000b99d430`; metaclass vtable `0xfffffe00082231a8`; class vtable `0xfffffe0008222c50`
- Registration (init): `0xfffffe00096ed544`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSPUBattChannelDriver` in [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md): `IOProviderClass` = `AppleSPUAppInterface`, `IONameMatch` = `['batt-adc']`

## Strings in its kext that name it (2)

- `site.AppleSPUBattChannelDriver`
- `AppleSPUBattChannelDriver`
