# `/arm-io/iop-audio-controller/siri-listening-device`

- Name: `siri-listening-device`
- Parent: [`/arm-io/iop-audio-controller`](root__arm-io__iop-audio-controller.md)
- phandle: `365`
- compatible: `iop-audio,client-manager-device`
- device_type: `siri-listening-device`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IOPAudioClientManagerDevice` | `IOPAudioNode` | [`com.apple.driver.IOPAudioClientManagerDevice`](../kexts/com.apple.driver.IOPAudioClientManagerDevice.md) | `iop-audio,client-manager-device` |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `cm_power_change_notify` | [`/arm-io/i2c2/audio-codec`](root__arm-io__i2c2__audio-codec.md) | `lpls` | `` |

## Firmware with a matching name [FW]

- [`Firmware/all_flash/DeviceTree.v68ap.im4p`](../firmware/Firmware__all_flash__DeviceTree.v68ap.im4p.md) (74,512 B) Tag: IM4P  Type: dtre  Version: EmbeddedDeviceTrees-12661.52.3

## All properties (9) [DT]

- **`AAPL,phandle`**: `365` (`0x16d`) → phandle of [`/arm-io/iop-audio-controller/siri-listening-device`](root__arm-io__iop-audio-controller__siri-listening-device.md)
- **`compatible`**: `iop-audio,client-manager-device`
- **`device_type`**: `siri-listening-device`
- **`external-named-power-provider`**: `AppleCS42L79Audio`
- **`function-cm_power_change_notify`**: `0x6c706c73000000b5` (u64; as two u32: `0xb5`, `0x6c706c73`)
- **`identifier`**: `1818323232` (`0x6c616920`) (four-char code `lai `)
- **`name`**: `siri-listening-device`
- **`publish-user-client`**: (present, empty)
- **`supports-multiple-user-clients`**: (present, empty)
