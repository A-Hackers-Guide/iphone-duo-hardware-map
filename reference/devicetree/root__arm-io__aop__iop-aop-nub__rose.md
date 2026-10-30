# `/arm-io/aop/iop-aop-nub/rose`

- Name: `rose`
- Parent: [`/arm-io/aop/iop-aop-nub`](root__arm-io__aop__iop-aop-nub.md)
- phandle: `101`
- device_type: `rose`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleSPURoseDriver` | `AppleSPUAppInterface` | [`com.apple.driver.AppleSPURose`](../kexts/com.apple.driver.AppleSPURose.md) | `rose` |
| `AppleSPURoseDriverV2` | `AppleSPUAppInterface` | [`com.apple.driver.AppleSPURose`](../kexts/com.apple.driver.AppleSPURose.md) | `rose` |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `rose_pwr` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x70634c44 0x0 0x80000` |
| `rose_reset` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x7063494f 0x800000 0x70000` |
| `rd_rose_pwr` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKR8` | `0x70634c44 0x0 0x80000` |
| `rose_coredump` | [`/arm-io/aop-gpio`](root__arm-io__aop-gpio.md) | `GPIO` | `0xc 0x101` |

## Referenced by (8) [DT]

- [`/arm-io/dart-dcp`](root__arm-io__dart-dcp.md): `dart-options`
- [`/arm-io/dart-disp0`](root__arm-io__dart-disp0.md): `dart-options`
- [`/arm-io/dart-dispgrt`](root__arm-io__dart-dispgrt.md): `dart-options`
- [`/arm-io/dart-dcpsec`](root__arm-io__dart-dcpsec.md): `dart-options`
- [`/arm-io/dart-dispsec`](root__arm-io__dart-dispsec.md): `dart-options`
- [`/arm-io/dart-dispsecgrt`](root__arm-io__dart-dispsecgrt.md): `dart-options`
- [`/arm-io/dart-dcpext0`](root__arm-io__dart-dcpext0.md): `dart-options`
- [`/arm-io/dart-dispext0`](root__arm-io__dart-dispext0.md): `dart-options`

## Firmware with a matching name [FW]

- [`Firmware/Rose/r2p1/ftab.bin`](../firmware/Firmware__Rose__r2p1__ftab.bin.md) (1,069,300 B) 

## All properties (12) [DT]

- **`AAPL,phandle`**: `101` (`0x65`) → phandle of [`/arm-io/aop/iop-aop-nub/rose`](root__arm-io__aop__iop-aop-nub__rose.md)
- **`device_type`**: `rose`
- **`function-rd_rose_pwr`**: 20 bytes
  - u32: `0x9f 0x704b5238 0x70634c44 0x0 0x80000`
  - text inside: `8RKpDLcp`
  ```
  000000  9f 00 00 00 38 52 4b 70 44 4c 63 70 00 00 00 00  ....8RKpDLcp....
  000010  00 00 08 00                                      ....
  ```
- **`function-rose_coredump`**: 16 bytes
  - u32: `0x72 0x4750494f 0xc 0x101`
  - text inside: `OIPG`
  ```
  000000  72 00 00 00 4f 49 50 47 0c 00 00 00 01 01 00 00  r...OIPG........
  ```
- **`function-rose_pwr`**: 20 bytes
  - u32: `0x9f 0x704b5738 0x70634c44 0x0 0x80000`
  - text inside: `8WKpDLcp`
  ```
  000000  9f 00 00 00 38 57 4b 70 44 4c 63 70 00 00 00 00  ....8WKpDLcp....
  000010  00 00 08 00                                      ....
  ```
- **`function-rose_reset`**: 20 bytes
  - u32: `0x9f 0x704b5738 0x7063494f 0x800000 0x70000`
  - text inside: `8WKpOIcp`
  ```
  000000  9f 00 00 00 38 57 4b 70 4f 49 63 70 00 00 80 00  ....8WKpOIcp....
  000010  00 00 07 00                                      ....
  ```
- **`iommu-parent`**: `152` (`0x98`) → phandle of [`/arm-io/dart-sbr/mapper-scm`](root__arm-io__dart-sbr__mapper-scm.md)
- **`name`**: `rose`
- **`sequence-power_off`**: 46 bytes
  - text inside: `function-rose_reset`, `function-rose_pwr`
  ```
  000000  66 75 6e 63 74 69 6f 6e 2d 72 6f 73 65 5f 72 65  function-rose_re
  000010  73 65 74 00 00 90 01 00 66 75 6e 63 74 69 6f 6e  set.....function
  000020  2d 72 6f 73 65 5f 70 77 72 00 00 0a 00 00        -rose_pwr.....
  ```
- **`sequence-power_on`**: 22 bytes
  - text inside: `function-rose_pwr`
  ```
  000000  66 75 6e 63 74 69 6f 6e 2d 72 6f 73 65 5f 70 77  function-rose_pw
  000010  72 00 01 64 00 00                                r..d..
  ```
- **`sequence-reset`**: 48 bytes
  - u32: `0x636e7566 0x6e6f6974 0x736f722d 0x65725f65 0x746573 0xa00 0x636e7566 0x6e6f6974 0x736f722d 0x65725f65 0x746573 0xa01`
  - text inside: `function-rose_reset`, `function-rose_reset`
  ```
  000000  66 75 6e 63 74 69 6f 6e 2d 72 6f 73 65 5f 72 65  function-rose_re
  000010  73 65 74 00 00 0a 00 00 66 75 6e 63 74 69 6f 6e  set.....function
  000020  2d 72 6f 73 65 5f 72 65 73 65 74 00 01 0a 00 00  -rose_reset.....
  ```
- **`sequence-trigger_coredump`**: 54 bytes
  - text inside: `function-rose_coredump`, `function-rose_coredump`
  ```
  000000  66 75 6e 63 74 69 6f 6e 2d 72 6f 73 65 5f 63 6f  function-rose_co
  000010  72 65 64 75 6d 70 00 01 14 00 00 66 75 6e 63 74  redump.....funct
  000020  69 6f 6e 2d 72 6f 73 65 5f 63 6f 72 65 64 75 6d  ion-rose_coredum
  000030  70 00 00 01 00 00                                p.....
  ```
