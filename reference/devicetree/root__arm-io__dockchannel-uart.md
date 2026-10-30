# `/arm-io/dockchannel-uart`

- Name: `dockchannel-uart`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `168`
- compatible: `aapl,dock-channels`
- device_type: `dockchannel`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleSerialShim` | `AppleARMIODevice` | [`com.apple.driver.AppleSerialShim`](../kexts/com.apple.driver.AppleSerialShim.md) | `dockchannel-uart` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x88128000` | `0x10000` (65,536 B) | `0x288128000`–`0x288137fff` |
| 1 | `0x8810c000` | `0x1000` (4,096 B) | `0x28810c000`–`0x28810cfff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`550`

## All properties (10) [DT]

- **`AAPL,phandle`**: `168` (`0xa8`) → phandle of [`/arm-io/dockchannel-uart`](root__arm-io__dockchannel-uart.md)
- **`compatible`**: `aapl,dock-channels`
- **`device_type`**: `dockchannel`
- **`dock-wstat-mask`**: `4095` (`0xfff`)
- **`enable-sw-drain`**: `1` (`0x1`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `550` (`0x226`)
- **`max-aop-clk`**: `288000000` (`0x112a8800`)
- **`name`**: `dockchannel-uart`
- **`reg`**: 32 bytes
  - u32: `0x88128000 0x0 0x10000 0x0 0x8810c000 0x0 0x1000 0x0`
  ```
  000000  00 80 12 88 00 00 00 00 00 00 01 00 00 00 00 00  ................
  000010  00 c0 10 88 00 00 00 00 00 10 00 00 00 00 00 00  ................
  ```
