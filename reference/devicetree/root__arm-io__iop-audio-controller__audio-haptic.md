# `/arm-io/iop-audio-controller/audio-haptic`

- Name: `audio-haptic`
- Parent: [`/arm-io/iop-audio-controller`](root__arm-io__iop-audio-controller.md)
- phandle: `373`
- compatible: `audio-control,audio-iop-haptics`
- device_type: `iop-audio-ns`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IOPHaptics` | `IOPAudioNode` | [`com.apple.driver.IOPHaptics`](../kexts/com.apple.driver.IOPHaptics.md) | `audio-control,audio-iop-haptics` |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `haptics_session` | [`/arm-io/haptics-support-interface`](root__arm-io__haptics-support-interface.md) | `hpsc` | `` |
| `hall_ctrl` | [`/arm-io/i2c2/audio-codec`](root__arm-io__i2c2__audio-codec.md) | `hall` | `` |
| `thermal_budget` | [`/arm-io/haptics-support-interface`](root__arm-io__haptics-support-interface.md) | `ther` | `` |
| `power_peak_budget` | [`/arm-io/haptics-support-interface`](root__arm-io__haptics-support-interface.md) | `pkpw` | `` |

## Firmware with a matching name [FW]

- [`Firmware/V68_HapticAssets.im4p`](../firmware/Firmware__V68_HapticAssets.im4p.md) (1,174 B) Tag: IM4P  Type: hpas  Version: 1

## All properties (19) [DT]

- **`AAPL,phandle`**: `373` (`0x175`) → phandle of [`/arm-io/iop-audio-controller/audio-haptic`](root__arm-io__iop-audio-controller__audio-haptic.md)
- **`audio-enable-warmup-ms`**: `3` (`0x3`)
- **`compatible`**: `audio-control,audio-iop-haptics`
- **`device_type`**: `iop-audio-ns`
- **`function-hall_ctrl`**: `0x68616c6c000000b5` (u64; as two u32: `0xb5`, `0x68616c6c`)
- **`function-haptics_session`**: `0x68707363000001b9` (u64; as two u32: `0x1b9`, `0x68707363`)
- **`function-power_peak_budget`**: `0x706b7077000001b9` (u64; as two u32: `0x1b9`, `0x706b7077`)
- **`function-thermal_budget`**: `0x74686572000001b9` (u64; as two u32: `0x1b9`, `0x74686572`)
- **`identifier`**: `1634756707` (`0x61706863`) (four-char code `aphc`)
- **`input-latency`**: `8` (`0x8`)
- **`model-name`**: `leap`
- **`name`**: `audio-haptic`
- **`output-latency`**: `8` (`0x8`)
- **`peak-power-range`**: 12 bytes
  - u32: `0x1644 0x534 0x1644`
  ```
  000000  44 16 00 00 34 05 00 00 44 16 00 00              D...4...D...
  ```
- **`powered-on-state`**: `1886876260` (`0x70777264`) (four-char code `pwrd`)
- **`prewarm-on-state`**: `1886859552` (`0x70773120`) (four-char code `pw1 `)
- **`thermal-budget-range`**: 12 bytes
  - u32: `0xb3f 0x177 0xb3f`
  ```
  000000  3f 0b 00 00 77 01 00 00 3f 0b 00 00              ?...w...?...
  ```
- **`uid`**: `Actuator`
- **`zerofill-buffer-size-ms`**: `5` (`0x5`)
