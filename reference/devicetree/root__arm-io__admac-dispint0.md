# `/arm-io/admac-dispint0`

- Name: `admac-dispint0`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `247`
- compatible: `admac,v5p0`
- device_type: `admac`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AudioDMAController` | `AppleARMIODevice` | [`com.apple.driver.AudioDMAController-Gen5p0`](../kexts/com.apple.driver.AudioDMAController-Gen5p0.md) | `admac,v5p0` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x186140000` | `0x84000` (540,672 B) | `0x386140000`–`0x3861c3fff` |
| 1 | `0x882a8000` | `0x8` (8 B) | `0x2882a8000`–`0x2882a8007` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`793`

## Referenced by (1) [DT]

- [`/arm-io/dp-audio0`](root__arm-io__dp-audio0.md): `dma-parent`

## All properties (18) [DT]

- **`#dma-channels-tx`**: `0x1` (u64; as two u32: `0x1`, `0x0`)
- **`AAPL,phandle`**: `247` (`0xf7`) → phandle of [`/arm-io/admac-dispint0`](root__arm-io__admac-dispint0.md)
- **`ced-ssw-service`**: `AudioDMACLLTEscalationDetectorDISP-I-ISOC`
- **`channel-buffer-alloc-base-rx`**: `0` (`0x0`)
- **`channel-buffer-alloc-base-tx`**: `0` (`0x0`)
- **`channel-buffer-allocation`**: `0x1900` (u64; as two u32: `0x1900`, `0x0`)
- **`channels-offset`**: `0` (`0x0`)
- **`compatible`**: `admac,v5p0`
- **`device_type`**: `admac`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `793` (`0x319`)
- **`iommu-parent`**: `246` (`0xf6`) → phandle of [`/arm-io/dart-disp0-isoc/mapper-disp0-dpa`](root__arm-io__dart-disp0-isoc__mapper-disp0-dpa.md)
- **`irq-destination-index`**: `0` (`0x0`)
- **`irq-destinations`**: 16 bytes
  - u32: `0x41494320 0x41435055 0x47544e20 0x554e5344`
  - text inside: ` CIAUPCA NTGDSNU`
  ```
  000000  20 43 49 41 55 50 43 41 20 4e 54 47 44 53 4e 55   CIAUPCA NTGDSNU
  ```
- **`name`**: `admac-dispint0`
- **`reg`**: 32 bytes
  - u32: `0x86140000 0x1 0x84000 0x0 0x882a8000 0x0 0x8 0x0`
  ```
  000000  00 00 14 86 01 00 00 00 00 40 08 00 00 00 00 00  .........@......
  000010  00 80 2a 88 00 00 00 00 08 00 00 00 00 00 00 00  ..*.............
  ```
- **`role`**: `1145129264` (`0x44414930`) (four-char code `DAI0`)
- **`self-actuated`**: (present, empty)
