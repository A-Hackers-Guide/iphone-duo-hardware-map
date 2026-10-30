# `/arm-io/iop-audio-controller/audio-leap-internal-loopback`

- Name: `audio-leap-internal-loopback`
- Parent: [`/arm-io/iop-audio-controller`](root__arm-io__iop-audio-controller.md)
- phandle: `353`
- compatible: `iop-adma-stream,leap`
- device_type: `iop-audio-ns`
- Children (1): [`/arm-io/iop-audio-controller/audio-leap-internal-loopback/audio-leap-internal-loopback`](root__arm-io__iop-audio-controller__audio-leap-internal-loopback__audio-leap-internal-loopback.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleIOPADMAStream` | `IOPAudioNode` | [`com.apple.driver.AppleIOPADMAStream`](../kexts/com.apple.driver.AppleIOPADMAStream.md) | `iop-adma-stream,leap` |
| `AppleAOPAudioClientManager` | `AppleAOPAudioDeviceNode` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) | `audio-leap-internal-loopback` |

## Firmware with a matching name [FW]

- [`Firmware/V68_LeapHapticsFirmware.im4p`](../firmware/Firmware__V68_LeapHapticsFirmware.im4p.md) (283,085 B) Tag: IM4P  Type: lphp  Version: 1

## All properties (8) [DT]

- **`AAPL,phandle`**: `353` (`0x161`) → phandle of [`/arm-io/iop-audio-controller/audio-leap-internal-loopback`](root__arm-io__iop-audio-controller__audio-leap-internal-loopback.md)
- **`clock-domain`**: `1835100526` (`0x6d61696e`) (four-char code `main`)
- **`compatible`**: `iop-adma-stream,leap`
- **`device_type`**: `iop-audio-ns`
- **`dma-provider-rx`**: `leap-ns-adma-rx-3`
- **`dma-provider-tx`**: `leap-ns-adma-tx-3`
- **`identifier`**: `1818848354` (`0x6c696c62`) (four-char code `lilb`)
- **`name`**: `audio-leap-internal-loopback`
