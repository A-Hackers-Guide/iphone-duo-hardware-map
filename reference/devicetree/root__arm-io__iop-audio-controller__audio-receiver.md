# `/arm-io/iop-audio-controller/audio-receiver`

- Name: `audio-receiver`
- Parent: [`/arm-io/iop-audio-controller`](root__arm-io__iop-audio-controller.md)
- phandle: `357`
- compatible: `iop-adma-stream,mca`
- device_type: `iop-audio-s`
- Children (1): [`/arm-io/iop-audio-controller/audio-receiver/audio-receiver`](root__arm-io__iop-audio-controller__audio-receiver__audio-receiver.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleIOPADMAStream` | `IOPAudioNode` | [`com.apple.driver.AppleIOPADMAStream`](../kexts/com.apple.driver.AppleIOPADMAStream.md) | `iop-adma-stream,mca` |

## All properties (7) [DT]

- **`AAPL,phandle`**: `357` (`0x165`) → phandle of [`/arm-io/iop-audio-controller/audio-receiver`](root__arm-io__iop-audio-controller__audio-receiver.md)
- **`clock-domain`**: `1835100526` (`0x6d61696e`) (four-char code `main`)
- **`compatible`**: `iop-adma-stream,mca`
- **`device_type`**: `iop-audio-s`
- **`dma-provider-tx`**: `base-s-adma-tx-3`
- **`identifier`**: `1919247222` (`0x72656376`) (four-char code `recv`)
- **`name`**: `audio-receiver`
