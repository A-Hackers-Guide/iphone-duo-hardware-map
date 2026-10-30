# `/arm-io/admac-leap-ns`

- Name: `admac-leap-ns`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `393`
- compatible: `admac-evolution,v5p0`
- device_type: `admac`
- Children (5): [`/arm-io/admac-leap-ns/leap-ns-adma-tx-1`](root__arm-io__admac-leap-ns__leap-ns-adma-tx-1.md), [`/arm-io/admac-leap-ns/leap-ns-adma-rx-1`](root__arm-io__admac-leap-ns__leap-ns-adma-rx-1.md), [`/arm-io/admac-leap-ns/leap-ns-adma-tx-2`](root__arm-io__admac-leap-ns__leap-ns-adma-tx-2.md), [`/arm-io/admac-leap-ns/leap-ns-adma-tx-3`](root__arm-io__admac-leap-ns__leap-ns-adma-tx-3.md), [`/arm-io/admac-leap-ns/leap-ns-adma-rx-3`](root__arm-io__admac-leap-ns__leap-ns-adma-rx-3.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AudioDMAController` | `AppleARMIODevice` | [`com.apple.driver.AudioDMAController-Gen5p0`](../kexts/com.apple.driver.AudioDMAController-Gen5p0.md) | `admac-evolution,v5p0` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x93300000` | `0xa4000` (671,744 B) | `0x293300000`–`0x2933a3fff` |
| 1 | `0x882a8000` | `0x8` (8 B) | `0x2882a8000`–`0x2882a8007` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`531`

## Firmware with a matching name [FW]

- [`Firmware/V68_LeapHapticsFirmware.im4p`](../firmware/Firmware__V68_LeapHapticsFirmware.im4p.md) (283,085 B) Tag: IM4P  Type: lphp  Version: 1

## All properties (21) [DT]

- **`#address-cells`**: `2` (`0x2`)
- **`#dma-channels-rx`**: `0x9` (u64; as two u32: `0x9`, `0x0`)
- **`#dma-channels-tx`**: `0x9` (u64; as two u32: `0x9`, `0x0`)
- **`#size-cells`**: `2` (`0x2`)
- **`AAPL,phandle`**: `393` (`0x189`) → phandle of [`/arm-io/admac-leap-ns`](root__arm-io__admac-leap-ns.md)
- **`admac-evolution`**: `1` (`0x1`)
- **`ced-ssw-service`**: `AudioDMACLLTEscalationDetectorADMAC-A`
- **`channel-buffer-alloc-base-rx`**: `0` (`0x0`)
- **`channel-buffer-alloc-base-tx`**: `0` (`0x0`)
- **`channel-buffer-allocation`**: 16 bytes
  - u32: `0xe00 0x0 0x1100 0x0`
  ```
  000000  00 0e 00 00 00 00 00 00 00 11 00 00 00 00 00 00  ................
  ```
- **`channels-offset`**: `0` (`0x0`)
- **`compatible`**: `admac-evolution,v5p0`
- **`device_type`**: `admac`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `531` (`0x213`)
- **`iommu-parent`**: `148` (`0x94`) → phandle of [`/arm-io/dart-sbr/mapper-admac-leap-ns`](root__arm-io__dart-sbr__mapper-admac-leap-ns.md)
- **`irq-destination-index`**: `0` (`0x0`)
- **`irq-destinations`**: 16 bytes
  - u32: `0x41494320 0x41435055 0x47544e20 0x554e5344`
  - text inside: ` CIAUPCA NTGDSNU`
  ```
  000000  20 43 49 41 55 50 43 41 20 4e 54 47 44 53 4e 55   CIAUPCA NTGDSNU
  ```
- **`name`**: `admac-leap-ns`
- **`reg`**: 32 bytes
  - u32: `0x93300000 0x0 0xa4000 0x0 0x882a8000 0x0 0x8 0x0`
  ```
  000000  00 00 30 93 00 00 00 00 00 40 0a 00 00 00 00 00  ..0......@......
  000010  00 80 2a 88 00 00 00 00 08 00 00 00 00 00 00 00  ..*.............
  ```
- **`role`**: `1279610451` (`0x4c454e53`) (four-char code `LENS`)
