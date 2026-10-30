# `/arm-io/dcpsec-expert`

- Name: `dcpsec-expert`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `257`
- compatible: `dcp-expert-v1`
- device_type: `dcp-expert`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleDCPExpert` | `AppleARMIODevice` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) | `dcp-expert-v1` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x18a42c0d0` | `0x4` (4 B) | `0x38a42c0d0`–`0x38a42c0d3` |
| 1 | `0x18a318000` | `0x40` (64 B) | `0x38a318000`–`0x38a31803f` |
| 2 | `0x18a3f4000` | `0x40` (64 B) | `0x38a3f4000`–`0x38a3f403f` |
| 3 | `0x18a3f8000` | `0x40` (64 B) | `0x38a3f8000`–`0x38a3f803f` |
| 4 | `0x18a404000` | `0x40` (64 B) | `0x38a404000`–`0x38a40403f` |
| 5 | `0x18a3fc000` | `0x40` (64 B) | `0x38a3fc000`–`0x38a3fc03f` |
| 6 | `0x18a400000` | `0x40` (64 B) | `0x38a400000`–`0x38a40003f` |
| 7 | `0x18a440000` | `0x40` (64 B) | `0x38a440000`–`0x38a44003f` |
| 8 | `0x18a408000` | `0x40` (64 B) | `0x38a408000`–`0x38a40803f` |
| 9 | `0x18a40c000` | `0x40` (64 B) | `0x38a40c000`–`0x38a40c03f` |
| 10 | `0x18a414000` | `0x40` (64 B) | `0x38a414000`–`0x38a41403f` |
| 11 | `0x18a418000` | `0x40` (64 B) | `0x38a418000`–`0x38a41803f` |
| 12 | `0x18a410000` | `0x40` (64 B) | `0x38a410000`–`0x38a41003f` |
| 13 | `0x18a41c000` | `0x40` (64 B) | `0x38a41c000`–`0x38a41c03f` |
| 14 | `0x18a420000` | `0x40` (64 B) | `0x38a420000`–`0x38a42003f` |
| 15 | `0x18a368000` | `0x40` (64 B) | `0x38a368000`–`0x38a36803f` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`875`

## All properties (28) [DT]

- **`AAPL,phandle`**: `257` (`0x101`) → phandle of [`/arm-io/dcpsec-expert`](root__arm-io__dcpsec-expert.md)
- **`compatible`**: `dcp-expert-v1`
- **`device_type`**: `dcp-expert`
- **`failsafe-category-0`**: `displayInternalFailures`
- **`failsafe-category-1`**: `sysClkInputFailures`
- **`failsafe-category-2`**: `alpdpMainLinkTrainingFailures`
- **`failsafe-category-3`**: `alpdpAuxFailures`
- **`failsafe-category-4`**: `alpdpMainLinkPayloadFailures`
- **`failsafe-category-5`**: `alpdpMainLinkTimingFailures`
- **`failsafe-category-6`**: `mainLinkXsyncMismatchFailures`
- **`failsafe-category-7`**: `noActionFailures`
- **`failsafe-telemetry-event`**: `com.apple.display.HealthMonitor.DisplayFailsafeCategorization`
- **`gapf-count`**: `15` (`0xf`)
- **`gapf-reg-first-index`**: `1` (`0x1`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `875` (`0x36b`)
- **`join-power-plane`**: `1` (`0x1`)
- **`mogul-auth-key`**: `auth-passed`
- **`mogul-auth-provider`**: `194` (`0xc2`)
- **`name`**: `dcpsec-expert`
- **`reg`**: 256 bytes
  - u32: `0x8a42c0d0 0x1 0x4 0x0 0x8a318000 0x1 0x40 0x0 0x8a3f4000 0x1 0x40 0x0 0x8a3f8000 0x1 0x40 0x0 0x8a404000 0x1 0x40 0x0 0x8a3fc000 0x1 0x40 0x0 0x8a400000 0x1 0x40 0x0 0x8a440000 0x1 0x40 0x0 0x8a408000 0x1 0x40 0x0 0x8a40c000 0x1 0x40 0x0 0x8a414000 0x1 0x40 0x0 0x8a418000 0x1 0x40 0x0 0x8a410000 0x1 0x40 0x0 0x8a41c000 0x1 0x40 0x0 0x8a420000 0x1 0x40 0x0 0x8a368000 0x1 0x40 0x0`
  ```
  000000  d0 c0 42 8a 01 00 00 00 04 00 00 00 00 00 00 00  ..B.............
  000010  00 80 31 8a 01 00 00 00 40 00 00 00 00 00 00 00  ..1.....@.......
  000020  00 40 3f 8a 01 00 00 00 40 00 00 00 00 00 00 00  .@?.....@.......
  000030  00 80 3f 8a 01 00 00 00 40 00 00 00 00 00 00 00  ..?.....@.......
  000040  00 40 40 8a 01 00 00 00 40 00 00 00 00 00 00 00  .@@.....@.......
  000050  00 c0 3f 8a 01 00 00 00 40 00 00 00 00 00 00 00  ..?.....@.......
  000060  00 00 40 8a 01 00 00 00 40 00 00 00 00 00 00 00  ..@.....@.......
  000070  00 00 44 8a 01 00 00 00 40 00 00 00 00 00 00 00  ..D.....@.......
  000080  00 80 40 8a 01 00 00 00 40 00 00 00 00 00 00 00  ..@.....@.......
  000090  00 c0 40 8a 01 00 00 00 40 00 00 00 00 00 00 00  ..@.....@.......
  0000a0  00 40 41 8a 01 00 00 00 40 00 00 00 00 00 00 00  .@A.....@.......
  0000b0  00 80 41 8a 01 00 00 00 40 00 00 00 00 00 00 00  ..A.....@.......
  0000c0  00 00 41 8a 01 00 00 00 40 00 00 00 00 00 00 00  ..A.....@.......
  0000d0  00 c0 41 8a 01 00 00 00 40 00 00 00 00 00 00 00  ..A.....@.......
  0000e0  00 00 42 8a 01 00 00 00 40 00 00 00 00 00 00 00  ..B.....@.......
  0000f0  00 80 36 8a 01 00 00 00 40 00 00 00 00 00 00 00  ..6.....@.......
  ```
- **`remote-power-state`**: `1` (`0x1`)
- **`role`**: `DCPSEC`
- **`security-reg-index`**: `0` (`0x0`)
- **`support-dptx-fifo-telemetry`**: `1` (`0x1`)
- **`support-health-telemetry`**: `1` (`0x1`)
- **`support-psd-self-vote`**: `1` (`0x1`)
- **`support-standalone`**: `1` (`0x1`)
