# `/arm-io/iop-audio-controller/audio-haptic-leap`

- Name: `audio-haptic-leap`
- Parent: [`/arm-io/iop-audio-controller`](root__arm-io__iop-audio-controller.md)
- phandle: `380`
- compatible: `iop-audio,haptics-leap-control-device`
- device_type: `iop-audio-ns`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IOPAudioHapticsLEAPControlDevice` | `IOPAudioNode` | [`com.apple.driver.IOPAudioHapticsLEAPControlDevice`](../kexts/com.apple.driver.IOPAudioHapticsLEAPControlDevice.md) | `iop-audio,haptics-leap-control-device` |
| `AppleAOPAudioHapticLEAP` | `AppleAOPAudioDeviceNode` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) | `audio-haptic-leap` |

## Firmware with a matching name [FW]

- [`Firmware/V68_HapticAssets.im4p`](../firmware/Firmware__V68_HapticAssets.im4p.md) (1,174 B) Tag: IM4P  Type: hpas  Version: 1
- [`Firmware/V68_LeapHapticsFirmware.im4p`](../firmware/Firmware__V68_LeapHapticsFirmware.im4p.md) (283,085 B) Tag: IM4P  Type: lphp  Version: 1

## All properties (8) [DT]

- **`AAPL,phandle`**: `380` (`0x17c`) → phandle of [`/arm-io/iop-audio-controller/audio-haptic-leap`](root__arm-io__iop-audio-controller__audio-haptic-leap.md)
- **`compatible`**: `iop-audio,haptics-leap-control-device`
- **`device_type`**: `iop-audio-ns`
- **`identifier`**: `1819307363` (`0x6c706d63`) (four-char code `lpmc`)
- **`kci-name`**: `AppleHapticsAudioInterface`
- **`name`**: `audio-haptic-leap`
- **`parking-node-id`**: `1886546766` (`0x70726b4e`) (four-char code `prkN`)
- **`remote-node-interface`**: `381` (`0x17d`)
