# `ApplePPMCPMSSystemCapabilityMonitor`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleiPhoneACSKPPM`](../kexts/com.apple.driver.AppleiPhoneACSKPPM.md)
- Object size: `0x2f8` (760 bytes)
- Metaclass: `0xfffffe000b9dbec8`; metaclass vtable `0xfffffe00082bda30`; class vtable `0xfffffe00082bd760`
- Registration (init): `0xfffffe0009b9f3ec`
- Superclasses: [`ApplePPMSystemCapabilityMonitor`](ApplePPMSystemCapabilityMonitor.md)

## Direct subclasses (1; 1 in total)

- [`ApplePPMCPMSSysCapMonitorv2`](ApplePPMCPMSSysCapMonitorv2.md) — `com.apple.driver.AppleiPhoneACSKPPM`

## Strings in its kext that name it (15)

- `virtual bool ApplePPMCPMSSystemCapabilityMonitor::updateSystemCapabilityWithPPM()`
- `static ApplePPMCPMSSystemCapabilityMonitor *ApplePPMCPMSSystemCapabilityMonitor::withParent(ApplePPM *, uint8_t, uint8_t)`
- `virtual void ApplePPMCPMSSystemCapabilityMonitor::stepBatteryModel()`
- `virtual bool ApplePPMCPMSSystemCapabilityMonitor::getCPMSBatteryPmaxState(CPMSPPMBatteryPmaxData *)`
- `virtual void ApplePPMCPMSSystemCapabilityMonitor::initFallbackTables(ApplePPM *)`
- `void ApplePPMCPMSSystemCapabilityMonitor::consumeInternalSourceData(OSDictionary *)`
- `void ApplePPMCPMSSystemCapabilityMonitor::consumeKeySet(keySet *, uint32_t, OSDictionary *)`
- `ApplePPMCPMSSystemCapabilityMonitor.cpp`
- `virtual IOReturn ApplePPMCPMSSystemCapabilityMonitor::sendAsbLpemData()`
- `ApplePPMCPMSSystemCapabilityMonitor`
- `site.ApplePPMCPMSSystemCapabilityMonitor`
- `virtual bool ApplePPMCPMSSystemCapabilityMonitor::readBatteryInputFromASB()`
- `virtual bool ApplePPMCPMSSystemCapabilityMonitor::initWithParent(ApplePPM *, uint8_t, uint8_t)`
- `void ApplePPMCPMSSystemCapabilityMonitor::updateReadingsFromGasGauge()`
- `virtual bool ApplePPMCPMSSystemCapabilityMonitor::_asbArrivalHandler(void *, IOService *, IONotifier *)`
