# `AppleAOPAudioController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md)
- Object size: `0xf0` (240 bytes)
- Metaclass: `0xfffffe000b933000`; metaclass vtable `0xfffffe0007fa8648`; class vtable `0xfffffe0007fa7fa0`
- Registration (init): `0xfffffe00086a6088`
- Superclasses: [`AppleBaseAudioController`](AppleBaseAudioController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleAOPAudioController` in [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md): `IOProviderClass` = `AppleSPUAppInterface`, `IONameMatch` = `['aop-audio']`, `IOResourceMatch` = `IOKit`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/aop/iop-aop-nub/aop-audio`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-audio.md) on `aop-audio`

## Strings in its kext that name it (4)

- `mService->RetrieveHistoricalData(AppleAOPAudioController::sHistoricalDataCallback, static_cast<OSObject*>(this))`
- `site.AppleAOPAudioController`
- `AppleAOPAudioController`
- `mService->RegisterCallback(AppleAOPAudioController::sServiceCallback, this)`
