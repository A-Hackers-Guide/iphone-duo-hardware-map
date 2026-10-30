# `AppleASCWrapV8SISP`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md)
- Object size: `0x1d8` (472 bytes)
- Metaclass: `0xfffffe000b9321c8`; metaclass vtable `0xfffffe0007f96570`; class vtable `0xfffffe0007f95e30`
- Registration (init): `0xfffffe000866c018`
- Superclasses: [`AppleASCWrapV8`](AppleASCWrapV8.md) → [`AppleA7IOP`](AppleA7IOP.md) → [`AppleIOP`](AppleIOP.md) → [`IOSlaveCPU`](IOSlaveCPU.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleASCWrapV8SISP` in [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['iop-isp,ascwrap-v8']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) on `iop-isp,ascwrap-v8`

## Strings in its kext that name it (2)

- `site.AppleASCWrapV8SISP`
- `AppleASCWrapV8SISP`
