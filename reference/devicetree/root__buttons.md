# `/buttons`

- Name: `buttons`
- Parent: [`/`](root.md)
- phandle: `452`
- compatible: `buttons`
- device_type: `buttons`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleM68Buttons` | `IOPlatformDevice` | [`com.apple.driver.AppleM68Buttons`](../kexts/com.apple.driver.AppleM68Buttons.md) | `buttons` |
| `AppleM68Buttons` | `IOPlatformDevice` | [`com.apple.driver.AppleM68Buttons`](../kexts/com.apple.driver.AppleM68Buttons.md) | `buttons` |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `button_volup` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `btnR` | `0x62565550` |
| `button_voldown` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `btnR` | `0x6256444e` |
| `button_hold` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `btnR` | `0x62484c44` |

## Referenced by (2) [DT]

- [`/arm-io/spi1/mesa`](root__arm-io__spi1__mesa.md): function-hid_event_dispatch `ButD`
- [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md): function-pmu_button `ButD`

## All properties (19) [DT]

- **`AAPL,phandle`**: `452` (`0x1c4`) → phandle of [`/buttons`](root__buttons.md)
- **`aot-power`**: `0x100000001` (u64; as two u32: `0x1`, `0x1`)
- **`button-delay_hold`**: `75000` (`0x124f8`)
- **`button-delay_voldown`**: `75000` (`0x124f8`)
- **`button-delay_volup`**: `75000` (`0x124f8`)
- **`button-names`**: `volup`, `voldown`, `hold`
- **`button-priority_hold`**: `1` (`0x1`)
- **`button-priority_voldown`**: `2` (`0x2`)
- **`button-priority_volup`**: `2` (`0x2`)
- **`compatible`**: `buttons`
- **`device_type`**: `buttons`
- **`diagnostic-mask-all`**: `voldown`, `volup`, `hold`
- **`function-button_hold`**: 12 bytes
  - u32: `0x9f 0x62746e52 0x62484c44`
  - text inside: `RntbDLHb`
  ```
  000000  9f 00 00 00 52 6e 74 62 44 4c 48 62              ....RntbDLHb
  ```
- **`function-button_voldown`**: 12 bytes
  - u32: `0x9f 0x62746e52 0x6256444e`
  - text inside: `RntbNDVb`
  ```
  000000  9f 00 00 00 52 6e 74 62 4e 44 56 62              ....RntbNDVb
  ```
- **`function-button_volup`**: 12 bytes
  - u32: `0x9f 0x62746e52 0x62565550`
  - text inside: `RntbPUVb`
  ```
  000000  9f 00 00 00 52 6e 74 62 50 55 56 62              ....RntbPUVb
  ```
- **`home-button-type`**: `2` (`0x2`)
- **`name`**: `buttons`
- **`remap-usages`**: `0xb002d000b002e` (u64; as two u32: `0xb002e`, `0xb002d`)
- **`stackshot-mask`**: `voldown`, `volup`, `hold`
