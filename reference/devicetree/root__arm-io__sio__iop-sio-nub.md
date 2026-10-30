# `/arm-io/sio/iop-sio-nub`

- Name: `iop-sio-nub`
- Parent: [`/arm-io/sio`](root__arm-io__sio.md)
- phandle: `136`
- compatible: `iop-nub,rtbuddy-v2`
- Children (1): [`/arm-io/sio/iop-sio-nub/sio-dma`](root__arm-io__sio__iop-sio-nub__sio-dma.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `RTBuddy` | `AppleA7IOPNub` | [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md) | `iop-nub,rtbuddy-v2` |

## All properties (6) [DT]

- **`AAPL,phandle`**: `136` (`0x88`) → phandle of [`/arm-io/sio/iop-sio-nub`](root__arm-io__sio__iop-sio-nub.md)
- **`compatible`**: `iop-nub,rtbuddy-v2`
- **`coredump-enable`**: `64` (`0x40`)
- **`name`**: `iop-sio-nub`
- **`no-firmware-service`**: (present, empty)
- **`user-power-managed`**: `1` (`0x1`)
