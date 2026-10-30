# `ApplePPMPmgrAdapter`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleiPhoneACSKPPM`](../kexts/com.apple.driver.AppleiPhoneACSKPPM.md)
- Object size: `0x178` (376 bytes)
- Metaclass: `0xfffffe000b9dd480`; metaclass vtable `0xfffffe00082be038`; class vtable `0xfffffe00082bdf88`
- Registration (init): `0xfffffe0009ba4144`
- Superclasses: [`ApplePPMPTDManagerBase`](ApplePPMPTDManagerBase.md)

## Strings in its kext that name it (8)

- `virtual IOReturn ApplePPMPmgrAdapter::enableInterruptForSMCToPPM()`
- `virtual IOReturn ApplePPMPmgrAdapter::disableInterruptForSMCToPPM()`
- `virtual IOReturn ApplePPMPmgrAdapter::writeOutboundPacket(const uint64_t *, uint32_t, uint16_t, uint16_t)`
- `site.ApplePPMPmgrAdapter`
- `bool ApplePPMPmgrAdapter::initWithParams(ApplePMGRNub *, IOService *, lowerLayerUpdateHandlerType, fetchClientPowerConsumptionHandlerType, uint32_t)`
- `ApplePPMPmgrAdapter.cpp`
- `virtual void ApplePPMPmgrAdapter::handleRangeInterrupt(uint32_t)`
- `ApplePPMPmgrAdapter`
