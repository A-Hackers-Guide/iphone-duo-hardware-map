# `/arm-io/admac-speaker-tx-ec-proxy`

- Name: `admac-speaker-tx-ec-proxy`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `404`
- compatible: `admac-ec-proxy`
- device_type: `admac-proxy`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `DMAChannelProxy` | `IOService` | [`com.apple.driver.DMAChannelProxy`](../kexts/com.apple.driver.DMAChannelProxy.md) | `admac-ec-proxy` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x2d3700000` | `0xb8000` (753,664 B) | not memory-mapped (bus address) |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `iommu_handler` | [`/arm-io/audio-shared-dart-proxy`](root__arm-io__audio-shared-dart-proxy.md) | `sdpr` | `` |

## All properties (11) [DT]

- **`AAPL,phandle`**: `404` (`0x194`) → phandle of [`/arm-io/admac-speaker-tx-ec-proxy`](root__arm-io__admac-speaker-tx-ec-proxy.md)
- **`compatible`**: `admac-ec-proxy`
- **`device_type`**: `admac-proxy`
- **`dma-channel`**: `2` (`0x2`)
- **`exclave-assigned`**: (present, empty)
- **`exclave-edk-service`**: `com.apple.service.SpeakerOutputStreamDMA_EDK`
- **`exclave-service`**: `com.apple.service.SpeakerOutputStreamDMA`
- **`function-iommu_handler`**: `0x736470720000019d` (u64; as two u32: `0x19d`, `0x73647072`)
- **`name`**: `admac-speaker-tx-ec-proxy`
- **`reg`**: 16 bytes
  - u32: `0xd3700000 0x2 0xb8000 0x0`
  ```
  000000  00 00 70 d3 02 00 00 00 00 80 0b 00 00 00 00 00  ..p.............
  ```
- **`use-case`**: `1936747343` (`0x73706b4f`) (four-char code `spkO`)
