# `/arm-io/iop-audio-controller/lp-mic-device`

- Name: `lp-mic-device`
- Parent: [`/arm-io/iop-audio-controller`](root__arm-io__iop-audio-controller.md)
- phandle: `363`
- compatible: `iop-audio,lp-mic-device`
- device_type: `lp-mic-device`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IOPAudioLPMicDevice` | `IOPAudioNode` | [`com.apple.driver.IOPAudioLPMicDevice`](../kexts/com.apple.driver.IOPAudioLPMicDevice.md) | `iop-audio,lp-mic-device` |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `cm_power_change_notify` | [`/arm-io/i2c2/audio-codec`](root__arm-io__i2c2__audio-codec.md) | `lpsm` | `` |

## Firmware with a matching name [FW]

- [`Firmware/all_flash/DeviceTree.v68ap.im4p`](../firmware/Firmware__all_flash__DeviceTree.v68ap.im4p.md) (74,512 B) Tag: IM4P  Type: dtre  Version: EmbeddedDeviceTrees-12661.52.3

## All properties (7) [DT]

- **`AAPL,phandle`**: `363` (`0x16b`) → phandle of [`/arm-io/iop-audio-controller/lp-mic-device`](root__arm-io__iop-audio-controller__lp-mic-device.md)
- **`compatible`**: `iop-audio,lp-mic-device`
- **`device_type`**: `lp-mic-device`
- **`external-named-power-provider`**: `AppleCS42L79Audio`
- **`function-cm_power_change_notify`**: `0x6c70736d000000b5` (u64; as two u32: `0xb5`, `0x6c70736d`)
- **`identifier`**: `1819304297` (`0x6c706169`) (four-char code `lpai`)
- **`name`**: `lp-mic-device`
