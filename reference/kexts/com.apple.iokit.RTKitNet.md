# `com.apple.iokit.RTKitNet`

- Name: RTKitNet
- Version: `1.0`
- UUID: `BB112928-5FC7-3DE9-B17C-7F4F5170D75C`
- Source version: `251.40.7.0.0`
- Depends on: [`com.apple.driver.AppleFirmwareKit`](com.apple.driver.AppleFirmwareKit.md) 1, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 25.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 25.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 25.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 25.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### IORTKitNetSharedMemory
- `CFBundleIdentifier`: `com.apple.iokit.RTKitNet`
- `IOClass`: `RTKitNetKernelSharedMemory`
- `IOKitDebug`: `255`
- `IOName`: `RTKitNetKernelSharedMemory`
- `IONameMatch`: `aop2.network.aop2apkernel`
- `IOPersonalityPublisher`: `com.apple.iokit.RTKitNet`
- `IOProviderClass`: `AFKSharedMemoryRegionBase`
- `IOResourceMatch`: `IOBSD`

### IORTKitNetTightbeam
- `CFBundleIdentifier`: `com.apple.iokit.RTKitNet`
- `IOClass`: `RTKitNetKernelPacketCapture`
- `IOKitDebug`: `65535`
- `IONameMatch`:
  - `com.apple.aop2.ulpn.xnu-com.apple.aop2.ulpn.xnu.ap.client-rev`
  - `com.apple.aop2.ulpn.xnu-com.apple.aop2.ulpn.xnu.ap.client-fwd`
- `IOPersonalityPublisher`: `com.apple.iokit.RTKitNet`
- `IOProviderClass`: `AFKEndpointInterface`


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `RTKitNetKernelPacketCapture` | 0xd0 | AFKTightbeamEndpoint → IOService → IORegistryEntry |
| `RTKitNetKernelSharedMemory` | 0xa0 | IOService → IORegistryEntry |
| `RTKitNetKernelStatistics` | 0x30 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1800)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001475 off=0x00ba68a0-0x00ba7d15 addr=0xfffffe0007baa8a0-0xfffffe0007babd15 r--/r--   __TEXT            
	sz=0x0000026b off=0x00ba7008-0x00ba7273 addr=0xfffffe0007bab008-0xfffffe0007bab273               __TEXT.__os_log           
	sz=0x000000a8 off=0x00ba7278-0x00ba7320 addr=0xfffffe0007bab278-0xfffffe0007bab320               __TEXT.__const            
	sz=0x000009f5 off=0x00ba7320-0x00ba7d15 addr=0xfffffe0007bab320-0xfffffe0007babd15               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00004c04 off=0x0394f210-0x03953e14 addr=0xfffffe000a953210-0xfffffe000a957e14 r-x/r-x   __TEXT_EXEC       
	sz=0x00004764 off=0x0394f210-0x03953974 addr=0xfffffe000a953210-0xfffffe000a957974          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000004a0 off=0x03953974-0x03953e14 addr=0xfffffe000a957974-0xfffffe000a957e14          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001e0 off=0x04a20100-0x04a202e0 addr=0xfffffe000ba24100-0xfffffe000ba242e0 rw-/rw-   __DATA            
	sz=0x00000106 off=0x04a20100-0x04a20206 addr=0xfffffe000ba24100-0xfffffe000ba24206               __DATA.__data             
	sz=0x000000b8 off=0x00000000-0x000000b8 addr=0xfffffe000ba24208-0xfffffe000ba242c0               __DATA.__common           (Zerofill)
	sz=0x00000020 off=0x00000000-0x00000020 addr=0xfffffe000ba242c0-0xfffffe000ba242e0               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000012f0 off=0x01497a68-0x01498d58 addr=0xfffffe000849ba68-0xfffffe000849cd58 rw-/rw-   __DATA_CONST      
	sz=0x00000018 off=0x01497a68-0x01497a80 addr=0xfffffe000849ba68-0xfffffe000849ba80         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000018 off=0x01497a80-0x01497a98 addr=0xfffffe000849ba80-0xfffffe000849ba98         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000eb8 off=0x01497a98-0x01498950 addr=0xfffffe000849ba98-0xfffffe000849c950         __DATA_CONST.__const            
	sz=0x000000c0 off=0x01498950-0x01498a10 addr=0xfffffe000849c950-0xfffffe000849ca10         __DATA_CONST.__kalloc_type      
	sz=0x000000a0 off=0x01498a10-0x01498ab0 addr=0xfffffe000849ca10-0xfffffe000849cab0         __DATA_CONST.__kalloc_var       
	sz=0x00000250 off=0x01498ab0-0x01498d00 addr=0xfffffe000849cab0-0xfffffe000849cd00         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000050 off=0x01498d00-0x01498d50 addr=0xfffffe000849cd00-0xfffffe000849cd50         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x01498d50-0x01498d58 addr=0xfffffe000849cd50-0xfffffe000849cd58         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 158 at 0x04afd61c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     BB112928-5FC7-3DE9-B17C-7F4F5170D75C
008: LC_SOURCE_VERSION           251.40.7.0.0
009: LC_FUNCTION_STARTS          offset=0x004acc380 size=0xf8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `RTKitNet`
- `CFBundleIdentifier`: `com.apple.iokit.RTKitNet`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `RTKitNet`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2025 Apple Inc. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/RTKitNet.kext`
- `_PrelinkExecutableLoadAddr`: `-2198893582176`
- `_PrelinkExecutableRelativePath`: `RTKitNet`
- `_PrelinkExecutableSize`: `30025`
- `_PrelinkExecutableSourceAddr`: `-2198893582176`
- `_PrelinkKmodInfo`: `-2198828072704`

## Strings (65) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__os_log]**

- `%s:%d init() failed, baseAddr %p memSize %u bufferSize %u syncBatch %u # of rings %u`
- `%s:%d processCompletion() channel %p numBuffers %u`
- `%s:%d processSubmission() channel %p ringId %u numBuffers %u`
- `AONNetBufferPool::regBufferAvailableObserver satisfiable. observer=[%p]`
- `AONNetBufferPool::regBufferAvailableObserver failed. observer=[%p]`
- `AONNetBufferPool::deregBufferAvailableObserver failed. observer=[%p]`
- `%s:%d channel %p destructed`
- `%s:%d reset() channel %p`
- `Buffer Pool [%p] reset`
- `AONNetBufferPool::regBufferAvailableObserver success. observer=[%p]`
- `AONNetBufferPool::deregBufferAvailableObserver success. observer=[%p]`

**[__TEXT.__cstring]**

- `RTKitNetKernelStatistics`
- `site.RTKitNetKernelSharedMemory`
- `%30s:%d flow stats is NULL\n`
- `%30s:%d invalid global stats type %u\n`
- `%30s:%d global IP stats not available\n`
- `%30s:%d global UDP stats not available\n`
- `%30s:%d global driver stats not available\n`
- `%30s:%d inout_count is NULL\n`
- `121211`
- `RTKitNetKernelSharedMemory`
- `12111112122212121111`
- `/Library/Caches/com.apple.xbs/236004E1-A52B-48CC-92D8-0A3096B3CEC6/TemporaryDirectory.BreRZD/Sources/RTKitNet_AP_Libraries/src/AlwaysOnNetworking/RTKitNet/RTKitNetKernelSharedMemory.cpp`
- `%30s:%d RTKitNetKernelSharedMemory::start, shared memory size %llu less than required %zu\n`
- `%30s:%d global IPv6 stats not available\n`
- `%30s:%d invalid stats len for global UDP stats\n`
- `12111112122212121111111121`
- `%30s:%d afk memory descriptor map is null\n`
- `kern_pbufpool_create failed: %d\n`
- `kern_pbufpool_alloc_nosleep failed:%d (pp:%p)\n`
- `v28@?0[16C]8[64S]16I24`
- `aon_networking_diag.c`
- `%30s:%d failed to get stats provider context\n`
- `site.RTKitNetKernelStatistics`
- `%30s:%d invalid stats len for global TCP stats\n`
- `site.RTKitNetKernelPacketCapture`
- `IOBSD`
- `Failed initializing SharedMemory consumer`
- `start_tightbeam_fwd: aonnetworkingdiag_aop2__init failed: 0x%x\n`
- `submitcapturebuffers: shared memory is unmapped\n`
- `site.struct flowTrack`
- `%30s:%d invalid stats len for global IPv6 stats\n`
- `%30s:%d invalid stats len for global QUIC stats\n`
- `ulpn shared pp`
- `start_tightbeam_fwd: getTightbeamEndpoint returned 0x0\n`
- `start_tightbeam_rev: getTightbeamEndpoint returned 0x0\n`
- `\"TB_FATAL: \" \"unrecognized selector: %llu\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->submitcapturebuffers != ((void*)0)) && \\\"implementation for submitCaptureBuffers is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `%30s:%d afk memory descriptor is null\n`
- `%30s:%d failed to RTKitNetKernelStatistics object\n`
- `%30s:%d invalid flow stats index %u\n`
- `%30s:%d invalid stats pointer\n`
- `failed to start super\n`
- `%30s:%d stats index is NULL\n`
- `%30s:%d invalid stats len for global IP stats\n`
- `%30s:%d global TCP stats not available\n`
- `%30s:%d invalid stats len for global driver stats\n`
- `ifnet_find_by_name failed:%d (ifName:%s)\n`
- `start_tightbeam_rev: aonnetworkingdiag_ap__server_start_owned failed: 0x%x\n`
- `\"TB_ASSERT: \" \"(server->returncapturebuffers != ((void*)0)) && \\\"implementation for returnCaptureBuffers is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `%30s:%d global QUIC stats not available\n`
- `RTKitNetKernelPacketCapture`
- `%s`
- `failed returning capture buffers, err:%d\n`
- `^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[97c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16`
