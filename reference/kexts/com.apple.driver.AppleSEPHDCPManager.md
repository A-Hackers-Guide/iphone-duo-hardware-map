# `com.apple.driver.AppleSEPHDCPManager`

- Name: AppleSEPHDCPManager
- Version: `1.0.1`
- UUID: `0AD81150-3C6B-3B17-A26F-414858092D1D`
- Source version: `111.0.0.0.0`
- Depends on: [`com.apple.driver.AppleSEPManager`](com.apple.driver.AppleSEPManager.md) 1.0.1, [`com.apple.driver.IOSlaveProcessor`](com.apple.driver.IOSlaveProcessor.md) 1.0.0, [`com.apple.iokit.IOHDCPFamily`](com.apple.iokit.IOHDCPFamily.md) 1.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleSEPHDCPManager
- `CFBundleIdentifier`: `com.apple.driver.AppleSEPHDCPManager`
- `IOClass`: `AppleSEPHDCPManager`
- `IONameMatch`: `sep-endpoint,hdcp`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSEPHDCPManager`
- `IOProviderClass`: `AppleSEPDeviceService`


## C++ classes (4) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleHDCPInterface` | 0xb8 | IOHDCPInterface → IOService → IORegistryEntry |
| `AppleHDCPManager` | 0xa8 | IOService → IORegistryEntry |
| `AppleSEPHDCPEndpoint` | 0xf0 | AppleSEPEndpoint → IOSlaveEndpoint → IOEventSource |
| `AppleSEPHDCPManager` | 0xa8 | AppleHDCPManager → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001425 off=0x00733a10-0x00734e35 addr=0xfffffe0007737a10-0xfffffe0007738e35 r--/r--   __TEXT            
	sz=0x00000876 off=0x00734038-0x007348ae addr=0xfffffe0007738038-0xfffffe00077388ae               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000587 off=0x007348ae-0x00734e35 addr=0xfffffe00077388ae-0xfffffe0007738e35               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00004a60 off=0x025d56a0-0x025da100 addr=0xfffffe00095d96a0-0xfffffe00095de100 r-x/r-x   __TEXT_EXEC       
	sz=0x00004840 off=0x025d56a0-0x025d9ee0 addr=0xfffffe00095d96a0-0xfffffe00095ddee0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000220 off=0x025d9ee0-0x025da100 addr=0xfffffe00095ddee0-0xfffffe00095de100          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000178 off=0x049956b0-0x04995828 addr=0xfffffe000b9996b0-0xfffffe000b999828 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049956b0-0x04995778 addr=0xfffffe000b9996b0-0xfffffe000b999778               __DATA.__data             
	sz=0x000000b0 off=0x00000000-0x000000b0 addr=0xfffffe000b999778-0xfffffe000b999828               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00001888 off=0x011e4a60-0x011e62e8 addr=0xfffffe00081e8a60-0xfffffe00081ea2e8 rw-/rw-   __DATA_CONST      
	sz=0x00000020 off=0x011e4a60-0x011e4a80 addr=0xfffffe00081e8a60-0xfffffe00081e8a80         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000020 off=0x011e4a80-0x011e4aa0 addr=0xfffffe00081e8a80-0xfffffe00081e8aa0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000015e0 off=0x011e4aa0-0x011e6080 addr=0xfffffe00081e8aa0-0xfffffe00081ea080         __DATA_CONST.__const            
	sz=0x00000100 off=0x011e6080-0x011e6180 addr=0xfffffe00081ea080-0xfffffe00081ea180         __DATA_CONST.__kalloc_type      
	sz=0x00000110 off=0x011e6180-0x011e6290 addr=0xfffffe00081ea180-0xfffffe00081ea290         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000058 off=0x011e6290-0x011e62e8 addr=0xfffffe00081ea290-0xfffffe00081ea2e8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 79 at 0x04ae4264
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     0AD81150-3C6B-3B17-A26F-414858092D1D
008: LC_SOURCE_VERSION           111.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab0060 size=0xe8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleSEPHDCPManager`
- `CFBundleIdentifier`: `com.apple.driver.AppleSEPHDCPManager`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleSEPHDCPManager`
- `CFBundleNumericVersion`: `16875520`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2016 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleSEPHDCPManager.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898247152`
- `_PrelinkExecutableRelativePath`: `AppleSEPHDCPManager`
- `_PrelinkExecutableSize`: `30853`
- `_PrelinkExecutableSourceAddr`: `-2198898247152`
- `_PrelinkKmodInfo`: `-2198828640592`

## Strings (121) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `retInterfaceMake`
- `No interface number provided\n`
- `site.AppleSEPHDCPManager`
- `121112111111211111112211112222`
- `\"Insufficient page size configuration\" @%s:%d`
- `reply endpoint %u result %u size %u data 0x%08x\n`
- `AppleHDCPManager@%p::start(provider %p)\n`
- `start failed\n`
- `HDCPChannel`
- `Error 0x%x making SEP request %d\n`
- `AppleHDCPManager`
- `site.AppleHDCPManager`
- `open interface failed, ret=0x%0x\n`
- `AppleSEPHDCPManager failed in super::start`
- `interface[%u] hdcp-fuse-mask=0x%x applied\n`
- `HDCPCapabilityMask`
- `Trying to match...\n`
- `Interface ID <%x> matched!\n`
- `waking on _pendingRequest\n`
- `121111121222121211122`
- `AppleHDCPManager requires valid endpoint to start`
- `AppleHDCPManager failed in super::start`
- `valNumInterfaces`
- `Unable to open interface\n`
- `Unable to free interface\n`
- `readCert`
- `consumeNewKm[%zu] = { %*D }\n`
- `launchInterfaces error - Returning 0x%08x\n`
- `AppleHDCPInterface`
- `HDCPInterface detaching\n`
- `prepareReceiveOOLBuffer failed, ret=0x%08x\n`
- `action`
- `signalForEndpointAvailabilty`
- `site.AppleHDCPInterface`
- `handleOpen`
- `matchPropertyTable`
- `No stored Km found for this receiver\n`
- `consumeNewKm`
- `launchInterfaces`
- `HDCPRole`
- `AppleSEPHDCPEndpoint`
- `waiting for availability failed, ret=0x%08x\n`
- `_pendingRequest=%p\n`
- `logic error: called with request == NULL\n`
- `interface[%u] = ch:%u, die:%u, mask:%x, handle:%p\n`
- `attach failed\n`
- `No specific channel data found\n`
- `handleRequestGated`
- `Timeout waiting for response from SEP (request %d)%s\n`
- `waitForEndpointAvailability`
- `sleeping on _pendingRequest\n`
- `retInterfaceInfo`
- `AppleSEPHDCPManager`
- `AppleSEPHDCPEndpoint.cpp`
- `HDCPTransport`
- `handleClose`
- `site.AppleSEPHDCPEndpoint`
- `request #%4lu token %016llx requestID %u\n`
- `request #%4lu ret=0x%08x\n`
- `DebugInfo`
- `Couldn't start launchInterfaces thread\n`
- `withOptions`
- `not inGate()?!\n`
- `; Response recovered!`
- `Unexpected error 0x%08x waiting for response from SEP (request %d)\n`
- `ignoring message received with no _pendingRequest: message=%p\n`
- `ret=0x%08x\n`
- `hdcp-fuse-mask`
- `init failed\n`
- `readCert[%zu] = { %*D }\n`
- `, `
- `prepareSendOOLBuffer failed, ret=0x%08x\n`
- `retNumInterfaces`
- `(None - Not Open)`
- `AppleSEPHDCPManager failed to get provider`
- `\"Unbalanced use count update attempt detected\\n\" @%s:%d`
- `start`
- `12111112122212121121222`
- `Unable to read fuses\n`
- `waking pending _pendingRequest\n`

**[__TEXT.__os_log]**

- `consumeNewKm[%zu] = { %*D }\n`
- `prepareReceiveOOLBuffer failed, ret=0x%08x\n`
- `not inGate()?!\n`
- `Error 0x%x making SEP request %d\n`
- `waiting for availability failed, ret=0x%08x\n`
- `request #%4lu token %016llx requestID %u\n`
- `prepareSendOOLBuffer failed, ret=0x%08x\n`
- `No stored Km found for this receiver\n`
- `waking pending _pendingRequest\n`
- `HDCPInterface detaching\n`
- `Unable to open interface\n`
- `Unable to read fuses\n`
- `No interface number provided\n`
- `_pendingRequest=%p\n`
- `AppleHDCPManager failed in super::start`
- `launchInterfaces error - Returning 0x%08x\n`
- `init failed\n`
- `Unable to free interface\n`
- `Trying to match...\n`
- `Interface ID <%x> matched!\n`
- `request #%4lu ret=0x%08x\n`
- `ignoring message received with no _pendingRequest: message=%p\n`
- `interface[%u] = ch:%u, die:%u, mask:%x, handle:%p\n`
- `No specific channel data found\n`
- `reply endpoint %u result %u size %u data 0x%08x\n`
- `interface[%u] hdcp-fuse-mask=0x%x applied\n`
- `attach failed\n`
- `Timeout waiting for response from SEP (request %d)%s\n`
- `Unexpected error 0x%08x waiting for response from SEP (request %d)\n`
- `waking on _pendingRequest\n`
- `logic error: called with request == NULL\n`
- `AppleHDCPManager@%p::start(provider %p)\n`
- `open interface failed, ret=0x%0x\n`
- `AppleSEPHDCPManager failed in super::start`
- `sleeping on _pendingRequest\n`
- `Couldn't start launchInterfaces thread\n`
- `AppleSEPHDCPManager failed to get provider`
- `ret=0x%08x\n`
- `AppleHDCPManager requires valid endpoint to start`
- `start failed\n`
- `readCert[%zu] = { %*D }\n`
