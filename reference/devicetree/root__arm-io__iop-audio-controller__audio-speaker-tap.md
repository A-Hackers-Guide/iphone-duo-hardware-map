# `/arm-io/iop-audio-controller/audio-speaker-tap`

- Name: `audio-speaker-tap`
- Parent: [`/arm-io/iop-audio-controller`](root__arm-io__iop-audio-controller.md)
- phandle: `370`
- compatible: `iop-adma-stream,mca`
- device_type: `iop-audio-ns`
- Children (1): [`/arm-io/iop-audio-controller/audio-speaker-tap/audio-speaker-tap`](root__arm-io__iop-audio-controller__audio-speaker-tap__audio-speaker-tap.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleIOPADMAStream` | `IOPAudioNode` | [`com.apple.driver.AppleIOPADMAStream`](../kexts/com.apple.driver.AppleIOPADMAStream.md) | `iop-adma-stream,mca` |

## All properties (7) [DT]

- **`AAPL,phandle`**: `370` (`0x172`) → phandle of [`/arm-io/iop-audio-controller/audio-speaker-tap`](root__arm-io__iop-audio-controller__audio-speaker-tap.md)
- **`clock-domain`**: `1835100526` (`0x6d61696e`) (four-char code `main`)
- **`compatible`**: `iop-adma-stream,mca`
- **`device_type`**: `iop-audio-ns`
- **`dma-provider-rx`**: `base-ns-adma-rx-3`
- **`identifier`**: `1952542752` (`0x74617020`) (four-char code `tap `)
- **`name`**: `audio-speaker-tap`
