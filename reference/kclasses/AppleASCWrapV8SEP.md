# `AppleASCWrapV8SEP`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md)
- Object size: `0x1d8` (472 bytes)
- Metaclass: `0xfffffe000b9321a0`; metaclass vtable `0xfffffe0007f95d98`; class vtable `0xfffffe0007f95658`
- Registration (init): `0xfffffe000866bb14`
- Superclasses: [`AppleASCWrapV8`](AppleASCWrapV8.md) → [`AppleA7IOP`](AppleA7IOP.md) → [`AppleIOP`](AppleIOP.md) → [`IOSlaveCPU`](IOSlaveCPU.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleASCWrapV8SEP` in [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['iop-sep,ascwrap-v8']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/sep`](../devicetree/root__arm-io__sep.md) on `iop-sep,ascwrap-v8`

## Strings in its kext that name it (2)

- `AppleASCWrapV8SEP`
- `site.AppleASCWrapV8SEP`
