# `/arm-io/wdt`

- Name: `wdt`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `52`
- compatible: `wdt,t8101`, `wdt,s5l8960x`
- device_type: `wdt`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleARMWatchdogTimer` | `AppleARMIODevice` | [`com.apple.driver.AppleARMWatchdogTimer`](../kexts/com.apple.driver.AppleARMWatchdogTimer.md) | `wdt,s5l8960x` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x882b0000` | `0x4000` (16,384 B) | `0x2882b0000`–`0x2882b3fff` |
| 1 | `0x882bc058` | `0x4` (4 B) | `0x2882bc058`–`0x2882bc05b` |
| 2 | `0x882b8008` | `0x4` (4 B) | `0x2882b8008`–`0x2882b800b` |
| 3 | `0x882b802c` | `0x4` (4 B) | `0x2882b802c`–`0x2882b802f` |
| 4 | `0x882b8020` | `0x4` (4 B) | `0x2882b8020`–`0x2882b8023` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`341, 0`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `panic_notify` | [`/arm-io/gpio0`](root__arm-io__gpio0.md) | `GPIO` | `0x40 0x100` |

## All properties (16) [DT]

- **`AAPL,phandle`**: `52` (`0x34`) → phandle of [`/arm-io/wdt`](root__arm-io__wdt.md)
- **`awl-scratch-supported`**: `1` (`0x1`)
- **`clock-ids`**: `4` (`0x4`)
- **`compatible`**: `wdt,t8101`, `wdt,s5l8960x`
- **`device_type`**: `wdt`
- **`function-panic_notify`**: 16 bytes
  - u32: `0x35 0x4750494f 0x40 0x100`
  - text inside: `OIPG@`
  ```
  000000  35 00 00 00 4f 49 50 47 40 00 00 00 00 01 00 00  5...OIPG@.......
  ```
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `0x155` (u64; as two u32: `0x155`, `0x0`)
- **`name`**: `wdt`
- **`panic-save-flag-bit`**: `0` (`0x0`)
- **`reg`**: 80 bytes
  - u32: `0x882b0000 0x0 0x4000 0x0 0x882bc058 0x0 0x4 0x0 0x882b8008 0x0 0x4 0x0 0x882b802c 0x0 0x4 0x0 0x882b8020 0x0 0x4 0x0`
  ```
  000000  00 00 2b 88 00 00 00 00 00 40 00 00 00 00 00 00  ..+......@......
  000010  58 c0 2b 88 00 00 00 00 04 00 00 00 00 00 00 00  X.+.............
  000020  08 80 2b 88 00 00 00 00 04 00 00 00 00 00 00 00  ..+.............
  000030  2c 80 2b 88 00 00 00 00 04 00 00 00 00 00 00 00  ,.+.............
  000040  20 80 2b 88 00 00 00 00 04 00 00 00 00 00 00 00   .+.............
  ```
- **`simple-reconfig-wdog-icc-time`**: `5` (`0x5`)
- **`simple-reconfig-wdog-support`**: (present, empty)
- **`trigger-ce`**: 16 bytes
  - u32: `0x80780068 0x2 0x0 0x1`
  ```
  000000  68 00 78 80 02 00 00 00 00 00 00 00 01 00 00 00  h.x.............
  ```
- **`trigger-config`**: 96 bytes
  - u32: `0x10020284 0x2 0xf 0x1 0x10120284 0x2 0xf 0x1 0x10220284 0x2 0xf 0x1 0x10320284 0x2 0xf 0x1 0x11020284 0x2 0xf 0x1 0x11120284 0x2 0xf 0x1`
  ```
  000000  84 02 02 10 02 00 00 00 0f 00 00 00 01 00 00 00  ................
  000010  84 02 12 10 02 00 00 00 0f 00 00 00 01 00 00 00  ................
  000020  84 02 22 10 02 00 00 00 0f 00 00 00 01 00 00 00  ..".............
  000030  84 02 32 10 02 00 00 00 0f 00 00 00 01 00 00 00  ..2.............
  000040  84 02 02 11 02 00 00 00 0f 00 00 00 01 00 00 00  ................
  000050  84 02 12 11 02 00 00 00 0f 00 00 00 01 00 00 00  ................
  ```
- **`wdt-version`**: `2` (`0x2`)
