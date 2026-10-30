# `IOPAudioController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOPAudioDriverFamily`](../kexts/com.apple.iokit.IOPAudioDriverFamily.md)
- Object size: `0xf0` (240 bytes)
- Metaclass: `0xfffffe000ba180a0`; metaclass vtable `0xfffffe00083cba78`; class vtable `0xfffffe00083cb4f0`
- Registration (init): `0xfffffe000a2ea7d0`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IOPAudioController` in [`com.apple.iokit.IOPAudioDriverFamily`](../kexts/com.apple.iokit.IOPAudioDriverFamily.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['iop-audio,controller']`

## Device-tree nodes it binds (2) [DT]

- [`/arm-io/iop-audio-controller`](../devicetree/root__arm-io__iop-audio-controller.md) on `iop-audio,controller`
- [`/arm-io/iop-voicetrigger-controller`](../devicetree/root__arm-io__iop-voicetrigger-controller.md) on `iop-audio,controller`

## Strings in its kext that name it (6)

- `virtual IOReturn IOPAudioController::powerStateDidChangeTo(IOPMPowerFlags, unsigned long, IOService *)_block_invoke`
- `IOPAudioController`
- `/Library/Caches/com.apple.xbs/C9C26AD7-9CB6-4E87-BD55-E0086C9C4601/TemporaryDirectory.bWezrQ/Sources/IOPAudioDriverFamily/src/kext/IOPAudioDriverFamily/controller/IOPAudioController/IOPAudioController.cpp`
- `IOPAudioController.cpp`
- `site.IOPAudioController`
- `virtual IOReturn IOPAudioController::setPowerState(unsigned long, IOService *)_block_invoke`
