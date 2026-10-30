# `/arm-io/exdisplaypipe`

- Name: `exdisplaypipe`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `253`
- compatible: `exdisplaypipe,t8160`
- device_type: `exdisplaypipe`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `EXDisplayPipe` | `AppleARMIODevice` | [`com.apple.driver.EXDisplayPipeH19P`](../kexts/com.apple.driver.EXDisplayPipeH19P.md) | `exdisplaypipe,t8160` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`803, 804, 762, 805`

## All properties (12) [DT]

- **`AAPL,phandle`**: `253` (`0xfd`) → phandle of [`/arm-io/exdisplaypipe`](root__arm-io__exdisplaypipe.md)
- **`compatible`**: `exdisplaypipe,t8160`
- **`device_type`**: `exdisplaypipe`
- **`display-index`**: `0` (`0x0`)
- **`exclave-assigned`**: (present, empty)
- **`exclave-edk-service`**: `com.apple.service.EXDisplayPipeDriver_EDK_xnuproxy`
- **`exclave-service`**: `com.apple.service.EXDisplayPipeDriver_xnuproxy`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 16 bytes
  - u32: `0x323 0x324 0x2fa 0x325`
  ```
  000000  23 03 00 00 24 03 00 00 fa 02 00 00 25 03 00 00  #...$.......%...
  ```
- **`iommu-parent`**: `0xf2000000f1` (u64; as two u32: `0xf1`, `0xf2`)
- **`name`**: `exdisplaypipe`
- **`tunable-target`**: `TDispTargetP68`
