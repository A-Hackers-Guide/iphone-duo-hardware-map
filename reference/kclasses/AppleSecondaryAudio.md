# `AppleSecondaryAudio`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md)
- Object size: `0x300` (768 bytes)
- Metaclass: `0xfffffe000b9420a8`; metaclass vtable `0xfffffe00080746c8`; class vtable `0xfffffe0008073e38`
- Registration (init): `0xfffffe0008bf9fc4`
- Superclasses: [`AppleARMIISAudioDevice`](AppleARMIISAudioDevice.md) → [`AppleARMDMAAudioDevice`](AppleARMDMAAudioDevice.md) → [`IOAudio2Device`](IOAudio2Device.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 3 in total)

- [`AppleActuatorSecondaryAudio`](AppleActuatorSecondaryAudio.md) — `com.apple.driver.AppleEmbeddedAudio`
- [`AppleExternalSecondaryAudio`](AppleExternalSecondaryAudio.md) — `com.apple.driver.AppleEmbeddedAudio`

## IOKit personalities that instantiate it (20)

- `AppleAOPMCALoopbackAudio` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,audio-aop-mca-loopback`, `IOMatchCategory` = `AppleSecondaryAudio`, `IOProbeScore` = `1000`
- `AppleBasebandAudio` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,baseband`, `IOMatchCategory` = `AppleBasebandAudio`, `IOProbeScore` = `1000`
- `AppleBasebandVoice` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,baseband-voice`, `IOMatchCategory` = `AppleBasebandVoiceAudio`, `IOProbeScore` = `1000`
- `AppleBluetoothVoice` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,bluetooth-voice`, `IOMatchCategory` = `AppleBluetoothVoiceAudio`, `IOProbeScore` = `1000`
- `AppleCS42L83InputAudio` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,cs42l83-input`, `IOMatchCategory` = `AppleSecondaryAudio`
- `AppleCS42L84InputAudio` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,cs42l84-input`, `IOMatchCategory` = `AppleSecondaryAudio`
- `AppleDSPDebug1` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,dsp-debug1`, `IOMatchCategory` = `AppleSecondaryAudio`, `IOProbeScore` = `1000`
- `AppleDSPDebug2` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,dsp-debug2`, `IOMatchCategory` = `AppleSecondaryAudio`, `IOProbeScore` = `1000`
- `AppleExtendedHapticDebug` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,ext-haptic-debug`, `IOMatchCategory` = `AppleSecondaryAudio`, `IOProbeScore` = `1000`
- `AppleHalogen` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,halogen`, `IOMatchCategory` = `AppleSecondaryAudio`
- `AppleHapticDebug` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,haptic-debug`, `IOMatchCategory` = `AppleSecondaryAudio`
- `AppleHawkingAudio` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,hawking`, `IOMatchCategory` = `AppleSecondaryAudio`, `IOProbeScore` = `1000`
- `AppleLoopbackAudio` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,audio-loopback`, `IOMatchCategory` = `AppleSecondaryAudio`, `IOProbeScore` = `1000`
- `AppleMaggieDebugAudio` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,maggie-debug`, `IOMatchCategory` = `AppleSecondaryAudio`, `IOProbeScore` = `1000`
- `AppleMikeyBusSecondaryAudio` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,mikeybus-secondary`, `IOMatchCategory` = `AppleSecondaryAudio`
- `AppleReferenceAudio` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,reference`, `IOMatchCategory` = `AppleSecondaryAudio`, `IOProbeScore` = `1000`
- `AppleSecondaryAudio` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,secondary`
- `AppleTapAudio` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,audio-tap`, `IOMatchCategory` = `AppleSecondaryAudio`, `IOProbeScore` = `1000`
- `AppleVirtualSecondary` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,virtual-secondary`, `IOMatchCategory` = `AppleSecondaryAudio`, `IOProbeScore` = `1000`
- `AppleVoiceAudio` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,voice`, `IOMatchCategory` = `AppleSecondaryAudio`, `IOProbeScore` = `1000`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/iop-audio-controller/audio-mca-loopback/audio-mca-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-mca-loopback__audio-mca-loopback.md) on `audio-data,audio-loopback`

## Strings in its kext that name it (4)

- `site.AppleSecondaryAudioFunction`
- `AppleSecondaryAudioFunction`
- `AppleSecondaryAudio`
- `site.AppleSecondaryAudio`
