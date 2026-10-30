# `/arm-io/aon-ptd`

- Name: `aon-ptd`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `166`
- compatible: `ptd,v1`
- device_type: `interrupt-controller`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `ApplePTD` | `AppleARMIODevice` | [`com.apple.driver.ApplePTD`](../kexts/com.apple.driver.ApplePTD.md) | `ptd,v1` |
| `AppleSPUAONPTDDriver` | `AppleSPUAppInterface` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) | `aon-ptd` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x8c840000` | `0x4000` (16,384 B) | `0x28c840000`–`0x28c843fff` |
| 1 | `0x8c850000` | `0x4000` (16,384 B) | `0x28c850000`–`0x28c853fff` |
| 2 | `0x8c858000` | `0x4000` (16,384 B) | `0x28c858000`–`0x28c85bfff` |
| 3 | `0x8c860000` | `0x4000` (16,384 B) | `0x28c860000`–`0x28c863fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648`

## Referenced by (11) [DT]

- [`/arm-io/pmgr/pmgrtools`](root__arm-io__pmgr__pmgrtools.md): interrupts 1330861125, 1278297177
- [`/arm-io/pmgr/clpc`](root__arm-io__pmgr__clpc.md): function-clpc_clvr_peek_0 `ptdP`
- [`/arm-io/pmgr/clpc`](root__arm-io__pmgr__clpc.md): function-lostperf_report_write `ptdW`
- [`/arm-io/pmgr/clpc`](root__arm-io__pmgr__clpc.md): function-ptd_read_mult `ptMR`
- [`/arm-io/pmgr/clpc`](root__arm-io__pmgr__clpc.md): function-clpc_clvr_read_0 `ptdR`
- [`/arm-io/mtp/iop-mtp-nub/mtp`](root__arm-io__mtp__iop-mtp-nub__mtp.md): function-ptd_lookup_mult `ptML`
- [`/arm-io/nub-spmi0/btm`](root__arm-io__nub-spmi0__btm.md): interrupts 1651797296, 1651797297, 1651797298, 1651797299
- [`/arm-io/baseband-ptd`](root__arm-io__baseband-ptd.md): function-ptd_read_mult `ptMR`
- [`/arm-io/baseband-ptd`](root__arm-io__baseband-ptd.md): function-ptd_lookup_mult `ptML`
- [`/arm-io/baseband-ptd`](root__arm-io__baseband-ptd.md): function-ptd_peek_mult `ptMP`
- [`/arm-io/baseband-ptd`](root__arm-io__baseband-ptd.md): interrupts 1128484931, 1128485705, 1128486221, 1128481603, 1128485714, 1128485701

## All properties (15) [DT]

- **`#address-cells`**: `0` (`0x0`)
- **`#interrupt-cells`**: `1` (`0x1`)
- **`AAPL,phandle`**: `166` (`0xa6`) → phandle of [`/arm-io/aon-ptd`](root__arm-io__aon-ptd.md)
- **`compatible`**: `ptd,v1`
- **`device_type`**: `interrupt-controller`
- **`interrupt-controller`**: (present, empty)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 128 bytes
  - u32: `0x269 0x26a 0x26b 0x26c 0x26d 0x26e 0x26f 0x270 0x271 0x272 0x273 0x274 0x275 0x276 0x277 0x278 0x279 0x27a 0x27b 0x27c 0x27d 0x27e 0x27f 0x280 0x281 0x282 0x283 0x284 0x285 0x286 0x287 0x288`
  ```
  000000  69 02 00 00 6a 02 00 00 6b 02 00 00 6c 02 00 00  i...j...k...l...
  000010  6d 02 00 00 6e 02 00 00 6f 02 00 00 70 02 00 00  m...n...o...p...
  000020  71 02 00 00 72 02 00 00 73 02 00 00 74 02 00 00  q...r...s...t...
  000030  75 02 00 00 76 02 00 00 77 02 00 00 78 02 00 00  u...v...w...x...
  000040  79 02 00 00 7a 02 00 00 7b 02 00 00 7c 02 00 00  y...z...{...|...
  000050  7d 02 00 00 7e 02 00 00 7f 02 00 00 80 02 00 00  }...~...........
  000060  81 02 00 00 82 02 00 00 83 02 00 00 84 02 00 00  ................
  000070  85 02 00 00 86 02 00 00 87 02 00 00 88 02 00 00  ................
  ```
- **`name`**: `aon-ptd`
- **`ptd-hw-irq-vectors`**: `32` (`0x20`)
- **`ptd-int-enable-clr-offset`**: `0x300` (u64; as two u32: `0x300`, `0x0`)
- **`ptd-int-enable-offset`**: `0x100` (u64; as two u32: `0x100`, `0x0`)
- **`ptd-int-enable-set-offset`**: `0x200` (u64; as two u32: `0x200`, `0x0`)
- **`ptd-int-status-offset`**: `0x0` (u64; as two u32: `0x0`, `0x0`)
- **`reg`**: 64 bytes
  - u32: `0x8c840000 0x0 0x4000 0x0 0x8c850000 0x0 0x4000 0x0 0x8c858000 0x0 0x4000 0x0 0x8c860000 0x0 0x4000 0x0`
  ```
  000000  00 00 84 8c 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000010  00 00 85 8c 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000020  00 80 85 8c 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000030  00 00 86 8c 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```
