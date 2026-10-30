# `AppleGPIOCanary`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleGPIOCanary`](../kexts/com.apple.driver.AppleGPIOCanary.md)
- Object size: `0x98` (152 bytes)
- Metaclass: `0xfffffe000b9462e0`; metaclass vtable `0xfffffe00080b3b10`; class vtable `0xfffffe00080b35b8`
- Registration (init): `0xfffffe0008d02efc`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleGPIOCanary` in [`com.apple.driver.AppleGPIOCanary`](../kexts/com.apple.driver.AppleGPIOCanary.md): `IOProviderClass` = `IOService`, `IONameMatch` = `gpio-canary,t8101`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/gpio-canary`](../devicetree/root__arm-io__gpio-canary.md) on `gpio-canary,t8101`

## Strings in its kext that name it (4)

- `AppleGPIOCanary`
- `site.AppleGPIOCanary`
- `AppleGPIOCanary::start: this: %p\n`
- `AppleGPIOCanary.cpp`
