# `/arm-io/admac-base-s`

- Name: `admac-base-s`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `399`
- compatible: `admac-evolution,v5p0`
- device_type: `admac`
- Children (3): [`/arm-io/admac-base-s/base-s-adma-tx-2`](root__arm-io__admac-base-s__base-s-adma-tx-2.md), [`/arm-io/admac-base-s/base-s-adma-tx-3`](root__arm-io__admac-base-s__base-s-adma-tx-3.md), [`/arm-io/admac-base-s/base-s-adma-rx-4`](root__arm-io__admac-base-s__base-s-adma-rx-4.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AudioDMAController` | `AppleARMIODevice` | [`com.apple.driver.AudioDMAController-Gen5p0`](../kexts/com.apple.driver.AudioDMAController-Gen5p0.md) | `admac-evolution,v5p0` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x93700000` | `0xb8000` (753,664 B) | `0x293700000`–`0x2937b7fff` |
| 1 | `0x882a8000` | `0x8` (8 B) | `0x2882a8000`–`0x2882a8007` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`527`

## All properties (21) [DT]

- **`#address-cells`**: `2` (`0x2`)
- **`#dma-channels-rx`**: `0xe` (u64; as two u32: `0xe`, `0x0`)
- **`#dma-channels-tx`**: `0x5` (u64; as two u32: `0x5`, `0x0`)
- **`#size-cells`**: `2` (`0x2`)
- **`AAPL,phandle`**: `399` (`0x18f`) → phandle of [`/arm-io/admac-base-s`](root__arm-io__admac-base-s.md)
- **`admac-evolution`**: `1` (`0x1`)
- **`ced-ssw-service`**: `AudioDMACLLTEscalationDetectorADMAC-A`
- **`channel-buffer-alloc-base-rx`**: `0` (`0x0`)
- **`channel-buffer-alloc-base-tx`**: `0` (`0x0`)
- **`channel-buffer-allocation`**: 16 bytes
  - u32: `0x180 0x0 0x4000 0x0`
  ```
  000000  80 01 00 00 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```
- **`channels-offset`**: `0` (`0x0`)
- **`compatible`**: `admac-evolution,v5p0`
- **`device_type`**: `admac`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `527` (`0x20f`)
- **`iommu-parent`**: (present, empty)
- **`irq-destination-index`**: `0` (`0x0`)
- **`irq-destinations`**: 16 bytes
  - u32: `0x41494320 0x41435055 0x47544e20 0x554e5344`
  - text inside: ` CIAUPCA NTGDSNU`
  ```
  000000  20 43 49 41 55 50 43 41 20 4e 54 47 44 53 4e 55   CIAUPCA NTGDSNU
  ```
- **`name`**: `admac-base-s`
- **`reg`**: 32 bytes
  - u32: `0x93700000 0x0 0xb8000 0x0 0x882a8000 0x0 0x8 0x0`
  ```
  000000  00 00 70 93 00 00 00 00 00 80 0b 00 00 00 00 00  ..p.............
  000010  00 80 2a 88 00 00 00 00 08 00 00 00 00 00 00 00  ..*.............
  ```
- **`role`**: `1111577427` (`0x42415353`) (four-char code `BASS`)
