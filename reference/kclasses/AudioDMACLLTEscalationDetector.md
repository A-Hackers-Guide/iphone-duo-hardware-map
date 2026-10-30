# `AudioDMACLLTEscalationDetector`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AudioDMACLLTEscalationDetector-Gen1p0`](../kexts/com.apple.driver.AudioDMACLLTEscalationDetector-Gen1p0.md)
- Object size: `0x3c0` (960 bytes)
- Metaclass: `0xfffffe000b9deca8`; metaclass vtable `0xfffffe00082c3040`; class vtable `0xfffffe00082c2ad8`
- Registration (init): `0xfffffe0009bd3978`
- Superclasses: [`ADMACCEDInterface`](ADMACCEDInterface.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AudioDMACLLTEscalationDetector` in [`com.apple.driver.AudioDMACLLTEscalationDetector-Gen1p0`](../kexts/com.apple.driver.AudioDMACLLTEscalationDetector-Gen1p0.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['admacled,v1p0']`

## Device-tree nodes it binds (3) [DT]

- [`/arm-io/admac-dispint0-ced-ssw`](../devicetree/root__arm-io__admac-dispint0-ced-ssw.md) on `admacled,v1p0`
- [`/arm-io/admac-dispext0-ced-ssw`](../devicetree/root__arm-io__admac-dispext0-ced-ssw.md) on `admacled,v1p0`
- [`/arm-io/admac-aop-ced-ssw`](../devicetree/root__arm-io__admac-aop-ced-ssw.md) on `admacled,v1p0`

## Strings in its kext that name it (3)

- `AudioDMACLLTEscalationDetector`
- `site.AudioDMACLLTEscalationDetector`
- `AudioDMACLLTEscalationDetector.cpp`
