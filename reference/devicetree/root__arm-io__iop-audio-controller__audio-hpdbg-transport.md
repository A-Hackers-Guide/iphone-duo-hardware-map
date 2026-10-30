# `/arm-io/iop-audio-controller/audio-hpdbg-transport`

- Name: `audio-hpdbg-transport`
- Parent: [`/arm-io/iop-audio-controller`](root__arm-io__iop-audio-controller.md)
- phandle: `378`
- compatible: `iop-adma-stream,leap`
- device_type: `iop-audio-ns`
- Children (1): [`/arm-io/iop-audio-controller/audio-hpdbg-transport/audio-hpdbg`](root__arm-io__iop-audio-controller__audio-hpdbg-transport__audio-hpdbg.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleIOPADMAStream` | `IOPAudioNode` | [`com.apple.driver.AppleIOPADMAStream`](../kexts/com.apple.driver.AppleIOPADMAStream.md) | `iop-adma-stream,leap` |

## All properties (7) [DT]

- **`AAPL,phandle`**: `378` (`0x17a`) → phandle of [`/arm-io/iop-audio-controller/audio-hpdbg-transport`](root__arm-io__iop-audio-controller__audio-hpdbg-transport.md)
- **`clock-domain`**: `1835100526` (`0x6d61696e`) (four-char code `main`)
- **`compatible`**: `iop-adma-stream,leap`
- **`device_type`**: `iop-audio-ns`
- **`dma-provider-rx`**: `leap-ns-adma-rx-1`
- **`identifier`**: `1634756708` (`0x61706864`) (four-char code `aphd`)
- **`name`**: `audio-hpdbg-transport`
