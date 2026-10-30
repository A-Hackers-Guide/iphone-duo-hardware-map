# `/arm-io/nub-spmi1`

- Name: `nub-spmi1`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `202`
- compatible: `aapl,spmi`
- device_type: `interrupt-controller`
- Children (2): [`/arm-io/nub-spmi1/shamisen`](root__arm-io__nub-spmi1__shamisen.md), [`/arm-io/nub-spmi1/stonehenge`](root__arm-io__nub-spmi1__stonehenge.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleSPMIController` | `AppleARMIODevice` | [`com.apple.driver.AppleSPMI`](../kexts/com.apple.driver.AppleSPMI.md) | `aapl,spmi` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x88614000` | `0x4000` (16,384 B) | `0x288614000`–`0x288617fff` |
| 1 | `0x88604000` | `0x4000` (16,384 B) | `0x288604000`–`0x288607fff` |
| 2 | `0x88600000` | `0x4000` (16,384 B) | `0x288600000`–`0x288603fff` |

## Interrupts [DT]

Controller: unresolved

`256, 568, 281, 260, 261, 264, 265, 266, 268, 269, 279, 280, 282, 283, 284, 285, 272, 273, 262, 263, 267`

## All properties (15) [DT]

- **`#address-cells`**: `0` (`0x0`)
- **`#interrupt-cells`**: `1` (`0x1`)
- **`AAPL,phandle`**: `202` (`0xca`) → phandle of [`/arm-io/nub-spmi1`](root__arm-io__nub-spmi1.md)
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
  - u32: `0xca 0x2d 0xca`
  ```
  000000  ca 00 00 00 2d 00 00 00 ca 00 00 00              ....-.......
  ```
- **`interrupts`**: 84 bytes
  - u32: `0x100 0x238 0x119 0x104 0x105 0x108 0x109 0x10a 0x10c 0x10d 0x117 0x118 0x11a 0x11b 0x11c 0x11d 0x110 0x111 0x106 0x107 0x10b`
  ```
  000000  00 01 00 00 38 02 00 00 19 01 00 00 04 01 00 00  ....8...........
  000010  05 01 00 00 08 01 00 00 09 01 00 00 0a 01 00 00  ................
  000020  0c 01 00 00 0d 01 00 00 17 01 00 00 18 01 00 00  ................
  000030  1a 01 00 00 1b 01 00 00 1c 01 00 00 1d 01 00 00  ................
  000040  10 01 00 00 11 01 00 00 06 01 00 00 07 01 00 00  ................
  000050  0b 01 00 00                                      ....
  ```
- **`name`**: `nub-spmi1`
- **`other-interrupts`**: 12 bytes
  - u32: `0x106 0x107 0x10b`
  ```
  000000  06 01 00 00 07 01 00 00 0b 01 00 00              ............
  ```
- **`queue-depth`**: `0x10000000100` (u64; as two u32: `0x100`, `0x100`)
- **`reg`**: 48 bytes
  - u32: `0x88614000 0x0 0x4000 0x0 0x88604000 0x0 0x4000 0x0 0x88600000 0x0 0x4000 0x0`
  ```
  000000  00 40 61 88 00 00 00 00 00 40 00 00 00 00 00 00  .@a......@......
  000010  00 40 60 88 00 00 00 00 00 40 00 00 00 00 00 00  .@`......@......
  000020  00 00 60 88 00 00 00 00 00 40 00 00 00 00 00 00  ..`......@......
  ```
