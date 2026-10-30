# `/arm-io/audio-shared-dart-proxy`

- Name: `audio-shared-dart-proxy`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `413`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `SharedDARTMapperProxy` | `IOService` | [`com.apple.driver.AudioSharedDARTMapperProxy`](../kexts/com.apple.driver.AudioSharedDARTMapperProxy.md) | `audio-shared-dart-proxy` |

## Referenced by (4) [DT]

- [`/arm-io/admac-hp-mic-ec-proxy`](root__arm-io__admac-hp-mic-ec-proxy.md): function-iommu_handler `sdpr`
- [`/arm-io/admac-speaker-tx-ec-proxy`](root__arm-io__admac-speaker-tx-ec-proxy.md): function-iommu_handler `sdpr`
- [`/arm-io/admac-receiver-tx-ec-proxy`](root__arm-io__admac-receiver-tx-ec-proxy.md): function-iommu_handler `sdpr`
- [`/arm-io/admac-sllb-ec-proxy`](root__arm-io__admac-sllb-ec-proxy.md): function-iommu_handler `sdpr`

## All properties (7) [DT]

- **`AAPL,phandle`**: `413` (`0x19d`) → phandle of [`/arm-io/audio-shared-dart-proxy`](root__arm-io__audio-shared-dart-proxy.md)
- **`exclave-assigned`**: (present, empty)
- **`exclave-edk-service`**: `com.apple.service.AudioSharedDARTMapper_EDK`
- **`exclave-service`**: `com.apple.service.AudioSharedDARTMapper`
- **`iommu-parent`**: `0x9600000097` (u64; as two u32: `0x97`, `0x96`)
- **`name`**: `audio-shared-dart-proxy`
- **`usecase-dart-map`**: 24 bytes
  - u32: `0x68706169 0x0 0x61647078 0x0 0x736c6c62 0x1`
  - text inside: `iaph`, `xpda`, `blls`
  ```
  000000  69 61 70 68 00 00 00 00 78 70 64 61 00 00 00 00  iaph....xpda....
  000010  62 6c 6c 73 01 00 00 00                          blls....
  ```
