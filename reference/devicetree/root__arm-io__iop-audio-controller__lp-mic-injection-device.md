# `/arm-io/iop-audio-controller/lp-mic-injection-device`

- Name: `lp-mic-injection-device`
- Parent: [`/arm-io/iop-audio-controller`](root__arm-io__iop-audio-controller.md)
- phandle: `366`
- compatible: `iop-adma-stream,mca`
- device_type: `iop-audio-ns`
- Children (1): [`/arm-io/iop-audio-controller/lp-mic-injection-device/lp-mic-injection-device`](root__arm-io__iop-audio-controller__lp-mic-injection-device__lp-mic-injection-device.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleIOPADMAStream` | `IOPAudioNode` | [`com.apple.driver.AppleIOPADMAStream`](../kexts/com.apple.driver.AppleIOPADMAStream.md) | `iop-adma-stream,mca` |

## Firmware with a matching name [FW]

- [`Firmware/all_flash/DeviceTree.v68ap.im4p`](../firmware/Firmware__all_flash__DeviceTree.v68ap.im4p.md) (74,512 B) Tag: IM4P  Type: dtre  Version: EmbeddedDeviceTrees-12661.52.3

## All properties (7) [DT]

- **`AAPL,phandle`**: `366` (`0x16e`) → phandle of [`/arm-io/iop-audio-controller/lp-mic-injection-device`](root__arm-io__iop-audio-controller__lp-mic-injection-device.md)
- **`clock-domain`**: `1835100526` (`0x6d61696e`) (four-char code `main`)
- **`compatible`**: `iop-adma-stream,mca`
- **`device_type`**: `iop-audio-ns`
- **`dma-provider-tx`**: `base-ns-adma-tx-7`
- **`identifier`**: `1819306346` (`0x6c70696a`) (four-char code `lpij`)
- **`name`**: `lp-mic-injection-device`
