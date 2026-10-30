# `AppleM2ScalerCSCDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleM2ScalerCSCDriver`](../kexts/com.apple.driver.AppleM2ScalerCSCDriver.md)
- Object size: `0x640` (1,600 bytes)
- Metaclass: `0xfffffe000b979328`; metaclass vtable `0xfffffe0008150108`; class vtable `0xfffffe000814fb70`
- Registration (init): `0xfffffe000914c968`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `s5l8720x` in [`com.apple.driver.AppleM2ScalerCSCDriver`](../kexts/com.apple.driver.AppleM2ScalerCSCDriver.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['scaler,s5l8960x']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) on `scaler,s5l8960x`

## Strings in its kext that name it (10)

- `com.apple.AppleM2ScalerCSCDriver.blockEnablement`
- `AppleM2ScalerCSCDriver`
- `AppleM2ScalerCSCDriverFilters`
- `AppleM2ScalerCSCDriver::notify_event() req %d surface %d event %d value: %lld (%lld)\n`
- `/Library/Caches/com.apple.xbs/522A5A31-EB7C-4ABF-8E34-D1BC4D0B2069/TemporaryDirectory.PZnBn7/Sources/IOSurfaceAccelerator_kexts/AppleM2ScalerCSCDriver.cpp`
- `AppleM2ScalerCSCDriverFilters.cpp`
- `site.AppleM2ScalerCSCDriverFilters`
- `site.AppleM2ScalerCSCDriver`
- `/Library/Caches/com.apple.xbs/522A5A31-EB7C-4ABF-8E34-D1BC4D0B2069/TemporaryDirectory.PZnBn7/Sources/IOSurfaceAccelerator_kexts/AppleM2ScalerCSCDriverFilters.cpp`
- `AppleM2ScalerCSCDriver.cpp`
