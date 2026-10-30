# `/arm-io/iop-audio-controller/audio-speaker-mca`

- Name: `audio-speaker-mca`
- Parent: [`/arm-io/iop-audio-controller`](root__arm-io__iop-audio-controller.md)
- phandle: `368`
- compatible: `iop-adma-stream,mca`
- device_type: `iop-audio-s`
- Children (1): [`/arm-io/iop-audio-controller/audio-speaker-mca/audio-speaker`](root__arm-io__iop-audio-controller__audio-speaker-mca__audio-speaker.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleIOPADMAStream` | `IOPAudioNode` | [`com.apple.driver.AppleIOPADMAStream`](../kexts/com.apple.driver.AppleIOPADMAStream.md) | `iop-adma-stream,mca` |

## All properties (8) [DT]

- **`AAPL,phandle`**: `368` (`0x170`) → phandle of [`/arm-io/iop-audio-controller/audio-speaker-mca`](root__arm-io__iop-audio-controller__audio-speaker-mca.md)
- **`clock-domain`**: `1835100526` (`0x6d61696e`) (four-char code `main`)
- **`compatible`**: `iop-adma-stream,mca`
- **`device_type`**: `iop-audio-s`
- **`dma-provider-rx`**: `base-ns-adma-rx-2`
- **`dma-provider-tx`**: `base-s-adma-tx-2`
- **`identifier`**: `1836281963` (`0x6d73706b`) (four-char code `mspk`)
- **`name`**: `audio-speaker-mca`
