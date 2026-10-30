# `/arm-io/exdisplaypipe1`

- Name: `exdisplaypipe1`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `273`
- compatible: `exdisplaypipe1,t8160`
- device_type: `exdisplaypipe1`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `EXDisplayPipe` | `AppleARMIODevice` | [`com.apple.driver.EXDisplayPipeH19P`](../kexts/com.apple.driver.EXDisplayPipeH19P.md) | `exdisplaypipe1,t8160` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`912, 913, 871, 914`

## All properties (12) [DT]

- **`AAPL,phandle`**: `273` (`0x111`) → phandle of [`/arm-io/exdisplaypipe1`](root__arm-io__exdisplaypipe1.md)
- **`compatible`**: `exdisplaypipe1,t8160`
- **`device_type`**: `exdisplaypipe1`
- **`display-index`**: `1` (`0x1`)
- **`exclave-assigned`**: (present, empty)
- **`exclave-edk-service`**: `com.apple.service.EXDisplayPipe1Driver_EDK_xnuproxy`
- **`exclave-service`**: `com.apple.service.EXDisplayPipe1Driver_xnuproxy`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 16 bytes
  - u32: `0x390 0x391 0x367 0x392`
  ```
  000000  90 03 00 00 91 03 00 00 67 03 00 00 92 03 00 00  ........g.......
  ```
- **`iommu-parent`**: `0x10b0000010a` (u64; as two u32: `0x10a`, `0x10b`)
- **`name`**: `exdisplaypipe1`
- **`tunable-target`**: `TDispTargetS68`
