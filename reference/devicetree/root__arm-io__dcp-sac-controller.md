# `/arm-io/dcp-sac-controller`

- Name: `dcp-sac-controller`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `250`
- device_type: `dcp-sac-controller`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `DCPAVSACController` | `IOService` | [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md) | `dcp-sac-controller` |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `saca_lcd0` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x6c636430` |
| `saca_lcd1` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x6c636431` |

## Firmware with a matching name [FW]

- [`Firmware/dcp/t8160dcp.im4p`](../firmware/Firmware__dcp__t8160dcp.im4p.md) (3,016,187 B) Tag: IM4P  Type: dcpf  Version: 1
- [`Firmware/dcp/t8160dcp_restore.im4p`](../firmware/Firmware__dcp__t8160dcp_restore.im4p.md) (3,016,667 B) Tag: IM4P  Type: dcpf  Version: 1

## All properties (6) [DT]

- **`AAPL,phandle`**: `250` (`0xfa`) → phandle of [`/arm-io/dcp-sac-controller`](root__arm-io__dcp-sac-controller.md)
- **`device_type`**: `dcp-sac-controller`
- **`function-saca_lcd0`**: 12 bytes
  - u32: `0x1d2 0x53414341 0x6c636430`
  - text inside: `ACAS0dcl`
  ```
  000000  d2 01 00 00 41 43 41 53 30 64 63 6c              ....ACAS0dcl
  ```
- **`function-saca_lcd1`**: 12 bytes
  - u32: `0x1d2 0x53414341 0x6c636431`
  - text inside: `ACAS1dcl`
  ```
  000000  d2 01 00 00 41 43 41 53 31 64 63 6c              ....ACAS1dcl
  ```
- **`name`**: `dcp-sac-controller`
- **`sac-index-count`**: `2` (`0x2`)
