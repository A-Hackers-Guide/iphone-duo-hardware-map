# `/arm-io/audio-sllb-proxy`

- Name: `audio-sllb-proxy`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `409`
- compatible: `iisaudio,isolated-stream-proxy`
- device_type: `iis-ec-proxy`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IISAudioIsolatedStreamECProxy` | `IOService` | [`com.apple.driver.IISAudioIsolatedStreamECProxy`](../kexts/com.apple.driver.IISAudioIsolatedStreamECProxy.md) | `iisaudio,isolated-stream-proxy` |

## All properties (10) [DT]

- **`AAPL,phandle`**: `409` (`0x199`) → phandle of [`/arm-io/audio-sllb-proxy`](root__arm-io__audio-sllb-proxy.md)
- **`compatible`**: `iisaudio,isolated-stream-proxy`
- **`device_type`**: `iis-ec-proxy`
- **`exclave-assigned`**: (present, empty)
- **`exclave-edk-service`**: `com.apple.service.SecureLEAPLoopbackDevice_EDK`
- **`exclave-service`**: `com.apple.service.SecureLEAPLoopbackDevice`
- **`identifier`**: `1936485474` (`0x736c6c62`) (four-char code `sllb`)
- **`name`**: `audio-sllb-proxy`
- **`physical-descriptions`**: 24 bytes
  - u32: `0x3de0 0xbb80 0x6c70636d 0x9 0x8 0x220`
  - text inside: `mcpl`
  ```
  000000  e0 3d 00 00 80 bb 00 00 6d 63 70 6c 09 00 00 00  .=......mcpl....
  000010  08 00 00 00 20 02 00 00                          .... ...
  ```
- **`release-arbiter-shared-mem`**: (present, empty)
