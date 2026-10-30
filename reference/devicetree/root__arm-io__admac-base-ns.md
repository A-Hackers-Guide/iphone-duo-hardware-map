# `/arm-io/admac-base-ns`

- Name: `admac-base-ns`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `385`
- compatible: `admac-evolution,v5p0`
- device_type: `admac`
- Children (7): [`/arm-io/admac-base-ns/base-ns-adma-rx-2`](root__arm-io__admac-base-ns__base-ns-adma-rx-2.md), [`/arm-io/admac-base-ns/base-ns-adma-rx-3`](root__arm-io__admac-base-ns__base-ns-adma-rx-3.md), [`/arm-io/admac-base-ns/base-ns-adma-rx-4`](root__arm-io__admac-base-ns__base-ns-adma-rx-4.md), [`/arm-io/admac-base-ns/base-ns-adma-rx-5`](root__arm-io__admac-base-ns__base-ns-adma-rx-5.md), [`/arm-io/admac-base-ns/base-ns-adma-tx-7`](root__arm-io__admac-base-ns__base-ns-adma-tx-7.md), [`/arm-io/admac-base-ns/base-ns-adma-tx-8`](root__arm-io__admac-base-ns__base-ns-adma-tx-8.md), [`/arm-io/admac-base-ns/base-ns-adma-rx-8`](root__arm-io__admac-base-ns__base-ns-adma-rx-8.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AudioDMAController` | `AppleARMIODevice` | [`com.apple.driver.AudioDMAController-Gen5p0`](../kexts/com.apple.driver.AudioDMAController-Gen5p0.md) | `admac-evolution,v5p0` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x93900000` | `0xb4000` (737,280 B) | `0x293900000`–`0x2939b3fff` |
| 1 | `0x882a8000` | `0x8` (8 B) | `0x2882a8000`–`0x2882a8007` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`528`

## All properties (21) [DT]

- **`#address-cells`**: `2` (`0x2`)
- **`#dma-channels-rx`**: `0xd` (u64; as two u32: `0xd`, `0x0`)
- **`#dma-channels-tx`**: `0xd` (u64; as two u32: `0xd`, `0x0`)
- **`#size-cells`**: `2` (`0x2`)
- **`AAPL,phandle`**: `385` (`0x181`) → phandle of [`/arm-io/admac-base-ns`](root__arm-io__admac-base-ns.md)
- **`admac-evolution`**: `1` (`0x1`)
- **`ced-ssw-service`**: `AudioDMACLLTEscalationDetectorADMAC-A`
- **`channel-buffer-alloc-base-rx`**: `0` (`0x0`)
- **`channel-buffer-alloc-base-tx`**: `0` (`0x0`)
- **`channel-buffer-allocation`**: 16 bytes
  - u32: `0x1e00 0x0 0x1e00 0x0`
  ```
  000000  00 1e 00 00 00 00 00 00 00 1e 00 00 00 00 00 00  ................
  ```
- **`channels-offset`**: `0` (`0x0`)
- **`compatible`**: `admac-evolution,v5p0`
- **`device_type`**: `admac`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `528` (`0x210`)
- **`iommu-parent`**: `149` (`0x95`) → phandle of [`/arm-io/dart-sbr/mapper-admac-base-ns`](root__arm-io__dart-sbr__mapper-admac-base-ns.md)
- **`irq-destination-index`**: `0` (`0x0`)
- **`irq-destinations`**: 16 bytes
  - u32: `0x41494320 0x41435055 0x47544e20 0x554e5344`
  - text inside: ` CIAUPCA NTGDSNU`
  ```
  000000  20 43 49 41 55 50 43 41 20 4e 54 47 44 53 4e 55   CIAUPCA NTGDSNU
  ```
- **`name`**: `admac-base-ns`
- **`reg`**: 32 bytes
  - u32: `0x93900000 0x0 0xb4000 0x0 0x882a8000 0x0 0x8 0x0`
  ```
  000000  00 00 90 93 00 00 00 00 00 40 0b 00 00 00 00 00  .........@......
  000010  00 80 2a 88 00 00 00 00 08 00 00 00 00 00 00 00  ..*.............
  ```
- **`role`**: `1111576147` (`0x42414e53`) (four-char code `BANS`)
