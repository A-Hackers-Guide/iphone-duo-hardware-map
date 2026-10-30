# `ApplePPMPolicyCPMSv2`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleiPhoneACSKPPM`](../kexts/com.apple.driver.AppleiPhoneACSKPPM.md)
- Object size: `0x5b48` (23,368 bytes)
- Metaclass: `0xfffffe000b9dddb0`; metaclass vtable `0xfffffe00082be880`; class vtable `0xfffffe00082be638`
- Registration (init): `0xfffffe0009bac9cc`
- Superclasses: [`ApplePPMPolicyCPMSPowerServo`](ApplePPMPolicyCPMSPowerServo.md) → [`ApplePPMPolicyCPMS`](ApplePPMPolicyCPMS.md)

## Strings in its kext that name it (14)

- `bool ApplePPMPolicyCPMSv2::initWithParams(IOService *, uint32_t, ApplePPMEDTData *, IOKitMessageCallbackType, IOKitMessageCallbackType)`
- `site.ApplePPMPolicyCPMSv2`
- `virtual float ApplePPMPolicyCPMSv2::controlEffortForLane(int)`
- `virtual void ApplePPMPolicyCPMSv2::updateACSKDroop(float)`
- `void ApplePPMPolicyCPMSv2::executeACSKBlocks()`
- `virtual void ApplePPMPolicyCPMSv2::setSystemStress(uint32_t, bool)`
- `virtual void ApplePPMPolicyCPMSv2::setIBInputs(uint32_t, float)`
- `ApplePPMPolicyCPMSv2`
- `virtual void ApplePPMPolicyCPMSv2::setPredictiveSysCap(uint32_t, int32_t, int32_t)`
- `virtual bool ApplePPMPolicyCPMSv2::getBrownoutRiskBool()`
- `virtual void ApplePPMPolicyCPMSv2::advanceServosWithPmargin(float)`
- `virtual bool ApplePPMPolicyCPMSv2::anyServosEngaged()`
- `static ApplePPMPolicyCPMSv2 *ApplePPMPolicyCPMSv2::withParams(IOService *, uint32_t, ApplePPMEDTData *, IOKitMessageCallbackType, IOKitMessageCallbackType)`
- `ApplePPMPolicyCPMSv2.cpp`
