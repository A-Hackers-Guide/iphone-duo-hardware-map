# `com.apple.driver.usb.IOUSBHostHIDDevice`

- Name: I/O Kit Driver for USB HID Devices
- Version: `1.2`
- UUID: `58BE4D8E-B8E0-31E8-8DF3-B8E0868B35E7`
- Source version: `1617.40.10.0.0`
- Depends on: [`com.apple.driver.usb.AppleUSBCommon`](com.apple.driver.usb.AppleUSBCommon.md) 1.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 2.0, [`com.apple.iokit.IOUSBHostFamily`](com.apple.iokit.IOUSBHostFamily.md) 1.2, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 23.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 23.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 23.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 23.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### Generic Keyboard
- `CFBundleIdentifier`: `com.apple.driver.usb.IOUSBHostHIDDevice`
- `HIDDefaultBehavior`: ``
- `IOClass`: `IOUSBHostHIDDevice`
- `IOMatchDefer`: `True`
- `IOPersonalityPublisher`: `com.apple.driver.usb.IOUSBHostHIDDevice`
- `IOProviderClass`: `IOUSBHostInterface`
- `bInterfaceClass`: `3`
- `bInterfaceProtocol`: `1`
- `bInterfaceSubClass`: `1`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSBHostBulkHIDDevice` | 0x170 | IOUSBHostHIDDevice → IOHIDDevice → IOService → IORegistryEntry |
| `IOUSBHostHIDDevice` | 0x168 | IOHIDDevice → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001a9b off=0x00b62500-0x00b63f9b addr=0xfffffe0007b66500-0xfffffe0007b67f9b r--/r--   __TEXT            
	sz=0x00000ac4 off=0x00b62b28-0x00b635ec addr=0xfffffe0007b66b28-0xfffffe0007b675ec               __TEXT.__cstring          (CstringLiterals)
	sz=0x000009af off=0x00b635ec-0x00b63f9b addr=0xfffffe0007b675ec-0xfffffe0007b67f9b               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00007024 off=0x03851890-0x038588b4 addr=0xfffffe000a855890-0xfffffe000a85c8b4 r-x/r-x   __TEXT_EXEC       
	sz=0x00006df4 off=0x03851890-0x03858684 addr=0xfffffe000a855890-0xfffffe000a85c684          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000230 off=0x03858684-0x038588b4 addr=0xfffffe000a85c684-0xfffffe000a85c8b4          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000128 off=0x04a1c8f0-0x04a1ca18 addr=0xfffffe000ba208f0-0xfffffe000ba20a18 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a1c8f0-0x04a1c9b8 addr=0xfffffe000ba208f0-0xfffffe000ba209b8               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000ba209b8-0xfffffe000ba20a18               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000012b8 off=0x0146f5a8-0x01470860 addr=0xfffffe00084735a8-0xfffffe0008474860 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x0146f5a8-0x0146f5b8 addr=0xfffffe00084735a8-0xfffffe00084735b8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x0146f5b8-0x0146f5c8 addr=0xfffffe00084735b8-0xfffffe00084735c8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000f20 off=0x0146f5c8-0x014704e8 addr=0xfffffe00084735c8-0xfffffe00084744e8         __DATA_CONST.__const            
	sz=0x00000200 off=0x014704e8-0x014706e8 addr=0xfffffe00084744e8-0xfffffe00084746e8         __DATA_CONST.__kalloc_type      
	sz=0x00000118 off=0x014706e8-0x01470800 addr=0xfffffe00084746e8-0xfffffe0008474800         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000060 off=0x01470800-0x01470860 addr=0xfffffe0008474800-0xfffffe0008474860         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 82 at 0x04afb6b4
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     58BE4D8E-B8E0-31E8-8DF3-B8E0868B35E7
008: LC_SOURCE_VERSION           1617.40.10.0.0
009: LC_FUNCTION_STARTS          offset=0x004aca650 size=0x78
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOUSBHostHIDDevice`
- `CFBundleIdentifier`: `com.apple.driver.usb.IOUSBHostHIDDevice`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `I/O Kit Driver for USB HID Devices`
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
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Console`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOUSBHostFamily.kext/PlugIns/IOUSBHostHIDDevice.kext`
- `_PrelinkExecutableLoadAddr`: `-2198893861632`
- `_PrelinkExecutableRelativePath`: `IOUSBHostHIDDevice`
- `_PrelinkExecutableSize`: `40607`
- `_PrelinkExecutableSourceAddr`: `-2198893861632`
- `_PrelinkKmodInfo`: `-2198828087056`

## Strings (140) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `getReport Compatibility`
- `readInterruptPipeAsyncGated`
- `%s: %s::%s: resetting: clearStall failed with 0x%08x\n`
- `%s: %s::%s: IO error 0x%08x, %d retries remaining\n`
- `%s: %s::%s: not enough memory\n`
- `%s: %s::%s: not enough bandwidth\n`
- `%s: %s::%s: start has failed\n`
- `%s: %s::%s: \n`
- `%s: %s::%s: IOHIDDevice handleStart failure\n`
- `%s: %s::%s: unsupported device\n`
- `%s: %s::%s: index is 0\n`
- `%s: %s::%s: hid descriptor not found\n`
- `site.AppleUSBBulkHidExpansionData`
- `%s: %s::%s: unable to get zlp descriptor\n`
- `%s: %s::%s: unable to obtain device\n`
- `%s: %s::%s: interface is null\n`
- `ReportInterval`
- `getHidDescriptorGated`
- `SIXAXIS compatibility`
- `getReport`
- `%s: %s::%s: interrupt pipe read\n`
- `interruptRetry`
- `%s: %s::%s: unable to open interface\n`
- `%s: %s::%s: unable to obtain workLoop\n`
- `USB`
- `kUSBHIDDeviceIdlePolicy`
- `newCountryCodeNumber`
- `setReport`
- `%s: %s::%s: not enough space\n`
- `%s: %s::%s: resetting interrupt retries\n`
- `site.tAsyncContext`
- `site.AppleUSBHostBulkHIDDevice`
- `%s: %s::%s: unable to get input pipe\n`
- `MaxFeatureReportSize`
- `%s: %s::%s: setting idle policy of %u ms\n`
- `IOUSBHostHIDDevice`
- `%s: %s::%s: failed to get interface descriptor\n`
- `%s: %s::%s: unable to get interrupt pipe\n`
- `%s: %s::%s: unable to obtain commandGate\n`
- `newLocationIDNumber`
- `locationID`
- `newReportDescriptor`
- `setProtocol`
- `MaxInputReportSize`
- `setProperty`
- `%s: %s::%s: IO is busy\n`
- `%s: %s::%s: pipe halted\n`
- `%s: %s::%s: IO aborted\n`
- `%s: %s::%s: resetting due to errors\n`
- `%s: %s::%s: resetting: IO error 0x%08x, %d retries remaining\n`
- `%s: %s::%s: provider not an IOUSBHostInterface\n`
- `%s: %s::%s: unable to request SIXAXIS device\n`
- `%s: %s::%s: failed to create _interruptRetriesTimer\n`
- `11111`
- `%s: %s::%s: IO not permitted\n`
- `%s: %s::%s: unable to set Saitek device idle milliseconds\n`
- `AppleUSBHostBulkHIDDevice`
- `%s,%s`
- `SetIdleMillisecs`
- `handleStart`
- `121111121222121211211122211111111111111112221`
- `%s: %s::%s: unable to start IOHIDDevice\n`
- `%s: %s::%s: setting interval %u microseconds\n`
- `getHidDescriptor`
- `%s: %s::%s: interface or device is null\n`
- `readInterruptPipeAsync`
- `%s: %s::%s: interface is closed or inactive\n`
- `1211111212221212112111222111111111111111122211`
- `2112`
- `%s: %s::%s: bad argument\n`
- `%s: %s::%s: unable to obtain context buffer\n`
- `newReportIntervalNumber`
- `%s: %s::%s: commandGate is null`
- `%s: %s::%s: IO not ready\n`
- `%s: %s::%s: unable to obtain expansion data buffer\n`
- `site.IOUSBHostHIDDevice`
- `site.tIOUSBHidExpansionData`
- `MaxOutputReportSize`
- `%s: %s::%s: interrupt out pipe failed or doesn't exist\n`
- `getStringAtIndex`
- `%s: %s::%s: unable to get proper HID report descriptor size\n`
- `start`
- `%s: %s::%s: inputReportSize = %u, maxPacketSize = %u\n`
- `%s: %s::%s: unable to read interrupt pipe\n`
- `%s: %s::%s: unable to obtain interface\n`
- `%s: %s::%s: device is null\n`
- `%s: %s::%s: reading interrupt pipe async\n`
- `interruptReadComplete`
- `RegisterService`
- `%s: %s::%s: unable to get I/O buffer\n`

**[__TEXT.__os_log]**

- `%s: %s::%s: unable to set Saitek device idle milliseconds\n`
- `%s: %s::%s: unable to read interrupt pipe\n`
- `%s: %s::%s: failed to create _interruptRetriesTimer\n`
- `%s: %s::%s: unable to get proper HID report descriptor size\n`
- `%s: %s::%s: interface or device is null\n`
- `%s: %s::%s: reading interrupt pipe async\n`
- `%s: %s::%s: IO not ready\n`
- `%s: %s::%s: \n`
- `%s: %s::%s: setting idle policy of %u ms\n`
- `%s: %s::%s: IOHIDDevice handleStart failure\n`
- `%s: %s::%s: unable to obtain interface\n`
- `%s: %s::%s: unable to obtain workLoop\n`
- `%s: %s::%s: interrupt out pipe failed or doesn't exist\n`
- `%s: %s::%s: not enough memory\n`
- `%s: %s::%s: resetting due to errors\n`
- `%s: %s::%s: unable to obtain expansion data buffer\n`
- `%s: %s::%s: unable to get zlp descriptor\n`
- `%s: %s::%s: unable to obtain commandGate\n`
- `%s: %s::%s: hid descriptor not found\n`
- `%s: %s::%s: resetting: IO error 0x%08x, %d retries remaining\n`
- `%s: %s::%s: unable to get I/O buffer\n`
- `%s: %s::%s: bad argument\n`
- `%s: %s::%s: index is 0\n`
- `%s: %s::%s: device is null\n`
- `%s: %s::%s: IO is busy\n`
- `%s: %s::%s: IO aborted\n`
- `%s: %s::%s: resetting interrupt retries\n`
- `%s: %s::%s: unable to get input pipe\n`
- `%s: %s::%s: provider not an IOUSBHostInterface\n`
- `%s: %s::%s: unable to obtain context buffer\n`
- `%s: %s::%s: setting interval %u microseconds\n`
- `%s: %s::%s: IO not permitted\n`
- `%s: %s::%s: resetting: clearStall failed with 0x%08x\n`
- `%s: %s::%s: IO error 0x%08x, %d retries remaining\n`
- `%s: %s::%s: start has failed\n`
- `%s: %s::%s: failed to get interface descriptor\n`
- `%s: %s::%s: unsupported device\n`
- `%s: %s::%s: not enough space\n`
- `%s: %s::%s: pipe halted\n`
- `%s: %s::%s: unable to get interrupt pipe\n`
- `%s: %s::%s: inputReportSize = %u, maxPacketSize = %u\n`
- `%s: %s::%s: unable to obtain device\n`
- `%s: %s::%s: commandGate is null`
- `%s: %s::%s: not enough bandwidth\n`
- `%s: %s::%s: interrupt pipe read\n`
- `%s: %s::%s: unable to start IOHIDDevice\n`
- `%s: %s::%s: unable to request SIXAXIS device\n`
- `%s: %s::%s: unable to open interface\n`
- `%s: %s::%s: interface is null\n`
- `%s: %s::%s: interface is closed or inactive\n`
