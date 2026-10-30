# `AppleSecureRepair`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSecureRepair`](../kexts/com.apple.driver.AppleSecureRepair.md)
- Object size: `0x98` (152 bytes)
- Metaclass: `0xfffffe000b99e420`; metaclass vtable `0xfffffe000822b538`; class vtable `0xfffffe000822afe0`
- Registration (init): `0xfffffe000972c308`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSecureRepair` in [`com.apple.driver.AppleSecureRepair`](../kexts/com.apple.driver.AppleSecureRepair.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `secure-repair,1`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/secure-repair`](../devicetree/root__arm-io__secure-repair.md) on `secure-repair,1`

## Strings in its kext that name it (5)

- `site.AppleSecureRepair`
- `AppleSecureRepairUserClient`
- `site.AppleSecureRepairUserClient`
- `AppleSecureRepair`
- `com.apple.private.AppleSecureRepair.allow`
