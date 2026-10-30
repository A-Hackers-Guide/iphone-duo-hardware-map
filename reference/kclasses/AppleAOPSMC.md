# `AppleAOPSMC`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md)
- Object size: `0xa8` (168 bytes)
- Metaclass: `0xfffffe000b99b668`; metaclass vtable `0xfffffe0008203410`; class vtable `0xfffffe0008202eb8`
- Registration (init): `0xfffffe0009688310`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSMCAOP` in [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md): `IOProviderClass` = `AppleSMCInterface`, `IONameMatch` = `['smc-aop']`, `IOProbeScore` = `1000`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/smc/iop-smc-nub/smc-aop`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-aop.md) on `smc-aop`

## Strings in its kext that name it (7)

- `bool AppleAOPSMC::aopServiceMatched(void *, IOService *, IONotifier *)`
- `site.AppleAOPSMCLink`
- `AppleAOPSMC`
- `site.AppleAOPSMC`
- `IOReturn AppleAOPSMCLink::configureEndpoints(AppleSMCFamily *)`
- `AppleAOPSMCDriver`
- `static AppleAOPSMCLink *AppleAOPSMCLink::withProvider(IOService *)`
