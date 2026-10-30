# `/arm-io/dart-dcpsec/mapper-dcpsec-exclave`

- Name: `mapper-dcpsec-exclave`
- Parent: [`/arm-io/dart-dcpsec`](root__arm-io__dart-dcpsec.md)
- phandle: `262`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x4` | | |

## Referenced by (1) [DT]

- [`/arm-io/dcpsec-exclave-mailbox`](root__arm-io__dcpsec-exclave-mailbox.md): `iommu-parent`

## All properties (5) [DT]

- **`AAPL,phandle`**: `262` (`0x106`) → phandle of [`/arm-io/dart-dcpsec/mapper-dcpsec-exclave`](root__arm-io__dart-dcpsec__mapper-dcpsec-exclave.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-dcpsec-exclave`
- **`reg`**: `4` (`0x4`)
