# `ApplePPMPTDManagerBase`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleiPhoneACSKPPM`](../kexts/com.apple.driver.AppleiPhoneACSKPPM.md)
- Object size: `0x110` (272 bytes)
- Metaclass: `0xfffffe000b9ddd88`; metaclass vtable `0xfffffe00082be5a0`; class vtable `0xfffffe00082be4f0`
- Registration (init): `0xfffffe0009baa838`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Direct subclasses (2; 2 in total)

- [`ApplePPMAONPTDAdapter`](ApplePPMAONPTDAdapter.md) — `com.apple.driver.AppleiPhoneACSKPPM`
- [`ApplePPMPmgrAdapter`](ApplePPMPmgrAdapter.md) — `com.apple.driver.AppleiPhoneACSKPPM`

## Strings in its kext that name it (8)

- `static ApplePPMPTDManagerBase *ApplePPMPTDManagerBase::withPmgrProvider(ApplePMGRNub *, IOService *, lowerLayerUpdateHandlerType, fetchClientPowerConsumptionHandlerType, uint32_t)`
- `IOReturn ApplePPMPTDManagerBase::sendPacket()`
- `void ApplePPMPTDManagerBase::enableRangeInterrupt(bool)`
- `site.ApplePPMPTDManagerBase`
- `ApplePPMPTDManagerBase`
- `static ApplePPMPTDManagerBase *ApplePPMPTDManagerBase::withAONPTDProvider(IOService *, IOService *, lowerLayerUpdateHandlerType, fetchClientPowerConsumptionHandlerType, uint32_t)`
- `ApplePPMPTDManagerBase.cpp`
- `bool ApplePPMPTDManagerBase::processInboundEntry(InboundParseContext &, uint32_t, uint64_t)`
