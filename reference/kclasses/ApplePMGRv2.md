# `ApplePMGRv2`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.ApplePMGR`](../kexts/com.apple.driver.ApplePMGR.md)
- Object size: `0x700` (1,792 bytes)
- Metaclass: `0xfffffe000b9874a8`; metaclass vtable `0xfffffe0008190be8`; class vtable `0xfffffe00081901d0`
- Registration (init): `0xfffffe0009343e70`
- Superclasses: [`ApplePMGRBase`](ApplePMGRBase.md) → [`IOPMGR`](IOPMGR.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `ApplePMGRv2` in [`com.apple.driver.ApplePMGR`](../kexts/com.apple.driver.ApplePMGR.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `pmgr2,arch`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) on `pmgr2,arch`

## Strings in its kext that name it (20)

- `ApplePMGRv2.cpp`
- `UInt32 ApplePMGRv2::_getParamValue(Param)`
- `void ApplePMGRv2::_cpuTopologyInit()`
- `virtual bool ApplePMGRv2::start(IOService *)`
- `void ApplePMGRv2::_publishNubs(IORegistryEntry *)`
- `virtual void ApplePMGRv2::enableCPUCores(UInt64, bool)`
- `UInt32 ApplePMGRv2::_getCoreToDie(UInt32)`
- `ApplePMGRv2: Starting %s\n`
- `UInt32 ApplePMGRv2::_getComplexToDie(UInt32)`
- `ApplePMGRv2`
- `site.ApplePMGRv2`
- `ApplePMGRv2: Started %s\n`
- `virtual void ApplePMGRv2::_enablePSDService(uintptr_t, uintptr_t, uintptr_t, uintptr_t, char *)`
- `virtual void ApplePMGRv2::_enableDevice(uintptr_t, uintptr_t, uintptr_t, uintptr_t)`
- `AbstractPMGR *ApplePMGRv2::getChildPMGRInstance(UInt32) const`
- `void ApplePMGRv2::getPMGRChildInstances()`
- `void ApplePMGRv2::_initAnalyticsTimer()`
- `bool ApplePMGRv2::_validParam(Param)`
- `virtual ApplePMGRAnalytics *ApplePMGRv2::getAnalyticsManager(ApplePMGRAnalytics::ca_pmgr_type_t, ApplePMGRAnalytics::ca_ps_state_t, UInt32)`
- `ApplePMGRv2.h`
