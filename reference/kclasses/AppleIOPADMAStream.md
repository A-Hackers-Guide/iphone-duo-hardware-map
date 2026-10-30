# `AppleIOPADMAStream`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleIOPADMAStream`](../kexts/com.apple.driver.AppleIOPADMAStream.md)
- Object size: `0x700` (1,792 bytes)
- Metaclass: `0xfffffe000b951558`; metaclass vtable `0xfffffe00081166e8`; class vtable `0xfffffe0008116020`
- Registration (init): `0xfffffe00090140a0`
- Superclasses: [`AppleIASMCA`](AppleIASMCA.md) → [`AppleARMIISController`](AppleARMIISController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleIOPADMAStream` in [`com.apple.driver.AppleIOPADMAStream`](../kexts/com.apple.driver.AppleIOPADMAStream.md): `IOProviderClass` = `IOPAudioNode`, `IONameMatch` = `['iop-adma-stream,mca', 'iop-adma-stream,leap', 'iop-adma-stream,sense', 'iop-ad`

## Device-tree nodes it binds (11) [DT]

- [`/arm-io/iop-audio-controller/audio-hp`](../devicetree/root__arm-io__iop-audio-controller__audio-hp.md) on `iop-adma-stream,mca`
- [`/arm-io/iop-audio-controller/audio-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-leap-internal-loopback.md) on `iop-adma-stream,leap`
- [`/arm-io/iop-audio-controller/audio-mca-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-mca-loopback.md) on `iop-adma-stream,mca`
- [`/arm-io/iop-audio-controller/audio-receiver`](../devicetree/root__arm-io__iop-audio-controller__audio-receiver.md) on `iop-adma-stream,mca`
- [`/arm-io/iop-audio-controller/audio-flicker`](../devicetree/root__arm-io__iop-audio-controller__audio-flicker.md) on `iop-adma-stream,mca`
- [`/arm-io/iop-audio-controller/audio-s-leap-internal-loopback`](../devicetree/root__arm-io__iop-audio-controller__audio-s-leap-internal-loopback.md) on `iop-adma-stream,leap`
- [`/arm-io/iop-audio-controller/lp-mic-injection-device`](../devicetree/root__arm-io__iop-audio-controller__lp-mic-injection-device.md) on `iop-adma-stream,mca`
- [`/arm-io/iop-audio-controller/audio-speaker-mca`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker-mca.md) on `iop-adma-stream,mca`
- [`/arm-io/iop-audio-controller/audio-speaker-tap`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker-tap.md) on `iop-adma-stream,mca`
- [`/arm-io/iop-audio-controller/audio-haptic-transport`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic-transport.md) on `iop-adma-stream,leap`
- [`/arm-io/iop-audio-controller/audio-hpdbg-transport`](../devicetree/root__arm-io__iop-audio-controller__audio-hpdbg-transport.md) on `iop-adma-stream,leap`

## Strings in its kext that name it (4)

- `/Library/Caches/com.apple.xbs/0B7523CF-8499-456F-8339-DF1B4FF76BA8/TemporaryDirectory.0iB1H1/Sources/AppleIOPADMAStream/Source/AppleIOPADMAStream.cpp`
- `/Library/Caches/com.apple.xbs/0B7523CF-8499-456F-8339-DF1B4FF76BA8/TemporaryDirectory.0iB1H1/Sources/AppleIOPADMAStream/Source/AppleIASMCA.cpp`
- `site.AppleIOPADMAStream`
- `AppleIOPADMAStream.cpp`
