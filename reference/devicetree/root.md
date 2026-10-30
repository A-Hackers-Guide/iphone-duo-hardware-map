# `/`

- Name: `device-tree`
- Parent: none (root)
- phandle: `1`
- compatible: `V68AP`, `iPhone19,4`, `AppleARM`
- device_type: `bootrom`
- Children (32): [`/machine-timeouts`](root__machine-timeouts.md), [`/chosen`](root__chosen.md), [`/options`](root__options.md), [`/cpus`](root__cpus.md), [`/aliases`](root__aliases.md), [`/memory`](root__memory.md), [`/pram`](root__pram.md), [`/vram`](root__vram.md), [`/arm-io`](root__arm-io.md), [`/buttons`](root__buttons.md), [`/port-usb-c-1`](root__port-usb-c-1.md), [`/port-magsafe-1`](root__port-magsafe-1.md), [`/backlight`](root__backlight.md), [`/core-brightness`](root__core-brightness.md), [`/exbright`](root__exbright.md), [`/display-health-monitor`](root__display-health-monitor.md), [`/socd-trace-ram`](root__socd-trace-ram.md), [`/baseband`](root__baseband.md), [`/sacm-general`](root__sacm-general.md), [`/sacm-jasper`](root__sacm-jasper.md), [`/defaults`](root__defaults.md), [`/product`](root__product.md), [`/filesystems`](root__filesystems.md), [`/fillmore`](root__fillmore.md), [`/iboot-syscfg`](root__iboot-syscfg.md), [`/centauri`](root__centauri.md), [`/dart-tlbi-aperture`](root__dart-tlbi-aperture.md), [`/ced-ssw`](root__ced-ssw.md), [`/osenvironments`](root__osenvironments.md), [`/exclaves-test`](root__exclaves-test.md), [`/:borneo`](root___borneo.md), [`/:version`](root___version.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleARMPE` | `IOPlatformExpertDevice` | [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md) | `AppleARM` |

## Referenced by (2) [DT]

- [`/arm-io/spi1`](root__arm-io__spi1.md): function-spi_cs0 `null`
- [`/arm-io/aop-spmi0/stockholm-spmi`](root__arm-io__aop-spmi0__stockholm-spmi.md): `spmiFollowerReset`

## Firmware with a matching name [FW]

- [`Firmware/all_flash/DeviceTree.v68ap.im4p`](../firmware/Firmware__all_flash__DeviceTree.v68ap.im4p.md) (74,512 B) Tag: IM4P  Type: dtre  Version: EmbeddedDeviceTrees-12661.52.3

## All properties (23) [DT]

- **`#address-cells`**: `2` (`0x2`)
- **`#size-cells`**: `2` (`0x2`)
- **`AAPL,phandle`**: `1` (`0x1`) → phandle of [`/`](root.md)
- **`clock-frequency`**: `0` (`0x0`)
- **`compatible`**: `V68AP`, `iPhone19,4`, `AppleARM`
- **`config-number`**: `syscfg/CFG#/0x40,zeroes/0x40` *(placeholder, filled in by iBoot at boot)*
- **`country-of-origin`**: `syscfg/Coor` *(placeholder, filled in by iBoot at boot)*
- **`device-tree-tag`**: `EmbeddedDeviceTrees-12661.52.3`
- **`device_type`**: `bootrom`
- **`manufacturer`**: `Apple Inc.`
- **`mlb-serial-number`**: `syscfg/MLB#/0x20,zeroes/0x20` *(placeholder, filled in by iBoot at boot)*
- **`model`**: `iPhone19,4`
- **`model-config`**: `syscfg/MdlC` *(placeholder, filled in by iBoot at boot)*
- **`model-number`**: `syscfg/Mod#/0x20,zeroes/0x20` *(placeholder, filled in by iBoot at boot)*
- **`name`**: `device-tree`
- **`platform-name`**: 32 bytes
  - u32: `0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0`
  ```
  000000  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000010  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  ```
- **`region-info`**: `syscfg/Regn/0x20,zeroes/0x20` *(placeholder, filled in by iBoot at boot)*
- **`regulatory-model-number`**: `syscfg/RMd#/0x20` *(placeholder, filled in by iBoot at boot)*
- **`secure-root-prefix`**: `md`
- **`serial-number`**: `syscfg/SrNm/0x20,zeroes/0x20` *(placeholder, filled in by iBoot at boot)*
- **`target-sub-type`**: `V68AP`
- **`target-type`**: `V68`
- **`time-stamp`**: `Tue Oct 13 23:32:31 PDT 2026`
