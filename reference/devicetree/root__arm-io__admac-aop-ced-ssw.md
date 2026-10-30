# `/arm-io/admac-aop-ced-ssw`

- Name: `admac-aop-ced-ssw`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `384`
- compatible: `admacled,v1p0`
- device_type: `ced-ssw`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AudioDMACLLTEscalationDetector` | `AppleARMIODevice` | [`com.apple.driver.AudioDMACLLTEscalationDetector-Gen1p0`](../kexts/com.apple.driver.AudioDMACLLTEscalationDetector-Gen1p0.md) | `admacled,v1p0` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x93c80000` | `0x4000` (16,384 B) | `0x293c80000`–`0x293c83fff` |
| 1 | `0x93c84000` | `0x4000` (16,384 B) | `0x293c84000`–`0x293c87fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`548`

## Firmware with a matching name [FW]

- [`Firmware/AOP/aopfw-v68aop.RELEASE.im4p`](../firmware/Firmware__AOP__aopfw-v68aop.RELEASE.im4p.md) (5,546,009 B) Tag: IM4P  Type: aopf  Version: 1
- [`Firmware/AOP2/aop2fw-v68aop2.RELEASE.im4p`](../firmware/Firmware__AOP2__aop2fw-v68aop2.RELEASE.im4p.md) (9,650,201 B) Tag: IM4P  Type: aop2  Version: 1

## All properties (13) [DT]

- **`#dma-channels-rx`**: 32 bytes
  - u32: `0xe 0x0 0xd 0x0 0x9 0x0 0x9 0x0`
  ```
  000000  0e 00 00 00 00 00 00 00 0d 00 00 00 00 00 00 00  ................
  000010  09 00 00 00 00 00 00 00 09 00 00 00 00 00 00 00  ................
  ```
- **`#dma-channels-tx`**: 32 bytes
  - u32: `0x5 0x0 0xd 0x0 0x4 0x0 0x9 0x0`
  ```
  000000  05 00 00 00 00 00 00 00 0d 00 00 00 00 00 00 00  ................
  000010  04 00 00 00 00 00 00 00 09 00 00 00 00 00 00 00  ................
  ```
- **`#dma-controllers`**: `4` (`0x4`)
- **`#ssw-register-count`**: `135` (`0x87`)
- **`AAPL,phandle`**: `384` (`0x180`) → phandle of [`/arm-io/admac-aop-ced-ssw`](root__arm-io__admac-aop-ced-ssw.md)
- **`compatible`**: `admacled,v1p0`
- **`device_type`**: `ced-ssw`
- **`dma-controllers`**: 16 bytes
  - u32: `0x42415353 0x42414e53 0x4c455353 0x4c454e53`
  - text inside: `SSABSNABSSELSNEL`
  ```
  000000  53 53 41 42 53 4e 41 42 53 53 45 4c 53 4e 45 4c  SSABSNABSSELSNEL
  ```
- **`identity`**: `ADMAC-A`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `548` (`0x224`)
- **`name`**: `admac-aop-ced-ssw`
- **`reg`**: 32 bytes
  - u32: `0x93c80000 0x0 0x4000 0x0 0x93c84000 0x0 0x4000 0x0`
  ```
  000000  00 00 c8 93 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000010  00 40 c8 93 00 00 00 00 00 40 00 00 00 00 00 00  .@.......@......
  ```
