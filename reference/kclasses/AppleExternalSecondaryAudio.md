# `AppleExternalSecondaryAudio`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md)
- Object size: `0x318` (792 bytes)
- Metaclass: `0xfffffe000b942170`; metaclass vtable `0xfffffe0008076818`; class vtable `0xfffffe0008075f78`
- Registration (init): `0xfffffe0008bfdf1c`
- Superclasses: [`AppleSecondaryAudio`](AppleSecondaryAudio.md) → [`AppleARMIISAudioDevice`](AppleARMIISAudioDevice.md) → [`AppleARMDMAAudioDevice`](AppleARMDMAAudioDevice.md) → [`IOAudio2Device`](IOAudio2Device.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AppleHapticsExternalSecondaryAudio`](AppleHapticsExternalSecondaryAudio.md) — `com.apple.driver.AppleEmbeddedAudio`

## IOKit personalities that instantiate it (1)

- `AppleExternalAudio` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,external`, `IOMatchCategory` = `AppleSecondaryAudio`

## Device-tree nodes it binds (6) [DT]

- [`/arm-io/iop-audio-controller/audio-leap-internal-loopback/audio-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-leap-internal-loopback__audio-leap-internal-loopback.md) on `audio-data,external`
- [`/arm-io/iop-audio-controller/audio-receiver/audio-receiver`](../devicetree/root__arm-io__iop-audio-controller__audio-receiver__audio-receiver.md) on `audio-data,external`
- [`/arm-io/iop-audio-controller/audio-flicker/audio-flicker`](../devicetree/root__arm-io__iop-audio-controller__audio-flicker__audio-flicker.md) on `audio-data,external`
- [`/arm-io/iop-audio-controller/audio-s-leap-internal-loopback/audio-s-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-s-leap-internal-loopback__audio-s-leap-internal-loopback.md) on `audio-data,external`
- [`/arm-io/iop-audio-controller/lp-mic-injection-device/lp-mic-injection-device`](../devicetree/root__arm-io__iop-audio-controller__lp-mic-injection-device__lp-mic-injection-device.md) on `audio-data,external`
- [`/arm-io/iop-audio-controller/audio-speaker-tap/audio-speaker-tap`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker-tap__audio-speaker-tap.md) on `audio-data,external`

## Strings in its kext that name it (2)

- `AppleExternalSecondaryAudio`
- `site.AppleExternalSecondaryAudio`
