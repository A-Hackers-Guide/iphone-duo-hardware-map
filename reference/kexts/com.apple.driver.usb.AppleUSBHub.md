# `com.apple.driver.usb.AppleUSBHub`

- Name: I/O Kit Driver for USB Hubs
- Version: `1.2`
- UUID: `5AB0DC79-F478-3B74-8700-A797B9E59BD5`
- Source version: `1617.40.10.0.0`
- Depends on: [`com.apple.driver.usb.AppleUSBCommon`](com.apple.driver.usb.AppleUSBCommon.md) 1.0, [`com.apple.iokit.IOUSBHostFamily`](com.apple.iokit.IOUSBHostFamily.md) 1.2, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 23.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 23.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 23.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 23.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (38) [KC]

### Apple Aluminium Keyboard Properties
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBConfigurationCurrentOverride`: `500`
  - `kUSBHubPortSequenceDelay`: `350`
  - `kUSBSleepPortCurrentLimit`: `500`
  - `kUSBWakePortCurrentLimit`: `500`
- `idProductArray`:
  - `4101`
  - `4102`
- `idVendor`: `1452`

### Apple DVI to display port hub
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBSleepPortCurrentLimit`: `500`
  - `kUSBWakePortCurrentLimit`: `500`
- `idProduct`: `4104`
- `idVendor`: `1452`

### Apple Display Properties
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBHubPowerSupply`: `7500`
  - `kUSBSleepPortCurrentLimit`: `1500`
  - `kUSBWakePortCurrentLimit`: `1500`
- `idProductArray`:
  - `37176`
  - `37177`
  - `4125`
  - `4126`
  - `32785`
  - `32786`
  - `32787`
  - `32788`
- `idVendor`: `1452`

### Apple USB-C Digital AV Multiport Adapter Properties V1
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBHubIdlePolicy`: `500`
  - `kUSBHubPowerSupply`: `1676`
  - `kUSBSleepPortCurrentLimit`: `1100`
  - `kUSBWakePortCurrentLimit`: `1100`
- `idProductArray`:
  - `4110`
  - `4111`
- `idVendor`: `1452`

### Apple USB-C Digital AV Multiport Adapter Properties V2 4.3.2
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBHubIdlePolicy`: `500`
  - `kUSBHubPowerSupplyType`: `2`
  - `kUSBSleepPortCurrentLimit`: `1100`
  - `kUSBWakePortCurrentLimit`: `1100`
- `bcdDeviceRange`:
  - `0`
  - `17154`
- `idProductArray`:
  - `4119`
  - `4120`
- `idVendor`: `1452`

### Apple USB-C Digital AV Multiport Adapter Properties V2 4.3.3
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBHubIdlePolicy`: `500`
  - `kUSBHubPowerSupply`: `1676`
  - `kUSBSleepPortCurrentLimit`: `1100`
  - `kUSBWakePortCurrentLimit`: `1100`
- `bcdDeviceRange`:
  - `17155`
  - `65535`
- `idProductArray`:
  - `4119`
  - `4120`
- `idVendor`: `1452`

### Apple USB-C VGA Multiport Adapter Properties
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBHubIdlePolicy`: `500`
  - `kUSBHubPowerSupply`: `1676`
  - `kUSBSleepPortCurrentLimit`: `1100`
  - `kUSBWakePortCurrentLimit`: `1100`
- `idProductArray`:
  - `4112`
  - `4113`
- `idVendor`: `1452`

### AppleHub5678v1
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBHubPowerSupply`: `1000`
  - `kUSBHubPowerSupplyType`: `1`
  - `kUSBSleepPortCurrentLimit`: `1000`
  - `kUSBWakePortCurrentLimit`: `1000`
- `idProduct`: `5678`
- `idVendor`: `1452`

### AppleUSB20CameraKitHub
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHub`
- `IOClass`: `AppleUSB20CameraKitHub`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `idProduct`: `4109`
- `idVendor`: `1452`

### AppleUSB20Hub0
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHub`
- `IOClass`: `AppleUSB20Hub`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `bDeviceClass`: `9`
- `bDeviceSubClass`: `0`

### AppleUSB20Hub1
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHub`
- `IOClass`: `AppleUSB20Hub`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `bDeviceClass`: `9`
- `bDeviceSubClass`: `1`

### AppleUSB30Hub0
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHub`
- `IOClass`: `AppleUSB30Hub`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `USBSpeed`: `4`
- `bDeviceClass`: `9`
- `bDeviceSubClass`: `0`

### AppleUSB30Hub1
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHub`
- `IOClass`: `AppleUSB30Hub`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `USBSpeed`: `4`
- `bDeviceClass`: `9`
- `bDeviceSubClass`: `1`

### AppleUSB31Hub0
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHub`
- `IOClass`: `AppleUSB30Hub`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `USBSpeed`: `5`
- `bDeviceClass`: `9`
- `bDeviceSubClass`: `0`

### AppleUSB31Hub1
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHub`
- `IOClass`: `AppleUSB30Hub`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `USBSpeed`: `5`
- `bDeviceClass`: `9`
- `bDeviceSubClass`: `1`

### AppleUSB32Hub0
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHub`
- `IOClass`: `AppleUSB30Hub`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `USBSpeed`: `6`
- `bDeviceClass`: `9`
- `bDeviceSubClass`: `0`

### AppleUSB32Hub1
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHub`
- `IOClass`: `AppleUSB30Hub`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `USBSpeed`: `6`
- `bDeviceClass`: `9`
- `bDeviceSubClass`: `1`

### AppleUSBCameraKitHub
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBHubPowerSupply`: `900`
  - `kUSBWakePortCurrentLimit`: `900`
- `idProductArray`:
  - `4108`
  - `4109`
- `idVendor`: `1452`

### AppleUSBHub37143
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `AAPL,current-available`: `1500`
  - `kUSBHubIdlePolicy`: `0`
  - `kUSBHubStartupDelay`: `200`
- `idProduct`: `37143`
- `idVendor`: `1452`

### AppleUSBHub37144
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBHubIdlePolicy`: `0`
- `idProduct`: `37144`
- `idVendor`: `1452`

### AppleUSBHub37149v1
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `OverrideConfig0MaxPower`: `50`
- `bcdDevice`: `1`
- `idProduct`: `37149`
- `idVendor`: `1452`

### AppleUSBHub37151v1
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBConfigurationCurrentOverride`: `50`
  - `kUSBHubPowerSupplyType`: `1`
- `bcdDevice`: `1`
- `idProductArray`:
  - `37151`
  - `37152`
- `idVendor`: `1452`

### AppleUSBHub37152v307
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `OverrideConfig0MaxPower`: `50`
- `bcdDevice`: `307`
- `idProduct`: `37152`
- `idVendor`: `1452`

### AppleUSBHub37158
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBHubPowerSupply`: `4500`
  - `kUSBHubStartupDelay`: `500`
  - `kUSBSleepPortCurrentLimit`: `1500`
  - `kUSBWakePortCurrentLimit`: `1500`
- `idProduct`: `37158`
- `idVendor`: `1452`

### AppleUSBHub37159
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBHubStartupDelay`: `500`
- `idProduct`: `37159`
- `idVendor`: `1452`

### AppleUSBHub37174
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBHubPowerSupply`: `3300`
  - `kUSBSleepPortCurrentLimit`: `1500`
  - `kUSBWakePortCurrentLimit`: `1500`
- `idProduct`: `37174`
- `idVendor`: `1452`

### Bretford Cart 4-port
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBHubPowerSupply`: `10000`
  - `kUSBSleepPortCurrentLimit`: `2500`
  - `kUSBWakePortCurrentLimit`: `2500`
- `bcdDevice`: `1`
- `idProduct`: `20`
- `idVendor`: `10351`

### Bretford Cart 7-port
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBHubPowerSupply`: `17500`
  - `kUSBSleepPortCurrentLimit`: `2500`
  - `kUSBWakePortCurrentLimit`: `2500`
- `idProduct`: `23`
- `idVendor`: `10351`

### GenesysUSB30Hub-GL3520
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBHubPowerSupplyType`: `1`
- `USBSpeed`: `4`
- `bDeviceClass`: `9`
- `bDeviceSubClass`: `0`
- `idProduct`: `1554`
- `idVendor`: `1507`

### GenesysUSB30Hubs
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBHubIdlePolicy`: `0`
- `USBSpeed`: `4`
- `bDeviceClass`: `9`
- `bDeviceSubClass`: `0`
- `idProduct`: `*`
- `idVendor`: `1507`

### Kinesis Keyboard Hub
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBHubPortSequenceDelay`: `250`
- `idProduct`: `129`
- `idVendor`: `1523`

### LG USBC External Hub
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBHubPowerSupply`: `6000`
  - `kUSBSleepPortCurrentLimit`: `1500`
  - `kUSBWakePortCurrentLimit`: `1500`
- `idProductArray`:
  - `39492`
  - `39494`
  - `39520`
  - `39521`
- `idVendor`: `1086`

### Lenovo VL820
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `UsbStreamsSupported`: `False`
- `idProductArray`:
  - `41873`
- `idVendor`: `6127`

### Personality1
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderParentUSBNubMergeProperties`:
  - `AAPL,current-available`: `3000`
- `idProduct`: `37395`
- `idVendor`: `1452`

### ThunderboltDisplay2011-InternalHub
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `port-count`: `<data 22 chars>`
  - `ports`:
    - `PRT1`:
      - `usb-port-number`: `<data 26 chars>`
      - `usb-port-type`: `<data 26 chars>`
    - `PRT2`:
      - `usb-port-number`: `<data 26 chars>`
      - `usb-port-type`: `<data 26 chars>`
    - `PRT3`:
      - `usb-port-number`: `<data 26 chars>`
      - `usb-port-type`: `<data 26 chars>`
    - `PRT4`:
      - `usb-port-number`: `<data 26 chars>`
      - `usb-port-type`: `<data 26 chars>`
    - `PRT5`:
      - `usb-port-number`: `<data 26 chars>`
      - `usb-port-type`: `<data 26 chars>`
    - `PRT7`:
      - `usb-port-number`: `<data 26 chars>`
      - `usb-port-type`: `<data 26 chars>`
- `idProduct`: `37159`
- `idVendor`: `1452`

### USBHub8193-61699
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBHubIdlePolicy`: `0`
- `idProduct`: `61699`
- `idVendor`: `8193`

### VIA Labs VL820
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `UsbStreamsSupported`: `False`
- `idProductArray`:
  - `2080`
  - `10272`
  - `34848`
- `idVendor`: `8457`

### ViaVL210Hubs
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBHostMergeProperties`
- `IOClass`: `AppleUSBHostMergeProperties`
- `IOPersonalityPublisher`: `com.apple.driver.usb.AppleUSBHub`
- `IOProviderClass`: `IOUSBHostDevice`
- `IOProviderMergeProperties`:
  - `kUSBHubIdlePolicy`: `0`
- `bDeviceClass`: `9`
- `bDeviceSubClass`: `0`
- `idProductArray`:
  - `528`
  - `8720`
- `idVendor`: `8457`


## C++ classes (7) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSB20CameraKitHub` | 0x2e0 | AppleUSB20Hub → AppleUSBHub → IOService → IORegistryEntry |
| `AppleUSB20Hub` | 0x258 | AppleUSBHub → IOService → IORegistryEntry |
| `AppleUSB20HubPort` | 0x410 | AppleUSBHubPort → AppleUSBHostPort → IOService → IORegistryEntry |
| `AppleUSB30Hub` | 0x258 | AppleUSBHub → IOService → IORegistryEntry |
| `AppleUSB30HubPort` | 0x420 | AppleUSBHubPort → AppleUSBHostPort → IOService → IORegistryEntry |
| `AppleUSBHub` | 0x250 | IOService → IORegistryEntry |
| `AppleUSBHubPort` | 0x408 | AppleUSBHostPort → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00004498 off=0x00b530c0-0x00b57558 addr=0xfffffe0007b570c0-0xfffffe0007b5b558 r--/r--   __TEXT            
	sz=0x00001e4b off=0x00b53738-0x00b55583 addr=0xfffffe0007b57738-0xfffffe0007b59583               __TEXT.__cstring          (CstringLiterals)
	sz=0x00001f61 off=0x00b55583-0x00b574e4 addr=0xfffffe0007b59583-0xfffffe0007b5b4e4               __TEXT.__os_log           
	sz=0x00000068 off=0x00b574f0-0x00b57558 addr=0xfffffe0007b5b4f0-0xfffffe0007b5b558               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00019f6c off=0x037f2cd0-0x0380cc3c addr=0xfffffe000a7f6cd0-0xfffffe000a810c3c r-x/r-x   __TEXT_EXEC       
	sz=0x00019b7c off=0x037f2cd0-0x0380c84c addr=0xfffffe000a7f6cd0-0xfffffe000a81084c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000003f0 off=0x0380c84c-0x0380cc3c addr=0xfffffe000a81084c-0xfffffe000a810c3c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001f0 off=0x04a1c240-0x04a1c430 addr=0xfffffe000ba20240-0xfffffe000ba20430 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a1c240-0x04a1c308 addr=0xfffffe000ba20240-0xfffffe000ba20308               __DATA.__data             
	sz=0x00000128 off=0x00000000-0x00000128 addr=0xfffffe000ba20308-0xfffffe000ba20430               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00003960 off=0x01464d60-0x014686c0 addr=0xfffffe0008468d60-0xfffffe000846c6c0 rw-/rw-   __DATA_CONST      
	sz=0x00000038 off=0x01464d60-0x01464d98 addr=0xfffffe0008468d60-0xfffffe0008468d98         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000038 off=0x01464d98-0x01464dd0 addr=0xfffffe0008468d98-0xfffffe0008468dd0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00003480 off=0x01464dd0-0x01468250 addr=0xfffffe0008468dd0-0xfffffe000846c250         __DATA_CONST.__const            
	sz=0x000001c0 off=0x01468250-0x01468410 addr=0xfffffe000846c250-0xfffffe000846c410         __DATA_CONST.__kalloc_type      
	sz=0x000001f8 off=0x01468410-0x01468608 addr=0xfffffe000846c410-0xfffffe000846c608         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000b8 off=0x01468608-0x014686c0 addr=0xfffffe000846c608-0xfffffe000846c6c0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 149 at 0x04afb040
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     5AB0DC79-F478-3B74-8700-A797B9E59BD5
008: LC_SOURCE_VERSION           1617.40.10.0.0
009: LC_FUNCTION_STARTS          offset=0x004aca0a0 size=0x160
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleUSBHub`
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBHub`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `I/O Kit Driver for USB Hubs`
- `CFBundleNumericVersion`: `18907136`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.2`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.2`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2000-2025 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.2`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOUSBHostFamily.kext/PlugIns/AppleUSBHub.kext`
- `_PrelinkExecutableLoadAddr`: `-2198893924160`
- `_PrelinkExecutableRelativePath`: `AppleUSBHub`
- `_PrelinkExecutableSize`: `139092`
- `_PrelinkExecutableSourceAddr`: `-2198893924160`
- `_PrelinkKmodInfo`: `-2198828088768`

## Strings (323) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `updateLPMPolicyGated`
- `%s@%s: %s::%s: change bits still set, port status 0x%08x\n`
- `registerHub`
- `%s@%s: %s::%s: failed to create clients set\n`
- `%s@%s: %s::%s: unable to find parent port\n`
- `kUSBConfigurationCurrentOverride`
- `%s@%s: %s::%s: failed to locate an interrupt pipe\n`
- `UsbBusCurrentPoolID`
- `%s@%s: %s::%s: port %u feature %d completed with 0x%08x\n`
- `%s@%s: %s::%s: overcurrent active\n`
- `clearPipeStallGated`
- `%s@%s: %s::%s: hubs with bcdVersion of 0x%04x are not supported\n`
- `getHubStatus`
- `%s@%s: %s::%s: failed to queue new IO\n`
- `%s@%s: %s::%s: Setting Timeout linkState %d timeoutUs %d result 0x%08x\n`
- `site.AppleUSBHubPort`
- `%s@%s: %s::%s: failed to create _busCurrentAllocator\n`
- `%s@%s: %s::%s: connect change\n`
- `%s@%s: %s::%s: unable to raise port power state from %d\n`
- `%s@%s: %s::%s: hubs with %d ports are not supported\n`
- `%s@%s: %s::%s: port needs to be resumed\n`
- `%s@%s: %s::%s: overcurrent cleared\n`
- `%s@%s: %s::%s: failed to allocate port %u\n`
- `%s@%s: %s::%s: failed to attach or start port %u\n`
- `clearPortFeatureGated`
- `hardwareException`
- `%s@%s: %s::%s: link configuration error\n`
- `%s@%s: %s::%s: txBitrate %llu.  laneSpeed %llu, laneMantissa %u laneCount %u\n`
- ` @%s:%d`
- `%s@%s: %s::%s: reset did not enable port\n`
- `start`
- `%s@%s: %s::%s: kUSBHubPortSequenceDelay %u ms\n`
- `%s@%s: %s::%s: port %u is requesting %d wakeUnits and %d sleepUnits mA\n`
- `clearHubFeature`
- `%s@%s: %s::%s: link state %u\n`
- `usb-port-current-policy`
- `1211111212221212112222222122222222222222222222222222222222222222222222222222212211111222211121122222222222111221121111111111111121`
- `%s@%s: %s::%s: unable to raise power state, deferring interrupt\n`
- `%s@%s: %s::%s: clearing suspend change\n`
- `%s@%s: %s::%s: reset change\n`
- `%s@%s: %s::%s: asserting reset\n`
- `%s@%s: %s::%s: failed to open device\n`
- `%s@%s: %s::%s: service is inactive\n`
- `%s@%s: %s::%s: invalid statusCode %u\n`
- `%08x`
- `%s@%s: %s::%s: failed to open interface\n`
- `%s@%s: %s::%s: port %u sleep units %d -> %d mA\n`
- `121111121222121211222222212222222222222222222222222222222222222222222222222221221111122221112112222222222211122112111111111111112`
- `UsbHostControllerStreamPolicy`
- `suspend`
- `%s@%s: %s::%s: hub power status change\n`
- `getHubPowerSupply`
- `getPortStatus`
- `%s@%s: %s::%s: setting hub depth %d\n`
- `AppleUSB20CameraKitHub`
- `%s@%s: %s::%s: reset did not complete\n`
- `%s@%s: %s::%s: provider is invalid\n`
- `kUSBWakePortCurrentLimit`
- `open`
- `ports`
- `%s@%s: %s::%s: client %p wakeUnits %d sleepUnits %d completed with 0x%08x\n`
- `%s@%s: %s::%s: notifying all ports of local power change\n`
- `12111112122212121121111111111121222211111111111111111122222222222222222222122222222222222222`
- `%s@%s: %s::%s: overcurrent change with portStatus = %x\n`
- `121111121222121211211111111111212222111111111111111111222222222222222222221`
- `%s@%s: %s::%s: failed to allocate _commandGate\n`
- `%s@%s: %s::%s: unable to open provider or inactive\n`
- `firstMatchNotificationThreadCall_block_invoke`
- `%s@%s: %s::%s: local power change\n`
- `%s@%s: %s::%s: power supply change encountered error 0x%08x\n`
- `site.AppleUSB30HubPort`
- `UsbProtocol (1.x)`
- `%s@%s: %s::%s: enable change\n`
- `kUSBHubIdlePolicy`
- `%s@%s: %s::%s: invalid client\n`
- `%s@%s: %s::%s: overcurrent change\n`
- `%s@%s: %s::%s: waiting for hot reset\n`
- `usb-port-number`
- `kUSBCameraKitHubTotalCurrent`
- `%s@%s: %s::%s: simulate over-current on power on\n`
- `site.AppleUSB20Hub`
- `kUSBSleepPortCurrentLimit`
- `%s@%s: %s::%s: failed to allocate _interruptBuffer\n`
- `openGated`
- `%s@%s: %s::%s: disabling idle policy\n`
- `%s@%s: %s::%s: failed initial port power allocations\n`
- `allocateDownstreamBusCurrent`
- `%s@%s: %s::%s: remote wake\n`
- `AppleUSBHub.cpp`
- `allocateDownstreamBusCurrentGated`
- `%s@%s: %s::%s: bus-powered override\n`
- `%s@%s: %s::%s: io returned 0x%08x\n`
- `interruptRetry`
- `%s@%s: %s::%s: port %u does not have an open session\n`
- `%s@%s: %s::%s: compliance violation: USB 2.0 11.24.1: hub did not complete control request 0x%02x %02x %04x %04x %04x in %d ms\n`
- `UsbProtocol (2.0)`
- `%s@%s: %s::%s: failed with 0x%08x and last reported status 0x%08x\n`
- `%s@%s: %s::%s: multi TT hub\n`
- `%s@%s: %s::%s: failed to set configuration with 0x%08x\n`
- `createPorts`
- `%s@%s: %s::%s: power supply type %d\n`
- `%s@%s: %s::%s: notifying all ports of overcurrent change\n`
- `AppleUSB30HubPort`
- `%s@%s: %s::%s: location not available\n`
- `powerStateDidChangeTo_block_invoke`
- `%s@%s: %s::%s: simulating power supply change to %d mA\n`
- `site.AppleUSB30Hub`
- `%s@%s: %s::%s: hub depth of %d is not permitted\n`
- `%s@%s: %s::%s: LinkState(%d) LatencyType(%d) result(0x%08x) Latency(%d)\n`
- `%s@%s: %s::%s: kUSBHubStartupDelay %u ms\n`
- `kUSBHubPowerSupply`
- `kUSBFailedRequestedPower`
- `%s@%s: %s::%s: adjusting sleepUnits downward from %d to %d mA\n`
- `%s@%s: %s::%s: self powered %d\n`
- `%s@%s: %s::%s: warm reset change\n`
- `%s@%s: %s::%s: warm reset\n`
- `%s@%s: %s::%s: getPortStatus extended failed 0x%08x\n`
- `com.apple.usb.hub.%s`
- `%s@%s: %s::%s: failed to set hub depth %d (0x%08x)\n`
- `12111112122212121121111111111121222211111111111111111122222222222222222222`
- `UsbHostControllerUSB3LPMPolicy`
- `%s@%s: %s::%s: unable to determine port number\n`
- `interruptOccurred`
- `disconnect`
- `%s@%s: %s::%s: hub rejected control request 0x%02x %02x %04x %04x %04x\n`
- `deviceRequest`
- `%s@%s: %s::%s: rxBitrate %llu.  laneSpeed %llu, laneMantissa %u laneCount %u\n`
- `%s@%s: %s::%s: portBitrate %llu speed %u define\n`
- `site.AppleUSB20CameraKitHub`
- `i8@?0`
- `%s@%s: %s::%s: hub power override with type %d\n`
- `%s@%s: %s::%s: clearStall returned 0x%08x\n`
- `UsbTunnel`
- `kUSBHubStartupDelay`
- `%s@%s: %s::%s: enabling idle policy\n`
- `setPropertiesGated`
- `UsbStreamsSupported`
- `%s@%s: %s::%s: clearing reset change\n`
- `%s@%s: %s::%s: connect\n`
- `%s@%s: %s::%s: resetTT failed with result 0x%08x\n`
- `AppleUSBHub`
- `%s@%s: %s::%s: controller is invalid\n`
- `kUSBHubPortSequenceDelay`
- `%s@%s: %s::%s: hub failed control request 0x%02x %02x %04x %04x %04x with 0x%08x\n`
- `%s@%s: %s::%s: failed hub IO with 0x%08x\n`
- `UsbHostControllerUSB2LPMPolicy`
- `%s@%s: %s::%s: failed to locate an interface\n`
- `%s@%s: %s::%s: failed to create _notifier\n`
- `%s@%s: %s::%s: adjusting wakeUnits downward from %d to %d mA\n`
- `121111121222121211222222212222222222222222222222222222222222222222222222222221221111122221112112222222222211122112111111111111112122`
- `%s@%s: %s::%s: clearing enable change\n`
- `AppleUSB20HubPort`
- `%s@%s: %s::%s: \n`
- `resume`
- `%s@%s: %s::%s: clearing connect change\n`
- `%s@%s: %s::%s: disconnect\n`
- `%s@%s: %s::%s: failed to get upstream port\n`
- `firstMatchNotification`
- `%s@%s: %s::%s: completed with 0x%08x\n`
- `%s@%s: %s::%s: failed to address device, disabling port\n`
- `%s@%s: %s::%s: device descriptor not available\n`
- `locationID`
- `UsbProtocol (3.x)`
- `%s@%s: %s::%s: completed with 0x%08x and status 0x%08x\n`
- `%s@%s: %s::%s: completed with status 0x%08x, bytesTransferred %d\n`
- `%s@%s: %s::%s: port %u is invalid\n`
- `%s@%s: %s::%s: clearing overcurrent change\n`
- `kUSBHubPowerSupplyType`
- `%s@%s: %s::%s: port %u status change\n`
- `setPortFeatureGated`
- `UsbHostControllerUSB4LPMPolicy`
- `AppleUSBHubPort`
- `powerOff`
- `kUSBContainerID`
- `%s@%s: %s::%s: simulate connect change on power on\n`
- `%s@%s: %s::%s: link change to inactive/compliance\n`
- `%s@%s: %s::%s: hot reset\n`
- `getPortSpeed`
- `AppleUSB30Hub`
- `%s@%s: %s::%s: %s property is unavailable\n`
- `AppleUSB20Hub`
- `warmReset`
- `%s@%s: %s::%s: total desired bus current %d mA\n`
- `powerOn`
- `%s@%s: %s::%s: failed to fetch hub descriptor\n`
- `%s@%s: %s::%s: failed to create _interruptRetriesTimer\n`
- `%s@%s: %s::%s: self powered %d, local power lost %d, completed with 0x%08x\n`
- `%s@%s: %s::%s: link state change\n`
- `%s@%s: %s::%s: clearing change bits failed with 0x%08x\n`
- `%s@%s: %s::%s: clearTT failed with result 0x%08x\n`
- `%s@%s: %s::%s: link state %d\n`
- `getLPMExitLatency`
- `site.AppleUSB20HubPort`
- `%s@%s: %s::%s: configuration descriptor is invalid\n`
- `powerStateWillChangeTo_block_invoke`
- `%s@%s: %s::%s: unexpected service %p or notifier %p\n`
- `%s@%s: %s::%s: hub status change\n`
- `%s@%s: %s::%s: type 0x%08x with error 0x%08x\n`
- `AppleUSB20HubPort.cpp`
- `resetAndCreateDevice`
- `site.AppleUSBHub`
- `\"%s[%p]::closeGated failed\" @%s:%d`
- `%s@%s: %s::%s: port %u wake units %d -> %d mA\n`
- `%s@%s: %s::%s: clearing link state change\n`

**[__TEXT.__os_log]**

- `%s@%s: %s::%s: overcurrent active\n`
- `%s@%s: %s::%s: location not available\n`
- `%s@%s: %s::%s: power supply change encountered error 0x%08x\n`
- `%s@%s: %s::%s: port %u feature %d completed with 0x%08x\n`
- `%s@%s: %s::%s: type 0x%08x with error 0x%08x\n`
- `%s@%s: %s::%s: warm reset change\n`
- `%s@%s: %s::%s: hub depth of %d is not permitted\n`
- `%s@%s: %s::%s: hot reset\n`
- `%s@%s: %s::%s: connect\n`
- `%s@%s: %s::%s: failed to locate an interrupt pipe\n`
- `%s@%s: %s::%s: failed to attach or start port %u\n`
- `%s@%s: %s::%s: link state %d\n`
- `%s@%s: %s::%s: failed to get upstream port\n`
- `%s@%s: %s::%s: failed initial port power allocations\n`
- `%s@%s: %s::%s: clearStall returned 0x%08x\n`
- `%s@%s: %s::%s: notifying all ports of local power change\n`
- `%s@%s: %s::%s: link configuration error\n`
- `%s@%s: %s::%s: clearing overcurrent change\n`
- `%s@%s: %s::%s: failed to create _interruptRetriesTimer\n`
- `%s@%s: %s::%s: failed to queue new IO\n`
- `%s@%s: %s::%s: clearTT failed with result 0x%08x\n`
- `%s@%s: %s::%s: kUSBHubStartupDelay %u ms\n`
- `%s@%s: %s::%s: service is inactive\n`
- `%s@%s: %s::%s: clearing reset change\n`
- `%s@%s: %s::%s: failed to fetch hub descriptor\n`
- `%s@%s: %s::%s: link change to inactive/compliance\n`
- `%s@%s: %s::%s: failed to create _notifier\n`
- `%s@%s: %s::%s: completed with status 0x%08x, bytesTransferred %d\n`
- `%s@%s: %s::%s: invalid statusCode %u\n`
- `%s@%s: %s::%s: controller is invalid\n`
- `%s@%s: %s::%s: configuration descriptor is invalid\n`
- `%s@%s: %s::%s: failed to locate an interface\n`
- `%s@%s: %s::%s: adjusting sleepUnits downward from %d to %d mA\n`
- `%s@%s: %s::%s: bus-powered override\n`
- `%s@%s: %s::%s: resetTT failed with result 0x%08x\n`
- `%s@%s: %s::%s: device descriptor not available\n`
- `%s@%s: %s::%s: self powered %d, local power lost %d, completed with 0x%08x\n`
- `%s@%s: %s::%s: Setting Timeout linkState %d timeoutUs %d result 0x%08x\n`
- `%s@%s: %s::%s: reset did not enable port\n`
- `%s@%s: %s::%s: self powered %d\n`
- `%s@%s: %s::%s: clearing link state change\n`
- `%s@%s: %s::%s: clearing suspend change\n`
- `%s@%s: %s::%s: clearing change bits failed with 0x%08x\n`
- `%s@%s: %s::%s: failed to open device\n`
- `%s@%s: %s::%s: simulate over-current on power on\n`
- `%s@%s: %s::%s: completed with 0x%08x and status 0x%08x\n`
- `%s@%s: %s::%s: rxBitrate %llu.  laneSpeed %llu, laneMantissa %u laneCount %u\n`
- `%s@%s: %s::%s: failed with 0x%08x and last reported status 0x%08x\n`
- `%s@%s: %s::%s: clearing enable change\n`
- `%s@%s: %s::%s: failed to allocate _interruptBuffer\n`
- `%s@%s: %s::%s: client %p wakeUnits %d sleepUnits %d completed with 0x%08x\n`
- `%s@%s: %s::%s: port %u wake units %d -> %d mA\n`
- `%s@%s: %s::%s: hub rejected control request 0x%02x %02x %04x %04x %04x\n`
- `%s@%s: %s::%s: unable to determine port number\n`
- `%s@%s: %s::%s: completed with 0x%08x\n`
- `%s@%s: %s::%s: remote wake\n`
- `%s@%s: %s::%s: overcurrent change with portStatus = %x\n`
- `%s@%s: %s::%s: overcurrent cleared\n`
- `%s@%s: %s::%s: hubs with %d ports are not supported\n`
- `%s@%s: %s::%s: getPortStatus extended failed 0x%08x\n`
- `%s@%s: %s::%s: %s property is unavailable\n`
- `%s@%s: %s::%s: notifying all ports of overcurrent change\n`
- `%s@%s: %s::%s: reset change\n`
- `%s@%s: %s::%s: failed to allocate port %u\n`
- `%s@%s: %s::%s: port %u is invalid\n`
- `%s@%s: %s::%s: clearing connect change\n`
- `%s@%s: %s::%s: failed to create _busCurrentAllocator\n`
- `%s@%s: %s::%s: \n`
- `%s@%s: %s::%s: enable change\n`
- `%s@%s: %s::%s: failed to set configuration with 0x%08x\n`
- `%s@%s: %s::%s: unable to open provider or inactive\n`
- `%s@%s: %s::%s: local power change\n`
- `%s@%s: %s::%s: reset did not complete\n`
- `%s@%s: %s::%s: kUSBHubPortSequenceDelay %u ms\n`
- `%s@%s: %s::%s: hub power override with type %d\n`
- `%s@%s: %s::%s: txBitrate %llu.  laneSpeed %llu, laneMantissa %u laneCount %u\n`
- `%s@%s: %s::%s: failed to address device, disabling port\n`
- `%s@%s: %s::%s: disabling idle policy\n`
- `%s@%s: %s::%s: port %u is requesting %d wakeUnits and %d sleepUnits mA\n`
- `%s@%s: %s::%s: hub failed control request 0x%02x %02x %04x %04x %04x with 0x%08x\n`
- `%s@%s: %s::%s: failed to set hub depth %d (0x%08x)\n`
- `%s@%s: %s::%s: simulate connect change on power on\n`
- `%s@%s: %s::%s: failed to allocate _commandGate\n`
- `%s@%s: %s::%s: adjusting wakeUnits downward from %d to %d mA\n`
- `%s@%s: %s::%s: io returned 0x%08x\n`
- `%s@%s: %s::%s: warm reset\n`
- `%s@%s: %s::%s: provider is invalid\n`
- `%s@%s: %s::%s: enabling idle policy\n`
- `%s@%s: %s::%s: link state change\n`
- `%s@%s: %s::%s: failed hub IO with 0x%08x\n`
- `%s@%s: %s::%s: link state %u\n`
- `%s@%s: %s::%s: disconnect\n`
- `%s@%s: %s::%s: power supply type %d\n`
- `%s@%s: %s::%s: port %u does not have an open session\n`
- `%s@%s: %s::%s: connect change\n`
- `%s@%s: %s::%s: unable to raise port power state from %d\n`
- `%s@%s: %s::%s: setting hub depth %d\n`
- `%s@%s: %s::%s: portBitrate %llu speed %u define\n`
- `%s@%s: %s::%s: hub power status change\n`
- `%s@%s: %s::%s: multi TT hub\n`
- `%s@%s: %s::%s: failed to open interface\n`
- `%s@%s: %s::%s: unexpected service %p or notifier %p\n`
- `%s@%s: %s::%s: port needs to be resumed\n`
- `%s@%s: %s::%s: unable to raise power state, deferring interrupt\n`
- `%s@%s: %s::%s: hubs with bcdVersion of 0x%04x are not supported\n`
- `%s@%s: %s::%s: invalid client\n`
- `%s@%s: %s::%s: change bits still set, port status 0x%08x\n`
- `%s@%s: %s::%s: failed to create clients set\n`
- `%s@%s: %s::%s: overcurrent change\n`
- `%s@%s: %s::%s: compliance violation: USB 2.0 11.24.1: hub did not complete control request 0x%02x %02x %04x %04x %04x in %d ms\n`
- `%s@%s: %s::%s: waiting for hot reset\n`
- `%s@%s: %s::%s: simulating power supply change to %d mA\n`
- `%s@%s: %s::%s: LinkState(%d) LatencyType(%d) result(0x%08x) Latency(%d)\n`
- `%s@%s: %s::%s: asserting reset\n`
- `%s@%s: %s::%s: unable to find parent port\n`
- `%s@%s: %s::%s: port %u sleep units %d -> %d mA\n`
- `%s@%s: %s::%s: hub status change\n`
- `%s@%s: %s::%s: port %u status change\n`
- `%s@%s: %s::%s: total desired bus current %d mA\n`
