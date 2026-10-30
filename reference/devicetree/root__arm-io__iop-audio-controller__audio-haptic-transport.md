# `/arm-io/iop-audio-controller/audio-haptic-transport`

- Name: `audio-haptic-transport`
- Parent: [`/arm-io/iop-audio-controller`](root__arm-io__iop-audio-controller.md)
- phandle: `374`
- compatible: `iop-adma-stream,leap`
- device_type: `iop-audio-ns`
- Children (1): [`/arm-io/iop-audio-controller/audio-haptic-transport/audio-haptic`](root__arm-io__iop-audio-controller__audio-haptic-transport__audio-haptic.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleIOPADMAStream` | `IOPAudioNode` | [`com.apple.driver.AppleIOPADMAStream`](../kexts/com.apple.driver.AppleIOPADMAStream.md) | `iop-adma-stream,leap` |

## Firmware with a matching name [FW]

- [`Firmware/V68_HapticAssets.im4p`](../firmware/Firmware__V68_HapticAssets.im4p.md) (1,174 B) Tag: IM4P  Type: hpas  Version: 1

## All properties (7) [DT]

- **`AAPL,phandle`**: `374` (`0x176`) → phandle of [`/arm-io/iop-audio-controller/audio-haptic-transport`](root__arm-io__iop-audio-controller__audio-haptic-transport.md)
- **`clock-domain`**: `1835100526` (`0x6d61696e`) (four-char code `main`)
- **`compatible`**: `iop-adma-stream,leap`
- **`device_type`**: `iop-audio-ns`
- **`dma-provider-tx`**: `leap-ns-adma-tx-1`
- **`identifier`**: `1634756640` (`0x61706820`) (four-char code `aph `)
- **`name`**: `audio-haptic-transport`
