# `/arm-io/iop-audio-controller/audio-hp`

- Name: `audio-hp`
- Parent: [`/arm-io/iop-audio-controller`](root__arm-io__iop-audio-controller.md)
- phandle: `351`
- compatible: `iop-adma-stream,mca`
- device_type: `iop-audio-s`
- Children (1): [`/arm-io/iop-audio-controller/audio-hp/audio-codec`](root__arm-io__iop-audio-controller__audio-hp__audio-codec.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleIOPADMAStream` | `IOPAudioNode` | [`com.apple.driver.AppleIOPADMAStream`](../kexts/com.apple.driver.AppleIOPADMAStream.md) | `iop-adma-stream,mca` |
| `AppleAOPAudioClientManager` | `AppleAOPAudioDeviceNode` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) | `audio-hp` |

## All properties (7) [DT]

- **`AAPL,phandle`**: `351` (`0x15f`) → phandle of [`/arm-io/iop-audio-controller/audio-hp`](root__arm-io__iop-audio-controller__audio-hp.md)
- **`clock-domain`**: `1835100526` (`0x6d61696e`) (four-char code `main`)
- **`compatible`**: `iop-adma-stream,mca`
- **`device_type`**: `iop-audio-s`
- **`dma-provider-rx`**: `base-s-adma-rx-4`
- **`identifier`**: `1752195433` (`0x68706169`) (four-char code `hpai`)
- **`name`**: `audio-hp`
