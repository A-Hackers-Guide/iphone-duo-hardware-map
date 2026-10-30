# `/arm-io/atc-phy0`

- Name: `atc-phy0`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `222`
- compatible: `atc-phy,t8160`
- device_type: `atc-phy`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8160TypeCPhy` | `AppleARMIODevice` | [`com.apple.driver.AppleT8160TypeCPhy`](../kexts/com.apple.driver.AppleT8160TypeCPhy.md) | `atc-phy,t8160` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x322418000` | `0x4000` (16,384 B) | `0x322418000`–`0x32241bfff` |
| 1 | `0x322448000` | `0x4000` (16,384 B) | `0x322448000`–`0x32244bfff` |
| 2 | `0x323000000` | `0x84000` (540,672 B) | `0x323000000`–`0x323083fff` |
| 3 | `0x320000000` | `0x1000000` (16,777,216 B) | `0x320000000`–`0x320ffffff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1486`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `dock_parent` | [`/port-usb-c-1`](root__port-usb-c-1.md) | `accP` | `` |

## Referenced by (1) [DT]

- [`/arm-io/usb-drd0`](root__arm-io__usb-drd0.md): `atc-phy-parent`

## All properties (16) [DT]

- **`AAPL,phandle`**: `222` (`0xde`) → phandle of [`/arm-io/atc-phy0`](root__arm-io__atc-phy0.md)
- **`clock-gates`**: `4`, `3`
- **`compatible`**: `atc-phy,t8160`
- **`device_type`**: `atc-phy`
- **`dp-training-table`**: (present, empty)
- **`dp-training-table-hbr`**: 64 bytes
  - u32: `0x24 0x413 0x70b 0x904 0x1c 0x40b 0x704 0x25 0x11 0x404 0x25 0x25 0x2 0x25 0x25 0x25`
  ```
  000000  24 00 00 00 13 04 00 00 0b 07 00 00 04 09 00 00  $...............
  000010  1c 00 00 00 0b 04 00 00 04 07 00 00 25 00 00 00  ............%...
  000020  11 00 00 00 04 04 00 00 25 00 00 00 25 00 00 00  ........%...%...
  000030  02 00 00 00 25 00 00 00 25 00 00 00 25 00 00 00  ....%...%...%...
  ```
- **`dp-training-table-rbr`**: 64 bytes
  - u32: `0x24 0x413 0x70b 0x904 0x1c 0x40b 0x704 0x25 0x11 0x404 0x25 0x25 0x2 0x25 0x25 0x25`
  ```
  000000  24 00 00 00 13 04 00 00 0b 07 00 00 04 09 00 00  $...............
  000010  1c 00 00 00 0b 04 00 00 04 07 00 00 25 00 00 00  ............%...
  000020  11 00 00 00 04 04 00 00 25 00 00 00 25 00 00 00  ........%...%...
  000030  02 00 00 00 25 00 00 00 25 00 00 00 25 00 00 00  ....%...%...%...
  ```
- **`function-dock_parent`**: `0x61636350000001c5` (u64; as two u32: `0x1c5`, `0x61636350`)
- **`instance`**: `0` (`0x0`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `1486` (`0x5ce`)
- **`name`**: `atc-phy0`
- **`port-number`**: `1` (`0x1`)
- **`port-type`**: `2` (`0x2`)
- **`reg`**: 64 bytes
  - u32: `0x22418000 0x3 0x4000 0x0 0x22448000 0x3 0x4000 0x0 0x23000000 0x3 0x84000 0x0 0x20000000 0x3 0x1000000 0x0`
  ```
  000000  00 80 41 22 03 00 00 00 00 40 00 00 00 00 00 00  ..A".....@......
  000010  00 80 44 22 03 00 00 00 00 40 00 00 00 00 00 00  ..D".....@......
  000020  00 00 00 23 03 00 00 00 00 40 08 00 00 00 00 00  ...#.....@......
  000030  00 00 00 20 03 00 00 00 00 00 00 01 00 00 00 00  ... ............
  ```
- **`service-gates`**: `4`, `3`
