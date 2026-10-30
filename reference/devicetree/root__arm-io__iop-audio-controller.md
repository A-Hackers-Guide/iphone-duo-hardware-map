# `/arm-io/iop-audio-controller`

- Name: `iop-audio-controller`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `350`
- compatible: `iop-audio,controller`
- device_type: `iop-audio-controller`
- Children (20): [`/arm-io/iop-audio-controller/audio-hp`](root__arm-io__iop-audio-controller__audio-hp.md), [`/arm-io/iop-audio-controller/audio-leap-internal-loopback`](root__arm-io__iop-audio-controller__audio-leap-internal-loopback.md), [`/arm-io/iop-audio-controller/audio-mca-loopback`](root__arm-io__iop-audio-controller__audio-mca-loopback.md), [`/arm-io/iop-audio-controller/audio-receiver`](root__arm-io__iop-audio-controller__audio-receiver.md), [`/arm-io/iop-audio-controller/audio-flicker`](root__arm-io__iop-audio-controller__audio-flicker.md), [`/arm-io/iop-audio-controller/audio-s-leap-internal-loopback`](root__arm-io__iop-audio-controller__audio-s-leap-internal-loopback.md), [`/arm-io/iop-audio-controller/lp-mic-device`](root__arm-io__iop-audio-controller__lp-mic-device.md), [`/arm-io/iop-audio-controller/lp-mic-io-buffer-device`](root__arm-io__iop-audio-controller__lp-mic-io-buffer-device.md), [`/arm-io/iop-audio-controller/siri-listening-device`](root__arm-io__iop-audio-controller__siri-listening-device.md), [`/arm-io/iop-audio-controller/lp-mic-injection-device`](root__arm-io__iop-audio-controller__lp-mic-injection-device.md), [`/arm-io/iop-audio-controller/audio-speaker-mca`](root__arm-io__iop-audio-controller__audio-speaker-mca.md), [`/arm-io/iop-audio-controller/audio-speaker-tap`](root__arm-io__iop-audio-controller__audio-speaker-tap.md), [`/arm-io/iop-audio-controller/audio-speaker`](root__arm-io__iop-audio-controller__audio-speaker.md), [`/arm-io/iop-audio-controller/audio-haptic`](root__arm-io__iop-audio-controller__audio-haptic.md), [`/arm-io/iop-audio-controller/audio-haptic-transport`](root__arm-io__iop-audio-controller__audio-haptic-transport.md), [`/arm-io/iop-audio-controller/audio-hw-pcm-audiomgr`](root__arm-io__iop-audio-controller__audio-hw-pcm-audiomgr.md), [`/arm-io/iop-audio-controller/audio-hpdbg`](root__arm-io__iop-audio-controller__audio-hpdbg.md), [`/arm-io/iop-audio-controller/audio-hpdbg-transport`](root__arm-io__iop-audio-controller__audio-hpdbg-transport.md), [`/arm-io/iop-audio-controller/audio-haptic-leap`](root__arm-io__iop-audio-controller__audio-haptic-leap.md), [`/arm-io/iop-audio-controller/audio-haptic-parking`](root__arm-io__iop-audio-controller__audio-haptic-parking.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IOPAudioController` | `AppleARMIODevice` | [`com.apple.iokit.IOPAudioDriverFamily`](../kexts/com.apple.iokit.IOPAudioDriverFamily.md) | `iop-audio,controller` |

## All properties (5) [DT]

- **`AAPL,phandle`**: `350` (`0x15e`) → phandle of [`/arm-io/iop-audio-controller`](root__arm-io__iop-audio-controller.md)
- **`compatible`**: `iop-audio,controller`
- **`device_type`**: `iop-audio-controller`
- **`iop-audio-service-name`**: `AOPAudioService`
- **`name`**: `iop-audio-controller`
