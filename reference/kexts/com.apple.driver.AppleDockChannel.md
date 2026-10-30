# `com.apple.driver.AppleDockChannel`

- Name: AppleDockChannel
- Version: `1`
- UUID: `BBE001DC-4893-3BD2-8382-9CB9AFBACEB3`
- Source version: `19.0.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleDockChannel
- `CFBundleIdentifier`: `com.apple.driver.AppleDockChannel`
- `IOClass`: `AppleDockChannel`
- `IONameMatch`: `dockchannel,t8002`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDockChannel`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleDockChannel` | 0x6278 | IOService → IORegistryEntry |
| `AppleDockChannelDevice` | 0x90 | IOService → IORegistryEntry |
| `AppleDockChannelUserClient` | 0xe8 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001b9b off=0x0042b180-0x0042cd1b addr=0xfffffe000742f180-0xfffffe0007430d1b r--/r--   __TEXT            
	sz=0x000015c3 off=0x0042b758-0x0042cd1b addr=0xfffffe000742f758-0xfffffe0007430d1b               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00002c9c off=0x01bc2930-0x01bc55cc addr=0xfffffe0008bc6930-0xfffffe0008bc95cc r-x/r-x   __TEXT_EXEC       
	sz=0x00002b1c off=0x01bc2930-0x01bc544c addr=0xfffffe0008bc6930-0xfffffe0008bc944c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000180 off=0x01bc544c-0x01bc55cc addr=0xfffffe0008bc944c-0xfffffe0008bc95cc          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000150 off=0x0493d6c0-0x0493d810 addr=0xfffffe000b9416c0-0xfffffe000b941810 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x0493d6c0-0x0493d788 addr=0xfffffe000b9416c0-0xfffffe000b941788               __DATA.__data             
	sz=0x00000088 off=0x00000000-0x00000088 addr=0xfffffe000b941788-0xfffffe000b941810               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000014e8 off=0x01062998-0x01063e80 addr=0xfffffe0008066998-0xfffffe0008067e80 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x01062998-0x010629a0 addr=0xfffffe0008066998-0xfffffe00080669a0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x010629a0-0x010629a8 addr=0xfffffe00080669a0-0xfffffe00080669a8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000012e8 off=0x010629a8-0x01063c90 addr=0xfffffe00080669a8-0xfffffe0008067c90         __DATA_CONST.__const            
	sz=0x000000c0 off=0x01063c90-0x01063d50 addr=0xfffffe0008067c90-0xfffffe0008067d50         __DATA_CONST.__kalloc_type      
	sz=0x000000c0 off=0x01063d50-0x01063e10 addr=0xfffffe0008067d50-0xfffffe0008067e10         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000070 off=0x01063e10-0x01063e80 addr=0xfffffe0008067e10-0xfffffe0008067e80         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 62 at 0x04ad7538
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     BBE001DC-4893-3BD2-8382-9CB9AFBACEB3
008: LC_SOURCE_VERSION           19.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9e0b0 size=0x78
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleDockChannel`
- `CFBundleIdentifier`: `com.apple.driver.AppleDockChannel`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleDockChannel`
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
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
  - `2`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleDockChannel.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901427840`
- `_PrelinkExecutableRelativePath`: `AppleDockChannel`
- `_PrelinkExecutableSize`: `24175`
- `_PrelinkExecutableSourceAddr`: `-2198901427840`
- `_PrelinkKmodInfo`: `-2198829001024`

## Strings (57) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `AppleDockChannel::%s: couldn't register filterInterruptEventSource\n`
- `AppleDockChannel::%s: dockchannel global register base is NULL\n`
- `AppleDockChannel::%s: dock data register base is NULL\n`
- `AppleDockChannel::%s: channel-name: %s, fifo-size: %dbytes, wstat-mask: %x, device-config-base %#lx device-data-base %#lx\n`
- `AppleDockChannel::%s: bytesToWrite is zero\n`
- `sFlush`
- `polling-mode`
- `AppleDockChannel::%s: super initWithTask failed\n`
- `AppleDockChannel::%s: failed to map memory descriptor\n`
- `AppleDockChannel::%s: failed to flush fifo %d: %#x\n`
- `AppleDockChannel`
- `AppleDockChannel::%s: Invalid channel-number\n`
- `12111112122212121111111111111`
- `channel-name`
- `site.AppleDockChannel`
- `start`
- `AppleDockChannel::%s: device config register base is NULL\n`
- `AppleDockChannel::%s: device data register base is NULL\n`
- `AppleDockChannel::%s: dock config register map is NULL\n`
- `channel-number`
- `AppleDockChannel::%s: failed to find channel number from device-tree node\n`
- `AppleDockChannel::%s: dockchannel global register map is NULL\n`
- `AppleDockChannel::%s: failed to create work-loop\n`
- `AppleDockChannel::%s: failed to find channel-name from device-tree node\n`
- `fifo-size`
- `site.AppleDockChannelDevice`
- `AppleDockChannel::%s: bytesToRead is zero\n`
- `AppleDockChannel::%s: Null pointer passed in as memory descriptor\n`
- `sWriteBytes`
- `dcRead`
- `dcWrite`
- `AppleDockChannelUserClient::start: provider is NULL\n`
- `IOUserClientClass`
- `AppleDockChannelUserClient`
- `AppleDockChannelUserClient::start: failed to start super class\n`
- `AppleDockChannel::%s: dock Agent AP register map is NULL\n`
- `AppleDockChannel::%s: failed to create memory descriptor\n`
- `_readBytesAsyncGated`
- `AppleDockChannel::%s: failed to find fifo size from device-tree node\n`
- `dock-wstat-mask`
- `site.AppleDockChannelUserClient`
- `initWithTask`
- `121111121222121211111111111111111111112112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `AppleDockChannelDevice`
- `AppleDockChannel::%s: Null pointer passed in as bytesRead\n`
- `AppleDockChannel::%s: sizeof(_channelName) 0x%lx < device tree property size \"channel-name\" 0x%x\n`
- `AppleDockChannel::%s: Asynchronous read called while a read is already underway\n`
- `AppleDockChannel::%s: device data register map is NULL\n`
- `AppleDockChannel::%s: dock data register map is NULL\n`
- `dcReadAsync`
- `sReadBytes`
- `AppleDockChannel::%s: dock Agent AP register base is NULL\n`
- `AppleDockChannel::%s: device config register map is NULL\n`
- `AppleDockChannel::%s: failed to create command-gate\n`
- `121111121222121211`
- `AppleDockChannel::%s: Null pointer passed in as bytesWritten\n`
- `AppleDockChannel::%s: dock config register base is NULL\n`
