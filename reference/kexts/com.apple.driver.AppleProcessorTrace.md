# `com.apple.driver.AppleProcessorTrace`

- Name: AppleProcessorTrace
- Version: `1.0.0`
- UUID: `2A69DEEF-3203-3D10-89B6-920D63BA6378`
- Source version: `130.40.7.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 22.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/apple-processor-trace`](../devicetree/root__arm-io__apple-processor-trace.md) | `AppleProcessorTraceT8160` | `apple-processor-trace,t8160` |

## IOKit personalities (23) [KC]

### AppleProcessorTraceBringUp
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `IOClass`: `AppleProcessorTraceBringUp`
- `IONameMatch`: `apple-processor-trace,bring-up`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProcessorTrace`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformSleepAction`: `1000`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleProcessorTraceT6000
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `IOClass`: `AppleProcessorTraceT6000`
- `IONameMatch`: `apple-processor-trace,t6000`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProcessorTrace`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformSleepAction`: `1000`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleProcessorTraceT6020
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `IOClass`: `AppleProcessorTraceT6020`
- `IONameMatch`: `apple-processor-trace,t6020`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProcessorTrace`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformSleepAction`: `1000`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleProcessorTraceT6030
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `IOClass`: `AppleProcessorTraceT6030`
- `IONameMatch`: `apple-processor-trace,t6030`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProcessorTrace`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformSleepAction`: `1000`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleProcessorTraceT6031
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `IOClass`: `AppleProcessorTraceT6031`
- `IONameMatch`: `apple-processor-trace,t6031`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProcessorTrace`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformSleepAction`: `1000`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleProcessorTraceT6040
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `IOClass`: `AppleProcessorTraceT6040`
- `IONameMatch`: `apple-processor-trace,t6040`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProcessorTrace`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformSleepAction`: `1000`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleProcessorTraceT6041
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `IOClass`: `AppleProcessorTraceT6040`
- `IONameMatch`: `apple-processor-trace,t6040`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProcessorTrace`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformSleepAction`: `1000`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleProcessorTraceT6050
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `IOClass`: `AppleProcessorTraceT6050`
- `IONameMatch`: `apple-processor-trace,t6050`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProcessorTrace`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformSleepAction`: `1000`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleProcessorTraceT8101
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `IOClass`: `AppleProcessorTraceT8101`
- `IONameMatch`: `apple-processor-trace,t8101`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProcessorTrace`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformSleepAction`: `1000`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleProcessorTraceT8103
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `IOClass`: `AppleProcessorTraceT8103`
- `IONameMatch`: `apple-processor-trace,t8103`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProcessorTrace`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformSleepAction`: `1000`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleProcessorTraceT8110
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `IOClass`: `AppleProcessorTraceT8110`
- `IONameMatch`: `apple-processor-trace,t8110`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProcessorTrace`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformSleepAction`: `1000`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleProcessorTraceT8112
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `IOClass`: `AppleProcessorTraceT8112`
- `IONameMatch`: `apple-processor-trace,t8112`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProcessorTrace`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformSleepAction`: `1000`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleProcessorTraceT8120
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `IOClass`: `AppleProcessorTraceT8120`
- `IONameMatch`: `apple-processor-trace,t8120`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProcessorTrace`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformSleepAction`: `1000`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleProcessorTraceT8122
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `IOClass`: `AppleProcessorTraceT8122`
- `IONameMatch`: `apple-processor-trace,t8122`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProcessorTrace`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformSleepAction`: `1000`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleProcessorTraceT8130
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `IOClass`: `AppleProcessorTraceT8130`
- `IONameMatch`: `apple-processor-trace,t8130`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProcessorTrace`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformSleepAction`: `1000`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleProcessorTraceT8132
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `IOClass`: `AppleProcessorTraceT8132`
- `IONameMatch`: `apple-processor-trace,t8132`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProcessorTrace`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformSleepAction`: `1000`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleProcessorTraceT8140
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `IOClass`: `AppleProcessorTraceT8140`
- `IONameMatch`: `apple-processor-trace,t8140`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProcessorTrace`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformSleepAction`: `1000`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleProcessorTraceT8142
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `IOClass`: `AppleProcessorTraceT8142`
- `IONameMatch`: `apple-processor-trace,t8142`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProcessorTrace`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformSleepAction`: `1000`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleProcessorTraceT8150
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `IOClass`: `AppleProcessorTraceT8150`
- `IONameMatch`: `apple-processor-trace,t8150`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProcessorTrace`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformSleepAction`: `1000`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleProcessorTraceT8152
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `IOClass`: `AppleProcessorTraceT8152`
- `IONameMatch`: `apple-processor-trace,t8152`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProcessorTrace`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformSleepAction`: `1000`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleProcessorTraceT8160
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `IOClass`: `AppleProcessorTraceT8160`
- `IONameMatch`: `apple-processor-trace,t8160`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProcessorTrace`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformSleepAction`: `1000`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleProcessorTraceT8310
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `IOClass`: `AppleProcessorTraceT8310`
- `IONameMatch`: `apple-processor-trace,t8310`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProcessorTrace`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformSleepAction`: `1000`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`

### AppleProcessorTraceT8320
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `IOClass`: `AppleProcessorTraceT8320`
- `IONameMatch`: `apple-processor-trace,t8320`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProcessorTrace`
- `IOPlatformPanicAction`: `1000`
- `IOPlatformSleepAction`: `1000`
- `IOPlatformWakeAction`: `1000`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (29) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleProcessorTrace` | 0xd8 | IOService → IORegistryEntry |
| `AppleProcessorTraceBringUp` | 0xd8 | AppleProcessorTrace → IOService → IORegistryEntry |
| `AppleProcessorTraceEventSource` | 0x58 | IOEventSource |
| `AppleProcessorTraceFracturedMemoryMap` | 0x28 |  |
| `AppleProcessorTraceNub` | 0x90 | IOService → IORegistryEntry |
| `AppleProcessorTraceSession` | 0x160 |  |
| `AppleProcessorTraceT6000` | 0x288 | AppleProcessorTrace → IOService → IORegistryEntry |
| `AppleProcessorTraceT6020` | 0x288 | AppleProcessorTrace → IOService → IORegistryEntry |
| `AppleProcessorTraceT6030` | 0x168 | AppleProcessorTrace → IOService → IORegistryEntry |
| `AppleProcessorTraceT6031` | 0x288 | AppleProcessorTrace → IOService → IORegistryEntry |
| `AppleProcessorTraceT6040` | 0x3a8 | AppleProcessorTrace → IOService → IORegistryEntry |
| `AppleProcessorTraceT6050` | 0x708 | AppleProcessorTrace → IOService → IORegistryEntry |
| `AppleProcessorTraceT8101` | 0x168 | AppleProcessorTrace → IOService → IORegistryEntry |
| `AppleProcessorTraceT8103` | 0x168 | AppleProcessorTrace → IOService → IORegistryEntry |
| `AppleProcessorTraceT8110` | 0x168 | AppleProcessorTrace → IOService → IORegistryEntry |
| `AppleProcessorTraceT8112` | 0x168 | AppleProcessorTrace → IOService → IORegistryEntry |
| `AppleProcessorTraceT8120` | 0x168 | AppleProcessorTrace → IOService → IORegistryEntry |
| `AppleProcessorTraceT8122` | 0x168 | AppleProcessorTrace → IOService → IORegistryEntry |
| `AppleProcessorTraceT8130` | 0x168 | AppleProcessorTrace → IOService → IORegistryEntry |
| `AppleProcessorTraceT8132` | 0x2b8 | AppleProcessorTrace → IOService → IORegistryEntry |
| `AppleProcessorTraceT8140` | 0x2b8 | AppleProcessorTrace → IOService → IORegistryEntry |
| `AppleProcessorTraceT8142` | 0x2e8 | AppleProcessorTrace → IOService → IORegistryEntry |
| `AppleProcessorTraceT8150` | 0x2e8 | AppleProcessorTrace → IOService → IORegistryEntry |
| `AppleProcessorTraceT8152` | 0x2e8 | AppleProcessorTrace → IOService → IORegistryEntry |
| `AppleProcessorTraceT8160` | 0x2e8 | AppleProcessorTrace → IOService → IORegistryEntry |
| `AppleProcessorTraceT8310` | 0x120 | AppleProcessorTrace → IOService → IORegistryEntry |
| `AppleProcessorTraceT8320` | 0x1e0 | AppleProcessorTrace → IOService → IORegistryEntry |
| `AppleProcessorTraceUserClient` | 0x100 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |
| `AppleProcessorTraceVirtualBufferMemoryDescriptor` | 0xc0 | IOGeneralMemoryDescriptor → IOMemoryDescriptor |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, WeakDefines, BindsToWeak, DylibInCache
000: LC_SEGMENT_64 sz=0x00007ae0 off=0x006c8be0-0x006d06c0 addr=0xfffffe00076ccbe0-0xfffffe00076d46c0 r--/r--   __TEXT            
	sz=0x00001993 off=0x006c92f8-0x006cac8b addr=0xfffffe00076cd2f8-0xfffffe00076cec8b               __TEXT.__os_log           
	sz=0x000000a8 off=0x006cac90-0x006cad38 addr=0xfffffe00076cec90-0xfffffe00076ced38               __TEXT.__const            
	sz=0x00005988 off=0x006cad38-0x006d06c0 addr=0xfffffe00076ced38-0xfffffe00076d46c0               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x0003c3fc off=0x0242ef10-0x0246b30c addr=0xfffffe0009432f10-0xfffffe000946f30c r-x/r-x   __TEXT_EXEC       
	sz=0x0003bc9c off=0x0242ef10-0x0246abac addr=0xfffffe0009432f10-0xfffffe000946ebac          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000760 off=0x0246abac-0x0246b30c addr=0xfffffe000946ebac-0xfffffe000946f30c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000828 off=0x0498f1d8-0x0498fa00 addr=0xfffffe000b9931d8-0xfffffe000b993a00 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x0498f1d8-0x0498f29c addr=0xfffffe000b9931d8-0xfffffe000b99329c               __DATA.__data             
	sz=0x00000760 off=0x00000000-0x00000760 addr=0xfffffe000b9932a0-0xfffffe000b993a00               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x0000c120 off=0x011b1c50-0x011bdd70 addr=0xfffffe00081b5c50-0xfffffe00081c1d70 rw-/rw-   __DATA_CONST      
	sz=0x000000e8 off=0x011b1c50-0x011b1d38 addr=0xfffffe00081b5c50-0xfffffe00081b5d38         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x000000e8 off=0x011b1d38-0x011b1e20 addr=0xfffffe00081b5d38-0xfffffe00081b5e20         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x0000b1c8 off=0x011b1e20-0x011bcfe8 addr=0xfffffe00081b5e20-0xfffffe00081c0fe8         __DATA_CONST.__const            
	sz=0x000000b0 off=0x011bcfe8-0x011bd098 addr=0xfffffe00081c0fe8-0xfffffe00081c1098         __DATA_CONST.__weak_auth_got    (NonLazySymbolPointers)
	sz=0x00000740 off=0x011bd098-0x011bd7d8 addr=0xfffffe00081c1098-0xfffffe00081c17d8         __DATA_CONST.__kalloc_type      
	sz=0x000001e0 off=0x011bd7d8-0x011bd9b8 addr=0xfffffe00081c17d8-0xfffffe00081c19b8         __DATA_CONST.__kalloc_var       
	sz=0x00000300 off=0x011bd9b8-0x011bdcb8 addr=0xfffffe00081c19b8-0xfffffe00081c1cb8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000b8 off=0x011bdcb8-0x011bdd70 addr=0xfffffe00081c1cb8-0xfffffe00081c1d70         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 259 at 0x04ae2dbc
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     2A69DEEF-3203-3D10-89B6-920D63BA6378
008: LC_SOURCE_VERSION           130.40.7.0.0
009: LC_FUNCTION_STARTS          offset=0x004aae320 size=0x700
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleProcessorTrace`
- `CFBundleIdentifier`: `com.apple.driver.AppleProcessorTrace`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleProcessorTrace`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2023 Apple Inc. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleProcessorTrace.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898684960`
- `_PrelinkExecutableRelativePath`: `AppleProcessorTrace`
- `_PrelinkExecutableSize`: `329764`
- `_PrelinkExecutableSourceAddr`: `-2198898684960`
- `_PrelinkKmodInfo`: `-2198828666408`

## Strings (521) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__os_log]**

- `AppleProcessorTrace::unmapBufferVA unlock\n`
- `AppleProcessorTraceSession::enableTracingForTask()\n`
- `AppleProcessorTraceUserClient::externalMethodConfigure\n`
- `%s: failed to allocate OSNumber for size=%llu\n`
- `AppleProcessorTrace::resumeTracingGated\n`
- `AppleProcessorTrace::validateConfig(buffer_phys=0x%llX, buffer_size=0x%llX)\n`
- `AppleProcessorTrace::start\n`
- `AppleProcessorTrace::enterSleep\n`
- `AppleProcessorTraceSession::initChunk(%u / %lu, 0x%llX, 0x%llX)\n`
- `%s: failed to create IODTNVRAM matching dictionary\n`
- `AppleProcessorTrace::mapBufferPA\n`
- `AppleProcessorTraceUserClient::clientClose\n`
- `AppleProcessorTraceUserClient::externalMethodAttach\n`
- `AppleProcessorTrace::publishNubs\n`
- `%s: apt-carveout-size-mb property not found\n`
- `%s: found apt-carveout-size-mb=%u MB from DT\n`
- `AppleProcessorTrace::mapBufferVA\n`
- `AppleProcessorTrace::mapBufferVA : mapping failed.\n`
- `AppleProcessorTrace::VATraceBufferMap unwire\n`
- `AppleProcessorTraceUserClient::start\n`
- `AppleProcessorTrace::allocateTraceBuffers\n`
- `AppleProcessorTrace::allocateDevTraceBuffer(reuseProdTraceBuffer=%u)\n`
- `AppleProcessorTrace::releaseChunkGated(idx=%u, id=%llu, offset=0x%llX, size=0x%llX, checksum=%llX, fill_size=0x%llX, fill_wrap=%u, cluster_id=%u)\n`
- `AppleProcessorTrace::validateConfig(stream_chunk_size=0x%llX, advisory_min_free_chunks=%u)\n`
- `AppleProcessorTrace::mapBufferVA : allocation failed.\n`
- `AppleProcessorTrace::getBufferVA\n`
- `AppleProcessorTraceUserClient::registerNotificationPort(%u)\n`
- `AppleProcessorTraceUserClient::interruptSession\n`
- `AppleProcessorTrace::buffer size %lx\n`
- `AppleProcessorTraceSession::sendThrottleAdvisory(%{public}X)\n`
- `AppleProcessorTraceUserClient::externalMethodRequestBuffer\n`
- `AppleProcessorTrace::pauseTracingGated\n`
- `AppleProcessorTrace::prepareForPanicTrace\n`
- `AppleProcessorTrace::unmapBufferPA\n`
- `AppleProcessorTrace::mapBufferVA : reset.\n`
- `AppleProcessorTraceUserClient::externalMethodPause\n`
- `AppleProcessorTraceUserClient::externalMethodUnconfigure\n`
- `AppleProcessorTraceSession::configured\n`
- `AppleProcessorTrace::sptm init\n`
- `AppleProcessorTrace::cores config\n`
- `AppleProcessorTraceUserClient::externalMethodAddTask\n`
- `AppleProcessorTrace::validateConfig:%u: fail condition '{public}%s' met.\n`
- `AppleProcessorTrace::allocateProdTraceBuffer\n`
- `AppleProcessorTrace::configureGated\n`
- `AppleProcessorTrace::startTracingOnClustersGated(%p)\n`
- `AppleProcessorTrace::apt_unregister_callback\n`
- `AppleProcessorTrace::unconfigureGated\n`
- `AppleProcessorTrace::validateConfig(panic_trace=%u)\n`
- `AppleProcessorTrace::mapBufferVA : mapped.\n`
- `AppleProcessorTraceSession::withConfig\n`
- `AppleProcessorTrace::stopTracingOnClustersGated\n`
- `%s: property not found or invalid type\n`
- `AppleProcessorTrace::mapBufferVA : wire.\n`
- `AppleProcessorTrace::VATraceBufferMap del\n`
- `AppleProcessorTraceSession::init\n`
- `AppleProcessorTraceSession::sendThrottleAdvisory failed %{public}X\n`
- `AppleProcessorTraceUserClient::externalMethodResume\n`
- `AppleProcessorTrace::reset\n`
- `AppleProcessorTrace::attachGated\n`
- `%s: failed to set property to size=%llu\n`
- `%s: failed to find /chosen node\n`
- `AppleProcessorTraceSession::drainDirtyChunk(idx=%u, id=%llu, offset=0x%llX, size=0x%llX, checksum=0x%llX, fill_size=0x%llX, fill_wrap=%u, cluster_id=%u)\n`
- `AppleProcessorTraceUserClient::externalMethodGetSystemMetadata\n`
- `AppleProcessorTrace::stop\n`
- `AppleProcessorTrace::clusters config\n`
- `%s: resume tracing`
- `AppleProcessorTrace::done\n`
- `AppleProcessorTrace::validateConfig(disabled_exception_levels=[%llu, %llu, %llu, %llu, %llu, %llu]\n`
- `AppleProcessorTrace::VA Done\n`
- `AppleProcessorTrace::unmapBufferVA\n`
- `AppleProcessorTraceUserClient::externalMethodStop\n`
- `%s: state=%d`
- `AppleProcessorTrace::startTracingGated: failed to register callback: %d\n`
- `AppleProcessorTrace::starting to trace\n`
- `AppleProcessorTrace::startPanicTrace\n`
- `%s: apt-carveout-size-mb property has invalid size (expected %zu, got %u)\n`
- `AppleProcessorTrace::mapBufferVA : allocated.\n`
- `AppleProcessorTraceUserClient::initWithTask\n`
- `AppleProcessorTraceUserClient::externalMethodReleaseChunk\n`
- `AppleProcessorTrace::startTracingGated(%p)\n`
- `%s: failed to allocate NVRAM key symbol\n`
- `AppleProcessorTraceSession::free\n`
- `AppleProcessorTrace::requestBuffer: size=%llx\n`
- `AppleProcessorTrace::enterWake\n`
- `AppleProcessorTrace::stopTracingGated\n`
- `AppleProcessorTrace::unconfiguredGated\n`
- `AppleProcessorTrace::validateConfig(version=%u.%u, session_type=%u, trace_mode=%u, prod=%s)\n`
- `AppleProcessorTraceSession::init: minFreeChunks = %zu (for throttling)\n`
- `AppleProcessorTraceUserClient::clientMemoryForType(%u)\n`
- `AppleProcessorTraceUserClient::externalMethodStart\n`
- `AppleProcessorTrace::addTaskGated(read_port=%u)\n`
- `AppleProcessorTrace::validateConfig(read_port=%u, task_filtering=%u)\n`
- `%s: failed to find IODTNVRAM service\n`
- `AppleProcessorTrace::VATraceBufferMap : locking\n`

**[__TEXT.__cstring]**

- `virtual void AppleProcessorTraceT8120::stopTracingOnCluster(bool)`
- `virtual void AppleProcessorTraceT8310::unconfigureCluster(bool)`
- `site.AppleProcessorTraceT8130`
- `AppleProcessorTraceUtils.hpp`
- `virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8132::getChunkForCluster(unsigned int, uint64_t)`
- `IOReturn AppleProcessorTrace::attachToSessionGated(MethodAttachArgs, OSSharedPtr<AppleProcessorTraceSession> &, AppleProcessorTraceUserClient *)`
- `virtual bool AppleProcessorTraceT6020::getTracePowerStateForCluster(bool)`
- `virtual void AppleProcessorTraceT8120::refeatureCore(bool)`
- `void AppleProcessorTraceSession::sendThrottleAdvisory(TaskState)`
- `222222221`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodResume(OSObject *, void *, IOExternalMethodArguments *)`
- `bool AppleProcessorTrace::validateConfig(const MethodConfigArgs)`
- `config.buffer_size < getClusters().size() * minimumChunkSize`
- `virtual void AppleProcessorTraceT6031::unconfigureCore(bool)`
- `uint64_t AppleProcessorTraceT8152::apt_msr_ro_ctl_read(ml_topology_cpu_t, uint8_t)`
- `virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8152::getChunkForCluster(unsigned int, uint64_t)`
- `AppleProcessorTraceT8320`
- `site.AppleProcessorTraceT8320`
- `virtual void AppleProcessorTraceT8103::refeatureCore(bool)`
- `void AppleProcessorTrace::startTracingOnTraceableCores()`
- `(config.buffer_size & ((128 << 10) - 1)) != 0`
- `config.buffer_size < getRecommendedCarveoutSizeInBytes()`
- `chosen`
- `virtual void AppleProcessorTraceT6031::unconfigureCluster(bool)`
- `virtual bool AppleProcessorTraceT6030::getTracePowerStateForCluster(bool)`
- `virtual void AppleProcessorTraceT8122::defeatureCore(bool)`
- `AppleProcessorTraceT8101`
- `virtual bool AppleProcessorTraceT8110::getTracePowerStateForCluster(bool)`
- `IOReturn AppleProcessorTrace::reset(OSSharedPtr<AppleProcessorTraceSession>)_block_invoke`
- `false`
- `config.trace_mode == TraceMode::CIO_Infinite && !caps.CIO`
- `AppleProcessorTraceEventSource`
- `site.AppleProcessorTraceUserClient`
- `AppleProcessorTraceT8140`
- `AppleProcessorTraceT8310`
- `ProductionTrace`
- `\"DRAM_Infinite is not supported\" @%s:%d`
- `config.ld_st_trace && config.prod`
- `virtual void AppleProcessorTraceT6031::refeatureCore(bool)`
- `page_vaddr == (sptm_vaddr_t)start_va`
- `uint64_t AppleProcessorTraceT8140::apt_msr_ro_ctl_read(ml_topology_cpu_t, uint8_t)`
- `AppleProcessorTraceT8103`
- `virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT6040::getChunkForCluster(unsigned int, uint64_t)`
- `AllocatedBufferSize`
- `121111121222121211111112112211211211211211211211211211211211211211211211211211211`
- `void AppleProcessorTraceT8142::apt_msr_ro_ctl_write(ml_topology_cpu_t, uint8_t, uint64_t)`
- `expectState(DriverState::Tracing)`
- `guard.acquired()`
- `bounded_ptr<T>::operator+=(n): Calculating the number of bytes to add to the offset (n * sizeof(T)) would trigger an overflow`
- `void IOVector<task_apt_token *>::resize() [T = task_apt_token *]`
- `pauseTracingGated(session) == kIOReturnSuccess`
- `IOReturn AppleProcessorTrace::configureGated(MethodConfigArgs, OSSharedPtr<AppleProcessorTraceSession> &, AppleProcessorTraceUserClient *)`
- `void AppleProcessorTrace::eventSourceHandler()`
- `bool AppleProcessorTraceSession::init(const MethodConfigArgs, OSSharedPtr<AppleProcessorTraceEventSource>)`
- `virtual IOReturn AppleProcessorTraceUserClient::registerNotificationPort(mach_port_t, UInt32, UInt32)`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodConfigure(OSObject *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodStart(OSObject *, void *, IOExternalMethodArguments *)`
- `AppleProcessorTraceT8130`
- `config.buffer_size / chunkSizeForConfig(config) <= UINT32_MAX`
- `AppleProcessorTraceT8152`
- `virtual void AppleProcessorTraceT8101::unconfigureCluster(bool)`
- `virtual void AppleProcessorTraceT8160::defeatureCore(bool)`
- `config.buffer_size > vm_map_kernel_max_simple_mappable_size()`
- `AppleProcessorTraceFracturedMemoryMap`
- `AppleProcessorTraceSession`
- `12122111121121222222222222221122111212112111`
- `chunkEventSource->getWorkLoop()->inGate()`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodReleaseChunk(OSObject *, void *, IOExternalMethodArguments *)`
- `AppleProcessorTraceBringUp`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `DevelopmentTrace`
- `startTracingOnClustersGated`
- `getWorkLoop()->inGate()`
- `1112`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodPause(OSObject *, void *, IOExternalMethodArguments *)`
- `virtual void AppleProcessorTraceT8103::defeatureCore(bool)`
- `AppleProcessorTrace.cpp`
- `site.AppleProcessorTraceT8150`
- `121111121222121211111112112211211211211211211`
- `virtual void AppleProcessorTraceT8122::refeatureCore(bool)`
- `IOUserClientDefaultLockingSetProperties`
- `virtual void AppleProcessorTraceT8152::defeatureCore(bool)`
- `site.AppleProcessorTraceT8112`
- `virtual void AppleProcessorTraceT8130::refeatureCore(bool)`
- `unconfigureGated(session) == kIOReturnSuccess`
- `virtual void AppleProcessorTraceT8112::defeatureCore(bool)`
- `virtual void AppleProcessorTraceT8101::unconfigureCore(bool)`
- `virtual void AppleProcessorTraceT8150::defeatureCore(bool)`
- `uint64_t AppleProcessorTraceT8160::apt_msr_ro_ctl_read(ml_topology_cpu_t, uint8_t)`
- `uint64_t AppleProcessorTraceT8142::apt_msr_ro_ctl_read(ml_topology_cpu_t, uint8_t)`
- `stopTracingGated(session) == kIOReturnSuccess`
- `ml_get_interrupts_enabled() == true`
- `\"'arm-io' EDT node not found.\" @%s:%d`
- `virtual void AppleProcessorTraceT6020::platformStopTracingOnCore(bool)`
- `virtual void AppleProcessorTraceT8310::unconfigureCore(bool)`
- `virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8160::getChunkForCluster(unsigned int, uint64_t)`
- `!_activeSession`
- `virtual void AppleProcessorTraceT6020::stopTracingOnCluster(bool)`
- `dsc`
- `B16@?0^{OSObject=^^?i}8`
- `121111121222121211111112112211211211`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `AppleProcessorTraceACC7Src.hpp`
- `apt_carveout_mb`
- `void AppleProcessorTrace::setState(DriverState)`
- `expectState(DriverState::Sleeping)`
- `void AppleProcessorTrace::traceRegionDeinit()`
- `void AppleProcessorTraceSession::unmapBufferVA()`
- `void IOVector<task_apt_token *>::push_back(const T &) [T = task_apt_token *]`
- `AppleProcessorTraceACC8Src.hpp`
- `AppleProcessorTraceT6000`
- `uint32_t getCarveoutSizeFromDeviceTree()`
- `12111211112`
- `void AppleProcessorTraceSession::enqueueDirtyChunk(Chunk *)`
- `data`
- `virtual void AppleProcessorTraceT6050::defeatureCore(bool)`
- `virtual void AppleProcessorTraceT8112::platformStopTracingOnCore(bool)`
- `_devFused`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `AppleProcessorTraceT6040`
- `virtual void AppleProcessorTraceT8132::defeatureCore(bool)`
- `virtual void AppleProcessorTraceT8142::defeatureCore(bool)`
- `IOReturn AppleProcessorTrace::pauseTracingGated(OSSharedPtr<AppleProcessorTraceSession>)`
- `virtual void AppleProcessorTraceT6030::platformStopTracingOnCore(bool)`
- `buffer_size`
- `LoadStoreTrace`
- `expectState(DriverState::Tracing) || expectState(DriverState::Paused)`
- `IOReturn AppleProcessorTrace::stopTracingGated(OSSharedPtr<AppleProcessorTraceSession>)`
- `virtual void AppleProcessorTraceT6020::refeatureCore(bool)`
- `start_va == (volatile const char *)VATraceBufferMap->getVirtualAddress()`
- `buffer_size == VATraceBufferMap->getLength()`
- `site.AppleProcessorTraceT8122`
- `virtual void AppleProcessorTraceT8101::platformStopTracingOnCore(bool)`
- `site.AppleProcessorTraceT8142`
- `IOReturn AppleProcessorTrace::unconfigureGated(OSSharedPtr<AppleProcessorTraceSession>)`
- `virtual IOReturn AppleProcessorTraceUserClient::clientClose()`
- `void AppleProcessorTraceUserClient::interruptSession()`
- `site.AppleProcessorTraceT8310`
- `site.AppleProcessorTraceT8152`
- `site.AppleProcessorTraceT6000`
- `!caps.Streaming`
- `reg`
- `site.AppleProcessorTraceVirtualBufferMemoryDescriptor`
- `virtual void AppleProcessorTraceT6031::platformStopTracingOnCore(bool)`
- `virtual void AppleProcessorTraceT6030::stopTracingOnCluster(bool)`
- `!va_region_locked`
- `virtual void AppleProcessorTraceSession::free()`
- `AppleProcessorTraceACC8_9_10Src.hpp`
- `\"CIO_Infinite is not supported\" @%s:%d`
- `site.AppleProcessorTraceT6040`
- `site.AppleProcessorTraceT8110`
- `IOReturn AppleProcessorTrace::releaseChunkGated(OSSharedPtr<AppleProcessorTraceSession>, ChunkData)`
- `void AppleProcessorTrace::traceRegionInit()`
- `site.AppleProcessorTraceT8120`
- `va_region_locked`
- `virtual void AppleProcessorTraceT8110::unconfigureCluster(bool)`
- `IOReturn AppleProcessorTrace::requestBuffer(uint64_t)`
- `void AppleProcessorTrace::startTracingOnClustersGated(DriverState)`
- `void AppleProcessorTrace::enterWake()`
- `bool isClusterLeader()`
- `VATraceBufferMap`
- `newCapacity > capacity`
- `IOUserClientDefaultLocking`
- `virtual bool AppleProcessorTrace::start(IOService *)`
- `config.buffer_size < (16 << 20)`
- `config.ld_st_trace && !caps.LdStTrace`
- `void AppleProcessorTraceSession::unlockBufferVA()`
- `void AppleProcessorTraceSession::transferFilledFreeChunksToDirtyQueue()`
- `virtual bool AppleProcessorTraceT8122::getTracePowerStateForCluster(bool)`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodRequestBuffer(OSObject *, void *, IOExternalMethodArguments *)`
- `inArg->scalarInputCount == 1`
- `ml_get_topology_info()->version == CPU_TOPOLOGY_VERSION`
- `name`
- `pmgr`
- `chunk != getOverflowChunk()`
- `virtual void AppleProcessorTraceT8122::platformStopTracingOnCore(bool)`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodRequestBuffer(OSObject *, void *, IOExternalMethodArguments *)_block_invoke`
- `virtual void AppleProcessorTraceT8112::unconfigureCluster(bool)`
- `virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8320::getChunkForCluster(unsigned int, uint64_t)`
- `AppleProcessorTraceT8150`
- `virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8142::getChunkForCluster(unsigned int, uint64_t)`
- `config.stream_chunk_size < minimumChunkSize`
- `getOrSetCarveoutSizeInMBProperty`
- `virtual void AppleProcessorTraceT6031::stopTracingOnCluster(bool)`
- `VATraceBuffer == nullptr`
- `virtual bool AppleProcessorTraceUserClient::start(IOService *)`
- `void AppleProcessorTraceT8152::apt_msr_ro_ctl_write(ml_topology_cpu_t, uint8_t, uint64_t)`
- `virtual void AppleProcessorTraceT6031::defeatureCore(bool)`
- `site.AppleProcessorTraceT6050`
- `AppleProcessorTraceT8112`
- `virtual void AppleProcessorTraceT8130::unconfigureCore(bool)`
- `virtual void AppleProcessorTraceT8103::unconfigureCluster(bool)`
- `virtual void AppleProcessorTraceT8103::unconfigureCore(bool)`
- `virtual void AppleProcessorTraceT8103::stopTracingOnCluster(bool)`
- `virtual void AppleProcessorTraceT8103::platformStopTracingOnCore(bool)`
- `virtual void AppleProcessorTraceT6040::defeatureCore(bool)`
- `AppleProcessorTraceT8160`
- `virtual void AppleProcessorTraceT6000::stopTracingOnCluster(bool)`
- `IOVector.hpp`
- `data && size < capacity`
- `void AppleProcessorTraceT8140::apt_msr_ro_ctl_write(ml_topology_cpu_t, uint8_t, uint64_t)`
- `site.AppleProcessorTraceT8101`
- `virtual void AppleProcessorTraceT8110::stopTracingOnCluster(bool)`
- `IODeviceMappedMemory.hpp`
- `uint64_t AppleProcessorTraceT6040::apt_msr_ro_ctl_read(ml_topology_cpu_t, uint8_t)`
- `!prod`
- `is_va`
- `site.AppleProcessorTraceT8140`
- `site.AppleProcessorTraceT8103`
- `virtual void AppleProcessorTraceT8101::defeatureCore(bool)`
- `ml_get_interrupts_enabled() == false`
- `VersionMajor`
- `DevelopmentTraceSWMessages`
- `void AppleProcessorTrace::setTraceChunksClusterGated()`
- `virtual bool AppleProcessorTraceT8120::getTracePowerStateForCluster(bool)`
- `site.AppleProcessorTraceFracturedMemoryMap`
- `1`
- `newData`
- `AppleProcessorTraceT8142`
- `config.version_major != VersionMajor`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodAttach(OSObject *, void *, IOExternalMethodArguments *)`
- `virtual void AppleProcessorTraceT8310::stopTracingOnCluster(bool)`
- `virtual void AppleProcessorTraceT8112::refeatureCore(bool)`
- `uint64_t AppleProcessorTraceT8320::apt_msr_ro_ctl_read(ml_topology_cpu_t, uint8_t)`
- `i8@?0`
- `SessionUUID`
- `!isExceptionLevelDisabled(config, ExceptionLevel::GL0)`
- `!(config.read_port || config.task_filtering) && config.prod`
- `ranges`
- `uint64_t AppleProcessorTraceT8132::apt_msr_ro_ctl_read(ml_topology_cpu_t, uint8_t)`
- `(!config.buffer_phys) && (!caps.ProdTraceVA)`
- `site.AppleProcessorTraceSession`
- `OSSharedPtr<IOMemoryDescriptor> AppleProcessorTraceSession::getBufferVA()`
- `void AppleProcessorTraceSession::setChunkForCluster(ml_topology_cluster_t, unsigned int, Chunk *)`
- `VersionMinor`
- `virtual void AppleProcessorTraceT8110::platformStopTracingOnCore(bool)`
- `(!isExceptionLevelDisabled(config, ExceptionLevel::EL2)) && (!caps.ProdTraceEL2)`
- `config.delay_posting_chunk_fills`
- `40A0DDD2-77F8-4392-B4A3-1E7304206516:apt-carveout-size-mb`
- `virtual void AppleProcessorTraceT8122::unconfigureCluster(bool)`
- `site.AppleProcessorTraceBringUp`
- `!os_add_overflow(virt_addr, offset, &vaddr)`
- `_activeSession`
- `virtual void AppleProcessorTraceT6000::unconfigureCluster(bool)`
- `IOReturn getOrSetCarveoutSizeInMBProperty(uint64_t, uint64_t *)`
- `OSSharedPtr<IOMemoryDescriptor> AppleProcessorTraceSession::getBufferPA()`
- `AppleProcessorTraceUserClient.cpp`
- `\"%s\" @%s:%d`
- `void AppleProcessorTrace::stopTracingOnCore(bool)`
- `!(caps.ProdTracePA || caps.ProdTraceVA)`
- `Q24@?0^v8Q16`
- `com.apple.private.AppleProcessorTrace.Control`
- `virtual bool AppleProcessorTraceT8310::getTracePowerStateForCluster(bool)`
- `virtual void AppleProcessorTraceT8310::defeatureCore(bool)`
- `virtual void AppleProcessorTraceT8130::unconfigureCluster(bool)`
- `virtual void AppleProcessorTraceT8110::unconfigureCore(bool)`
- `AppleProcessorTraceT6031`
- `virtual bool AppleProcessorTraceT6031::getTracePowerStateForCluster(bool)`
- `virtual void AppleProcessorTraceT6020::unconfigureCore(bool)`
- `AppleProcessorTraceT8122`
- `121111121222121211111112112211211211211211211211211211211211`
- `virtual bool AppleProcessorTraceT8101::getTracePowerStateForCluster(bool)`
- `bool AppleProcessorTrace::isVASession()`
- `AppleProcessorTraceT8132`
- `void AppleProcessorTraceT8160::apt_msr_ro_ctl_write(ml_topology_cpu_t, uint8_t, uint64_t)`
- `virtual void AppleProcessorTraceT8110::refeatureCore(bool)`
- `void AppleProcessorTrace::enterSleep()`
- `virtual void AppleProcessorTraceT8120::platformStopTracingOnCore(bool)`
- `bool AppleProcessorTraceSession::mapBufferPA()`
- `IOUserClientEntitlements`
- `12122`
- `com.apple.private.AppleProcessorTrace.CarveoutProperty`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodStop(OSObject *, void *, IOExternalMethodArguments *)`
- `virtual void AppleProcessorTraceT8310::platformStopTracingOnCore(bool)`
- `virtual bool AppleProcessorTraceT8112::getTracePowerStateForCluster(bool)`
- `virtual void AppleProcessorTraceT8130::platformStopTracingOnCore(bool)`
- `_workloop`
- `IOReturn AppleProcessorTrace::reset(OSSharedPtr<AppleProcessorTraceSession>)`
- `void AppleProcessorTrace::irqHandler()`
- `!config.prod && !caps.DevTrace`
- `ml_topology_cpu_t getCurrentCPU()`
- `apt_panic_trace`
- `config.nrg_trace && config.nrg_trace_trigger_lvl_pow2 < apple_processor_trace::NRGMinimumTriggerPow2`
- `!isExceptionLevelDisabled(config, ExceptionLevel::GL2)`
- `called && \"cpu_broadcast_xcallable not called\"`
- `12111112122212121111111111111112`
- `void AppleProcessorTrace::traceRegionReset()`
- `start_va`
- `VATraceBuffer`
- `uint64_t AppleProcessorTraceT8150::apt_msr_ro_ctl_read(ml_topology_cpu_t, uint8_t)`
- `void AppleProcessorTraceT8132::apt_msr_ro_ctl_write(ml_topology_cpu_t, uint8_t, uint64_t)`
- `site.AppleProcessorTraceT8160`
- `site.AppleProcessorTrace`
- `virtual void AppleProcessorTraceT6020::defeatureCore(bool)`
- `site.AppleProcessorTraceEventSource`
- `AppleProcessorTraceT6050`
- `121111121222121211111112112211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211`
- `site.AppleProcessorTraceT6020`
- `site.AppleProcessorTraceT6030`
- `virtual void AppleProcessorTraceT6030::defeatureCore(bool)`
- `virtual void AppleProcessorTraceT8122::stopTracingOnCluster(bool)`
- `void AppleProcessorTraceT6050::apt_msr_ro_ctl_write(ml_topology_cpu_t, uint8_t, uint64_t)`
- `virtual IOReturn AppleProcessorTraceUserClient::clientMemoryForType(UInt32, IOOptionBits *, IOMemoryDescriptor **)`
- `\"AppleProcessorTrace: %s:%u REQUIRE failed: %s\" @%s:%d`
- `void AppleProcessorTraceT8150::apt_msr_ro_ctl_write(ml_topology_cpu_t, uint8_t, uint64_t)`
- `IOReturn AppleProcessorTrace::resumeTracingGated(OSSharedPtr<AppleProcessorTraceSession>)`
- `virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8140::getChunkForCluster(unsigned int, uint64_t)`
- `virtual bool AppleProcessorTraceT8130::getTracePowerStateForCluster(bool)`
- `AppleProcessorTraceT8110`
- `isExceptionLevelDisabled(config, ExceptionLevel::EL0)`
- `cpu_broadcast_xcallable<XCallPayload>::~cpu_broadcast_xcallable() [T = XCallPayload]`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodUnconfigure(OSObject *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodAddTask(OSObject *, void *, IOExternalMethodArguments *)`
- `AppleProcessorTrace.hpp`
- `virtual bool AppleProcessorTraceT6000::getTracePowerStateForCluster(bool)`
- `virtual void AppleProcessorTraceT8120::unconfigureCluster(bool)`
- `virtual void AppleProcessorTraceT6030::unconfigureCluster(bool)`
- `virtual void AppleProcessorTraceT6000::defeatureCore(bool)`
- `121111121222121211111112112`
- `IODTNVRAM`
- `121111121222121211111112112211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211`
- `IOUserClientDefaultLockingSingleThreadExternalMethod`
- `virtual void AppleProcessorTraceT8112::stopTracingOnCluster(bool)`
- `virtual void AppleProcessorTraceT8130::defeatureCore(bool)`
- `virtual bool AppleProcessorTraceT8103::getTracePowerStateForCluster(bool)`
- `!config.buffer_size`
- `\"failed to find the PMGR block offset in EDT. Looked up under 'pmgr' and 'pmgr-child'.\" @%s:%d`
- `virtual void AppleProcessorTraceT8122::unconfigureCore(bool)`
- `virtual void AppleProcessorTraceT8112::unconfigureCore(bool)`
- `OSBoundedPtr.h`
- `virtual void AppleProcessorTraceT6000::platformStopTracingOnCore(bool)`
- `apt-carveout-size-mb`
- `AppleProcessorTraceT6030`
- `Chunk *AppleProcessorTraceSession::getChunkForCluster(ml_topology_cluster_t, unsigned int)`
- `uint64_t AppleProcessorTraceT6050::apt_msr_ro_ctl_read(ml_topology_cpu_t, uint8_t)`
- `Streaming`
- `DeviceCapabilities`
- `virtual void AppleProcessorTraceT6000::unconfigureCore(bool)`
- `AppleProcessorTrace`
- `IOReturn AppleProcessorTrace::allocateTraceBuffers()`
- `arm-io`
- `!called && \"cpu_broadcast_xcallable already called\"`
- `virtual void AppleProcessorTraceT8140::defeatureCore(bool)`
- `site.AppleProcessorTraceT6031`
- `void AppleProcessorTraceSession::enqueueFreeChunk(Chunk *)`
- `Chunk *AppleProcessorTraceSession::getFreeChunk()`
- `virtual void AppleProcessorTraceT8130::stopTracingOnCluster(bool)`
- `void AppleProcessorTraceT8320::apt_msr_ro_ctl_write(ml_topology_cpu_t, uint8_t, uint64_t)`
- `virtual void AppleProcessorTraceT8320::defeatureCore(bool)`
- `virtual void AppleProcessorTraceT8101::stopTracingOnCluster(bool)`
- `RequestedBufferSize`
- `IOReturn AppleProcessorTrace::addTaskGated(OSSharedPtr<AppleProcessorTraceSession>, MethodAddTaskArgs)`
- `chunk`
- `bufferIndex < clusterState.activeChunks.size()`
- `virtual bool AppleProcessorTraceUserClient::initWithTask(task_t, void *, UInt32, OSDictionary *)`
- `virtual void AppleProcessorTraceT8310::refeatureCore(bool)`
- `vm_offset_t IODeviceMappedMemory::addr(IOByteCount)`
- `virt_addr && \"Failed to map IODeviceMappedMemory\"`
- `AppleProcessorTraceT8120`
- `121111121222121211111112112211211211211211211211211211211211211211211211211211211211211211211`
- `!config.buffer_phys`
- `AppleProcessorTraceSession.cpp`
- `void AppleProcessorTraceSession::resetBufferVA()`
- `bool AppleProcessorTraceSession::enableTracingForTask(mach_port_name_t)`
- `uint32_t queueSizeForConfig(MethodConfigArgs)`
- `AppleProcessorTracePreACC7Src.hpp`
- `virtual void AppleProcessorTraceT6030::refeatureCore(bool)`
- `AppleProcessorTraceT6020`
- `IODeviceMappedMemory::IODeviceMappedMemory(OSSharedPtr<IODeviceMemory>)`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `AppleProcessorTraceUserClient`
- `virtual void AppleProcessorTrace::stop(IOService *)`
- `true`
- `virtual void AppleProcessorTraceT8101::refeatureCore(bool)`
- `setState`
- `!isExceptionLevelDisabled(config, ExceptionLevel::EL1)`
- `void cpu_broadcast_xcallable<AppleProcessorTrace>::operator()() [T = AppleProcessorTrace]`
- `!is_va`
- `bufID < 2`
- `virtual void AppleProcessorTraceT8120::unconfigureCore(bool)`
- `bool AppleProcessorTraceSession::mapBufferVA()`
- `numFreeChunks <= chunks.size()`
- `config.nrg_trace && !caps.EnergyTrace`
- `pmgr-child`
- `getCarveoutSizeFromDeviceTree`
- `const MethodConfigArgs &AppleProcessorTrace::getSessionConfig()`
- `site.AppleProcessorTraceNub`
- `SessionOwner`
- `%02x%02x%02x%02x-%02x%02x-%02x%02x-%02x%02x-%02x%02x%02x%02x%02x%02x`
- `IOReturn AppleProcessorTrace::startTracingGated(OSSharedPtr<AppleProcessorTraceSession>)`
- `\"EDT-provided PA of SoCPhys is null.\" @%s:%d`
- `121121212122121322132111`
- `virtual void AppleProcessorTraceT8110::defeatureCore(bool)`
- `virt_addr && \"Unmapped IODeviceMappedMemory\"`
- `The offset of the pointer inside its valid memory range can't be represented using int32_t`
- `site.AppleProcessorTraceT8132`
- `virtual void AppleProcessorTraceT8120::defeatureCore(bool)`
- `absMaxThresh < chunks_size`
- `ml_topology_cluster_t getCurrentCluster()`
- `void AppleProcessorTraceT6040::apt_msr_ro_ctl_write(ml_topology_cpu_t, uint8_t, uint64_t)`
- `AppleProcessorTraceNub`
- `ml_get_interrupts_enabled()`
- `AppleProcessorTrace Workloop`
- `!isExceptionLevelDisabled(config, ExceptionLevel::GL1)`
- `numFreeChunks < chunks.size()`
- `void AppleProcessorTraceSession::drainDirtyChunksAndAdviseThrottle()`
- `121111121222121211111112112211211211211211211211211211211211211211211211211211211211211`
- `FeatureFlags`
- `State`
- `bool AppleProcessorTrace::prepareForPanicTrace()`
- `virtual void AppleProcessorTraceT6020::unconfigureCluster(bool)`
- `virtual void AppleProcessorTraceT6030::unconfigureCore(bool)`
- `void AppleProcessorTraceSession::unmapBufferPA()`
- `com.apple.private.AppleProcessorTrace.Trace`
- `virtual void AppleProcessorTraceT6000::refeatureCore(bool)`
- `void AppleProcessorTrace::publishNubs()`
- `void AppleProcessorTrace::startTracingOnCore()`
- `AppleProcessorTraceVirtualBufferMemoryDescriptor`
- `site.T`
- `void AppleProcessorTraceSession::lockBufferVA()`
- `virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT6050::getChunkForCluster(unsigned int, uint64_t)`
- `static IOReturn AppleProcessorTraceUserClient::externalMethodGetSystemMetadata(OSObject *, void *, IOExternalMethodArguments *)`
- `virtual AppleProcessorTrace::ClusterChunkInfo AppleProcessorTraceT8150::getChunkForCluster(unsigned int, uint64_t)`
- `121111121222121211`
- `void AppleProcessorTrace::stopTracingOnClustersGated(ChunkQueueTarget)`
- `bool AppleProcessorTrace::startPanicTrace()`
- `cpu_broadcast_xcallable<AppleProcessorTrace>::~cpu_broadcast_xcallable() [T = AppleProcessorTrace]`
