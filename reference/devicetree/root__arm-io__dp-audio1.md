# `/arm-io/dp-audio1`

- Name: `dp-audio1`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `289`
- device_type: `dp-audio1`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `DCPAVAudioDMADelegate` | `AppleARMIODevice` | [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md) | `dp-audio1` |

## All properties (5) [DT]

- **`AAPL,phandle`**: `289` (`0x121`) → phandle of [`/arm-io/dp-audio1`](root__arm-io__dp-audio1.md)
- **`device_type`**: `dp-audio1`
- **`dma-channels`**: 32 bytes
  - u32: `0x0 0x2 0x0 0x1000 0x800 0x0 0x0 0x0`
  ```
  000000  00 00 00 00 02 00 00 00 00 00 00 00 00 10 00 00  ................
  000010  00 08 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  ```
- **`dma-parent`**: `287` (`0x11f`) → phandle of [`/arm-io/admac-dispext0`](root__arm-io__admac-dispext0.md)
- **`name`**: `dp-audio1`
