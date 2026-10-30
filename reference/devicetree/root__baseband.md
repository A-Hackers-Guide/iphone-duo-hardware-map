# `/baseband`

- Name: `baseband`
- Parent: [`/`](root.md)
- phandle: `465`
- compatible: `baseband,int1`
- device_type: `baseband`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleBasebandINT1` | `IOPlatformDevice` | [`com.apple.driver.AppleBasebandINT1`](../kexts/com.apple.driver.AppleBasebandINT1.md) | `baseband,int1` |

## Interrupts [DT]

Controller: unresolved

`16, 100663300, 13`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `pmu_exton_config` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x7063494f 0x7800000 0x60000` |
| `bb_on` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x7063494f 0x800000 0xe0000` |
| `bb_warm_reset` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW4` | `0x62706c69 0x0` |
| `pmu_exton` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKR8` | `0x7063494f 0x2000000 0x60000` |
| `pcie_port_control` | [`/arm-io/apcie`](root__arm-io__apcie.md) | `PrtC` | `0x1a3` |
| `sac` | [`/sacm-general`](root__sacm-general.md) | `SACC` | `0x6c636430 0x6c636431 0x6c636432 0x6c636433 0x63616d30 0x63616d31 0x63616d32 0x63616d33 0x63616d34 0x63616d35 0x63616d36 0x63616d37 0x63616d38 0x63616d39 0x63616d41 0x63616d42 0x63616d43 0x63616d44 0x63616d45 0x63616d46 0x70726f78` |
| `jasper-sac` | [`/sacm-jasper`](root__sacm-jasper.md) | `SACC` | `0x63616d47` |
| `reset_det` | [`/arm-io/aop-gpio`](root__arm-io__aop-gpio.md) | `GPIO` | `0x10 0x0` |

## All properties (29) [DT]

- **`AAPL,phandle`**: `465` (`0x1d1`) → phandle of [`/baseband`](root__baseband.md)
- **`baseband-heb`**: `209` (`0xd1`)
- **`baseband-idc`**: `218` (`0xda`)
- **`class`**: `3` (`0x3`)
- **`compatible`**: `baseband,int1`
- **`config`**: 40 bytes
  - u32: `0xfa 0x1f4 0x0 0x3e8 0x64 0x64 0x0 0x0 0x0 0x64`
  ```
  000000  fa 00 00 00 f4 01 00 00 00 00 00 00 e8 03 00 00  ................
  000010  64 00 00 00 64 00 00 00 00 00 00 00 00 00 00 00  d...d...........
  000020  00 00 00 00 64 00 00 00                          ....d...
  ```
- **`default-options`**: `4` (`0x4`)
- **`device-imei`**: 32 bytes
  - u32: `0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0`
  ```
  000000  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000010  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  ```
- **`device_type`**: `baseband`
- **`function-bb_on`**: 20 bytes
  - u32: `0x9f 0x704b5738 0x7063494f 0x800000 0xe0000`
  - text inside: `8WKpOIcp`
  ```
  000000  9f 00 00 00 38 57 4b 70 4f 49 63 70 00 00 80 00  ....8WKpOIcp....
  000010  00 00 0e 00                                      ....
  ```
- **`function-bb_warm_reset`**: 16 bytes
  - u32: `0x9f 0x704b5734 0x62706c69 0x0`
  - text inside: `4WKpilpb`
  ```
  000000  9f 00 00 00 34 57 4b 70 69 6c 70 62 00 00 00 00  ....4WKpilpb....
  ```
- **`function-jasper-sac`**: 12 bytes
  - u32: `0x1d3 0x53414343 0x63616d47`
  - text inside: `CCASGmac`
  ```
  000000  d3 01 00 00 43 43 41 53 47 6d 61 63              ....CCASGmac
  ```
- **`function-pcie_port_control`**: 12 bytes
  - u32: `0x19e 0x50727443 0x1a3`
  - text inside: `CtrP`
  ```
  000000  9e 01 00 00 43 74 72 50 a3 01 00 00              ....CtrP....
  ```
- **`function-pmu_exton`**: 20 bytes
  - u32: `0x9f 0x704b5238 0x7063494f 0x2000000 0x60000`
  - text inside: `8RKpOIcp`
  ```
  000000  9f 00 00 00 38 52 4b 70 4f 49 63 70 00 00 00 02  ....8RKpOIcp....
  000010  00 00 06 00                                      ....
  ```
- **`function-pmu_exton_config`**: 20 bytes
  - u32: `0x9f 0x704b5738 0x7063494f 0x7800000 0x60000`
  - text inside: `8WKpOIcp`
  ```
  000000  9f 00 00 00 38 57 4b 70 4f 49 63 70 00 00 80 07  ....8WKpOIcp....
  000010  00 00 06 00                                      ....
  ```
- **`function-reset_det`**: 16 bytes
  - u32: `0x72 0x4750494f 0x10 0x0`
  - text inside: `OIPG`
  ```
  000000  72 00 00 00 4f 49 50 47 10 00 00 00 00 00 00 00  r...OIPG........
  ```
- **`function-sac`**: 92 bytes
  - u32: `0x1d2 0x53414343 0x6c636430 0x6c636431 0x6c636432 0x6c636433 0x63616d30 0x63616d31 0x63616d32 0x63616d33 0x63616d34 0x63616d35 0x63616d36 0x63616d37 0x63616d38 0x63616d39 0x63616d41 0x63616d42 0x63616d43 0x63616d44 0x63616d45 0x63616d46 0x70726f78`
  - text inside: `CCAS0dcl1dcl2dcl3dcl0mac1mac2mac3mac4mac5mac6mac7mac8mac9macAmacBmacCmacDmacEmacFmacxorp`
  ```
  000000  d2 01 00 00 43 43 41 53 30 64 63 6c 31 64 63 6c  ....CCAS0dcl1dcl
  000010  32 64 63 6c 33 64 63 6c 30 6d 61 63 31 6d 61 63  2dcl3dcl0mac1mac
  000020  32 6d 61 63 33 6d 61 63 34 6d 61 63 35 6d 61 63  2mac3mac4mac5mac
  000030  36 6d 61 63 37 6d 61 63 38 6d 61 63 39 6d 61 63  6mac7mac8mac9mac
  000040  41 6d 61 63 42 6d 61 63 43 6d 61 63 44 6d 61 63  AmacBmacCmacDmac
  000050  45 6d 61 63 46 6d 61 63 78 6f 72 70              EmacFmacxorp
  ```
- **`gnss-comms-interface`**: `2` (`0x2`)
- **`imeisv`**: `4` (`0x4`)
- **`interrupt-parent`**: `0x9f00000072` (u64; as two u32: `0x72`, `0x9f`)
- **`interrupts`**: 12 bytes
  - u32: `0x10 0x6000004 0xd`
  ```
  000000  10 00 00 00 04 00 00 06 0d 00 00 00              ............
  ```
- **`name`**: `baseband`
- **`ppm-idle-budget`**: `10` (`0xa`)
- **`ppm-low-budget`**: `1` (`0x1`)
- **`ppm-max-budget`**: `10000` (`0x2710`)
- **`region-sku`**: `syscfg/RSKU/0x40,zeroes/0x40` *(placeholder, filled in by iBoot at boot)*
- **`sdd-vers`**: `197123` (`0x30203`)
- **`smc-thermal-report-version`**: `3` (`0x3`)
- **`supports-cpms-via-spmi`**: `1` (`0x1`)
