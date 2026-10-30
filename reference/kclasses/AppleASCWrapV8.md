# `AppleASCWrapV8`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md)
- Object size: `0x1d8` (472 bytes)
- Metaclass: `0xfffffe000b932178`; metaclass vtable `0xfffffe0007f955c0`; class vtable `0xfffffe0007f94e80`
- Registration (init): `0xfffffe000866b604`
- Superclasses: [`AppleA7IOP`](AppleA7IOP.md) → [`AppleIOP`](AppleIOP.md) → [`IOSlaveCPU`](IOSlaveCPU.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (3; 3 in total)

- [`AppleASCWrapV8ANE`](AppleASCWrapV8ANE.md) — `com.apple.driver.AppleA7IOP-ASCWrap-v8`
- [`AppleASCWrapV8SEP`](AppleASCWrapV8SEP.md) — `com.apple.driver.AppleA7IOP-ASCWrap-v8`
- [`AppleASCWrapV8SISP`](AppleASCWrapV8SISP.md) — `com.apple.driver.AppleA7IOP-ASCWrap-v8`

## IOKit personalities that instantiate it (1)

- `AppleASCWrapV8` in [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['iop,ascwrap-v8']`

## Device-tree nodes it binds (12) [DT]

- [`/arm-io/aop`](../devicetree/root__arm-io__aop.md) on `iop,ascwrap-v8`
- [`/arm-io/aop2`](../devicetree/root__arm-io__aop2.md) on `iop,ascwrap-v8`
- [`/arm-io/pmp`](../devicetree/root__arm-io__pmp.md) on `iop,ascwrap-v8`
- [`/arm-io/sio`](../devicetree/root__arm-io__sio.md) on `iop,ascwrap-v8`
- [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) on `iop,ascwrap-v8`
- [`/arm-io/smc`](../devicetree/root__arm-io__smc.md) on `iop,ascwrap-v8`
- [`/arm-io/mtp`](../devicetree/root__arm-io__mtp.md) on `iop,ascwrap-v8`
- [`/arm-io/dcp`](../devicetree/root__arm-io__dcp.md) on `iop,ascwrap-v8`
- [`/arm-io/dcpsec`](../devicetree/root__arm-io__dcpsec.md) on `iop,ascwrap-v8`
- [`/arm-io/dcpext0`](../devicetree/root__arm-io__dcpext0.md) on `iop,ascwrap-v8`
- [`/arm-io/gfx-asc`](../devicetree/root__arm-io__gfx-asc.md) on `iop,ascwrap-v8`
- [`/arm-io/gfx1-asc`](../devicetree/root__arm-io__gfx1-asc.md) on `iop,ascwrap-v8`

## Strings in its kext that name it (10)

- `AppleASCWrapV8SEP`
- `AppleASCWrapV8`
- `site.AppleASCWrapV8`
- `site.AppleASCWrapV8SISP`
- `site.AppleASCWrapV8SEP`
- `AppleASCWrapV8ANE`
- `site.AppleASCWrapV8ANE`
- `virtual IOReturn AppleASCWrapV8::getMailboxBulk(void *, unsigned int *)`
- `AppleASCWrapV8SISP`
- `virtual bool AppleASCWrapV8::initialize()`
