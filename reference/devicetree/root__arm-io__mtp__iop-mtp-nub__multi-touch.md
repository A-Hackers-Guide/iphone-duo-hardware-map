# `/arm-io/mtp/iop-mtp-nub/multi-touch`

- Name: `multi-touch`
- Parent: [`/arm-io/mtp/iop-mtp-nub`](root__arm-io__mtp__iop-mtp-nub.md)
- phandle: `173`
- device_type: `multi-touch`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleSPUControl` | `AppleARMIODevice` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) | `multi-touch` |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `clock_enable` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x7063494f 0x8000000 0x0` |
| `reset` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x7063494f 0x0 0x1050000` |
| `power_1v2_core` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x70634c44 0x0 0xe0000` |

## Firmware with a matching name [FW]

- [`Firmware/V68_Multitouch.im4p`](../firmware/Firmware__V68_Multitouch.im4p.md) (2,657,500 B) Tag: IM4P  Type: mtfw  Version: 1

## All properties (17) [DT]

- **`AAPL,phandle`**: `173` (`0xad`) → phandle of [`/arm-io/mtp/iop-mtp-nub/multi-touch`](root__arm-io__mtp__iop-mtp-nub__multi-touch.md)
- **`auth-required`**: (present, empty)
- **`auth-source-index`**: `1` (`0x1`)
- **`bootloader-type`**: `CBOR`
- **`device_type`**: `multi-touch`
- **`eeprom-read-property`**: `AppleDiagnosticDataDisplay`
- **`fdr-classes`**: `DspB/ADTN`, `adtn-calibration`, `DspB/CDTN`, `cdtn-calibration`, `DspB/CMFS`, `cmfs-calibration`, `DspB/DGFS`, `dgfs-calibration`, `DspB/FDTN`, `fdtn-calibration`, `DspB/FSPS`, `fsps-calibration`, `DspB/MTCL`, `mtcl-calibration`, `DspB/PCFG`, `pcfg-calibration`, `DspB/PDTN`, `pdtn-calibration`, `DspB/PGFS`, `pgfs-calibration`, `DspB/PSSS`, `psss-calibration`
- **`fdr-data-identifier`**: `DspB/ADTN`, `OWi11Urd09rDmPVy1z5dOQ`, `DspB/CDTN`, `OWi11Urd09rDmPVy1z5dOQ`, `DspB/CMFS`, `OWi11Urd09rDmPVy1z5dOQ`, `DspB/DGFS`, `OWi11Urd09rDmPVy1z5dOQ`, `DspB/FDTN`, `OWi11Urd09rDmPVy1z5dOQ`, `DspB/FSPS`, `OWi11Urd09rDmPVy1z5dOQ`, `DspB/MTCL`, `OWi11Urd09rDmPVy1z5dOQ`, `DspB/PCFG`, `OWi11Urd09rDmPVy1z5dOQ`, `DspB/PDTN`, `OWi11Urd09rDmPVy1z5dOQ`, `DspB/PGFS`, `OWi11Urd09rDmPVy1z5dOQ`, `DspB/PSSS`, `OWi11Urd09rDmPVy1z5dOQ`
- **`function-clock_enable`**: 20 bytes
  - u32: `0x9f 0x704b5738 0x7063494f 0x8000000 0x0`
  - text inside: `8WKpOIcp`
  ```
  000000  9f 00 00 00 38 57 4b 70 4f 49 63 70 00 00 00 08  ....8WKpOIcp....
  000010  00 00 00 00                                      ....
  ```
- **`function-power_1v2_core`**: 20 bytes
  - u32: `0x9f 0x704b5738 0x70634c44 0x0 0xe0000`
  - text inside: `8WKpDLcp`
  ```
  000000  9f 00 00 00 38 57 4b 70 44 4c 63 70 00 00 00 00  ....8WKpDLcp....
  000010  00 00 0e 00                                      ....
  ```
- **`function-reset`**: 20 bytes
  - u32: `0x9f 0x704b5738 0x7063494f 0x0 0x1050000`
  - text inside: `8WKpOIcp`
  ```
  000000  9f 00 00 00 38 57 4b 70 4f 49 63 70 00 00 00 00  ....8WKpOIcp....
  000010  00 00 05 01                                      ....
  ```
- **`hid-merge-personality`**: `V68PS1`
- **`image-tag`**: `1836344951` (`0x6d746677`) (four-char code `mtfw`)
- **`name`**: `multi-touch`
- **`non-auth-personality`**: `non-auth`
- **`service-display`**: `233` (`0xe9`)
- **`ttw-supported`**: (present, empty)
