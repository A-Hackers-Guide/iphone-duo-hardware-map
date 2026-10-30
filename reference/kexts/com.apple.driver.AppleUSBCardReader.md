# `com.apple.driver.AppleUSBCardReader`

- Name: AppleUSBCardReader
- Version: `564`
- UUID: `45CD1567-8E6A-3244-99F5-7CE1CEA6A791`
- Source version: `564.0.0.0.0`
- Depends on: [`com.apple.iokit.IOSCSIArchitectureModelFamily`](com.apple.iokit.IOSCSIArchitectureModelFamily.md) 2.1.0, [`com.apple.iokit.IOSCSIBlockCommandsDevice`](com.apple.iokit.IOSCSIBlockCommandsDevice.md) 2.1.0, [`com.apple.iokit.IOStorageFamily`](com.apple.iokit.IOStorageFamily.md) 1.5.6, [`com.apple.iokit.IOUSBHostFamily`](com.apple.iokit.IOUSBHostFamily.md) 1.0.1, [`com.apple.iokit.IOUSBMassStorageDriver`](com.apple.iokit.IOUSBMassStorageDriver.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (7) [KC]

### AppleSDCardReader
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBCardReader`
- `IOClass`: `com_apple_driver_AppleUSBCardReaderSBC`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBCardReader`
- `IOProviderClass`: `IOSCSILogicalUnitNub`
- `Peripheral Device Type`: `0`
- `Physical Interconnect`: `USB`
- `Product Identification`: `SD Card Reader`
- `Vendor Identification`: `APPLE`

### Apple_Internal_SD_Card_Reader_4_00
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBCardReader`
- `IOClass`: `com_apple_driver_AppleUSBCardReaderUMC`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBCardReader`
- `IOProviderClass`: `IOUSBMassStorageDriverNub`
- `Physical Interconnect`: `USB`
- `Read Time Out Duration`: `30000`
- `SCSI Device Characteristics`:
  - `IOMaximumBlockCountRead`: `8192`
  - `IOMaximumBlockCountWrite`: `8192`
  - `IOMaximumByteCountRead`: `4194304`
  - `IOMaximumByteCountWrite`: `4194304`
- `USB Mass Storage Characteristics`:
  - `Max Logical Unit Number`: `0`
  - `USB3LPM`: `3`
- `Write Time Out Duration`: `30000`
- `bConfigurationValue`: `1`
- `bInterfaceNumber`: `0`
- `idProduct`: `33799`
- `idVendor`: `1452`

### Apple_Internal_SD_Card_Reader_4_00_Driver_Nub
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBCardReader`
- `IOClass`: `com_apple_driver_AppleUSBCardReaderDriverNub`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBCardReader`
- `IOProviderClass`: `com_apple_driver_AppleUSBCardReaderInterfaceNub`
- `bConfigurationValue`: `1`
- `bInterfaceNumber`: `0`
- `idProduct`: `33799`
- `idVendor`: `1452`

### Apple_Internal_SD_Card_Reader_4_00_Interface_Nub 
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBCardReader`
- `IOClass`: `com_apple_driver_AppleUSBCardReaderInterfaceNub`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBCardReader`
- `IOProviderClass`: `IOUSBHostInterface`
- `Physical Interconnect Location`: `External`
- `bConfigurationValue`: `1`
- `bInterfaceNumber`: `0`
- `idProduct`: `33799`
- `idVendor`: `1452`

### Apple_Internal_SD_Card_Reader_6_00
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBCardReader`
- `IOClass`: `com_apple_driver_AppleUSBCardReaderUMC`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBCardReader`
- `IOProviderClass`: `IOUSBMassStorageDriverNub`
- `Physical Interconnect`: `USB`
- `Read Time Out Duration`: `30000`
- `SCSI Device Characteristics`:
  - `IOMaximumBlockCountRead`: `8192`
  - `IOMaximumBlockCountWrite`: `8192`
  - `IOMaximumByteCountRead`: `4194304`
  - `IOMaximumByteCountWrite`: `4194304`
- `USB Mass Storage Characteristics`:
  - `Max Logical Unit Number`: `0`
  - `USB3LPM`: `3`
- `Write Time Out Duration`: `30000`
- `bConfigurationValue`: `1`
- `bInterfaceNumber`: `0`
- `idProduct`: `33801`
- `idVendor`: `1452`

### Apple_Internal_SD_Card_Reader_6_00_Driver_Nub
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBCardReader`
- `IOClass`: `com_apple_driver_AppleUSBCardReaderDriverNub`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBCardReader`
- `IOProviderClass`: `com_apple_driver_AppleUSBCardReaderInterfaceNub`
- `bConfigurationValue`: `1`
- `bInterfaceNumber`: `0`
- `idProduct`: `33801`
- `idVendor`: `1452`

### Apple_Internal_SD_Card_Reader_6_00_Interface_Nub
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBCardReader`
- `IOClass`: `com_apple_driver_AppleUSBCardReaderInterfaceNub`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBCardReader`
- `IOProviderClass`: `IOUSBHostInterface`
- `Physical Interconnect Location`: `External`
- `bConfigurationValue`: `1`
- `bInterfaceNumber`: `0`
- `idProduct`: `33801`
- `idVendor`: `1452`


## C++ classes (5) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSBCardReaderBlockStorageServices` | 0xb8 | IOBlockStorageServices → IOBlockStorageDevice → IOService → IORegistryEntry |
| `com_apple_driver_AppleUSBCardReaderDriverNub` | 0x6c0 | IOUSBMassStorageDriverNub → IOService → IORegistryEntry |
| `com_apple_driver_AppleUSBCardReaderInterfaceNub` | 0x508 | IOUSBMassStorageInterfaceNub → IOService → IORegistryEntry |
| `com_apple_driver_AppleUSBCardReaderSBC` | 0x180 | IOSCSIPeripheralDeviceType00 → IOSCSIBlockCommandsDevice → IOSCSIPrimaryCommandsDevice → IOSCSIProtocolInterface → IOService → IORegistryEntry |
| `com_apple_driver_AppleUSBCardReaderUMC` | 0x1f0 | IOUSBMassStorageDriver → IOSCSIProtocolServices → IOSCSIProtocolInterface → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000019a8 off=0x0079a570-0x0079bf18 addr=0xfffffe000779e570-0xfffffe000779ff18 r--/r--   __TEXT            
	sz=0x00000f97 off=0x0079ab98-0x0079bb2f addr=0xfffffe000779eb98-0xfffffe000779fb2f               __TEXT.__cstring          (CstringLiterals)
	sz=0x000003e8 off=0x0079bb30-0x0079bf18 addr=0xfffffe000779fb30-0xfffffe000779ff18               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x0000a174 off=0x0277b1c0-0x02785334 addr=0xfffffe000977f1c0-0xfffffe0009789334 r-x/r-x   __TEXT_EXEC       
	sz=0x00009d24 off=0x0277b1c0-0x02784ee4 addr=0xfffffe000977f1c0-0xfffffe0009788ee4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000450 off=0x02784ee4-0x02785334 addr=0xfffffe0009788ee4-0xfffffe0009789334          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000628 off=0x049a10d8-0x049a1700 addr=0xfffffe000b9a50d8-0xfffffe000b9a5700 rw-/rw-   __DATA            
	sz=0x00000548 off=0x049a10d8-0x049a1620 addr=0xfffffe000b9a50d8-0xfffffe000b9a5620               __DATA.__data             
	sz=0x000000e0 off=0x00000000-0x000000e0 addr=0xfffffe000b9a5620-0xfffffe000b9a5700               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000027a8 off=0x012342a8-0x01236a50 addr=0xfffffe00082382a8-0xfffffe000823aa50 rw-/rw-   __DATA_CONST      
	sz=0x00000028 off=0x012342a8-0x012342d0 addr=0xfffffe00082382a8-0xfffffe00082382d0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000028 off=0x012342d0-0x012342f8 addr=0xfffffe00082382d0-0xfffffe00082382f8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00002308 off=0x012342f8-0x01236600 addr=0xfffffe00082382f8-0xfffffe000823a600         __DATA_CONST.__const            
	sz=0x00000140 off=0x01236600-0x01236740 addr=0xfffffe000823a600-0xfffffe000823a740         __DATA_CONST.__kalloc_type      
	sz=0x00000228 off=0x01236740-0x01236968 addr=0xfffffe000823a740-0xfffffe000823a968         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000e8 off=0x01236968-0x01236a50 addr=0xfffffe000823a968-0xfffffe000823aa50         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 167 at 0x04ae7754
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     45CD1567-8E6A-3244-99F5-7CE1CEA6A791
008: LC_SOURCE_VERSION           564.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab3510 size=0x130
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleUSBCardReader`
- `CFBundleGetInfoString`: `564, Copyright Apple Inc. 2014-2016`
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBCardReader`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleUSBCardReader`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `564`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `564`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleStorageDrivers.kext/PlugIns/AppleUSBCardReader.kext`
- `_PrelinkExecutableLoadAddr`: `-2198897826448`
- `_PrelinkExecutableRelativePath`: `AppleUSBCardReader`
- `_PrelinkExecutableSize`: `59628`
- `_PrelinkExecutableSourceAddr`: `-2198897826448`
- `_PrelinkKmodInfo`: `-2198828592936`

## Strings (143) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `com_apple_driver_AppleUSBCardReaderInterfaceNub`
- `%s %s\n`
- `%s Setting TXSW value to 0x%x result 0x%x\n`
- `%s Could not read SLEW data from card\n`
- `EQR`
- `USB CR UMC rPD1 0x%x\n`
- `USB CR UMC cPST1 0x%x\n`
- `%s Firmware does not support setting specific UHS modes\n`
- `%s Setting RXEQ value to 0x%x result 0x%x\n`
- `%s Firmware does not support setting specific power states\n`
- `USB CR SBC cPST3 0x%x\n`
- `SPLTSET`
- `%s SLEW can be read only for UHS mode 1, current is %d\n`
- `RXEQ`
- `USB CR IN mU 0x%x\n`
- `12111112122212121111221112111111222111121111222222122222112222`
- `%s:: logical reset wait for reconnect returned 0x%x\n`
- `%s %s %x\n`
- `S025SET`
- `%s Setting UHS Mode to 0x%x result 0x%x\n`
- `USBCardReader-50`
- `NULL`
- `121111121222121211112211212121221211222211112222`
- `S104SET`
- `%s Unable to read mode number\n`
- `Card Type`
- `USB CR UMC cPST2 0x%x\n`
- `USB device %016llX - %s, %s - found new interfaceNub upon waking\n`
- `%s Could not read TXSW data from card\n`
- `UHS-II Mode`
- `Link Error Count 0x%x\n`
- `USB CR TES init failed\n`
- `%s No object found for Base Frequency\n`
- `Full Duplex`
- `SDSC`
- `SSC`
- `USB CR IN cPST 0x%x\n`
- `USBCardReader`
- `%s Setting UHS Mode parameter not an OSNumber?\n`
- `Write Protect`
- `Setting Test Mode to 0x%x`
- `0x%02X 0x%02X 0x%02X 0x%02X 0x%02X 0x%02X 0x%02X 0x%02X 0x%02X\n`
- `Device Speed`
- `USB CR DN tPCO 0x%x\n`
- `site.com_apple_driver_AppleUSBCardReaderSBC`
- `%s Frequency %d incorrect for UHS2\n`
- `%s Firmware does not support reading SLEW property\n`
- `0x%02X 0x%02X 0x%02X 0x%02X 0x%02X 0x%02X 0x%02X 0x%02X 0x%02X 0x%02X\n`
- `%s:: Start: %u, Speed: %d\n`
- `USB CR DN cPST2 0x%x\n`
- `%s Setting SLEW value to 0x%x result 0x%x\n`
- `DriverPowerState`
- `USBCardReader-PS`
- `idProduct`
- `site.AppleUSBCardReaderBlockStorageServices`
- `VCommand`
- `%s Setting Frequency to %d for UHS Mode to 0x%x result 0x%x\n`
- `LEC`
- `UHS mode`
- `%s Invalid power state transition to %x\n`
- `Bus Width`
- `%s:: Controller Reset Error:0x%x\n`
- `USB CR SBC cPST1 0x%x\n`
- `Half Duplex`
- `USB CR port could not be turned on\n`
- `USB CR DN IN cPS 0x%x\n`
- `USB device %016llX - %s, %s - detected termination of interfaceNub, currentPowerState %lu, provider is %s\n`
- `USB Mass Storage Trace ID`
- `ResultData`
- `CRC Error Count`
- `S025`
- `Checking SD WP`
- `Base Frequency`
- `%s Setting frequency for UHS1 failed\n`
- `UCR PPST 0x%x\n`
- `RDYG`
- `site.com_apple_driver_AppleUSBCardReaderDriverNub`
- `USB CR TES add failed\n`
- `USB CR DN rPD1 0x%x\n`
- `SLEW`
- `AppleUSBCardReaderBlockStorageServices`
- `UHSMode`
- `%s Firmware does not support setting specific Clock Rates\n`
- `%s TXSW can be read only for UHS mode 1, current is %d\n`
- `ResetDriverPower`
- `121111121222121211212222222222222222222222222222222222222222222222222222222222222222222111211122111111121111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111112112222112122`
- `com_apple_driver_AppleUSBCardReaderDriverNub`
- `IOPMDeepIdleSupported`
- `Card Characteristics`
- `USB CR has no interface nub after %lu->%lu transition\n`
- `Product Revision Level`
- `Disabled`
- `%s Setting frequency for UHS2 failed\n`
- `Power Transition Period`
- `USB CR IN rPD 0x%x\n`
- `com_apple_driver_AppleUSBCardReaderUMC`
- `USB CR UMC tPCO 0x%x\n`
- `TestMode`
- `USB CR SBC gPMRD\n`
- `USB CR SBC cPST2 0x%x\n`
- `SDHC`
- `model`
- `CMD-D`
- `USB CR SBC mU 0x%x\n`
- `MMC`
- `iPhone`
- `IOMaximumSegmentCountWrite`
- `TXSW`
- `USB CR DN IN MI\n`
- `12111112122212121121221`
- `%s Firmware does not support reading RXEQ property\n`
- `USB CR SBC rPD1 0x%x\n`
- `USB CR UMC rPD2 0x%x\n`
- `USB CR UMC cPST3 0x%x\n`
- `PowerGating`
- `%s Frequency %d incorrect for UHS1\n`
- `%s Setting Compliance Mode to 0x%x result 0x%x\n`
- `SDXC`
- `PlatformSettings`
- `USB CR SBC sITP 0x%x\n`
- `USB CR DN fPMR MI\n`
- `USB CR DN cPST1 0x%x\n`
- `USB CR DN rPD2 0x%x\n`
- `%s Firmware does not support reading TXSW property\n`
- `USBCardReader-ITP`
- `USBCardReader-104`
- `debug`
- `S050`
- `USBCardReader-25`
- `12111112122212121121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222112222`
- `com_apple_driver_AppleUSBCardReaderSBC`
- `IOMaximumSegmentCountRead`
- `S104`
- `site.com_apple_driver_AppleUSBCardReaderInterfaceNub`
- `ITP`
- `non-NULL`
- `S050SET`
- `CheckSDWP`
- `%s Could not read RXEQ data from card\n`
- `Compliance mode`
- `USB CR SBC rPD2 0x%x\n`
- `site.com_apple_driver_AppleUSBCardReaderUMC`
- `ComplianceMode`
