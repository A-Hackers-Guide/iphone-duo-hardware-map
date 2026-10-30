# `/arm-io/audio-speaker-tx-stream-proxy`

- Name: `audio-speaker-tx-stream-proxy`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `406`
- compatible: `iisaudio,isolated-output-stream-proxy`
- device_type: `iis-ec-proxy`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IISAudioIsolatedOutputStreamECProxy` | `IOService` | [`com.apple.driver.IISAudioIsolatedStreamECProxy`](../kexts/com.apple.driver.IISAudioIsolatedStreamECProxy.md) | `iisaudio,isolated-output-stream-proxy` |

## All properties (9) [DT]

- **`AAPL,phandle`**: `406` (`0x196`) → phandle of [`/arm-io/audio-speaker-tx-stream-proxy`](root__arm-io__audio-speaker-tx-stream-proxy.md)
- **`compatible`**: `iisaudio,isolated-output-stream-proxy`
- **`device_type`**: `iis-ec-proxy`
- **`exclave-assigned`**: (present, empty)
- **`exclave-edk-service`**: `com.apple.service.SpeakerOutputStreamDriver_EDK`
- **`exclave-service`**: `com.apple.service.SpeakerOutputStreamDriver`
- **`identifier`**: `1936747343` (`0x73706b4f`) (four-char code `spkO`)
- **`name`**: `audio-speaker-tx-stream-proxy`
- **`physical-descriptions`**: 24 bytes
  - u32: `0x3de0 0xbb80 0x6c70636d 0xc 0x4 0x210`
  - text inside: `mcpl`
  ```
  000000  e0 3d 00 00 80 bb 00 00 6d 63 70 6c 0c 00 00 00  .=......mcpl....
  000010  04 00 00 00 10 02 00 00                          ........
  ```
