# `/arm-io/smc/iop-smc-nub/smc-ext-charger`

- Name: `smc-ext-charger`
- Parent: [`/arm-io/smc/iop-smc-nub`](root__arm-io__smc__iop-smc-nub.md)
- phandle: `161`
- device_type: `smc-ext-charger`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleSMCWirelessCharger` | `AppleSMCInterface` | [`com.apple.driver.AppleSMCWirelessCharger`](../kexts/com.apple.driver.AppleSMCWirelessCharger.md) | `smc-ext-charger` |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `dock_parent` | [`/port-magsafe-1`](root__port-magsafe-1.md) | `accP` | `` |
| `dock_wired` | [`/port-usb-c-1`](root__port-usb-c-1.md) | `accP` | `` |

## All properties (17) [DT]

- **`AAPL,phandle`**: `161` (`0xa1`) → phandle of [`/arm-io/smc/iop-smc-nub/smc-ext-charger`](root__arm-io__smc__iop-smc-nub__smc-ext-charger.md)
- **`audio-driver`**: `AppleCS42L79Audio`
- **`backlight-detection`**: `0` (`0x0`)
- **`camera-driver`**: `AppleCamera`
- **`device_type`**: `smc-ext-charger`
- **`extended-otp-cal`**: `1` (`0x1`)
- **`function-dock_parent`**: `0x61636350000001c6` (u64; as two u32: `0x1c6`, `0x61636350`)
- **`function-dock_wired`**: `0x61636350000001c5` (u64; as two u32: `0x1c5`, `0x61636350`)
- **`has-espresso`**: `1` (`0x1`)
- **`has-ironbull-camera-cloak`**: `1` (`0x1`)
- **`has-ironman-camera-cloak`**: `1` (`0x1`)
- **`has-ironman-charging`**: `1` (`0x1`)
- **`has-peripheral-logs`**: `4` (`0x4`)
- **`hd-mic-coex`**: `1` (`0x1`)
- **`name`**: `smc-ext-charger`
- **`port-number`**: `1` (`0x1`)
- **`port-type`**: `9` (`0x9`)
