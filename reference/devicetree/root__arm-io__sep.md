# `/arm-io/sep`

- Name: `sep`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `126`
- compatible: `iop-sep,ascwrap-v8`
- device_type: `sep`
- Children (1): [`/arm-io/sep/iop-sep-nub`](root__arm-io__sep__iop-sep-nub.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleASCWrapV8SEP` | `AppleARMIODevice` | [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md) | `iop-sep,ascwrap-v8` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0xa2600000` | `0x74000` (475,136 B) | `0x2a2600000`–`0x2a2673fff` |
| 1 | `0xa2050000` | `0x60000` (393,216 B) | `0x2a2050000`–`0x2a20affff` |
| 2 | `0xa2700000` | `0x14000` (81,920 B) | `0x2a2700000`–`0x2a2713fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`424, 423`

## Referenced by (3) [DT]

- [`/arm-io/dcp`](root__arm-io__dcp.md): `hdcp-parent`
- [`/arm-io/dcpsec`](root__arm-io__dcpsec.md): `hdcp-parent`
- [`/arm-io/dcpext0`](root__arm-io__dcpext0.md): `hdcp-parent`

## Firmware with a matching name [FW]

- [`Firmware/all_flash/sep-firmware.v68.RELEASE.im4p`](../firmware/Firmware__all_flash__sep-firmware.v68.RELEASE.im4p.md) (7,216,106 B) Tag: IM4P  Type: sepi  Version: 1
- [`Firmware/all_flash/sep-patches.v68.im4p`](../firmware/Firmware__all_flash__sep-patches.v68.im4p.md) (21,137 B) Tag: IM4P  Type: stg1  Version: AppleSEPROM-1483.0.0.100.14

## All properties (23) [DT]

- **`AAPL,phandle`**: `126` (`0x7e`) → phandle of [`/arm-io/sep`](root__arm-io__sep.md)
- **`SEPHiddenKeySupport`**: (present, empty)
- **`aarch64`**: (present, empty)
- **`clock-gates`**: (present, empty)
- **`clock-ids`**: `401` (`0x191`)
- **`compatible`**: `iop-sep,ascwrap-v8`
- **`cpu-ctrl-filtered`**: (present, empty)
- **`device_type`**: `sep`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `0x1a7000001a8` (u64; as two u32: `0x1a8`, `0x1a7`)
- **`iommu-parent`**: `132` (`0x84`) → phandle of [`/arm-io/dart-sep/mapper-sep`](root__arm-io__dart-sep__mapper-sep.md)
- **`iop-version`**: `1` (`0x1`)
- **`low-power-enable`**: (present, empty)
- **`name`**: `sep`
- **`power-gates`**: (present, empty)
- **`reg`**: 48 bytes
  - u32: `0xa2600000 0x0 0x74000 0x0 0xa2050000 0x0 0x60000 0x0 0xa2700000 0x0 0x14000 0x0`
  ```
  000000  00 00 60 a2 00 00 00 00 00 40 07 00 00 00 00 00  ..`......@......
  000010  00 00 05 a2 00 00 00 00 00 00 06 00 00 00 00 00  ................
  000020  00 00 70 a2 00 00 00 00 00 40 01 00 00 00 00 00  ..p......@......
  ```
- **`role`**: `SEP`
- **`self-power-gate`**: (present, empty)
- **`sika-support`**: `1` (`0x1`)
- **`ucert-offset`**: `0` (`0x0`)
- **`ucert-size`**: `588` (`0x24c`)
- **`ucont-offset`**: `592` (`0x250`)
- **`ucont-size`**: `1324` (`0x52c`)
