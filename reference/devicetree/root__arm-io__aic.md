# `/arm-io/aic`

- Name: `aic`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `45`
- compatible: `aic,3`
- device_type: `interrupt-controller`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleInterruptControllerV3` | `AppleARMIODevice` | [`com.apple.driver.AppleInterruptControllerV3`](../kexts/com.apple.driver.AppleInterruptControllerV3.md) | `aic,3` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x81000000` | `0x1cc000` (1,884,160 B) | `0x281000000`–`0x2811cbfff` |

## Referenced by (115) [DT]

- [`/cpus/cpu0`](root__cpus__cpu0.md): interrupts 50
- [`/cpus/cpu1`](root__cpus__cpu1.md): interrupts 53
- [`/cpus/cpu2`](root__cpus__cpu2.md): interrupts 56
- [`/cpus/cpu3`](root__cpus__cpu3.md): interrupts 59
- [`/cpus/cpu4`](root__cpus__cpu4.md): interrupts 70
- [`/cpus/cpu5`](root__cpus__cpu5.md): interrupts 73
- [`/arm-io/pmgr-child`](root__arm-io__pmgr-child.md): interrupts 314, 299, 44, 46, 64, 66
- [`/arm-io/pmgr/ppm`](root__arm-io__pmgr__ppm.md): interrupts 1064, 0
- [`/arm-io/wdt`](root__arm-io__wdt.md): interrupts 341, 0
- [`/arm-io/gpio0`](root__arm-io__gpio0.md): interrupts 327, 328, 329, 330, 331, 332
- [`/arm-io/error-handler/amcc-error-handler`](root__arm-io__error-handler__amcc-error-handler.md): interrupts 356, 358, 360
- [`/arm-io/error-handler/dcs-error-handler`](root__arm-io__error-handler__dcs-error-handler.md): interrupts 362, 363, 365, 366, 368, 369
- [`/arm-io/error-handler/pmgr-error-handler`](root__arm-io__error-handler__pmgr-error-handler.md): interrupts 1118, 1112
- [`/arm-io/error-handler/cllt-error-handler`](root__arm-io__error-handler__cllt-error-handler.md): interrupts 304
- [`/arm-io/error-handler/sep-error-handler`](root__arm-io__error-handler__sep-error-handler.md): interrupts 428, 427
- [`/arm-io/error-handler/ni0-error-handler`](root__arm-io__error-handler__ni0-error-handler.md): interrupts 80
- [`/arm-io/error-handler/ni1-error-handler`](root__arm-io__error-handler__ni1-error-handler.md): interrupts 81
- [`/arm-io/error-handler/ni2-error-handler`](root__arm-io__error-handler__ni2-error-handler.md): interrupts 82
- [`/arm-io/error-handler/ni3-error-handler`](root__arm-io__error-handler__ni3-error-handler.md): interrupts 83
- [`/arm-io/error-handler/ni4-error-handler`](root__arm-io__error-handler__ni4-error-handler.md): interrupts 84
- [`/arm-io/error-handler/nsi-error-handler`](root__arm-io__error-handler__nsi-error-handler.md): interrupts 85, 86
- [`/arm-io/error-handler/pio-error-handler`](root__arm-io__error-handler__pio-error-handler.md): interrupts 87
- [`/arm-io/error-handler/psd-error-handler`](root__arm-io__error-handler__psd-error-handler.md): interrupts 1128
- [`/arm-io/error-handler/gpce-error-handler`](root__arm-io__error-handler__gpce-error-handler.md): interrupts 1093, 1095
- [`/arm-io/error-handler/ipce-error-handler`](root__arm-io__error-handler__ipce-error-handler.md): interrupts 105, 418, 677, 725, 799, 908
- [`/arm-io/fpwm`](root__arm-io__fpwm.md): interrupts 1353
- [`/arm-io/event-log-handler`](root__arm-io__event-log-handler.md): interrupts 26, 27, 39, 300, 325, 338
- [`/arm-io/spi1`](root__arm-io__spi1.md): interrupts 1337
- [`/arm-io/aes`](root__arm-io__aes.md): interrupts 1343
- [`/arm-io/aop`](root__arm-io__aop.md): interrupts 194, 154, 114
- [`/arm-io/aop-exclave-mailbox`](root__arm-io__aop-exclave-mailbox.md): interrupts 173, 213, 133
- [`/arm-io/aop2`](root__arm-io__aop2.md): interrupts 195, 155, 115
- [`/arm-io/aop2-exclave-mailbox`](root__arm-io__aop2-exclave-mailbox.md): interrupts 174, 214, 134
- [`/arm-io/aop-gpio`](root__arm-io__aop-gpio.md): interrupts 456, 457, 458, 459, 460, 461
- [`/arm-io/nub-gpio`](root__arm-io__nub-gpio.md): interrupts 553, 554, 555, 556, 557, 558
- [`/arm-io/smc-gpio`](root__arm-io__smc-gpio.md): interrupts 606, 607, 608, 609, 610, 611
- [`/arm-io/mtp-gpio`](root__arm-io__mtp-gpio.md): interrupts 1392, 1393, 1394, 1395, 1396, 1397
- [`/arm-io/pmp`](root__arm-io__pmp.md): interrupts 198, 158, 118
- [`/arm-io/sep`](root__arm-io__sep.md): interrupts 424, 423
- [`/arm-io/dart-sep`](root__arm-io__dart-sep.md): interrupts 429
- [`/arm-io/esm`](root__arm-io__esm.md): interrupts 425, 426
- [`/arm-io/sio`](root__arm-io__sio.md): interrupts 202, 162, 122
- [`/arm-io/dart-sio`](root__arm-io__dart-sio.md): interrupts 1356
- [`/arm-io/dart-sbr`](root__arm-io__dart-sbr.md): interrupts 102
- [`/arm-io/ans`](root__arm-io__ans.md): interrupts 201, 161, 121, 1280
- [`/arm-io/smc`](root__arm-io__smc.md): interrupts 196, 156, 116
- [`/arm-io/aon-ptd`](root__arm-io__aon-ptd.md): interrupts 617, 618, 619, 620, 621, 622
- [`/arm-io/rsm`](root__arm-io__rsm.md): interrupts 371
- [`/arm-io/dockchannel-uart`](root__arm-io__dockchannel-uart.md): interrupts 550
- [`/arm-io/mtp`](root__arm-io__mtp.md): interrupts 197, 157, 117
- [`/arm-io/uart0`](root__arm-io__uart0.md): interrupts 1328
- [`/arm-io/i2c2`](root__arm-io__i2c2.md): interrupts 1346
- [`/arm-io/i2c3`](root__arm-io__i2c3.md): interrupts 1347
- [`/arm-io/i2c4`](root__arm-io__i2c4.md): interrupts 1348
- [`/arm-io/atc-phy0`](root__arm-io__atc-phy0.md): interrupts 1486
- [`/arm-io/dart-usb0`](root__arm-io__dart-usb0.md): interrupts 1492
- [`/arm-io/usb-drd0`](root__arm-io__usb-drd0.md): interrupts 1497, 1498, 1499, 1500, 1481
- [`/arm-io/dcp`](root__arm-io__dcp.md): interrupts 203, 163, 123
- [`/arm-io/dcp0-expert`](root__arm-io__dcp0-expert.md): interrupts 766
- [`/arm-io/dart-dcp`](root__arm-io__dart-dcp.md): interrupts 771
- [`/arm-io/dart-disp0`](root__arm-io__dart-disp0.md): interrupts 771
- [`/arm-io/dart-dispgrt`](root__arm-io__dart-dispgrt.md): interrupts 771
- [`/arm-io/dart-disp0-isoc`](root__arm-io__dart-disp0-isoc.md): interrupts 794
- [`/arm-io/admac-dispint0`](root__arm-io__admac-dispint0.md): interrupts 793
- [`/arm-io/admac-dispint0-ced-ssw`](root__arm-io__admac-dispint0-ced-ssw.md): interrupts 795
- [`/arm-io/dcp-exclave-mailbox`](root__arm-io__dcp-exclave-mailbox.md): interrupts 175, 215, 135
- [`/arm-io/exdisplaypipe`](root__arm-io__exdisplaypipe.md): interrupts 803, 804, 762, 805
- [`/arm-io/dcpsec`](root__arm-io__dcpsec.md): interrupts 205, 165, 125
- [`/arm-io/dcpsec-expert`](root__arm-io__dcpsec-expert.md): interrupts 875
- [`/arm-io/dart-dcpsec`](root__arm-io__dart-dcpsec.md): interrupts 880
- [`/arm-io/dart-dispsec`](root__arm-io__dart-dispsec.md): interrupts 880
- [`/arm-io/dart-dispsecgrt`](root__arm-io__dart-dispsecgrt.md): interrupts 880
- [`/arm-io/dcpsec-exclave-mailbox`](root__arm-io__dcpsec-exclave-mailbox.md): interrupts 184, 224, 144
- [`/arm-io/exdisplaypipe1`](root__arm-io__exdisplaypipe1.md): interrupts 912, 913, 871, 914
- [`/arm-io/dcpext0-expert`](root__arm-io__dcpext0-expert.md): interrupts 984
- [`/arm-io/dcpext0`](root__arm-io__dcpext0.md): interrupts 204, 164, 124
- [`/arm-io/dart-dcpext0`](root__arm-io__dart-dcpext0.md): interrupts 989
- [`/arm-io/dart-dispext0`](root__arm-io__dart-dispext0.md): interrupts 989
- [`/arm-io/dart-dispext0-isoc`](root__arm-io__dart-dispext0-isoc.md): interrupts 1012
- [`/arm-io/admac-dispext0`](root__arm-io__admac-dispext0.md): interrupts 1011
- [`/arm-io/admac-dispext0-ced-ssw`](root__arm-io__admac-dispext0-ced-ssw.md): interrupts 1013
- [`/arm-io/scaler0`](root__arm-io__scaler0.md): interrupts 1290, 1292, 1293, 1294, 1298, 1299
- [`/arm-io/dart-scaler`](root__arm-io__dart-scaler.md): interrupts 1291
- [`/arm-io/jpeg`](root__arm-io__jpeg.md): interrupts 1282
- [`/arm-io/dart-jpeg`](root__arm-io__dart-jpeg.md): interrupts 1283
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): interrupts 212, 172, 132, 410, 411, 412
- [`/arm-io/isp`](root__arm-io__isp.md): interrupts 410, 411, 412, 413, 183
- [`/arm-io/dart-isp`](root__arm-io__dart-isp.md): interrupts 416
- [`/arm-io/ave`](root__arm-io__ave.md): interrupts 1210, 1199, 1198
- [`/arm-io/dart-ave`](root__arm-io__dart-ave.md): interrupts 1209
- [`/arm-io/avd`](root__arm-io__avd.md): interrupts 207, 167
- [`/arm-io/dart-avd`](root__arm-io__dart-avd.md): interrupts 1183
- [`/arm-io/ane0`](root__arm-io__ane0.md): interrupts 210, 170, 678, 691
- [`/arm-io/dart-ane0`](root__arm-io__dart-ane0.md): interrupts 679
- [`/arm-io/ane1`](root__arm-io__ane1.md): interrupts 211, 171, 726, 739
- [`/arm-io/dart-ane1`](root__arm-io__dart-ane1.md): interrupts 727
- [`/arm-io/sgx`](root__arm-io__sgx.md): interrupts 1226, 1227, 1228, 1229, 1260, 1262
- [`/arm-io/gfx-asc`](root__arm-io__gfx-asc.md): interrupts 199, 159
- [`/arm-io/gfx1-asc`](root__arm-io__gfx1-asc.md): interrupts 200, 160
- [`/arm-io/admac-aop-ced-ssw`](root__arm-io__admac-aop-ced-ssw.md): interrupts 548
- [`/arm-io/admac-base-ns`](root__arm-io__admac-base-ns.md): interrupts 528
- [`/arm-io/admac-leap-ns`](root__arm-io__admac-leap-ns.md): interrupts 531
- [`/arm-io/admac-base-s`](root__arm-io__admac-base-s.md): interrupts 527
- [`/arm-io/admac-leap-s`](root__arm-io__admac-leap-s.md): interrupts 530
- [`/arm-io/apcie`](root__arm-io__apcie.md): interrupts 1457, 1469, 1452
- [`/arm-io/apcie`](root__arm-io__apcie.md): `msi-parent-controller`
- [`/arm-io/dart-apcie0`](root__arm-io__dart-apcie0.md): interrupts 1458
- [`/arm-io/apcie0-piodma`](root__arm-io__apcie0-piodma.md): interrupts 1459
- [`/arm-io/apcie0-plce`](root__arm-io__apcie0-plce.md): interrupts 1466, 1467
- [`/arm-io/dart-apcie1`](root__arm-io__dart-apcie1.md): interrupts 1470
- [`/arm-io/apcie1-piodma`](root__arm-io__apcie1-piodma.md): interrupts 1471
- [`/arm-io/apcie1-plce`](root__arm-io__apcie1-plce.md): interrupts 1478, 1479
- [`/arm-io/dbgCPU`](root__arm-io__dbgCPU.md): interrupts 374
- [`/arm-io/msg`](root__arm-io__msg.md): interrupts 92, 93, 94, 95, 96, 97
- [`/arm-io/secure-repair`](root__arm-io__secure-repair.md): interrupts 456, 457, 458, 459, 460, 461

## All properties (27) [DT]

- **`#address-cells`**: `0` (`0x0`)
- **`#interrupt-cells`**: `1` (`0x1`)
- **`#main-cpus`**: `6` (`0x6`)
- **`#shared-timestamps`**: `16` (`0x10`)
- **`AAPL,phandle`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`aicglbcfg-offset`**: `20` (`0x14`)
- **`cap0-offset`**: `4` (`0x4`)
- **`cap0_max_interrupt_umask`**: `65535` (`0xffff`)
- **`compatible`**: `aic,3`
- **`device_type`**: `interrupt-controller`
- **`extint-baseaddress`**: `65536` (`0x10000`)
- **`extintrcfg-stride`**: `18944` (`0x4a00`)
- **`hwintmon-stride`**: `18944` (`0x4a00`)
- **`interrupt-controller`**: `master`
- **`intmaskclear-stride`**: `18944` (`0x4a00`)
- **`intmaskset-stride`**: `18944` (`0x4a00`)
- **`max_irq_interrupt_umask`**: `65535` (`0xffff`)
- **`maxnumirq-offset`**: `12` (`0xc`)
- **`name`**: `aic`
- **`pubstampcfg0-offset`**: `4096` (`0x1000`)
- **`pubstampcfg0inttype-mask`**: `3` (`0x3`)
- **`pubstampdcfg0en-mask`**: `2147483648` (`0x80000000`)
- **`pubstampdhi-offset`**: `4108` (`0x100c`)
- **`pubstamplo0-offset`**: `4104` (`0x1008`)
- **`pubstampstride-mask`**: `16` (`0x10`)
- **`reg`**: 16 bytes
  - u32: `0x81000000 0x0 0x1cc000 0x0`
  ```
  000000  00 00 00 81 00 00 00 00 00 c0 1c 00 00 00 00 00  ................
  ```
- **`rev-offset`**: `0` (`0x0`)
