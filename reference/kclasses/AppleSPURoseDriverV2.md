# `AppleSPURoseDriverV2`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSPURose`](../kexts/com.apple.driver.AppleSPURose.md)
- Object size: `0x400` (1,024 bytes)
- Metaclass: `0xfffffe000b99dd20`; metaclass vtable `0xfffffe0008225f40`; class vtable `0xfffffe0008225818`
- Registration (init): `0xfffffe0009711f74`
- Superclasses: [`AppleSPURTKitOSClientDriver`](AppleSPURTKitOSClientDriver.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSPURoseDriverV2` in [`com.apple.driver.AppleSPURose`](../kexts/com.apple.driver.AppleSPURose.md): `IOProviderClass` = `AppleSPUAppInterface`, `IONameMatch` = `['rose']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) on `rose`

## Strings in its kext that name it (3)

- `/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/Rose/AppleSPURose/RoseV2/AppleSPURoseDriverV2.cpp`
- `site.AppleSPURoseDriverV2`
- `AppleSPURoseDriverV2`
