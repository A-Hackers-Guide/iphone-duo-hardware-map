# `/arm-io/ane-exclave-proxy`

- Name: `ane-exclave-proxy`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `342`
- compatible: `ane,ane-exclave-proxy`
- device_type: `ane`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `ANEExclaveProxy` | `AppleARMIODevice` | [`com.apple.driver.AppleH16ANEInterface`](../kexts/com.apple.driver.AppleH16ANEInterface.md) | `ane,ane-exclave-proxy` |

## Referenced by (1) [DT]

- [`/arm-io/ane0`](root__arm-io__ane0.md): `exclave-proxy-parent`

## Firmware with a matching name [FW]

- [`Firmware/ane/h19_ane0_fw_perses_v6x.im4p`](../firmware/Firmware__ane__h19_ane0_fw_perses_v6x.im4p.md) (1,556,505 B) Tag: IM4P  Type: anef  Version: 1
- [`Firmware/ane/h19_ane1_fw_perses_v6x.im4p`](../firmware/Firmware__ane__h19_ane1_fw_perses_v6x.im4p.md) (1,556,505 B) Tag: IM4P  Type: ane1  Version: 1

## All properties (8) [DT]

- **`AAPL,phandle`**: `342` (`0x156`) → phandle of [`/arm-io/ane-exclave-proxy`](root__arm-io__ane-exclave-proxy.md)
- **`compatible`**: `ane,ane-exclave-proxy`
- **`device_type`**: `ane`
- **`exclave-assigned`**: (present, empty)
- **`exclave-edk-service`**: `com.apple.service.ANEExclave_EDK`
- **`exclave-reg`**: 16 bytes
  - u32: `0x4f400000 0x4 0x88000 0x0`
  ```
  000000  00 00 40 4f 04 00 00 00 00 80 08 00 00 00 00 00  ..@O............
  ```
- **`exclave-service`**: `com.apple.service.ANEExclave`
- **`name`**: `ane-exclave-proxy`
