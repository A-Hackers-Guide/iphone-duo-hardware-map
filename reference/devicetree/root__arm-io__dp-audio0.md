# `/arm-io/dp-audio0`

- Name: `dp-audio0`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `249`
- device_type: `dp-audio0`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `DCPAVAudioDMADelegate` | `AppleARMIODevice` | [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md) | `dp-audio0` |

## All properties (8) [DT]

- **`AAPL,phandle`**: `249` (`0xf9`) → phandle of [`/arm-io/dp-audio0`](root__arm-io__dp-audio0.md)
- **`clock-gates`**: `34` (`0x22`)
- **`device_type`**: `dp-audio0`
- **`dma-channels`**: 32 bytes
  - u32: `0x0 0x2 0x0 0x1000 0x800 0x0 0x0 0x0`
  ```
  000000  00 00 00 00 02 00 00 00 00 00 00 00 00 10 00 00  ................
  000010  00 08 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  ```
- **`dma-parent`**: `247` (`0xf7`) → phandle of [`/arm-io/admac-dispint0`](root__arm-io__admac-dispint0.md)
- **`name`**: `dp-audio0`
- **`power-gates`**: `34` (`0x22`)
- **`service-gates`**: `34` (`0x22`)
