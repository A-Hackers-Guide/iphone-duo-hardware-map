# `AppleCLCD2`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleMobileDispH19P-DCP`](../kexts/com.apple.driver.AppleMobileDispH19P-DCP.md)
- Object size: `0x61b8` (25,016 bytes)
- Metaclass: `0xfffffe000b97dad0`; metaclass vtable `0xfffffe0008174dc0`; class vtable `0xfffffe00081740d8`
- Registration (init): `0xfffffe000928ff80`
- Superclasses: [`UnifiedPipeline2`](UnifiedPipeline2.md) → [`IOMobileFramebufferAP`](IOMobileFramebufferAP.md) → [`IOMobileFramebufferService`](IOMobileFramebufferService.md) → [`IOMobileFramebuffer`](IOMobileFramebuffer.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleADBE0-8970X` in [`com.apple.driver.AppleMobileDispH19P-DCP`](../kexts/com.apple.driver.AppleMobileDispH19P-DCP.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['disp0,t8160', 'dispext0,t8160', 'dispsec,t8160']`

## Device-tree nodes it binds (3) [DT]

- [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) on `disp0,t8160`
- [`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) on `dispsec,t8160`
- [`/arm-io/dispext0`](../devicetree/root__arm-io__dispext0.md) on `dispext0,t8160`

## Strings in its kext that name it (2)

- `site.AppleCLCD2`
- `AppleCLCD2`
