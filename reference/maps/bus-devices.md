# Serial-bus device map

Every device that sits on an I2C, SPI, SPMI or UART controller, with its bus address, interrupt and driver. **[DT]**

## [`/arm-io/spi1`](../devicetree/root__arm-io__spi1.md) — `spi-1,spimc` — AppleSPIMCController

| Device | compatible | Bus address | IRQ (controller) | Driver |
|---|---|---|---|---|
| [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) | `biosensor,mesa` | — | 12, 83886083 (/arm-io/nub-gpio) | AppleMesa, AppleSandDollar |

## [`/arm-io/dockchannel-uart`](../devicetree/root__arm-io__dockchannel-uart.md) — `aapl,dock-channels` — AppleSerialShim

No child devices.

## [`/arm-io/uart0`](../devicetree/root__arm-io__uart0.md) — `uart-1,samsung` — AppleSamsungSerial, AppleSerialShim

| Device | compatible | Bus address | IRQ (controller) | Driver |
|---|---|---|---|---|
| [`/arm-io/uart0/debug-console`](../devicetree/root__arm-io__uart0__debug-console.md) | `` | — |   |  |

## [`/arm-io/i2c2`](../devicetree/root__arm-io__i2c2.md) — `i2c,t8101, i2c,s5l8940x, iic,soft` — AppleARMSoftIICController, AppleS5L8940XI2CController

| Device | compatible | Bus address | IRQ (controller) | Driver |
|---|---|---|---|---|
| [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) | `audio-control,cs42l79` | — | 134, 1 (/arm-io/gpio0) | AppleCS42L79Audio |

## [`/arm-io/i2c3`](../devicetree/root__arm-io__i2c3.md) — `i2c,t8101, i2c,s5l8940x, iic,soft` — AppleARMSoftIICController, AppleS5L8940XI2CController

| Device | compatible | Bus address | IRQ (controller) | Driver |
|---|---|---|---|---|
| [`/arm-io/i2c3/display-eeprom`](../devicetree/root__arm-io__i2c3__display-eeprom.md) | `eeprom,i2c` | — |   | AppleARMI2CEEPROM |
| [`/arm-io/i2c3/display-eeprom-hi`](../devicetree/root__arm-io__i2c3__display-eeprom-hi.md) | `eeprom,i2c` | — |   | AppleARMI2CEEPROM |
| [`/arm-io/i2c3/display-eeprom-2`](../devicetree/root__arm-io__i2c3__display-eeprom-2.md) | `eeprom,i2c` | — |   | AppleARMI2CEEPROM |
| [`/arm-io/i2c3/display-eeprom-2-hi`](../devicetree/root__arm-io__i2c3__display-eeprom-2-hi.md) | `eeprom,i2c` | — |   | AppleARMI2CEEPROM |
| [`/arm-io/i2c3/mogul-display`](../devicetree/root__arm-io__i2c3__mogul-display.md) | `mogul,a1222` | — |   | MogulAuthI2CRelayInterface, MogulAuthSMCRelayInterface |
| [`/arm-io/i2c3/mogul-display2`](../devicetree/root__arm-io__i2c3__mogul-display2.md) | `mogul,a1222` | — |   | MogulAuthI2CRelayInterface, MogulAuthSMCRelayInterface |

## [`/arm-io/i2c4`](../devicetree/root__arm-io__i2c4.md) — `i2c,t8101, i2c,s5l8940x, iic,soft` — AppleARMSoftIICController, AppleS5L8940XI2CController

| Device | compatible | Bus address | IRQ (controller) | Driver |
|---|---|---|---|---|
| [`/arm-io/i2c4/mogul-mlb`](../devicetree/root__arm-io__i2c4__mogul-mlb.md) | `mogul,a1222` | — |   | MogulAuthI2CRelayInterface, MogulAuthSMCRelayInterface |

## [`/arm-io/nub-spmi0`](../devicetree/root__arm-io__nub-spmi0.md) — `aapl,spmi` — AppleSPMIController

| Device | compatible | Bus address | IRQ (controller) | Driver |
|---|---|---|---|---|
| [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) | `pmu,spmi, pmu,becketts` | `0x0`, `0x0`, `0x0` | 2, 62 (/arm-io/nub-spmi0) | AppleDialogSPMIPMU, ApplePMUFirmwareDriver |
| [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) | `btm,phone` | `0x0`, `0x0`, `0x0` | 1651797296, 1651797297, 1651797298, 1651797299 (/arm-io/aon-ptd) | AppleBTM |

## [`/arm-io/nub-spmi1`](../devicetree/root__arm-io__nub-spmi1.md) — `aapl,spmi` — AppleSPMIController

| Device | compatible | Bus address | IRQ (controller) | Driver |
|---|---|---|---|---|
| [`/arm-io/nub-spmi1/shamisen`](../devicetree/root__arm-io__nub-spmi1__shamisen.md) | `` | `0x0`, `0x0`, `0x0` |   |  |
| [`/arm-io/nub-spmi1/stonehenge`](../devicetree/root__arm-io__nub-spmi1__stonehenge.md) | `` | `0x0`, `0x0`, `0x0` |   |  |

## [`/arm-io/nub-spmi2`](../devicetree/root__arm-io__nub-spmi2.md) — `aapl,spmi` — AppleSPMIController

| Device | compatible | Bus address | IRQ (controller) | Driver |
|---|---|---|---|---|
| [`/arm-io/nub-spmi2/spmi-hpm0`](../devicetree/root__arm-io__nub-spmi2__spmi-hpm0.md) | `usbc,cbtl1702,spmi` | `0x0`, `0x0`, `0x0` | 11, 17, 19 (/arm-io/nub-spmi2) | AppleHPMARMSPMI |

## [`/arm-io/aop-spmi0`](../devicetree/root__arm-io__aop-spmi0.md) — `aapl,spmi` — AppleSPMIController

| Device | compatible | Bus address | IRQ (controller) | Driver |
|---|---|---|---|---|
| [`/arm-io/aop-spmi0/wlan-heb`](../devicetree/root__arm-io__aop-spmi0__wlan-heb.md) | `` | `0x0`, `0x0`, `0x0` |   |  |
| [`/arm-io/aop-spmi0/baseband-heb`](../devicetree/root__arm-io__aop-spmi0__baseband-heb.md) | `baseband,heb` | `0x0`, `0x0`, `0x0` | 0, 71, 65, 75 (/arm-io/aop-spmi0) | AppleBasebandSPMIHEB, AppleSARSPMIHEB |
| [`/arm-io/aop-spmi0/stockholm-spmi`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi.md) | `nfc,primary,spmi` | `0x0`, `0x0`, `0x0` | 176, 177, 178, 179 (/arm-io/aop-spmi0) | AppleStockholmSPMI |
| [`/arm-io/aop-spmi0/hammerfest-spmi`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi.md) | `nfc,secondary,spmi` | `0x0`, `0x0`, `0x0` | 160, 161, 162, 163 (/arm-io/aop-spmi0) | AppleStockholmSPMI |
| [`/arm-io/aop-spmi0/uwb0`](../devicetree/root__arm-io__aop-spmi0__uwb0.md) | `` | `0x0`, `0x0`, `0x0` |   |  |

## [`/arm-io/aop-spmi1`](../devicetree/root__arm-io__aop-spmi1.md) — `aapl,spmi` — AppleSPMIController

| Device | compatible | Bus address | IRQ (controller) | Driver |
|---|---|---|---|---|
| [`/arm-io/aop-spmi1/uwb`](../devicetree/root__arm-io__aop-spmi1__uwb.md) | `` | `0x0`, `0x0`, `0x0` |   |  |
| [`/arm-io/aop-spmi1/wlan-idc`](../devicetree/root__arm-io__aop-spmi1__wlan-idc.md) | `wlan,idc` | `0x0`, `0x0`, `0x0` | 28, 26, 29, 32 (/arm-io/aop-spmi1) | AppleSARSPMIIDCWLAN |
| [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) | `baseband,idc` | `0x0`, `0x0`, `0x0` | 0, 71, 65, 75 (/arm-io/aop-spmi1) | AppleBasebandSPMIHEB, AppleSARSPMIIDC |

## [`/arm-io/admac-dispint0`](../devicetree/root__arm-io__admac-dispint0.md) — `admac,v5p0` — AudioDMAController

No child devices.

## [`/arm-io/admac-dispint0-ced-ssw`](../devicetree/root__arm-io__admac-dispint0-ced-ssw.md) — `admacled,v1p0` — AudioDMACLLTEscalationDetector

No child devices.
