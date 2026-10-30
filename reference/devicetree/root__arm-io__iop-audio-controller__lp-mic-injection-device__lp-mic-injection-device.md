# `/arm-io/iop-audio-controller/lp-mic-injection-device/lp-mic-injection-device`

- Name: `lp-mic-injection-device`
- Parent: [`/arm-io/iop-audio-controller/lp-mic-injection-device`](root__arm-io__iop-audio-controller__lp-mic-injection-device.md)
- phandle: `367`
- compatible: `audio-data,external`
- device_type: `audio-data`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleExternalSecondaryAudio` | `AppleARMIISDevice` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) | `audio-data,external` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x201 0x10004 0xb71b00 0x102ee 0x10010 0xf 0x0 0x100004 0x0` | | |

## Firmware with a matching name [FW]

- [`Firmware/all_flash/DeviceTree.v68ap.im4p`](../firmware/Firmware__all_flash__DeviceTree.v68ap.im4p.md) (74,512 B) Tag: IM4P  Type: dtre  Version: EmbeddedDeviceTrees-12661.52.3

## All properties (8) [DT]

- **`AAPL,phandle`**: `367` (`0x16f`) → phandle of [`/arm-io/iop-audio-controller/lp-mic-injection-device/lp-mic-injection-device`](root__arm-io__iop-audio-controller__lp-mic-injection-device__lp-mic-injection-device.md)
- **`compatible`**: `audio-data,external`
- **`data-sources`**: 36 bytes
  - u32: `0x6c70696a 0x800 0x10002 0x0 0x3e80 0x694d504c 0x6e492063 0x7463656a 0x6e6f69`
  - text inside: `jipl`, `LPMic Injection`
  ```
  000000  6a 69 70 6c 00 08 00 00 02 00 01 00 00 00 00 00  jipl............
  000010  80 3e 00 00 4c 50 4d 69 63 20 49 6e 6a 65 63 74  .>..LPMic Inject
  000020  69 6f 6e 00                                      ion.
  ```
- **`device-name`**: `LPMic Injection`
- **`device-uid`**: `LPMicInjection`
- **`device_type`**: `audio-data`
- **`name`**: `lp-mic-injection-device`
- **`reg`**: 36 bytes
  - u32: `0x201 0x10004 0xb71b00 0x102ee 0x10010 0xf 0x0 0x100004 0x0`
  ```
  000000  01 02 00 00 04 00 01 00 00 1b b7 00 ee 02 01 00  ................
  000010  10 00 01 00 0f 00 00 00 00 00 00 00 04 00 10 00  ................
  000020  00 00 00 00                                      ....
  ```
