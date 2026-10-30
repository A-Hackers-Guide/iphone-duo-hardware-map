# `/arm-io/iop-audio-controller/audio-hw-pcm-audiomgr`

- Name: `audio-hw-pcm-audiomgr`
- Parent: [`/arm-io/iop-audio-controller`](root__arm-io__iop-audio-controller.md)
- phandle: `376`
- compatible: `iop-audio,pcm-asset-manager-device`
- device_type: `iop-audio-ns`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IOPAudioPCMAssetManagerDevice` | `IOPAudioNode` | [`com.apple.driver.IOPAudioPCMAssetManagerDevice`](../kexts/com.apple.driver.IOPAudioPCMAssetManagerDevice.md) | `iop-audio,pcm-asset-manager-device` |
| `AppleAOPAudioPCMAssetManagerDevice` | `AppleAOPAudioDeviceNode` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) | `audio-hw-pcm-audiomgr` |

## All properties (6) [DT]

- **`AAPL,phandle`**: `376` (`0x178`) → phandle of [`/arm-io/iop-audio-controller/audio-hw-pcm-audiomgr`](root__arm-io__iop-audio-controller__audio-hw-pcm-audiomgr.md)
- **`compatible`**: `iop-audio,pcm-asset-manager-device`
- **`device_type`**: `iop-audio-ns`
- **`identifier`**: `1885564237` (`0x70636d4d`) (four-char code `pcmM`)
- **`kci-name`**: `AOPAudioHWPCMAssetManagerInterface`
- **`name`**: `audio-hw-pcm-audiomgr`
