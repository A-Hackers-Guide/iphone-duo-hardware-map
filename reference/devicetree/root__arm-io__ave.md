# `/arm-io/ave`

- Name: `ave`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `310`
- compatible: `ave2`
- device_type: `ave`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleAVE2Driver` | `AppleARMIODevice` | [`com.apple.driver.AppleAVE2`](../kexts/com.apple.driver.AppleAVE2.md) | `ave2` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x203064000` | `0x4000` (16,384 B) | `0x403064000`–`0x403067fff` |
| 1 | `0x201000000` | `0x7f4000` (8,339,456 B) | `0x401000000`–`0x4017f3fff` |
| 2 | `0x203050000` | `0x4000` (16,384 B) | `0x403050000`–`0x403053fff` |
| 3 | `0x80708000` | `0x4000` (16,384 B) | `0x280708000`–`0x28070bfff` |
| 4 | `0x200000000` | `0x1000000` (16,777,216 B) | `0x400000000`–`0x400ffffff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1210, 1199, 1198`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `get_valid_perf_states` | [`/arm-io/pmgr`](root__arm-io__pmgr.md) | `PRFG` | `0x2f 0x102` |
| `clock_req_interrupt` | [`/arm-io/pmgr`](root__arm-io__pmgr.md) | `CIRQ` | `0x73 0x23 0x1` |
| `mcc_dataset` | [`/arm-io/mcc`](root__arm-io__mcc.md) | `M$DS` | `` |
| `set_perf_state_floor` | [`/arm-io/pmgr`](root__arm-io__pmgr.md) | `PRFS` | `0x2f 0x102` |

## Firmware with a matching name [FW]

- [`Firmware/ave/AppleAVE2FW_H19.im4p`](../firmware/Firmware__ave__AppleAVE2FW_H19.im4p.md) (2,737,129 B) Tag: IM4P  Type: avef  Version: 1
- [`Firmware/ave/AppleAVE2FW_H19_AVE0.im4p`](../firmware/Firmware__ave__AppleAVE2FW_H19_AVE0.im4p.md) (10,387 B) Tag: IM4P  Type: ave0  Version: 1
- [`Firmware/ave/AppleAVE2FW_H19_AVE1.im4p`](../firmware/Firmware__ave__AppleAVE2FW_H19_AVE1.im4p.md) (17,563 B) Tag: IM4P  Type: ave1  Version: 1
- [`Firmware/ave/AppleAVE2FW_H19_AVE2.im4p`](../firmware/Firmware__ave__AppleAVE2FW_H19_AVE2.im4p.md) (11,863 B) Tag: IM4P  Type: ave2  Version: 1
- [`Firmware/ave/AppleAVE2FW_H19_AVE3.im4p`](../firmware/Firmware__ave__AppleAVE2FW_H19_AVE3.im4p.md) (9,975 B) Tag: IM4P  Type: ave3  Version: 1
- [`Firmware/ave/AppleAVE2FW_H19_AVE4.im4p`](../firmware/Firmware__ave__AppleAVE2FW_H19_AVE4.im4p.md) (12,207 B) Tag: IM4P  Type: ave4  Version: 1
- [`Firmware/ave/AppleAVE2FW_H19_AVE5.im4p`](../firmware/Firmware__ave__AppleAVE2FW_H19_AVE5.im4p.md) (11,911 B) Tag: IM4P  Type: ave5  Version: 1
- [`Firmware/ave/AppleAVE2FW_H19_AVE6.im4p`](../firmware/Firmware__ave__AppleAVE2FW_H19_AVE6.im4p.md) (9,695 B) Tag: IM4P  Type: ave6  Version: 1
- [`Firmware/ave/AppleAVE2FW_H19_AVE7.im4p`](../firmware/Firmware__ave__AppleAVE2FW_H19_AVE7.im4p.md) (12,915 B) Tag: IM4P  Type: ave7  Version: 1
- [`Firmware/ave/AppleAVE2FW_H19_AVE8.im4p`](../firmware/Firmware__ave__AppleAVE2FW_H19_AVE8.im4p.md) (26,311 B) Tag: IM4P  Type: ave8  Version: 1

## All properties (18) [DT]

- **`AAPL,phandle`**: `310` (`0x136`) → phandle of [`/arm-io/ave`](root__arm-io__ave.md)
- **`clock-gates`**: `47` (`0x2f`)
- **`clock-ids`**: `370` (`0x172`)
- **`compatible`**: `ave2`
- **`device_type`**: `ave`
- **`function-clock_req_interrupt`**: 20 bytes
  - u32: `0x30 0x43495251 0x73 0x23 0x1`
  - text inside: `QRICs`
  ```
  000000  30 00 00 00 51 52 49 43 73 00 00 00 23 00 00 00  0...QRICs...#...
  000010  01 00 00 00                                      ....
  ```
- **`function-get_valid_perf_states`**: 16 bytes
  - u32: `0x30 0x50524647 0x2f 0x102`
  - text inside: `GFRP/`
  ```
  000000  30 00 00 00 47 46 52 50 2f 00 00 00 02 01 00 00  0...GFRP/.......
  ```
- **`function-mcc_dataset`**: `0x4d24445300000036` (u64; as two u32: `0x36`, `0x4d244453`)
- **`function-set_perf_state_floor`**: 16 bytes
  - u32: `0x30 0x50524653 0x2f 0x102`
  - text inside: `SFRP/`
  ```
  000000  30 00 00 00 53 46 52 50 2f 00 00 00 02 01 00 00  0...SFRP/.......
  ```
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 12 bytes
  - u32: `0x4ba 0x4af 0x4ae`
  ```
  000000  ba 04 00 00 af 04 00 00 ae 04 00 00              ............
  ```
- **`iommu-parent`**: `312` (`0x138`) → phandle of [`/arm-io/dart-ave/mapper-ave`](root__arm-io__dart-ave__mapper-ave.md)
- **`name`**: `ave`
- **`power-gates`**: `47` (`0x2f`)
- **`reg`**: 80 bytes
  - u32: `0x3064000 0x2 0x4000 0x0 0x1000000 0x2 0x7f4000 0x0 0x3050000 0x2 0x4000 0x0 0x80708000 0x0 0x4000 0x0 0x0 0x2 0x1000000 0x0`
  ```
  000000  00 40 06 03 02 00 00 00 00 40 00 00 00 00 00 00  .@.......@......
  000010  00 00 00 01 02 00 00 00 00 40 7f 00 00 00 00 00  .........@......
  000020  00 00 05 03 02 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000030  00 80 70 80 00 00 00 00 00 40 00 00 00 00 00 00  ..p......@......
  000040  00 00 00 00 02 00 00 00 00 00 00 01 00 00 00 00  ................
  ```
- **`service-gates`**: `47` (`0x2f`)
- **`service-reset`**: `11` (`0xb`)
- **`soc-id`**: `t8160`
