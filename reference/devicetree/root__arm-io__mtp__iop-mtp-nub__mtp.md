# `/arm-io/mtp/iop-mtp-nub/mtp`

- Name: `mtp`
- Parent: [`/arm-io/mtp/iop-mtp-nub`](root__arm-io__mtp__iop-mtp-nub.md)
- phandle: `175`
- device_type: `mtp-info`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `ptd_lookup_mult` | [`/arm-io/aon-ptd`](root__arm-io__aon-ptd.md) | `ptML` | `` |

## Firmware with a matching name [FW]

- [`Firmware/V68_MtpFirmware.im4p`](../firmware/Firmware__V68_MtpFirmware.im4p.md) (2,308,247 B) Tag: IM4P  Type: mtpf  Version: 1

## All properties (4) [DT]

- **`AAPL,phandle`**: `175` (`0xaf`) → phandle of [`/arm-io/mtp/iop-mtp-nub/mtp`](root__arm-io__mtp__iop-mtp-nub__mtp.md)
- **`device_type`**: `mtp-info`
- **`function-ptd_lookup_mult`**: `0x70744d4c000000a6` (u64; as two u32: `0xa6`, `0x70744d4c`)
- **`name`**: `mtp`
