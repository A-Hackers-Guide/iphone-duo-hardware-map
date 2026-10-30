# `ApplePMGRv2Impl`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleT8160PMGR`](../kexts/com.apple.driver.AppleT8160PMGR.md)
- Object size: `0x118` (280 bytes)
- Metaclass: `0xfffffe000b9d13e0`; metaclass vtable `0xfffffe000826f038`; class vtable `0xfffffe000826e7d8`
- Registration (init): `0xfffffe00098cebc8`
- Superclasses: [`AbstractPMGR`](AbstractPMGR.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AppleT8160PMGR`](AppleT8160PMGR.md) — `com.apple.driver.AppleT8160PMGR`

## Strings in its kext that name it (18)

- `virtual void ApplePMGRv2Impl::enableCPUCores(UInt64, bool)`
- `virtual UInt32 ApplePMGRv2Impl::getCurrentCPU()`
- `site.ApplePMGRv2Impl`
- `virtual void ApplePMGRv2Impl::initCPUIdle(ml_processor_info_t *)`
- `void ApplePMGRv2Impl::_enableSystemInterrupts()`
- `ApplePMGRv2Impl.cpp`
- `virtual void ApplePMGRv2Impl::enableCPUCore(unsigned int)`
- `virtual void ApplePMGRv2Impl::_handleCPUPerfStateRequest(UInt32, UInt32, bool)`
- `virtual void ApplePMGRv2Impl::disableCPUCluster(unsigned int)`
- `virtual void ApplePMGRv2Impl::enterCPUIdle(UInt64 *)`
- `virtual OSDictionary *ApplePMGRv2Impl::_returnPerfDomainInfo(PerfDomainID)`
- `virtual void ApplePMGRv2Impl::disableCPUCore(unsigned int)`
- `virtual void ApplePMGRv2Impl::updateCPUIdle(UInt64 *)`
- `virtual OSDictionary *ApplePMGRv2Impl::getPerfDomainInfoForCPUClusterID(UInt32)`
- `virtual void ApplePMGRv2Impl::enableCPUCluster(unsigned int)`
- `virtual void ApplePMGRv2Impl::exitCPUIdle(UInt64 *)`
- `ApplePMGRv2Impl`
- `virtual bool ApplePMGRv2Impl::start(IOService *)`
