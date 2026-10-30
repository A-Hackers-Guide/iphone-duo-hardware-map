# `AppleSPURoseDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSPURose`](../kexts/com.apple.driver.AppleSPURose.md)
- Object size: `0x2f0` (752 bytes)
- Metaclass: `0xfffffe000b99dca8`; metaclass vtable `0xfffffe0008225530`; class vtable `0xfffffe0008224e88`
- Registration (init): `0xfffffe000970dd94`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSPURoseDriver` in [`com.apple.driver.AppleSPURose`](../kexts/com.apple.driver.AppleSPURose.md): `IOProviderClass` = `AppleSPUAppInterface`, `IONameMatch` = `['rose']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) on `rose`

## Strings in its kext that name it (16)

- `AppleSPURoseDriver`
- `/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/Rose/AppleSPURose/RoseV2/AppleSPURoseDriverV2.cpp`
- `AppleSPURoseDriverUserClient`
- `selector < (uint32_t) kAppleSPURoseDriverNumberOfMethods`
- `site.AppleSPURoseDriverV2`
- `/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/Rose/AppleSPURose/RoseV1/AppleSPURoseDriverUCV1.cpp`
- `AppleSPURoseDriverUserClientV2`
- `/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/Rose/AppleSPURose/RoseV2/AppleSPURoseDriverUCV2.cpp`
- `AppleSPURoseDriver.cpp`
- `site.AppleSPURoseDriverUserClientV2`
- `site.AppleSPURoseDriverUserClient`
- `AppleSPURoseDriverV2`
- `/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/Rose/AppleSPURose/RoseV1/AppleSPURoseDriver.cpp`
- `site.AppleSPURoseDriver`
- `AppleSPURoseDriver::handleClose`
- `AppleSPURoseDriver::handleOpen ret=%d`
