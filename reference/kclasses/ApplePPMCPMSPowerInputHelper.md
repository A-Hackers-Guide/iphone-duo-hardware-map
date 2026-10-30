# `ApplePPMCPMSPowerInputHelper`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleiPhoneACSKPPM`](../kexts/com.apple.driver.AppleiPhoneACSKPPM.md)
- Object size: `0x1e0` (480 bytes)
- Metaclass: `0xfffffe000b9ddfc0`; metaclass vtable `0xfffffe00082bf480`; class vtable `0xfffffe00082bf3d0`
- Registration (init): `0xfffffe0009bb82d4`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Direct subclasses (1; 1 in total)

- [`ApplePPMCPMSPowerInputHelperBatteryFirmware`](ApplePPMCPMSPowerInputHelperBatteryFirmware.md) — `com.apple.driver.AppleiPhoneACSKPPM`

## Strings in its kext that name it (14)

- `virtual void ApplePPMCPMSPowerInputHelperBatteryFirmware::inputHandler(OSArray *, uint32_t)`
- `ApplePPMCPMSPowerInputHelper.cpp`
- `ApplePPMCPMSPowerInputHelperBatteryFirmware`
- `void ApplePPMCPMSPowerInputHelperBatteryFirmware::processSystemCapabilityData(OSDictionary *, uint8_t)`
- `void ApplePPMCPMSPowerInputHelper::setOverrideSystemCapability(OSArray *, uint8_t)`
- `void ApplePPMCPMSPowerInputHelperBatteryFirmware::processPowerConsumptionData(OSDictionary *, uint8_t)`
- `site.ApplePPMCPMSPowerInputHelper`
- `virtual float ApplePPMCPMSPowerInputHelperBatteryFirmware::getIOHIDMaxControlEffort()`
- `virtual float ApplePPMCPMSPowerInputHelperBatteryFirmware::getIOHIDMaxIntegratorState()`
- `bool ApplePPMCPMSPowerInputHelperBatteryFirmware::initWithParams(ApplePPM *)`
- `site.ApplePPMCPMSPowerInputHelperBatteryFirmware`
- `virtual void ApplePPMCPMSPowerInputHelperBatteryFirmware::getIOHIDPbatData(int32_t *, uint32_t)`
- `ApplePPMCPMSPowerInputHelper`
- `void ApplePPMCPMSPowerInputHelper::setOverridePowerConsumption(OSArray *, uint8_t)`
