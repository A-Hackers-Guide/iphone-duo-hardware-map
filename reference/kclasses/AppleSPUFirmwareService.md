# `AppleSPUFirmwareService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md)
- Object size: `0x1c0` (448 bytes)
- Metaclass: `0xfffffe000b99cbd0`; metaclass vtable `0xfffffe000820e720`; class vtable `0xfffffe000820e1a0`
- Registration (init): `0xfffffe00096c61a4`
- Superclasses: [`RTBuddyFirmwareService`](RTBuddyFirmwareService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (3)

- `AppleSPUFirmwareService-AOP` in [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md): `IOProviderClass` = `RTBuddyService`, `IOPropertyMatch` = `{'role': 'AOP'}`, `IOMatchCategory` = `RTBuddyFirmwareService`
- `AppleSPUFirmwareService-SPU` in [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md): `IOProviderClass` = `RTBuddyService`, `IOPropertyMatch` = `{'role': 'SPU'}`, `IOMatchCategory` = `RTBuddyFirmwareService`
- `AppleSPUFirmwareService-SPU2` in [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md): `IOProviderClass` = `RTBuddyService`, `IOPropertyMatch` = `{'role': 'SPU2'}`, `IOMatchCategory` = `RTBuddyFirmwareService`

## Strings in its kext that name it (3)

- `AppleSPUFirmwareService.cpp`
- `site.AppleSPUFirmwareService`
- `AppleSPUFirmwareService`
