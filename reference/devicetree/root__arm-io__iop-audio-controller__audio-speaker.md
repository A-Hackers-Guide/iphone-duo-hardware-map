# `/arm-io/iop-audio-controller/audio-speaker`

- Name: `audio-speaker`
- Parent: [`/arm-io/iop-audio-controller`](root__arm-io__iop-audio-controller.md)
- phandle: `372`
- compatible: `audio-iop-speaker`
- device_type: `iop-audio-ns`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IOPAudioSpeaker` | `AppleAOPAudioDeviceProvider` | [`com.apple.driver.IOPAudioSpeaker`](../kexts/com.apple.driver.IOPAudioSpeaker.md) | `audio-iop-speaker` |
| `IOPAudioSpeaker` | `IOPAudioNode` | [`com.apple.driver.IOPAudioSpeaker`](../kexts/com.apple.driver.IOPAudioSpeaker.md) | `audio-iop-speaker` |

## Referenced by (1) [DT]

- [`/arm-io/i2c2/audio-codec`](root__arm-io__i2c2__audio-codec.md): function-pdm_rx_control `PDMi`

## All properties (9) [DT]

- **`AAPL,phandle`**: `372` (`0x174`) → phandle of [`/arm-io/iop-audio-controller/audio-speaker`](root__arm-io__iop-audio-controller__audio-speaker.md)
- **`compatible`**: `audio-iop-speaker`
- **`device_type`**: `iop-audio-ns`
- **`iboot-audio-volume`**: `32767` (`0x7fff`)
- **`identifier`**: `1936747378` (`0x73706b72`) (four-char code `spkr`)
- **`input-data-source-selectors`**: 48 bytes
  - u32: `0x73705630 0x73704930 0x73763230 0x73657230 0x73696630 0x73766630 0x73705631 0x73704931 0x73763231 0x73657231 0x73696631 0x73766631`
  - text inside: `0Vps0Ips02vs0res0fis0fvs1Vps1Ips12vs1res1fis1fvs`
  ```
  000000  30 56 70 73 30 49 70 73 30 32 76 73 30 72 65 73  0Vps0Ips02vs0res
  000010  30 66 69 73 30 66 76 73 31 56 70 73 31 49 70 73  0fis0fvs1Vps1Ips
  000020  31 32 76 73 31 72 65 73 31 66 69 73 31 66 76 73  12vs1res1fis1fvs
  ```
- **`name`**: `audio-speaker`
- **`output-data-source-selectors`**: `0x546f7053426f7453` (u64; as two u32: `0x426f7453`, `0x546f7053`)
- **`private`**: `1`
