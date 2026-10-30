# `AppleBaseAudioController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md)
- Object size: `0xc0` (192 bytes)
- Metaclass: `0xfffffe000b933220`; metaclass vtable `0xfffffe0007face20`; class vtable `0xfffffe0007fac7c0`
- Registration (init): `0xfffffe00086b8a18`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AppleAOPAudioController`](AppleAOPAudioController.md) — `com.apple.driver.AppleAOPAudio`

## Strings in its kext that name it (4)

- `mCommandGate->runAction(OSMemberFunctionCast(IOCommandGate::Action, this, &AppleBaseAudioController::_accessRegister), reinterpret_cast<void *>(inDeviceId), static_cast<void *>(inDescriptor))`
- `AppleBaseAudioController.cpp`
- `AppleBaseAudioController`
- `site.AppleBaseAudioController`
