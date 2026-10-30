# `AppleASCWrapV8ANE`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md)
- Object size: `0x1d8` (472 bytes)
- Metaclass: `0xfffffe000b9321f0`; metaclass vtable `0xfffffe0007f96d48`; class vtable `0xfffffe0007f96608`
- Registration (init): `0xfffffe000866c760`
- Superclasses: [`AppleASCWrapV8`](AppleASCWrapV8.md) → [`AppleA7IOP`](AppleA7IOP.md) → [`AppleIOP`](AppleIOP.md) → [`IOSlaveCPU`](IOSlaveCPU.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleASCWrapV8ANE` in [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['iop-ane,ascwrap-v8']`

## Device-tree nodes it binds (2) [DT]

- [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) on `iop-ane,ascwrap-v8`
- [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) on `iop-ane,ascwrap-v8`

## Strings in its kext that name it (2)

- `AppleASCWrapV8ANE`
- `site.AppleASCWrapV8ANE`
