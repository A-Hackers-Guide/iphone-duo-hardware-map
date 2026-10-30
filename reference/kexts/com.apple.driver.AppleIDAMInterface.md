# `com.apple.driver.AppleIDAMInterface`

- Name: AppleIDAMInterface
- Version: `1`
- UUID: `BE71E7DB-7426-3760-8180-D815E6CA7723`
- Source version: `24.0.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.iokit.IOUSBDeviceFamily`](com.apple.iokit.IOUSBDeviceFamily.md) 2.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 14.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 14.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 14.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleIDAMInterface
- `CFBundleIdentifier`: `com.apple.driver.AppleIDAMInterface`
- `IOClass`: `AppleIDAMInterface`
- `IOPersonalityPublisher`: `com.apple.driver.AppleIDAMInterface`
- `IOPropertyMatch`:
  - `USBDeviceFunction`: `IDAMInterface`
- `IOProviderClass`: `IOUSBDeviceInterface`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleIDAMInterface` | 0xa8 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000ccf off=0x00519300-0x00519fcf addr=0xfffffe000751d300-0xfffffe000751dfcf r--/r--   __TEXT            
	sz=0x00000008 off=0x00519978-0x00519980 addr=0xfffffe000751d978-0xfffffe000751d980               __TEXT.__const            
	sz=0x00000198 off=0x00519980-0x00519b18 addr=0xfffffe000751d980-0xfffffe000751db18               __TEXT.__cstring          (CstringLiterals)
	sz=0x000004b7 off=0x00519b18-0x00519fcf addr=0xfffffe000751db18-0xfffffe000751dfcf               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00000de0 off=0x01ffa050-0x01ffae30 addr=0xfffffe0008ffe050-0xfffffe0008ffee30 r-x/r-x   __TEXT_EXEC       
	sz=0x00000cb0 off=0x01ffa050-0x01ffad00 addr=0xfffffe0008ffe050-0xfffffe0008ffed00          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000130 off=0x01ffad00-0x01ffae30 addr=0xfffffe0008ffed00-0xfffffe0008ffee30          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000108 off=0x0494ced0-0x0494cfd8 addr=0xfffffe000b950ed0-0xfffffe000b950fd8 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x0494ced0-0x0494cf98 addr=0xfffffe000b950ed0-0xfffffe000b950f98               __DATA.__data             
	sz=0x00000040 off=0x00000000-0x00000040 addr=0xfffffe000b950f98-0xfffffe000b950fd8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000006f0 off=0x0110e3e0-0x0110ead0 addr=0xfffffe00081123e0-0xfffffe0008112ad0 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x0110e3e0-0x0110e3e8 addr=0xfffffe00081123e0-0xfffffe00081123e8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x0110e3e8-0x0110e3f0 addr=0xfffffe00081123e8-0xfffffe00081123f0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000005f0 off=0x0110e3f0-0x0110e9e0 addr=0xfffffe00081123f0-0xfffffe00081129e0         __DATA_CONST.__const            
	sz=0x00000040 off=0x0110e9e0-0x0110ea20 addr=0xfffffe00081129e0-0xfffffe0008112a20         __DATA_CONST.__kalloc_type      
	sz=0x00000098 off=0x0110ea20-0x0110eab8 addr=0xfffffe0008112a20-0xfffffe0008112ab8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000018 off=0x0110eab8-0x0110ead0 addr=0xfffffe0008112ab8-0xfffffe0008112ad0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 41 at 0x04adcdc0
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     BE71E7DB-7426-3760-8180-D815E6CA7723
008: LC_SOURCE_VERSION           24.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aa5140 size=0x30
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleIDAMInterface`
- `CFBundleIdentifier`: `com.apple.driver.AppleIDAMInterface`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleIDAMInterface`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2015 Apple Inc. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleIDAMInterface.kext`
- `_PrelinkExecutableLoadAddr`: `-2198900452608`
- `_PrelinkExecutableRelativePath`: `AppleIDAMInterface`
- `_PrelinkExecutableSize`: `8871`
- `_PrelinkExecutableSourceAddr`: `-2198900452608`
- `_PrelinkKmodInfo`: `-2198828937520`

## Strings (31) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `embedded`
- `IDAM MIDI assertion in %s at line %d\n`
- `IDAM MIDI assertion return 0x%X in %s at line %d\n`
- `true`
- `com.apple.idamd`
- `site.AppleIDAMInterface`
- `OUT`
- `external`
- `/Library/Caches/com.apple.xbs/33C2ED7E-847A-4758-89A8-8CD4351472CC/TemporaryDirectory.XCcxY0/Sources/AppleIDAMInterface/Aspen/IDAM/AppleIDAMInterface/AppleIDAMInterface.cpp`
- `IDAM MIDI Streaming Interface`
- `false`
- `AppleIDAMInterface`
- `121111121222121211112`
- `IN`

**[__TEXT.__os_log]**

- `-> AppleIDAMInterface::CreateMIDIStreamingInterfaceDescriptor()\n`
- `   AppleIDAMInterface::CreateMIDIStreamingInterfaceDescriptor() - Couldn't create streaming buffer!\n`
- `<- AppleIDAMInterface::addCSMSInterfaceDescriptor()\n`
- `-> AppleIDAMInterface::addClassSpecificDescriptorsAsMIDI()\n`
- `   AppleIDAMInterface::CreateMIDIStreamingInterfaceDescriptor() - printing class-specific interface descriptor.\n`
- `-> AppleIDAMInterface::addEPDescriptors(0x%0X, assocJackID = %d)\n`
- `<- AppleIDAMInterface::addEPDescriptors()\n`
- `   AppleIDAMInterface::addClassSpecificDescriptorsAsMIDI() - creating bulk pipes.\n`
- `<- AppleIDAMInterface::addClassSpecificDescriptorsAsMIDI() = 0x%x\n`
- `<- AppleIDAMInterface::start() returning %s\n`
- `   AppleIDAMInterface::CreateMIDIStreamingInterfaceDescriptor() - adding class-specific descriptor to interface.\n`
- `<- AppleIDAMInterface::CreateMIDIStreamingInterfaceDescriptor()\n`
- `-> AppleIDAMInterface::addCSMSInterfaceDescriptor()\n`
- `   AppleIDAMInterface::addClassSpecificDescriptorsAsMIDI() - creating endpoint descriptors.\n`
- `-> AppleIDAMInterface::start()\n`
- `-> AppleIDAMInterface::addJackDescriptor(%s, %s, jackID = %d, sourceID = %d)\n`
- `<- AppleIDAMInterface::addJackDescriptor()\n`
