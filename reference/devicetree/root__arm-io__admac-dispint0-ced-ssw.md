# `/arm-io/admac-dispint0-ced-ssw`

- Name: `admac-dispint0-ced-ssw`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `248`
- compatible: `admacled,v1p0`
- device_type: `ced-ssw`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AudioDMACLLTEscalationDetector` | `AppleARMIODevice` | [`com.apple.driver.AudioDMACLLTEscalationDetector-Gen1p0`](../kexts/com.apple.driver.AudioDMACLLTEscalationDetector-Gen1p0.md) | `admacled,v1p0` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x18636c000` | `0x4000` (16,384 B) | `0x38636c000`–`0x38636ffff` |
| 1 | `0x186260000` | `0x4000` (16,384 B) | `0x386260000`–`0x386263fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`795`

## All properties (13) [DT]

- **`#dma-channels-rx`**: `0x0` (u64; as two u32: `0x0`, `0x0`)
- **`#dma-channels-tx`**: `0x1` (u64; as two u32: `0x1`, `0x0`)
- **`#dma-controllers`**: `1` (`0x1`)
- **`#ssw-register-count`**: `4` (`0x4`)
- **`AAPL,phandle`**: `248` (`0xf8`) → phandle of [`/arm-io/admac-dispint0-ced-ssw`](root__arm-io__admac-dispint0-ced-ssw.md)
- **`compatible`**: `admacled,v1p0`
- **`device_type`**: `ced-ssw`
- **`dma-controllers`**: `1145129264` (`0x44414930`) (four-char code `DAI0`)
- **`identity`**: `DISP-I-ISOC`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `795` (`0x31b`)
- **`name`**: `admac-dispint0-ced-ssw`
- **`reg`**: 32 bytes
  - u32: `0x8636c000 0x1 0x4000 0x0 0x86260000 0x1 0x4000 0x0`
  ```
  000000  00 c0 36 86 01 00 00 00 00 40 00 00 00 00 00 00  ..6......@......
  000010  00 00 26 86 01 00 00 00 00 40 00 00 00 00 00 00  ..&......@......
  ```
