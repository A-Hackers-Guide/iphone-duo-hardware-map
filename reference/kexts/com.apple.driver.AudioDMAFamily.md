# `com.apple.driver.AudioDMAFamily`

- Name: AudioDMAFamily
- Version: `600.45`
- UUID: `F22DA1EE-1DFD-308D-A8BD-AAD77945F2AA`
- Source version: `600.45.0.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `ADMAChannel` | 0x88 | IOService → IORegistryEntry |
| `ADMAChannelInterface` | 0x90 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001980 off=0x00902ff0-0x00904970 addr=0xfffffe0007906ff0-0xfffffe0007908970 r--/r--   __TEXT            
	sz=0x00000e6b off=0x009036b8-0x00904523 addr=0xfffffe00079076b8-0xfffffe0007908523               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000428 off=0x00904523-0x0090494b addr=0xfffffe0007908523-0xfffffe000790894b               __TEXT.__os_log           
	sz=0x00000020 off=0x00904950-0x00904970 addr=0xfffffe0007908950-0xfffffe0007908970               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00005888 off=0x02bf6ff0-0x02bfc878 addr=0xfffffe0009bfaff0-0xfffffe0009c00878 r-x/r-x   __TEXT_EXEC       
	sz=0x00005688 off=0x02bf6ff0-0x02bfc678 addr=0xfffffe0009bfaff0-0xfffffe0009c00678          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000200 off=0x02bfc678-0x02bfc878 addr=0xfffffe0009c00678-0xfffffe0009c00878          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000128 off=0x049db090-0x049db1b8 addr=0xfffffe000b9df090-0xfffffe000b9df1b8 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049db090-0x049db158 addr=0xfffffe000b9df090-0xfffffe000b9df158               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b9df158-0xfffffe000b9df1b8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000010c8 off=0x012c19c8-0x012c2a90 addr=0xfffffe00082c59c8-0xfffffe00082c6a90 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x012c19c8-0x012c19d8 addr=0xfffffe00082c59c8-0xfffffe00082c59d8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x012c19d8-0x012c19e8 addr=0xfffffe00082c59d8-0xfffffe00082c59e8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000e40 off=0x012c19e8-0x012c2828 addr=0xfffffe00082c59e8-0xfffffe00082c6828         __DATA_CONST.__const            
	sz=0x00000080 off=0x012c2828-0x012c28a8 addr=0xfffffe00082c6828-0xfffffe00082c68a8         __DATA_CONST.__kalloc_type      
	sz=0x000000a0 off=0x012c28a8-0x012c2948 addr=0xfffffe00082c68a8-0xfffffe00082c6948         __DATA_CONST.__kalloc_var       
	sz=0x00000100 off=0x012c2948-0x012c2a48 addr=0xfffffe00082c6948-0xfffffe00082c6a48         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000048 off=0x012c2a48-0x012c2a90 addr=0xfffffe00082c6a48-0xfffffe00082c6a90         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 73 at 0x04aed98c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     F22DA1EE-1DFD-308D-A8BD-AAD77945F2AA
008: LC_SOURCE_VERSION           600.45.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab8e38 size=0x78
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleExecutable`: `AudioDMAFamily`
- `CFBundleIdentifier`: `com.apple.driver.AudioDMAFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AudioDMAFamily`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `600.45`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `600.45`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2022 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AudioDMAFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896349200`
- `_PrelinkExecutableRelativePath`: `AudioDMAFamily`
- `_PrelinkExecutableSize`: `33784`
- `_PrelinkExecutableSourceAddr`: `-2198896349200`
- `_PrelinkKmodInfo`: `-2198828355440`

## Strings (122) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `/Library/Caches/com.apple.xbs/EDB52463-4048-495D-AB86-88E13335F3E1/TemporaryDirectory.lXLcfx/Sources/AudioDMAController/ADMAEvolution/ADMAFamily/ADMAChannelInterface.cpp`
- `%s.%s`
- `%s: %s::%d: [%02u] Aperture: VA = 0x%016llx PA = 0x%016llx Length = %08llu\n`
- `max-bit-depth-bits`
- `%s: %s unallowed in BULK.`
- `%s: Failed to fetch stream config.`
- `translateStreamConfiguration`
- `set`
- `%s: %s::%d: Completion status shows error (0x%08x / %s).\n`
- `%s: Failed to super::start`
- `max-fifo-depth-bytes`
- `max-fifo-depth-us`
- `%s: %s::%d: Ignoring %s for BULK streams.\n`
- `i8@?0`
- `222222212111122111122`
- `fetchIndexAndDirection(this, pimpl, true)`
- `initial-trigger-bytes`
- `%s: Could not fetch path latency from the IP.`
- `%s: IOMD is a nullptr.`
- `static_cast<bool>(inFirstTransferSizeInBytes)`
- `site.ADMAChannel`
- `ADMAChannelInterface`
- `%s: Aperture at [%02u] returned a nullptr.`
- `static_cast<bool>(thisAperture)`
- `static_cast<bool>(thisAperture->getVirtualAddress())`
- `role`
- `start`
- `%s: Could not initialize with %s (0x%08x).`
- `debug`
- `%s: Aperture at [%02u] has a zero length.`
- `registryData != nullptr`
- `service-exclave_proxy`
- `!internalConfiguration.isM2M`
- `tReq.fullTransferSize <= inMemoryDescriptor->getLength()`
- `inFirstTransferSizeInBytes <= inMemoryDescriptor->getLength()`
- `static_cast<bool>(thisAperture->getLength())`
- `%s: Could not setDirectionAndRole.`
- `ret == 0 `
- `%s: Could not setExclaveProxyServiceName.`
- `%s: Full-transfer size is 0.`
- `%s: transfer failed with %s.`
- `%s: Size is too large (%u > %llu).`
- `%s:: super::init failed.`
- `%s: %s::%d: updateStreamConfig returns invalid configuration\n`
- `%s: updateConfiguration fails with %s.`
- `%s: Frame rate's unavailable.`
- `12111112122212121`
- `initWithRegistryEntry`
- `%s: %s::%d: DT Prop not seen; auto-inferred stream type as ISOC.\n`
- `!dmaConfiguration.isM2M`
- `%s: Invalid stream configuration.`
- `%s: Disallowed in M2M.`
- `static_cast<bool>(inMemoryDescriptor)`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `%s: Could not setOperationalApertures.`
- `result`
- `deviceMemoryArray != nullptr`
- `%s: Failed to super::attach`
- `23:38:17`
- `max-sample-rate-hz`
- `%s: Provider workloop is NUL.`
- `status`
- `YES`
- `NO`
- `AssertMacros: %s, %s file: %s, line: %d, value: %lld\n`
- `reg`
- `%s: Aperture at [%02u] has a zero VA.`
- `initWithRegistryEntry_block_invoke`
- `initial-trigger-us`
- `%s: Invoke the BULK version for M2M.`
- `121111121222121211`
- `directionDesignator == 't' || directionDesignator == 'r'`
- `v16@?0r^{CompletionContext=QIIi}8`
- `max-channel-count`
- `deactivate_block_invoke`
- `static_cast<bool>(inMemoryDescriptor->getLength())`
- `inByteCount <= inMemoryDescriptor->getLength()`
- `\"%s\" @%s:%d`
- `site.ADMAChannelInterface`
- `static_cast<bool>(pimpl)`
- `%s: Could not reckon index and direction.`
- `static_cast<bool>(inFullTransferSizeInMs)`
- `%s: First-transfer size is 0.`
- `%s: Invoke the ISOC version for non-M2M.`
- `static_cast<bool>(inByteCount)`
- `%s: abortTransfers failed with %s.`
- `%s: Could not fetch the role for this channel.`
- `static_cast<bool>(inFirstTransferSizeInMs)`
- `%s: Requested transfer size (%llu) violates IOMD size (%llu)`
- `internalConfiguration.isM2M`
- `%s: Size is 0.`
- `%s: Bytecount is 0.`
- `OSBoundedPtr.h`
- `bounded_ptr<T>::discard_bounds: Discarding the bounds on this pointer would lose the fact that it is outside of the bounds set originally`
- `Rx`
- `updateStreamConfig`
- `static_cast<bool>(mChannelInterfaceImpl->interfaceWorkLoop)`
- `setAudioStreamDescription_block_invoke`
- `%s: First-transfer size is too large (%u > %llu).`
- `ADMAChannel`
- `Tx`
- `Could not allocate ADMAChannelInterfaceImpl.`
- `%s: Failed to map 'reg' entries.`
- `%s: Built on %s at %s.           \nGeneral panic behavior:\n          \tdebugFacility = 0x%08x\n          \n`
- `dma-stream-type`
- `axi-burst-size-bytes`
- `Malformed node name.`
- `site.ADMAChannelInterfaceImpl`
- `Oct 13 2026`
- `%s: %s failed with %s.`
- `*endPtr == '\\0'`

**[__TEXT.__os_log]**

- `[%c%c%c%c Tx] Requested threshold bytes(%u) >= Requested transfer-end bytes(%u).`
- `[%c%c%c%c Rx] Requested threshold bytes(%u) <= Requested transfer-end bytes(%u).`
- `%s: [%c%c%c%c] Direction                          = %s`
- `%s: [%c%c%c%c] isM2M                              = %s`
- `%s: [%c%c%c%c] programmedByteSize                 = %hhu`
- `%s: [%c%c%c%c] programmedFIFODepthBytes           = %hu`
- `%s: [%c%c%c%c] programmedTransferThresholdBytes   = %hu`
- `%s: [%c%c%c%c] programmedAXIBurstSize             = %hhu`
- `[%c%c%c%c] Requested threshold bytes is 0.`
- `[%c%c%c%c] Requested threshold bytes(%u) >= Requested FIFO size bytes(%u).`
- `%s: [%c%c%c%c] programmedTransferEndLimitsBytes   = %hu`
