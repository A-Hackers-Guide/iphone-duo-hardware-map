# `/arm-io/dispext0`

- Name: `dispext0`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `275`
- compatible: `dispext0,t8160`
- device_type: `ext-display-subsystem`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleCLCD2` | `AppleARMIODevice` | [`com.apple.driver.AppleMobileDispH19P-DCP`](../kexts/com.apple.driver.AppleMobileDispH19P-DCP.md) | `dispext0,t8160` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x18c000000` | `0xe2c000` (14,860,288 B) | `0x38c000000`–`0x38ce2bfff` |
| 1 | `0x18e2c0000` | `0x10000` (65,536 B) | `0x38e2c0000`–`0x38e2cffff` |
| 2 | `0x18e42c000` | `0x4000` (16,384 B) | `0x38e42c000`–`0x38e42ffff` |
| 3 | `0x18e800000` | `0x7f4000` (8,339,456 B) | `0x38e800000`–`0x38eff3fff` |
| 4 | `0x82800000` | `0x1d4000` (1,916,928 B) | `0x282800000`–`0x2829d3fff` |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `send_disp_clock` | [`/arm-io/disp0`](root__arm-io__disp0.md) | `UPps` | `` |

## All properties (15) [DT]

- **`AAPL,phandle`**: `275` (`0x113`) → phandle of [`/arm-io/dispext0`](root__arm-io__dispext0.md)
- **`clcdclk_frequency`**: 12 bytes
  - u32: `0x30 0x52474243 0x1`
  - text inside: `CBGR`
  ```
  000000  30 00 00 00 43 42 47 52 01 00 00 00              0...CBGR....
  ```
- **`clock-ids`**: `0x1a200000152` (u64; as two u32: `0x152`, `0x1a2`)
- **`compatible`**: `dispext0,t8160`
- **`device_type`**: `ext-display-subsystem`
- **`display-default-color`**: `0` (`0x0`)
- **`display-timing-info`**: 32 bytes
  - u32: `0x400 0x32 0x33 0x32 0x258 0xda 0x6 0x32`
  ```
  000000  00 04 00 00 32 00 00 00 33 00 00 00 32 00 00 00  ....2...3...2...
  000010  58 02 00 00 da 00 00 00 06 00 00 00 32 00 00 00  X...........2...
  ```
- **`external`**: `1` (`0x1`)
- **`framebuffer-height`**: `2160` (`0x870`)
- **`framebuffer-width`**: `4096` (`0x1000`)
- **`function-send_disp_clock`**: `0x55507073000000e9` (u64; as two u32: `0xe9`, `0x55507073`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`iommu-parent`**: `0x11c0000011b` (u64; as two u32: `0x11b`, `0x11c`)
- **`name`**: `dispext0`
- **`reg`**: 80 bytes
  - u32: `0x8c000000 0x1 0xe2c000 0x0 0x8e2c0000 0x1 0x10000 0x0 0x8e42c000 0x1 0x4000 0x0 0x8e800000 0x1 0x7f4000 0x0 0x82800000 0x0 0x1d4000 0x0`
  ```
  000000  00 00 00 8c 01 00 00 00 00 c0 e2 00 00 00 00 00  ................
  000010  00 00 2c 8e 01 00 00 00 00 00 01 00 00 00 00 00  ..,.............
  000020  00 c0 42 8e 01 00 00 00 00 40 00 00 00 00 00 00  ..B......@......
  000030  00 00 80 8e 01 00 00 00 00 40 7f 00 00 00 00 00  .........@......
  000040  00 00 80 82 00 00 00 00 00 40 1d 00 00 00 00 00  .........@......
  ```
