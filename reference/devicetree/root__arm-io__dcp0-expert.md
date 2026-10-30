# `/arm-io/dcp0-expert`

- Name: `dcp0-expert`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `232`
- compatible: `dcp-expert-v1`
- device_type: `dcp-expert`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleDCPExpert` | `AppleARMIODevice` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) | `dcp-expert-v1` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x18642c0d0` | `0x4` (4 B) | `0x38642c0d0`–`0x38642c0d3` |
| 1 | `0x186318000` | `0x40` (64 B) | `0x386318000`–`0x38631803f` |
| 2 | `0x1863f4000` | `0x40` (64 B) | `0x3863f4000`–`0x3863f403f` |
| 3 | `0x1863f8000` | `0x40` (64 B) | `0x3863f8000`–`0x3863f803f` |
| 4 | `0x186404000` | `0x40` (64 B) | `0x386404000`–`0x38640403f` |
| 5 | `0x1863fc000` | `0x40` (64 B) | `0x3863fc000`–`0x3863fc03f` |
| 6 | `0x186400000` | `0x40` (64 B) | `0x386400000`–`0x38640003f` |
| 7 | `0x186440000` | `0x40` (64 B) | `0x386440000`–`0x38644003f` |
| 8 | `0x186408000` | `0x40` (64 B) | `0x386408000`–`0x38640803f` |
| 9 | `0x18640c000` | `0x40` (64 B) | `0x38640c000`–`0x38640c03f` |
| 10 | `0x186414000` | `0x40` (64 B) | `0x386414000`–`0x38641403f` |
| 11 | `0x186418000` | `0x40` (64 B) | `0x386418000`–`0x38641803f` |
| 12 | `0x186410000` | `0x40` (64 B) | `0x386410000`–`0x38641003f` |
| 13 | `0x18641c000` | `0x40` (64 B) | `0x38641c000`–`0x38641c03f` |
| 14 | `0x186420000` | `0x40` (64 B) | `0x386420000`–`0x38642003f` |
| 15 | `0x186368000` | `0x40` (64 B) | `0x386368000`–`0x38636803f` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`766`

## All properties (28) [DT]

- **`AAPL,phandle`**: `232` (`0xe8`) → phandle of [`/arm-io/dcp0-expert`](root__arm-io__dcp0-expert.md)
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
- **`interrupts`**: `766` (`0x2fe`)
- **`join-power-plane`**: `1` (`0x1`)
- **`mogul-auth-key`**: `auth-passed`
- **`mogul-auth-provider`**: `193` (`0xc1`)
- **`name`**: `dcp0-expert`
- **`reg`**: 256 bytes
  - u32: `0x8642c0d0 0x1 0x4 0x0 0x86318000 0x1 0x40 0x0 0x863f4000 0x1 0x40 0x0 0x863f8000 0x1 0x40 0x0 0x86404000 0x1 0x40 0x0 0x863fc000 0x1 0x40 0x0 0x86400000 0x1 0x40 0x0 0x86440000 0x1 0x40 0x0 0x86408000 0x1 0x40 0x0 0x8640c000 0x1 0x40 0x0 0x86414000 0x1 0x40 0x0 0x86418000 0x1 0x40 0x0 0x86410000 0x1 0x40 0x0 0x8641c000 0x1 0x40 0x0 0x86420000 0x1 0x40 0x0 0x86368000 0x1 0x40 0x0`
  ```
  000000  d0 c0 42 86 01 00 00 00 04 00 00 00 00 00 00 00  ..B.............
  000010  00 80 31 86 01 00 00 00 40 00 00 00 00 00 00 00  ..1.....@.......
  000020  00 40 3f 86 01 00 00 00 40 00 00 00 00 00 00 00  .@?.....@.......
  000030  00 80 3f 86 01 00 00 00 40 00 00 00 00 00 00 00  ..?.....@.......
  000040  00 40 40 86 01 00 00 00 40 00 00 00 00 00 00 00  .@@.....@.......
  000050  00 c0 3f 86 01 00 00 00 40 00 00 00 00 00 00 00  ..?.....@.......
  000060  00 00 40 86 01 00 00 00 40 00 00 00 00 00 00 00  ..@.....@.......
  000070  00 00 44 86 01 00 00 00 40 00 00 00 00 00 00 00  ..D.....@.......
  000080  00 80 40 86 01 00 00 00 40 00 00 00 00 00 00 00  ..@.....@.......
  000090  00 c0 40 86 01 00 00 00 40 00 00 00 00 00 00 00  ..@.....@.......
  0000a0  00 40 41 86 01 00 00 00 40 00 00 00 00 00 00 00  .@A.....@.......
  0000b0  00 80 41 86 01 00 00 00 40 00 00 00 00 00 00 00  ..A.....@.......
  0000c0  00 00 41 86 01 00 00 00 40 00 00 00 00 00 00 00  ..A.....@.......
  0000d0  00 c0 41 86 01 00 00 00 40 00 00 00 00 00 00 00  ..A.....@.......
  0000e0  00 00 42 86 01 00 00 00 40 00 00 00 00 00 00 00  ..B.....@.......
  0000f0  00 80 36 86 01 00 00 00 40 00 00 00 00 00 00 00  ..6.....@.......
  ```
- **`remote-power-state`**: `1` (`0x1`)
- **`role`**: `DCP`
- **`security-reg-index`**: `0` (`0x0`)
- **`support-dptx-fifo-telemetry`**: `1` (`0x1`)
- **`support-health-telemetry`**: `1` (`0x1`)
- **`support-psd-self-vote`**: `1` (`0x1`)
- **`support-standalone`**: `1` (`0x1`)
