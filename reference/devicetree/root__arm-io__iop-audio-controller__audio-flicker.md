# `/arm-io/iop-audio-controller/audio-flicker`

- Name: `audio-flicker`
- Parent: [`/arm-io/iop-audio-controller`](root__arm-io__iop-audio-controller.md)
- phandle: `359`
- compatible: `iop-adma-stream,mca`
- device_type: `iop-audio-ns`
- Children (1): [`/arm-io/iop-audio-controller/audio-flicker/audio-flicker`](root__arm-io__iop-audio-controller__audio-flicker__audio-flicker.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleIOPADMAStream` | `IOPAudioNode` | [`com.apple.driver.AppleIOPADMAStream`](../kexts/com.apple.driver.AppleIOPADMAStream.md) | `iop-adma-stream,mca` |

## All properties (7) [DT]

- **`AAPL,phandle`**: `359` (`0x167`) → phandle of [`/arm-io/iop-audio-controller/audio-flicker`](root__arm-io__iop-audio-controller__audio-flicker.md)
- **`clock-domain`**: `1835100526` (`0x6d61696e`) (four-char code `main`)
- **`compatible`**: `iop-adma-stream,mca`
- **`device_type`**: `iop-audio-ns`
- **`dma-provider-rx`**: `base-ns-adma-rx-5`
- **`identifier`**: `1718379371` (`0x666c636b`) (four-char code `flck`)
- **`name`**: `audio-flicker`
