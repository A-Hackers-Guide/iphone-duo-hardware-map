# `/arm-io/mtp/iop-mtp-nub/nova`

- Name: `nova`
- Parent: [`/arm-io/mtp/iop-mtp-nub`](root__arm-io__mtp__iop-mtp-nub.md)
- phandle: `174`
- device_type: `nova`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `over-current-write` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `keyW` | `0x706d4d53` |
| `over-current-read` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `keyR` | `0x706d4d53` |
| `power` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x70634c44 0x0 0xa0000` |
| `current-read` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKR8` | `0x70634853 0x22000000 0xa0000` |

## All properties (12) [DT]

- **`AAPL,phandle`**: `174` (`0xae`) → phandle of [`/arm-io/mtp/iop-mtp-nub/nova`](root__arm-io__mtp__iop-mtp-nub__nova.md)
- **`bootloader-type`**: `FlatPack`
- **`device_type`**: `nova`
- **`function-current-read`**: 20 bytes
  - u32: `0x9f 0x704b5238 0x70634853 0x22000000 0xa0000`
  - text inside: `8RKpSHcp`
  ```
  000000  9f 00 00 00 38 52 4b 70 53 48 63 70 00 00 00 22  ....8RKpSHcp..."
  000010  00 00 0a 00                                      ....
  ```
- **`function-over-current-read`**: 12 bytes
  - u32: `0x9f 0x6b657952 0x706d4d53`
  - text inside: `RyekSMmp`
  ```
  000000  9f 00 00 00 52 79 65 6b 53 4d 6d 70              ....RyekSMmp
  ```
- **`function-over-current-write`**: 12 bytes
  - u32: `0x9f 0x6b657957 0x706d4d53`
  - text inside: `WyekSMmp`
  ```
  000000  9f 00 00 00 57 79 65 6b 53 4d 6d 70              ....WyekSMmp
  ```
- **`function-power`**: 20 bytes
  - u32: `0x9f 0x704b5738 0x70634c44 0x0 0xa0000`
  - text inside: `8WKpDLcp`
  ```
  000000  9f 00 00 00 38 57 4b 70 44 4c 63 70 00 00 00 00  ....8WKpDLcp....
  000010  00 00 0a 00                                      ....
  ```
- **`hid-merge-personality`**: `M1`
- **`image-tag`**: `1835951215` (`0x6d6e646f`) (four-char code `mndo`)
- **`name`**: `nova`
- **`nova-force-cal`**: `syscfg/NvFc` *(placeholder, filled in by iBoot at boot)*
- **`nova-touch-cal`**: `syscfg/NvTh` *(placeholder, filled in by iBoot at boot)*
