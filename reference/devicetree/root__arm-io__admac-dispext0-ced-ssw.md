# `/arm-io/admac-dispext0-ced-ssw`

- Name: `admac-dispext0-ced-ssw`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `288`
- compatible: `admacled,v1p0`
- device_type: `ced-ssw`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AudioDMACLLTEscalationDetector` | `AppleARMIODevice` | [`com.apple.driver.AudioDMACLLTEscalationDetector-Gen1p0`](../kexts/com.apple.driver.AudioDMACLLTEscalationDetector-Gen1p0.md) | `admacled,v1p0` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x18e36c000` | `0x4000` (16,384 B) | `0x38e36c000`–`0x38e36ffff` |
| 1 | `0x18e260000` | `0x4000` (16,384 B) | `0x38e260000`–`0x38e263fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1013`

## All properties (13) [DT]

- **`#dma-channels-rx`**: `0x0` (u64; as two u32: `0x0`, `0x0`)
- **`#dma-channels-tx`**: `0x1` (u64; as two u32: `0x1`, `0x0`)
- **`#dma-controllers`**: `1` (`0x1`)
- **`#ssw-register-count`**: `4` (`0x4`)
- **`AAPL,phandle`**: `288` (`0x120`) → phandle of [`/arm-io/admac-dispext0-ced-ssw`](root__arm-io__admac-dispext0-ced-ssw.md)
- **`compatible`**: `admacled,v1p0`
- **`device_type`**: `ced-ssw`
- **`dma-controllers`**: `1145133104` (`0x44415830`) (four-char code `DAX0`)
- **`identity`**: `DISP-E0-ISOC`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `1013` (`0x3f5`)
- **`name`**: `admac-dispext0-ced-ssw`
- **`reg`**: 32 bytes
  - u32: `0x8e36c000 0x1 0x4000 0x0 0x8e260000 0x1 0x4000 0x0`
  ```
  000000  00 c0 36 8e 01 00 00 00 00 40 00 00 00 00 00 00  ..6......@......
  000010  00 00 26 8e 01 00 00 00 00 40 00 00 00 00 00 00  ..&......@......
  ```
