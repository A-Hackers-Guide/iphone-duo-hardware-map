# `/arm-io/iop-audio-controller/audio-mca-loopback`

- Name: `audio-mca-loopback`
- Parent: [`/arm-io/iop-audio-controller`](root__arm-io__iop-audio-controller.md)
- phandle: `355`
- compatible: `iop-adma-stream,mca`
- device_type: `iop-audio-ns`
- Children (1): [`/arm-io/iop-audio-controller/audio-mca-loopback/audio-mca-loopback`](root__arm-io__iop-audio-controller__audio-mca-loopback__audio-mca-loopback.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleIOPADMAStream` | `IOPAudioNode` | [`com.apple.driver.AppleIOPADMAStream`](../kexts/com.apple.driver.AppleIOPADMAStream.md) | `iop-adma-stream,mca` |

## All properties (8) [DT]

- **`AAPL,phandle`**: `355` (`0x163`) → phandle of [`/arm-io/iop-audio-controller/audio-mca-loopback`](root__arm-io__iop-audio-controller__audio-mca-loopback.md)
- **`clock-domain`**: `1835100526` (`0x6d61696e`) (four-char code `main`)
- **`compatible`**: `iop-adma-stream,mca`
- **`device_type`**: `iop-audio-ns`
- **`dma-provider-rx`**: `base-ns-adma-rx-8`
- **`dma-provider-tx`**: `base-ns-adma-tx-8`
- **`identifier`**: `1819304555` (`0x6c70626b`) (four-char code `lpbk`)
- **`name`**: `audio-mca-loopback`
