# `/arm-io/nub-spmi0`

- Name: `nub-spmi0`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `197`
- compatible: `aapl,spmi`
- device_type: `interrupt-controller`
- Children (2): [`/arm-io/nub-spmi0/pmu-main`](root__arm-io__nub-spmi0__pmu-main.md), [`/arm-io/nub-spmi0/btm`](root__arm-io__nub-spmi0__btm.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleSPMIController` | `AppleARMIODevice` | [`com.apple.driver.AppleSPMI`](../kexts/com.apple.driver.AppleSPMI.md) | `aapl,spmi` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x88714000` | `0x4000` (16,384 B) | `0x288714000`–`0x288717fff` |
| 1 | `0x88704000` | `0x4000` (16,384 B) | `0x288704000`–`0x288707fff` |
| 2 | `0x88700000` | `0x4000` (16,384 B) | `0x288700000`–`0x288703fff` |

## Interrupts [DT]

Controller: unresolved

`256, 563, 281, 260, 261, 264, 265, 266, 268, 269, 279, 280, 282, 283, 284, 285, 272, 273, 262, 263, 267`

## Referenced by (2) [DT]

- [`/arm-io/nub-spmi0/pmu-main`](root__arm-io__nub-spmi0__pmu-main.md): interrupts 2, 62
- [`/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main/pmu-secondary`](root__arm-io__nub-spmi0__pmu-main__sgpio-bridge-pmu-main__pmu-secondary.md): interrupts 126

## All properties (15) [DT]

- **`#address-cells`**: `0` (`0x0`)
- **`#interrupt-cells`**: `1` (`0x1`)
- **`AAPL,phandle`**: `197` (`0xc5`) → phandle of [`/arm-io/nub-spmi0`](root__arm-io__nub-spmi0.md)
- **`compatible`**: `aapl,spmi`
- **`device_type`**: `interrupt-controller`
- **`error-interrupts`**: 60 bytes
  - u32: `0x104 0x105 0x108 0x109 0x10a 0x10c 0x10d 0x117 0x118 0x11a 0x11b 0x11c 0x11d 0x110 0x111`
  ```
  000000  04 01 00 00 05 01 00 00 08 01 00 00 09 01 00 00  ................
  000010  0a 01 00 00 0c 01 00 00 0d 01 00 00 17 01 00 00  ................
  000020  18 01 00 00 1a 01 00 00 1b 01 00 00 1c 01 00 00  ................
  000030  1d 01 00 00 10 01 00 00 11 01 00 00              ............
  ```
- **`fatal-interrupts`**: `281` (`0x119`)
- **`gen`**: `4` (`0x4`)
- **`interrupt-controller`**: (present, empty)
- **`interrupt-parent`**: 12 bytes
  - u32: `0xc5 0x2d 0xc5`
  ```
  000000  c5 00 00 00 2d 00 00 00 c5 00 00 00              ....-.......
  ```
- **`interrupts`**: 84 bytes
  - u32: `0x100 0x233 0x119 0x104 0x105 0x108 0x109 0x10a 0x10c 0x10d 0x117 0x118 0x11a 0x11b 0x11c 0x11d 0x110 0x111 0x106 0x107 0x10b`
  ```
  000000  00 01 00 00 33 02 00 00 19 01 00 00 04 01 00 00  ....3...........
  000010  05 01 00 00 08 01 00 00 09 01 00 00 0a 01 00 00  ................
  000020  0c 01 00 00 0d 01 00 00 17 01 00 00 18 01 00 00  ................
  000030  1a 01 00 00 1b 01 00 00 1c 01 00 00 1d 01 00 00  ................
  000040  10 01 00 00 11 01 00 00 06 01 00 00 07 01 00 00  ................
  000050  0b 01 00 00                                      ....
  ```
- **`name`**: `nub-spmi0`
- **`other-interrupts`**: 12 bytes
  - u32: `0x106 0x107 0x10b`
  ```
  000000  06 01 00 00 07 01 00 00 0b 01 00 00              ............
  ```
- **`queue-depth`**: `0x10000000100` (u64; as two u32: `0x100`, `0x100`)
- **`reg`**: 48 bytes
  - u32: `0x88714000 0x0 0x4000 0x0 0x88704000 0x0 0x4000 0x0 0x88700000 0x0 0x4000 0x0`
  ```
  000000  00 40 71 88 00 00 00 00 00 40 00 00 00 00 00 00  .@q......@......
  000010  00 40 70 88 00 00 00 00 00 40 00 00 00 00 00 00  .@p......@......
  000020  00 00 70 88 00 00 00 00 00 40 00 00 00 00 00 00  ..p......@......
  ```
