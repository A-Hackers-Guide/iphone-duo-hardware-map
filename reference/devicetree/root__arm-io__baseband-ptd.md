# `/arm-io/baseband-ptd`

- Name: `baseband-ptd`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `449`
- compatible: `baseband,ptd`
- device_type: `baseband-ptd`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleBasebandSARPTD` | `AppleARMIODevice` | [`com.apple.driver.AppleSARService`](../kexts/com.apple.driver.AppleSARService.md) | `baseband,ptd` |

## Interrupts [DT]

Controller: [`/arm-io/aon-ptd`](root__arm-io__aon-ptd.md)

`1128484931, 1128485705, 1128486221, 1128481603, 1128485714, 1128485701, 1128484176, 1128484165, 1128485447, 1128485459, 1128485680, 1128485681, 1128485955, 1128485959, 1128485975`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `ptd_read_mult` | [`/arm-io/aon-ptd`](root__arm-io__aon-ptd.md) | `ptMR` | `` |
| `ptd_lookup_mult` | [`/arm-io/aon-ptd`](root__arm-io__aon-ptd.md) | `ptML` | `` |
| `ptd_peek_mult` | [`/arm-io/aon-ptd`](root__arm-io__aon-ptd.md) | `ptMP` | `` |

## All properties (9) [DT]

- **`AAPL,phandle`**: `449` (`0x1c1`) → phandle of [`/arm-io/baseband-ptd`](root__arm-io__baseband-ptd.md)
- **`compatible`**: `baseband,ptd`
- **`device_type`**: `baseband-ptd`
- **`function-ptd_lookup_mult`**: `0x70744d4c000000a6` (u64; as two u32: `0xa6`, `0x70744d4c`)
- **`function-ptd_peek_mult`**: `0x70744d50000000a6` (u64; as two u32: `0xa6`, `0x70744d50`)
- **`function-ptd_read_mult`**: `0x70744d52000000a6` (u64; as two u32: `0xa6`, `0x70744d52`)
- **`interrupt-parent`**: `166` (`0xa6`) → phandle of [`/arm-io/aon-ptd`](root__arm-io__aon-ptd.md)
- **`interrupts`**: 60 bytes
  - u32: `0x43435043 0x43435349 0x4343554d 0x43434343 0x43435352 0x43435345 0x43434d50 0x43434d45 0x43435247 0x43435253 0x43435330 0x43435331 0x43435443 0x43435447 0x43435457`
  - text inside: `CPCCISCCMUCCCCCCRSCCESCCPMCCEMCCGRCCSRCC0SCC1SCCCTCCGTCCWTCC`
  ```
  000000  43 50 43 43 49 53 43 43 4d 55 43 43 43 43 43 43  CPCCISCCMUCCCCCC
  000010  52 53 43 43 45 53 43 43 50 4d 43 43 45 4d 43 43  RSCCESCCPMCCEMCC
  000020  47 52 43 43 53 52 43 43 30 53 43 43 31 53 43 43  GRCCSRCC0SCC1SCC
  000030  43 54 43 43 47 54 43 43 57 54 43 43              CTCCGTCCWTCC
  ```
- **`name`**: `baseband-ptd`
