# `/arm-io/esm`

- Name: `esm`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `134`
- compatible: `iop,exclave-sep-manager`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `ExclaveSEPManagerProxy` | `IOService` | [`com.apple.driver.ExclaveSEPManagerProxy`](../kexts/com.apple.driver.ExclaveSEPManagerProxy.md) | `iop,exclave-sep-manager` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x2e2710000` | `0x4000` (16,384 B) | not memory-mapped (bus address) |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`425, 426`

## All properties (10) [DT]

- **`AAPL,phandle`**: `134` (`0x86`) → phandle of [`/arm-io/esm`](root__arm-io__esm.md)
- **`compatible`**: `iop,exclave-sep-manager`
- **`exclave-assigned`**: (present, empty)
- **`exclave-edk-service`**: `com.apple.service.ExclaveSEPManager_EDK`
- **`exclave-service`**: `com.apple.service.ExclaveSEPManager`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `0x1aa000001a9` (u64; as two u32: `0x1a9`, `0x1aa`)
- **`iommu-parent`**: `133` (`0x85`) → phandle of [`/arm-io/dart-sep/mapper-sep-exclave`](root__arm-io__dart-sep__mapper-sep-exclave.md)
- **`name`**: `esm`
- **`reg`**: 16 bytes
  - u32: `0xe2710000 0x2 0x4000 0x0`
  ```
  000000  00 00 71 e2 02 00 00 00 00 40 00 00 00 00 00 00  ..q......@......
  ```
