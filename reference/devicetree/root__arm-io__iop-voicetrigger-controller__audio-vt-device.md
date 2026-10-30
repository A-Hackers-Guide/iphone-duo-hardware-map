# `/arm-io/iop-voicetrigger-controller/audio-vt-device`

- Name: `audio-vt-device`
- Parent: [`/arm-io/iop-voicetrigger-controller`](root__arm-io__iop-voicetrigger-controller.md)
- phandle: `383`
- compatible: `iop-audio,isolated-vt-device`
- device_type: `iop-nub`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IOPAudioIsolatedVoiceTriggerDevice` | `IOPAudioNode` | [`com.apple.driver.IOPAudioVoiceTriggerDevice`](../kexts/com.apple.driver.IOPAudioVoiceTriggerDevice.md) | `iop-audio,isolated-vt-device` |

## Firmware with a matching name [FW]

- [`Firmware/all_flash/DeviceTree.v68ap.im4p`](../firmware/Firmware__all_flash__DeviceTree.v68ap.im4p.md) (74,512 B) Tag: IM4P  Type: dtre  Version: EmbeddedDeviceTrees-12661.52.3

## All properties (8) [DT]

- **`AAPL,phandle`**: `383` (`0x17f`) → phandle of [`/arm-io/iop-voicetrigger-controller/audio-vt-device`](root__arm-io__iop-voicetrigger-controller__audio-vt-device.md)
- **`compatible`**: `iop-audio,isolated-vt-device`
- **`device_type`**: `iop-nub`
- **`exclave-assigned`**: (present, empty)
- **`exclave-edk-service`**: `com.apple.service.AudioDriverVT_EDK`
- **`exclave-service`**: `com.apple.service.AudioDriverVT`
- **`identifier`**: `1987339117` (`0x7674636d`) (four-char code `vtcm`)
- **`name`**: `audio-vt-device`
