# `/arm-io/i2c2/audio-codec`

- Name: `audio-codec`
- Parent: [`/arm-io/i2c2`](root__arm-io__i2c2.md)
- phandle: `181`
- compatible: `audio-control,cs42l79`
- device_type: `audio-control`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleCS42L79Audio` | `AppleARMIICDevice` | [`com.apple.driver.AppleCS42L79Audio`](../kexts/com.apple.driver.AppleCS42L79Audio.md) | `audio-control,cs42l79` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x4a 0x3e8 0x0 0x0` | | |

## Interrupts [DT]

Controller: [`/arm-io/gpio0`](root__arm-io__gpio0.md)

`134, 1`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `Flicker_master` | [`/arm-io/iop-audio-controller/audio-flicker/audio-flicker`](root__arm-io__iop-audio-controller__audio-flicker__audio-flicker.md) | `AUD1` | `0x61703266` |
| `pdm_rx_control` | [`/arm-io/iop-audio-controller/audio-speaker`](root__arm-io__iop-audio-controller__audio-speaker.md) | `PDMi` | `` |
| `Receiver_master` | [`/arm-io/iop-audio-controller/audio-receiver/audio-receiver`](root__arm-io__iop-audio-controller__audio-receiver__audio-receiver.md) | `AUD1` | `0x61703272` |
| `reset` | [`/arm-io/aop-gpio`](root__arm-io__aop-gpio.md) | `GPIO` | `0x57 0x10001` |

## Referenced by (5) [DT]

- [`/arm-io/aop/iop-aop-nub/grimaldi-control`](root__arm-io__aop__iop-aop-nub__grimaldi-control.md): function-flicker_bias `flbs`
- [`/arm-io/iop-audio-controller/lp-mic-device`](root__arm-io__iop-audio-controller__lp-mic-device.md): function-cm_power_change_notify `lpsm`
- [`/arm-io/iop-audio-controller/siri-listening-device`](root__arm-io__iop-audio-controller__siri-listening-device.md): function-cm_power_change_notify `lpls`
- [`/arm-io/iop-audio-controller/audio-haptic`](root__arm-io__iop-audio-controller__audio-haptic.md): function-hall_ctrl `hall`
- [`/arm-io/iop-audio-controller/audio-hpdbg`](root__arm-io__iop-audio-controller__audio-hpdbg.md): function-hall_ctrl `hall`

## All properties (33) [DT]

- **`AAPL,phandle`**: `181` (`0xb5`) → phandle of [`/arm-io/i2c2/audio-codec`](root__arm-io__i2c2__audio-codec.md)
- **`ASP1`**: `0x600303034818` (u64; as two u32: `0x3034818`, `0x6003`)
- **`ASP2`**: `0x10300004818` (u64; as two u32: `0x4818`, `0x103`)
- **`ASP3`**: `0x707074810` (u64; as two u32: `0x7074810`, `0x7`)
- **`ASP4`**: `0x4818` (u64; as two u32: `0x4818`, `0x0`)
- **`Flicker`**: `0x2000102` (u64; as two u32: `0x2000102`, `0x0`)
- **`HPMic`**: `0x4000100` (u64; as two u32: `0x4000100`, `0x0`)
- **`Hall`**: `0x2020102` (u64; as two u32: `0x2020102`, `0x0`)
- **`LPMic`**: `0x8004060100` (u64; as two u32: `0x4060100`, `0x80`)
- **`Receiver`**: `0x1000000` (u64; as two u32: `0x1000000`, `0x0`)
- **`adc-gains`**: 12 bytes
  - u32: `0x6060606 0x86068383 0x8686`
  ```
  000000  06 06 06 06 83 83 06 86 86 86 00 00              ............
  ```
- **`compatible`**: `audio-control,cs42l79`
- **`device_type`**: `audio-control`
- **`flicker-config`**: `3` (`0x3`)
- **`fmic-mic`**: `0x309020903` (u64; as two u32: `0x9020903`, `0x3`)
- **`function-Flicker_master`**: 12 bytes
  - u32: `0x168 0x41554431 0x61703266`
  - text inside: `1DUAf2pa`
  ```
  000000  68 01 00 00 31 44 55 41 66 32 70 61              h...1DUAf2pa
  ```
- **`function-Receiver_master`**: 12 bytes
  - u32: `0x166 0x41554431 0x61703272`
  - text inside: `1DUAr2pa`
  ```
  000000  66 01 00 00 31 44 55 41 72 32 70 61              f...1DUAr2pa
  ```
- **`function-pdm_rx_control`**: `0x50444d6900000174` (u64; as two u32: `0x174`, `0x50444d69`)
- **`function-reset`**: 16 bytes
  - u32: `0x72 0x4750494f 0x57 0x10001`
  - text inside: `OIPGW`
  ```
  000000  72 00 00 00 4f 49 50 47 57 00 00 00 01 00 01 00  r...OIPGW.......
  ```
- **`halle-calibration`**: `syscfg/PSCl,syscfg-mismatch/PSCl` *(placeholder, filled in by iBoot at boot)*
- **`imic-mic`**: `0x307020701` (u64; as two u32: `0x7020701`, `0x3`)
- **`int-id`**: `0x8080404040404` (u64; as two u32: `0x4040404`, `0x80804`)
- **`int-offset`**: `0x1000d0b090200` (u64; as two u32: `0xb090200`, `0x1000d`)
- **`interrupt-parent`**: `53` (`0x35`) → phandle of [`/arm-io/gpio0`](root__arm-io__gpio0.md)
- **`interrupts`**: `0x100000086` (u64; as two u32: `0x86`, `0x1`)
- **`listening-mic-mask`**: `5` (`0x5`)
- **`lmic-mic`**: `0x30a020a04` (u64; as two u32: `0xa020a04`, `0x3`)
- **`name`**: `audio-codec`
- **`private`**: `1`
- **`reg`**: 16 bytes
  - u32: `0x4a 0x3e8 0x0 0x0`
  ```
  000000  4a 00 00 00 e8 03 00 00 00 00 00 00 00 00 00 00  J...............
  ```
- **`samplerate-default`**: `0xbb8000000000` (u64; as two u32: `0x0`, `0xbb80`)
- **`samplerate-subset`**: 16 bytes
  - u32: `0x0 0xbb80 0x0 0x0`
  ```
  000000  00 00 00 00 80 bb 00 00 00 00 00 00 00 00 00 00  ................
  ```
- **`smic-mic`**: `0x308020802` (u64; as two u32: `0x8020802`, `0x3`)
