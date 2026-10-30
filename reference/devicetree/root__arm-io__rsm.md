# `/arm-io/rsm`

- Name: `rsm`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `167`
- compatible: `rsm,t8101`
- device_type: `rsm`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x89825000` | `0x4000` (16,384 B) | `0x289825000`–`0x289828fff` |
| 1 | `0x898c0000` | `0x4` (4 B) | `0x2898c0000`–`0x2898c0003` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`371`

## All properties (17) [DT]

- **`AAPL,phandle`**: `167` (`0xa7`) → phandle of [`/arm-io/rsm`](root__arm-io__rsm.md)
- **`clock-gates`**: (present, empty)
- **`compatible`**: `rsm,t8101`
- **`configuration-string`**: `muxNcm`
- **`device_type`**: `rsm`
- **`dock-connect-sleep-duration-ms`**: `0` (`0x0`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `371` (`0x173`)
- **`iommu-parent`**: `153` (`0x99`) → phandle of [`/arm-io/dart-sbr/mapper-rsm`](root__arm-io__dart-sbr__mapper-rsm.md)
- **`name`**: `rsm`
- **`ncm-control-ecid-mac`**: `1` (`0x1`)
- **`port-number`**: `1` (`0x1`)
- **`port-type`**: `2` (`0x2`)
- **`reg`**: 32 bytes
  - u32: `0x89825000 0x0 0x4000 0x0 0x898c0000 0x0 0x4 0x0`
  ```
  000000  00 50 82 89 00 00 00 00 00 40 00 00 00 00 00 00  .P.......@......
  000010  00 00 8c 89 00 00 00 00 04 00 00 00 00 00 00 00  ................
  ```
- **`rsm-channel-max-ver`**: `2` (`0x2`)
- **`rsm-channel-min-ver`**: `1` (`0x1`)
- **`vhci-ports`**: `1768911648` (`0x696f7320`) (four-char code `ios `)
