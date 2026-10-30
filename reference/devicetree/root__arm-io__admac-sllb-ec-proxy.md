# `/arm-io/admac-sllb-ec-proxy`

- Name: `admac-sllb-ec-proxy`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `408`
- compatible: `admac-ec-proxy`
- device_type: `admac-proxy`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `DMAChannelProxy` | `IOService` | [`com.apple.driver.DMAChannelProxy`](../kexts/com.apple.driver.DMAChannelProxy.md) | `admac-ec-proxy` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x2d3100000` | `0xa4000` (671,744 B) | not memory-mapped (bus address) |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `iommu_handler` | [`/arm-io/audio-shared-dart-proxy`](root__arm-io__audio-shared-dart-proxy.md) | `sdpr` | `` |

## All properties (12) [DT]

- **`AAPL,phandle`**: `408` (`0x198`) → phandle of [`/arm-io/admac-sllb-ec-proxy`](root__arm-io__admac-sllb-ec-proxy.md)
- **`compatible`**: `admac-ec-proxy`
- **`device_type`**: `admac-proxy`
- **`dma-channel`**: `2` (`0x2`)
- **`exclave-assigned`**: (present, empty)
- **`exclave-edk-service`**: `com.apple.service.SecureLEAPLoopbackDMA_EDK`
- **`exclave-service`**: `com.apple.service.SecureLEAPLoopbackDMA`
- **`function-iommu_handler`**: `0x736470720000019d` (u64; as two u32: `0x19d`, `0x73647072`)
- **`name`**: `admac-sllb-ec-proxy`
- **`proxy-is-development-only`**: (present, empty)
- **`reg`**: 16 bytes
  - u32: `0xd3100000 0x2 0xa4000 0x0`
  ```
  000000  00 00 10 d3 02 00 00 00 00 40 0a 00 00 00 00 00  .........@......
  ```
- **`use-case`**: `1936485474` (`0x736c6c62`) (four-char code `sllb`)
