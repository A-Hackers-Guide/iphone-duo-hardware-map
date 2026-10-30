# `/arm-io/usb-drd0`

- Name: `usb-drd0`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `225`
- compatible: `usb-drd,t8160`
- device_type: `usb-drd`
- Children (3): [`/arm-io/usb-drd0/usb-drd0-port-hs`](root__arm-io__usb-drd0__usb-drd0-port-hs.md), [`/arm-io/usb-drd0/:borneo_h19a_5`](root__arm-io__usb-drd0___borneo_h19a_5.md), [`/arm-io/usb-drd0/:borneo_h19p_5`](root__arm-io__usb-drd0___borneo_h19p_5.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8160USBXDCI` | `AppleARMIODevice` | [`com.apple.driver.AppleUSBXDCIARM`](../kexts/com.apple.driver.AppleUSBXDCIARM.md) | `usb-drd,t8160` |
| `AppleT8160USBXHCI` | `AppleARMIODevice` | [`com.apple.driver.usb.AppleSynopsysUSBXHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSBXHCI.md) | `usb-drd,t8160` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x322430000` | `0x11800` (71,680 B) | `0x322430000`–`0x3224417ff` |
| 1 | `0x322440000` | `0x4000` (16,384 B) | `0x322440000`–`0x322443fff` |
| 2 | `0x32243c000` | `0x5800` (22,528 B) | `0x32243c000`–`0x3224417ff` |
| 3 | `0x322414000` | `0x4000` (16,384 B) | `0x322414000`–`0x322417fff` |
| 4 | `0x322448000` | `0x4000` (16,384 B) | `0x322448000`–`0x32244bfff` |
| 5 | `0x322410000` | `0x4000` (16,384 B) | `0x322410000`–`0x322413fff` |
| 6 | `0x322444000` | `0x4000` (16,384 B) | `0x322444000`–`0x322447fff` |
| 7 | `0x32243d000` | `0x4000` (16,384 B) | `0x32243d000`–`0x322440fff` |
| 8 | `0x322450000` | `0x4000` (16,384 B) | `0x322450000`–`0x322453fff` |
| 9 | `0x82838000` | `0x8` (8 B) | `0x282838000`–`0x282838007` |
| 10 | `0x323080000` | `0x4000` (16,384 B) | `0x323080000`–`0x323083fff` |
| 11 | `0x8002003c` | `0x4` (4 B) | `0x28002003c`–`0x28002003f` |
| 12 | `0x80020040` | `0x4` (4 B) | `0x280020040`–`0x280020043` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1497, 1498, 1499, 1500, 1481`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `vote_force_wakeup_dram` | [`/arm-io/soc-misc`](root__arm-io__soc-misc.md) | `VFWD` | `0x0 0x0` |
| `dock_parent` | [`/port-usb-c-1`](root__port-usb-c-1.md) | `accP` | `` |
| `parrot_srst` | [`/port-usb-c-1`](root__port-usb-c-1.md) | `prst` | `` |

## All properties (26) [DT]

- **`AAPL,phandle`**: `225` (`0xe1`) → phandle of [`/arm-io/usb-drd0`](root__arm-io__usb-drd0.md)
- **`atc-phy-parent`**: `222` (`0xde`) → phandle of [`/arm-io/atc-phy0`](root__arm-io__atc-phy0.md)
- **`bus-number`**: `0` (`0x0`)
- **`clock-gates`**: `53` (`0x35`)
- **`compatible`**: `usb-drd,t8160`
- **`configuration-string`**: `stdMuxPTPEthValIDA`
- **`device-mac-address`**: `macaddr/ethaddr,syscfg/EMac/6,zeroes/6` *(placeholder, filled in by iBoot at boot)*
- **`device_type`**: `usb-drd`
- **`eps-dir-bitmap`**: `612` (`0x264`)
- **`function-dock_parent`**: `0x61636350000001c5` (u64; as two u32: `0x1c5`, `0x61636350`)
- **`function-parrot_srst`**: `0x70727374000001c5` (u64; as two u32: `0x1c5`, `0x70727374`)
- **`function-vote_force_wakeup_dram`**: `H`, `DWFV`
- **`host-mac-address`**: `macaddr/wifiaddr,syscfg/WMac/6,zeroes/6` *(placeholder, filled in by iBoot at boot)*
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 20 bytes
  - u32: `0x5d9 0x5da 0x5db 0x5dc 0x5c9`
  ```
  000000  d9 05 00 00 da 05 00 00 db 05 00 00 dc 05 00 00  ................
  000010  c9 05 00 00                                      ....
  ```
- **`iommu-parent`**: `224` (`0xe0`) → phandle of [`/arm-io/dart-usb0/mapper-usb`](root__arm-io__dart-usb0__mapper-usb.md)
- **`name`**: `usb-drd0`
- **`parrot-port-number`**: `255` (`0xff`)
- **`port-number`**: `1` (`0x1`)
- **`port-type`**: `2` (`0x2`)
- **`reg`**: 208 bytes
  - u32: `0x22430000 0x3 0x11800 0x0 0x22440000 0x3 0x4000 0x0 0x2243c000 0x3 0x5800 0x0 0x22414000 0x3 0x4000 0x0 0x22448000 0x3 0x4000 0x0 0x22410000 0x3 0x4000 0x0 0x22444000 0x3 0x4000 0x0 0x2243d000 0x3 0x4000 0x0 0x22450000 0x3 0x4000 0x0 0x82838000 0x0 0x8 0x0 0x23080000 0x3 0x4000 0x0 0x8002003c 0x0 0x4 0x0 0x80020040 0x0 0x4 0x0`
  ```
  000000  00 00 43 22 03 00 00 00 00 18 01 00 00 00 00 00  ..C"............
  000010  00 00 44 22 03 00 00 00 00 40 00 00 00 00 00 00  ..D".....@......
  000020  00 c0 43 22 03 00 00 00 00 58 00 00 00 00 00 00  ..C".....X......
  000030  00 40 41 22 03 00 00 00 00 40 00 00 00 00 00 00  .@A".....@......
  000040  00 80 44 22 03 00 00 00 00 40 00 00 00 00 00 00  ..D".....@......
  000050  00 00 41 22 03 00 00 00 00 40 00 00 00 00 00 00  ..A".....@......
  000060  00 40 44 22 03 00 00 00 00 40 00 00 00 00 00 00  .@D".....@......
  000070  00 d0 43 22 03 00 00 00 00 40 00 00 00 00 00 00  ..C".....@......
  000080  00 00 45 22 03 00 00 00 00 40 00 00 00 00 00 00  ..E".....@......
  000090  00 80 83 82 00 00 00 00 08 00 00 00 00 00 00 00  ................
  0000a0  00 00 08 23 03 00 00 00 00 40 00 00 00 00 00 00  ...#.....@......
  0000b0  3c 00 02 80 00 00 00 00 04 00 00 00 00 00 00 00  <...............
  0000c0  40 00 02 80 00 00 00 00 04 00 00 00 00 00 00 00  @...............
  ```
- **`service-gates`**: `53` (`0x35`)
- **`soft-disconnect-interval`**: `240` (`0xf0`)
- **`usb-control-request-policy`**: `1` (`0x1`)
- **`usb-repeater`**: `1953395744` (`0x746e7420`) (four-char code `tnt `)
- **`usb-soft-retry-policy`**: `2` (`0x2`)
