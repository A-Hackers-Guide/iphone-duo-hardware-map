# `/arm-io/iop-audio-controller/lp-mic-io-buffer-device`

- Name: `lp-mic-io-buffer-device`
- Parent: [`/arm-io/iop-audio-controller`](root__arm-io__iop-audio-controller.md)
- phandle: `364`
- compatible: `iop-audio,isolated-io-buffer-device`
- device_type: `lp-mic-io-buffer-device`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IOPAudioIsolatedIOBufferDevice` | `IOPAudioNode` | [`com.apple.driver.IOPAudioIsolatedIOBufferDevice`](../kexts/com.apple.driver.IOPAudioIsolatedIOBufferDevice.md) | `iop-audio,isolated-io-buffer-device` |

## Firmware with a matching name [FW]

- [`Firmware/all_flash/DeviceTree.v68ap.im4p`](../firmware/Firmware__all_flash__DeviceTree.v68ap.im4p.md) (74,512 B) Tag: IM4P  Type: dtre  Version: EmbeddedDeviceTrees-12661.52.3

## All properties (10) [DT]

- **`AAPL,phandle`**: `364` (`0x16c`) → phandle of [`/arm-io/iop-audio-controller/lp-mic-io-buffer-device`](root__arm-io__iop-audio-controller__lp-mic-io-buffer-device.md)
- **`compatible`**: `iop-audio,isolated-io-buffer-device`
- **`device_type`**: `lp-mic-io-buffer-device`
- **`exclave-assigned`**: (present, empty)
- **`exclave-edk-service`**: `com.apple.service.AudioDriverLPMic_EDK`
- **`exclave-service`**: `com.apple.service.AudioDriverLPMic`
- **`external-named-power-provider`**: `SharedDARTMapperProxy`
- **`identifier`**: `1633972344` (`0x61647078`) (four-char code `adpx`)
- **`name`**: `lp-mic-io-buffer-device`
- **`physical-descriptions`**: 24 bytes
  - u32: `0xfa00 0x3e80 0x6c70636d 0xc 0x8 0x410`
  - text inside: `mcpl`
  ```
  000000  00 fa 00 00 80 3e 00 00 6d 63 70 6c 0c 00 00 00  .....>..mcpl....
  000010  08 00 00 00 10 04 00 00                          ........
  ```
