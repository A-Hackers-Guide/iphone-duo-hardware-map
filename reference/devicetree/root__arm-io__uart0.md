# `/arm-io/uart0`

- Name: `uart0`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `178`
- compatible: `uart-1,samsung`
- device_type: `uart`
- Children (1): [`/arm-io/uart0/debug-console`](root__arm-io__uart0__debug-console.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleSamsungSerial` | `AppleARMIODevice` | [`com.apple.driver.AppleSamsungSerial`](../kexts/com.apple.driver.AppleSamsungSerial.md) | `uart-1,samsung` |
| `AppleSerialShim` | `AppleARMIODevice` | [`com.apple.driver.AppleSerialShim`](../kexts/com.apple.driver.AppleSerialShim.md) | `uart0` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0xa5200000` | `0x4000` (16,384 B) | `0x2a5200000`–`0x2a5203fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1328`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `tx` | [`/arm-io/gpio0`](root__arm-io__gpio0.md) | `GPIO` | `0x42 0x102` |
| `rx` | [`/arm-io/gpio0`](root__arm-io__gpio0.md) | `GPIO` | `0x43 0x102` |

## All properties (14) [DT]

- **`AAPL,phandle`**: `178` (`0xb2`) → phandle of [`/arm-io/uart0`](root__arm-io__uart0.md)
- **`boot-console`**: (present, empty)
- **`clock-ids`**: `0x40000019f` (u64; as two u32: `0x19f`, `0x4`)
- **`compatible`**: `uart-1,samsung`
- **`device_type`**: `uart`
- **`function-rx`**: 16 bytes
  - u32: `0x35 0x4750494f 0x43 0x102`
  - text inside: `OIPGC`
  ```
  000000  35 00 00 00 4f 49 50 47 43 00 00 00 02 01 00 00  5...OIPGC.......
  ```
- **`function-tx`**: 16 bytes
  - u32: `0x35 0x4750494f 0x42 0x102`
  - text inside: `OIPGB`
  ```
  000000  35 00 00 00 4f 49 50 47 42 00 00 00 02 01 00 00  5...OIPGB.......
  ```
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `1328` (`0x530`)
- **`name`**: `uart0`
- **`no-flow-control`**: (present, empty)
- **`reg`**: 16 bytes
  - u32: `0xa5200000 0x0 0x4000 0x0`
  ```
  000000  00 00 20 a5 00 00 00 00 00 40 00 00 00 00 00 00  .. ......@......
  ```
- **`service-gates`**: `5` (`0x5`)
- **`uart-version`**: `1` (`0x1`)
