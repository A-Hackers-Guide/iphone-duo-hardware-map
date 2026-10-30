# `AOPAudioService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AOPAudio2`](../kexts/com.apple.driver.AOPAudio2.md)
- Object size: `0xc0` (192 bytes)
- Metaclass: `0xfffffe000b931bb8`; metaclass vtable `0xfffffe0007f8ecf0`; class vtable `0xfffffe0007f8e770`
- Registration (init): `0xfffffe000860dfb0`
- Superclasses: [`IOPAudioService`](IOPAudioService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AOPAudioService` in [`com.apple.driver.AOPAudio2`](../kexts/com.apple.driver.AOPAudio2.md): `IOProviderClass` = `AppleSPUAppInterface`, `IONameMatch` = `['aop-audio', 'aop-voicetrigger', 'iop-audio,aop-service']`

## Device-tree nodes it binds (4) [DT]

- [`/arm-io/aop/iop-aop-nub/aop-audio`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-audio.md) on `iop-audio,aop-service`
- [`/arm-io/aop/iop-aop-nub/aop-audio`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-audio.md) on `aop-audio`
- [`/arm-io/aop/iop-aop-nub/aop-voicetrigger`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-voicetrigger.md) on `iop-audio,aop-service`
- [`/arm-io/aop/iop-aop-nub/aop-voicetrigger`](../devicetree/root__arm-io__aop__iop-aop-nub__aop-voicetrigger.md) on `aop-voicetrigger`

## Strings in its kext that name it (6)

- `AOPAudioService`
- `site.AOPAudioService`
- `/Library/Caches/com.apple.xbs/C9C26AD7-9CB6-4E87-BD55-E0086C9C4601/TemporaryDirectory.bWezrQ/Sources/IOPAudioDriverFamily/src/kext/AOPAudioDriver/service/AOPAudioService/AOPAudioService.cpp`
- `/Library/Caches/com.apple.xbs/C9C26AD7-9CB6-4E87-BD55-E0086C9C4601/TemporaryDirectory.bWezrQ/Sources/IOPAudioDriverFamily/src/kext/AOPAudioDriver/service/AOPAudioService/AOPAudioServicePrivate.cpp`
- `AOPAudioService::Private`
- `AOPAudioService.cpp`
