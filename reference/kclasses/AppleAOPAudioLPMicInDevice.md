# `AppleAOPAudioLPMicInDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md)
- Object size: `0xcf0` (3,312 bytes)
- Metaclass: `0xfffffe000b9332e0`; metaclass vtable `0xfffffe0007fad590`; class vtable `0xfffffe0007faceb8`
- Registration (init): `0xfffffe00086bf000`
- Superclasses: [`AppleAOPAudioDevice`](AppleAOPAudioDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleAOPAudioLPMicInDevice` in [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md): `IOProviderClass` = `AppleAOPAudioDeviceNode`, `IONameMatch` = `['audio-lp-mic-in', 'audio-aop-lp-mic-in']`, `IOResourceMatch` = `IOKit`

## Strings in its kext that name it (27)

- `AppleAOPAudioLPMicInDevice::%s stopIO failed, ret=%#x\n`
- `AppleAOPAudioLPMicInDevice::%s inEnable=%d. isListeningEnabled()=%d \n`
- `AppleAOPAudioLPMicInDevice::%s inEnable=%d. isListeningEnabled()=%d calling stopIO\n`
- `AppleAOPAudioLPMicInDevice::%s could not find property for \"%s\"`
- `AppleAOPAudioLPMicInDevice::%s enable=%d. notifyCodecOfFailure=%d\n`
- `AppleAOPAudioLPMicInDevice`
- `AppleAOPAudioLPMicInDevice::%s enable=%d. Request the codec to enable listening\n`
- `AppleAOPAudioLPMicInDevice::%s configureCodec failed for kAOPLPMicInDeviceStopIO, ret=%#x\n`
- `AppleAOPAudioLPMicInDevice::%s configureCodec failed for kAOPLPMicInDeviceListeningDisabled, ret=%#x\n`
- `+ AppleAOPAudioLPMicInDevice::%s \n`
- `AppleAOPAudioLPMicInDevice::%s startIO failed, ret=%#x\n`
- `AppleAOPAudioLPMicInDevice::%s inEnable=%d. Notify the codec to turn on\n`
- `AppleAOPAudioLPMicInDevice::%s enable=%d. isHardwareEnabled()=%d \n`
- `AppleAOPAudioLPMicInDevice::%s() device tree property has unexpected size %lu bytes, expected %lu\n`
- `AppleAOPAudioLPMicInDevice.cpp`
- `AppleAOPAudioLPMicInDevice::%s configureCodec failed for kAOPLPMicInDeviceListeningEnabled ret=%#x\n`
- `AppleAOPAudioLPMicInDevice::%s inEnable=%d. Notify the codec to turn off \n`
- `- AppleAOPAudioLPMicInDevice::%s \n`
- `+ AppleAOPAudioLPMicInDevice::%s inEnable=%d. mListeningEnabled=%d\n`
- `site.AppleAOPAudioLPMicInDevice`
- `AppleAOPAudioLPMicInDevice::%s inEnable=%d. notifyCodecOfFailure=%d\n`
- `AppleAOPAudioLPMicInDevice::%s could not find registry entry at path \"%s\"`
- `AppleAOPAudioLPMicInDevice::%s configureCodec for kAOPLPMicInDeviceStartIO failed ret=%#x\n`
- `AppleAOPAudioLPMicInDevice::%s enable=%d. Request the codec to disable listening\n`
- `- AppleAOPAudioLPMicInDevice::%s enable=%d. mListeningEnabled=%d ret=%#x\n`
- `AppleAOPAudioLPMicInDevice::%s enableListeningClientManager failed, ret=%#x\n`
- `AppleAOPAudioLPMicInDevice::%s configureCodec ret=%#x\n`
