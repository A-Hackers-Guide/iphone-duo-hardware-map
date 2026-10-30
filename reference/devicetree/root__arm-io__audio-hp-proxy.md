# `/arm-io/audio-hp-proxy`

- Name: `audio-hp-proxy`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `412`
- compatible: `iisaudio,isolated-stream-proxy`
- device_type: `iis-ec-proxy`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IISAudioIsolatedStreamECProxy` | `IOService` | [`com.apple.driver.IISAudioIsolatedStreamECProxy`](../kexts/com.apple.driver.IISAudioIsolatedStreamECProxy.md) | `iisaudio,isolated-stream-proxy` |

## All properties (9) [DT]

- **`AAPL,phandle`**: `412` (`0x19c`) → phandle of [`/arm-io/audio-hp-proxy`](root__arm-io__audio-hp-proxy.md)
- **`compatible`**: `iisaudio,isolated-stream-proxy`
- **`device_type`**: `iis-ec-proxy`
- **`exclave-assigned`**: (present, empty)
- **`exclave-edk-service`**: `com.apple.service.HPMicAudioDriver_EDK`
- **`exclave-service`**: `com.apple.service.HPMicAudioDriver`
- **`identifier`**: `1752195433` (`0x68706169`) (four-char code `hpai`)
- **`name`**: `audio-hp-proxy`
- **`physical-descriptions`**: 24 bytes
  - u32: `0x3de0 0xbb80 0x6c70636d 0x4 0x10 0x418`
  - text inside: `mcpl`
  ```
  000000  e0 3d 00 00 80 bb 00 00 6d 63 70 6c 04 00 00 00  .=......mcpl....
  000010  10 00 00 00 18 04 00 00                          ........
  ```
