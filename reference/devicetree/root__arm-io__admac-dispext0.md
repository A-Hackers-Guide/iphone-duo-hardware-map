# `/arm-io/admac-dispext0`

- Name: `admac-dispext0`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `287`
- compatible: `admac,v5p0`
- device_type: `admac`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AudioDMAController` | `AppleARMIODevice` | [`com.apple.driver.AudioDMAController-Gen5p0`](../kexts/com.apple.driver.AudioDMAController-Gen5p0.md) | `admac,v5p0` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x18e140000` | `0x84000` (540,672 B) | `0x38e140000`–`0x38e1c3fff` |
| 1 | `0x882a8000` | `0x8` (8 B) | `0x2882a8000`–`0x2882a8007` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1011`

## Referenced by (1) [DT]

- [`/arm-io/dp-audio1`](root__arm-io__dp-audio1.md): `dma-parent`

## All properties (18) [DT]

- **`#dma-channels-tx`**: `0x1` (u64; as two u32: `0x1`, `0x0`)
- **`AAPL,phandle`**: `287` (`0x11f`) → phandle of [`/arm-io/admac-dispext0`](root__arm-io__admac-dispext0.md)
- **`ced-ssw-service`**: `AudioDMACLLTEscalationDetectorDISP-E0-ISOC`
- **`channel-buffer-alloc-base-rx`**: `0` (`0x0`)
- **`channel-buffer-alloc-base-tx`**: `0` (`0x0`)
- **`channel-buffer-allocation`**: `0x1900` (u64; as two u32: `0x1900`, `0x0`)
- **`channels-offset`**: `0` (`0x0`)
- **`compatible`**: `admac,v5p0`
- **`device_type`**: `admac`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `1011` (`0x3f3`)
- **`iommu-parent`**: `286` (`0x11e`) → phandle of [`/arm-io/dart-dispext0-isoc/mapper-dispext0-dpa`](root__arm-io__dart-dispext0-isoc__mapper-dispext0-dpa.md)
- **`irq-destination-index`**: `0` (`0x0`)
- **`irq-destinations`**: 16 bytes
  - u32: `0x41494320 0x41435055 0x47544e20 0x554e5344`
  - text inside: ` CIAUPCA NTGDSNU`
  ```
  000000  20 43 49 41 55 50 43 41 20 4e 54 47 44 53 4e 55   CIAUPCA NTGDSNU
  ```
- **`name`**: `admac-dispext0`
- **`reg`**: 32 bytes
  - u32: `0x8e140000 0x1 0x84000 0x0 0x882a8000 0x0 0x8 0x0`
  ```
  000000  00 00 14 8e 01 00 00 00 00 40 08 00 00 00 00 00  .........@......
  000010  00 80 2a 88 00 00 00 00 08 00 00 00 00 00 00 00  ..*.............
  ```
- **`role`**: `1145133104` (`0x44415830`) (four-char code `DAX0`)
- **`self-actuated`**: (present, empty)
