# `/arm-io/dcpext0-expert`

- Name: `dcpext0-expert`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `276`
- compatible: `dcp-expert-v1`
- device_type: `dcp-expert`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleDCPExpert` | `AppleARMIODevice` | [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md) | `dcp-expert-v1` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x18e42c0d0` | `0x4` (4 B) | `0x38e42c0d0`–`0x38e42c0d3` |
| 1 | `0x18e318000` | `0x40` (64 B) | `0x38e318000`–`0x38e31803f` |
| 2 | `0x18e3f4000` | `0x40` (64 B) | `0x38e3f4000`–`0x38e3f403f` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`984`

## All properties (13) [DT]

- **`AAPL,phandle`**: `276` (`0x114`) → phandle of [`/arm-io/dcpext0-expert`](root__arm-io__dcpext0-expert.md)
- **`compatible`**: `dcp-expert-v1`
- **`device_type`**: `dcp-expert`
- **`gapf-count`**: `2` (`0x2`)
- **`gapf-reg-first-index`**: `1` (`0x1`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `984` (`0x3d8`)
- **`join-power-plane`**: `1` (`0x1`)
- **`name`**: `dcpext0-expert`
- **`reg`**: 48 bytes
  - u32: `0x8e42c0d0 0x1 0x4 0x0 0x8e318000 0x1 0x40 0x0 0x8e3f4000 0x1 0x40 0x0`
  ```
  000000  d0 c0 42 8e 01 00 00 00 04 00 00 00 00 00 00 00  ..B.............
  000010  00 80 31 8e 01 00 00 00 40 00 00 00 00 00 00 00  ..1.....@.......
  000020  00 40 3f 8e 01 00 00 00 40 00 00 00 00 00 00 00  .@?.....@.......
  ```
- **`role`**: `DCPEXT`
- **`security-reg-index`**: `0` (`0x0`)
- **`support-psd-self-vote`**: `1` (`0x1`)
