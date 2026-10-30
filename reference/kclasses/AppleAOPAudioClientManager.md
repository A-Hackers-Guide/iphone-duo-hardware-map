# `AppleAOPAudioClientManager`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md)
- Object size: `0xc0` (192 bytes)
- Metaclass: `0xfffffe000b932e48`; metaclass vtable `0xfffffe0007fa5670`; class vtable `0xfffffe0007fa5080`
- Registration (init): `0xfffffe000869c018`
- Superclasses: [`AppleAOPAudioDevice`](AppleAOPAudioDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 2 in total)

- [`AppleAOPAudioLEAPClientManager`](AppleAOPAudioLEAPClientManager.md) — `com.apple.driver.AppleAOPAudio`

## IOKit personalities that instantiate it (1)

- `AppleAOPAudioClientManager` in [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md): `IOProviderClass` = `AppleAOPAudioDeviceNode`, `IONameMatch` = `['audio-hp', 'audio-aop-ldcm', 'audio-aop-hawking', 'audio-leap-internal-loopbac`, `IOResourceMatch` = `IOKit`

## Device-tree nodes it binds (3) [DT]

- [`/arm-io/iop-audio-controller/audio-hp`](../devicetree/root__arm-io__iop-audio-controller__audio-hp.md) on `audio-hp`
- [`/arm-io/iop-audio-controller/audio-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-leap-internal-loopback.md) on `audio-leap-internal-loopback`
- [`/arm-io/iop-audio-controller/audio-leap-internal-loopback/audio-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-leap-internal-loopback__audio-leap-internal-loopback.md) on `audio-leap-internal-loopback`

## Strings in its kext that name it (2)

- `AppleAOPAudioClientManager`
- `site.AppleAOPAudioClientManager`
