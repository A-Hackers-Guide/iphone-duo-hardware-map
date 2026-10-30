# `/arm-io/iop-audio-controller/audio-s-leap-internal-loopback`

- Name: `audio-s-leap-internal-loopback`
- Parent: [`/arm-io/iop-audio-controller`](root__arm-io__iop-audio-controller.md)
- phandle: `361`
- compatible: `iop-adma-stream,leap`
- device_type: `iop-audio-s`
- Children (1): [`/arm-io/iop-audio-controller/audio-s-leap-internal-loopback/audio-s-leap-internal-loopback`](root__arm-io__iop-audio-controller__audio-s-leap-internal-loopback__audio-s-leap-internal-loopback.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleIOPADMAStream` | `IOPAudioNode` | [`com.apple.driver.AppleIOPADMAStream`](../kexts/com.apple.driver.AppleIOPADMAStream.md) | `iop-adma-stream,leap` |

## Firmware with a matching name [FW]

- [`Firmware/V68_LeapHapticsFirmware.im4p`](../firmware/Firmware__V68_LeapHapticsFirmware.im4p.md) (283,085 B) Tag: IM4P  Type: lphp  Version: 1

## All properties (8) [DT]

- **`AAPL,phandle`**: `361` (`0x169`) → phandle of [`/arm-io/iop-audio-controller/audio-s-leap-internal-loopback`](root__arm-io__iop-audio-controller__audio-s-leap-internal-loopback.md)
- **`clock-domain`**: `1835100526` (`0x6d61696e`) (four-char code `main`)
- **`compatible`**: `iop-adma-stream,leap`
- **`device_type`**: `iop-audio-s`
- **`dma-provider-rx`**: `leap-s-adma-rx-2`
- **`dma-provider-tx`**: `leap-ns-adma-tx-2`
- **`identifier`**: `1936485474` (`0x736c6c62`) (four-char code `sllb`)
- **`name`**: `audio-s-leap-internal-loopback`
