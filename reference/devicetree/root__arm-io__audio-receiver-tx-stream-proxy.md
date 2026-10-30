# `/arm-io/audio-receiver-tx-stream-proxy`

- Name: `audio-receiver-tx-stream-proxy`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `407`
- compatible: `iisaudio,isolated-output-stream-proxy`
- device_type: `iis-ec-proxy`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IISAudioIsolatedOutputStreamECProxy` | `IOService` | [`com.apple.driver.IISAudioIsolatedStreamECProxy`](../kexts/com.apple.driver.IISAudioIsolatedStreamECProxy.md) | `iisaudio,isolated-output-stream-proxy` |

## All properties (9) [DT]

- **`AAPL,phandle`**: `407` (`0x197`) → phandle of [`/arm-io/audio-receiver-tx-stream-proxy`](root__arm-io__audio-receiver-tx-stream-proxy.md)
- **`compatible`**: `iisaudio,isolated-output-stream-proxy`
- **`device_type`**: `iis-ec-proxy`
- **`exclave-assigned`**: (present, empty)
- **`exclave-edk-service`**: `com.apple.service.ReceiverOutputStreamDriver_EDK`
- **`exclave-service`**: `com.apple.service.ReceiverOutputStreamDriver`
- **`identifier`**: `1919247222` (`0x72656376`) (four-char code `recv`)
- **`name`**: `audio-receiver-tx-stream-proxy`
- **`physical-descriptions`**: 24 bytes
  - u32: `0x3de0 0xbb80 0x6c70636d 0x4 0x4 0x118`
  - text inside: `mcpl`
  ```
  000000  e0 3d 00 00 80 bb 00 00 6d 63 70 6c 04 00 00 00  .=......mcpl....
  000010  04 00 00 00 18 01 00 00                          ........
  ```
