# `AppleHPMLDCM`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md)
- Object size: `0x1f8` (504 bytes)
- Metaclass: `0xfffffe000b94ec80`; metaclass vtable `0xfffffe00080f3368`; class vtable `0xfffffe00080f2ce0`
- Registration (init): `0xfffffe0008f65db8`
- Superclasses: [`IOPortFeatureLDCM`](IOPortFeatureLDCM.md) → [`IOPortFeature`](IOPortFeature.md) → [`IOPortFamily`](IOPortFamily.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 2 in total)

- [`AppleHPMLDCMType2`](AppleHPMLDCMType2.md) — `com.apple.driver.AppleHPM`
- [`AppleHPMLDCMType3`](AppleHPMLDCMType3.md) — `com.apple.driver.AppleHPM`

## Strings in its kext that name it (25)

- `AppleHPMLDCM::start - Periodic data gathering enable = 0x%x\n`
- `AppleHPMLDCM::start - couldn't allocate periodic buffer, failing start\n`
- `AppleHPMLDCM::isVoltageDetected - raw 0x%x\n`
- `AppleHPMLDCM::setVbusPresent - called setting %x\n`
- `AppleHPMLDCMType2`
- `site.AppleHPMLDCMType3`
- `%s::%s(0x%x@0x%x): LDCM not started, service not of AppleHPMLDCM\n\n`
- `AppleHPMLDCM::start - unexpected provider\n`
- `site.AppleHPMLDCM`
- `AppleHPMLDCM::disableOVPInterrupt - disabling ldcm ovp error\n`
- `AppleHPMLDCM::getLDCMStatusRegister - Invalid ret length of 0x%x retry = 0x%x\n`
- `AppleHPMLDCM::getLDCMStatusRegister - invalid buffer length, data gathering aborted\n`
- `AppleHPMLDCM::start - Failed to get command gate\n`
- `AppleHPMLDCM::start - couldn't get workloop failing start\n`
- `AppleHPMLDCM::start - couldn't allocate waveform buffer, failing start\n`
- `AppleHPMLDCM`
- `AppleHPMLDCM::start - couldn't allocate status buffer, failing start\n`
- `AppleHPMLDCM::getHPMCommsBus - failed to get communication bus service, no messages will be sent`
- `site.AppleHPMLDCMType2`
- `AppleHPMLDCMType3`
- `AppleHPMLDCM::enableLDCMMitigation - Mitigation enable = 0x%x\n`
- `AppleHPMLDCM::start - couldn't find communications bus, failing start\n`
- `AppleHPMLDCM::start - couldn't allocate temp status buffer, failing start\n`
- `AppleHPMLDCM::start - Mitigations disable = 0x%x\n`
- `AppleHPMLDCM::getVbusPresent - called returning false\n`
