# `ApplePMGRNub`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.ApplePMGR`](../kexts/com.apple.driver.ApplePMGR.md)
- Object size: `0x740` (1,856 bytes)
- Metaclass: `0xfffffe000b9879b0`; metaclass vtable `0xfffffe0008194538`; class vtable `0xfffffe0008193fe0`
- Registration (init): `0xfffffe0009351d68`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (20)

- `site.ApplePMGRNub`
- `\"ApplePMGRNub: %s:%u REQUIRE failed: %s\" @%s:%d`
- `void ApplePMGR::_handleCPUPerfRequest(CPUComplex *, UInt32, bool, UInt32, ApplePMGRNub::PerfLimitingReason)`
- `virtual void ApplePMGR::_handleCPUPerfRequest(UInt32, UInt32, bool, UInt32, ApplePMGRNub::PerfLimitingReason)`
- `IOReturn ApplePMGRNub::getPTDRangeInfo(UInt32, PTDRangeInfo &)`
- `IOReturn ApplePMGRNub::disablePTDEntryInterrupt(UInt32, UInt32)`
- `OSDictionary *ApplePMGRNub::getPerfDomainInfo(enum PerfDomain, UInt32)`
- `IOReturn ApplePMGRNub::writePTDEntry(UInt32, UInt32, UInt64)`
- `ApplePMGRNub`
- `bool ApplePMGRNub::initWithRegistryEntry(IORegistryEntry *, IOService *)`
- `void ApplePMGRNub::requestPerfState(UInt32, enum PerfDomain, UInt32)`
- `IOReturn ApplePMGRNub::dashboardOpsExternal(uint32_t, uintptr_t *)`
- `dvd->limitingReasonDVDFactor1 != ApplePMGRNub::kPerfLimitingReasonNone`
- `virtual IOReturn ApplePMGR::_getPTDRangeInfo(UInt32, ApplePMGRNub::PTDRangeInfo *, UInt32 *)`
- `site.ApplePMGRNub::DeviceDVFSState`
- `UInt64 ApplePMGRNub::getPTDInterruptStatus(UInt32)`
- `perfLimitReason >= ApplePMGRNub::kPerfLimitingReasonDVDFactor1Count`
- `IOReturn ApplePMGRNub::enablePTDEntryInterrupt(UInt32, UInt32)`
- `IOReturn ApplePMGRNub::readPTDEntry(UInt32, UInt32, PTDEntry &)`
- `ApplePMGRNub.cpp`
