# `/arm-io/dcpsec-sac-controller`

- Name: `dcpsec-sac-controller`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `270`
- compatible: `dcp-sac-controller`
- device_type: `dcpsec-sac-controller`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `DCPAVSACController` | `IOService` | [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md) | `dcp-sac-controller` |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `saca_lcd0` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x6c636432` |
| `saca_lcd1` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x6c636433` |

## All properties (8) [DT]

- **`AAPL,phandle`**: `270` (`0x10e`) → phandle of [`/arm-io/dcpsec-sac-controller`](root__arm-io__dcpsec-sac-controller.md)
- **`compatible`**: `dcp-sac-controller`
- **`device_type`**: `dcpsec-sac-controller`
- **`function-saca_lcd0`**: 12 bytes
  - u32: `0x1d2 0x53414341 0x6c636432`
  - text inside: `ACAS2dcl`
  ```
  000000  d2 01 00 00 41 43 41 53 32 64 63 6c              ....ACAS2dcl
  ```
- **`function-saca_lcd1`**: 12 bytes
  - u32: `0x1d2 0x53414341 0x6c636433`
  - text inside: `ACAS3dcl`
  ```
  000000  d2 01 00 00 41 43 41 53 33 64 63 6c              ....ACAS3dcl
  ```
- **`name`**: `dcpsec-sac-controller`
- **`role`**: `DCPSEC`
- **`sac-index-count`**: `2` (`0x2`)
