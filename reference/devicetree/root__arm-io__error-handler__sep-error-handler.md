# `/arm-io/error-handler/sep-error-handler`

- Name: `sep-error-handler`
- Parent: [`/arm-io/error-handler`](root__arm-io__error-handler.md)
- phandle: `60`
- device_type: `sep-error-handler`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0xa0d80000 0x0 0x40000 0x0` | | |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`428, 427`

## Firmware with a matching name [FW]

- [`Firmware/all_flash/sep-firmware.v68.RELEASE.im4p`](../firmware/Firmware__all_flash__sep-firmware.v68.RELEASE.im4p.md) (7,216,106 B) Tag: IM4P  Type: sepi  Version: 1
- [`Firmware/all_flash/sep-patches.v68.im4p`](../firmware/Firmware__all_flash__sep-patches.v68.im4p.md) (21,137 B) Tag: IM4P  Type: stg1  Version: AppleSEPROM-1483.0.0.100.14

## All properties (10) [DT]

- **`#address-cells`**: `2` (`0x2`)
- **`#size-cells`**: `2` (`0x2`)
- **`AAPL,phandle`**: `60` (`0x3c`) → phandle of [`/arm-io/error-handler/sep-error-handler`](root__arm-io__error-handler__sep-error-handler.md)
- **`device_type`**: `sep-error-handler`
- **`flags`**: `0` (`0x0`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `0x1ab000001ac` (u64; as two u32: `0x1ac`, `0x1ab`)
- **`name`**: `sep-error-handler`
- **`nametag`**: `1936027680` (`0x73657020`) (four-char code `sep `)
- **`reg`**: 16 bytes
  - u32: `0xa0d80000 0x0 0x40000 0x0`
  ```
  000000  00 00 d8 a0 00 00 00 00 00 00 04 00 00 00 00 00  ................
  ```
