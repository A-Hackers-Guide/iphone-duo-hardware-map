# `/arm-io/mtp/iop-mtp-nub/multi-touch2`

- Name: `multi-touch2`
- Parent: [`/arm-io/mtp/iop-mtp-nub`](root__arm-io__mtp__iop-mtp-nub.md)
- phandle: `171`
- device_type: `multi-touch2`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `clock_enable` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x7063494f 0x8000000 0x0` |
| `reset` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x7063494f 0x0 0x1060000` |
| `power_1v2_core` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x70634c44 0x0 0xe0000` |

## Firmware with a matching name [FW]

- [`Firmware/V68_Multitouch.im4p`](../firmware/Firmware__V68_Multitouch.im4p.md) (2,657,500 B) Tag: IM4P  Type: mtfw  Version: 1

## All properties (17) [DT]

- **`AAPL,phandle`**: `171` (`0xab`) → phandle of [`/arm-io/mtp/iop-mtp-nub/multi-touch2`](root__arm-io__mtp__iop-mtp-nub__multi-touch2.md)
- **`auth-required`**: (present, empty)
- **`auth-source-index`**: `2` (`0x2`)
- **`bootloader-type`**: `CBOR`
- **`device_type`**: `multi-touch2`
- **`eeprom-read-property`**: `AppleDiagnosticDataDisplay`
- **`fdr-classes`**: `DspB/ADTN`, `adtn-calibration`, `DspB/CDTN`, `cdtn-calibration`, `DspB/CMFS`, `cmfs-calibration`, `DspB/DGFS`, `dgfs-calibration`, `DspB/FDTN`, `fdtn-calibration`, `DspB/FSPS`, `fsps-calibration`, `DspB/MTCL`, `mtcl-calibration`, `DspB/PCFG`, `pcfg-calibration`, `DspB/PDTN`, `pdtn-calibration`, `DspB/PGFS`, `pgfs-calibration`, `DspB/PSSS`, `psss-calibration`
- **`fdr-data-identifier`**: `DspB/ADTN`, `ZG:CoverGlassSerialNumberSecondary`, `DspB/CDTN`, `ZG:CoverGlassSerialNumberSecondary`, `DspB/CMFS`, `ZG:CoverGlassSerialNumberSecondary`, `DspB/DGFS`, `ZG:CoverGlassSerialNumberSecondary`, `DspB/FDTN`, `ZG:CoverGlassSerialNumberSecondary`, `DspB/FSPS`, `ZG:CoverGlassSerialNumberSecondary`, `DspB/MTCL`, `ZG:CoverGlassSerialNumberSecondary`, `DspB/PCFG`, `ZG:CoverGlassSerialNumberSecondary`, `DspB/PDTN`, `ZG:CoverGlassSerialNumberSecondary`, `DspB/PGFS`, `ZG:CoverGlassSerialNumberSecondary`, `DspB/PSSS`, `ZG:CoverGlassSerialNumberSecondary`
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
  - u32: `0x9f 0x704b5738 0x7063494f 0x0 0x1060000`
  - text inside: `8WKpOIcp`
  ```
  000000  9f 00 00 00 38 57 4b 70 4f 49 63 70 00 00 00 00  ....8WKpOIcp....
  000010  00 00 06 01                                      ....
  ```
- **`hid-merge-personality`**: `V68SS1`
- **`image-tag`**: `1836344951` (`0x6d746677`) (four-char code `mtfw`)
- **`name`**: `multi-touch2`
- **`non-auth-personality`**: `non-auth`
- **`service-display`**: `258` (`0x102`)
- **`ttw-supported`**: (present, empty)
