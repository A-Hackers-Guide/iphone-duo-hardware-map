# `/arm-io/iop-voicetrigger-controller`

- Name: `iop-voicetrigger-controller`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `382`
- compatible: `iop-audio,controller`
- device_type: `iop-voicetrigger-controller`
- Children (1): [`/arm-io/iop-voicetrigger-controller/audio-vt-device`](root__arm-io__iop-voicetrigger-controller__audio-vt-device.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IOPAudioController` | `AppleARMIODevice` | [`com.apple.iokit.IOPAudioDriverFamily`](../kexts/com.apple.iokit.IOPAudioDriverFamily.md) | `iop-audio,controller` |

## All properties (5) [DT]

- **`AAPL,phandle`**: `382` (`0x17e`) → phandle of [`/arm-io/iop-voicetrigger-controller`](root__arm-io__iop-voicetrigger-controller.md)
- **`compatible`**: `iop-audio,controller`
- **`device_type`**: `iop-voicetrigger-controller`
- **`iop-audio-service-name`**: `AOPVoiceTriggerService`
- **`name`**: `iop-voicetrigger-controller`
