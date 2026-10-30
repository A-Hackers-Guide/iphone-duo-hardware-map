# `com.apple.iokit.IOSurface`

- Name: IOSurface
- Version: `403.1`
- UUID: `539CEB77-05AA-36C7-B4C4-2CB90BAFB810`
- Source version: `403.1.0.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.0.0b1, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0b1, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0b1, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0b1, [`com.apple.kpi.private`](com.apple.kpi.private.md) 9.0.0b1, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 9.0.0b1

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### FirstPersonality
- `CFBundleIdentifier`: `com.apple.iokit.IOSurface`
- `IOClass`: `IOSurfaceRoot`
- `IOMatchCategory`: `IOSurfaceRoot`
- `IOPersonalityPublisher`: `com.apple.iokit.IOSurface`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOBSD`


## C++ classes (27) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOFence` | 0xd8 |  |
| `IOFenceTransaction` | 0x58 |  |
| `IOSurface` | 0x3e0 |  |
| `IOSurfaceClient` | 0x98 |  |
| `IOSurfaceDescriptor` | 0x18 |  |
| `IOSurfaceDescriptorComponent` | 0x20 |  |
| `IOSurfaceDescriptorContext` | 0x40 |  |
| `IOSurfaceDeviceCache` | 0x68 |  |
| `IOSurfaceDeviceMemoryRegion` | 0x60 | IOSurfaceMemoryRegion |
| `IOSurfaceMemoryCallback` | 0x30 |  |
| `IOSurfaceMemoryPool` | 0xb0 |  |
| `IOSurfaceMemoryPoolBunch` | 0x48 |  |
| `IOSurfaceMemoryRegion` | 0x28 |  |
| `IOSurfaceMemoryTag` | 0x38 |  |
| `IOSurfaceRoot` | 0x4a0 | IOService → IORegistryEntry |
| `IOSurfaceRootParavirtMapperInterface` | 0x10 |  |
| `IOSurfaceRootUserClient` | 0x148 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |
| `IOSurfaceSendRight` | 0x28 |  |
| `IOSurfaceShared` | 0x48 |  |
| `IOSurfaceSharedEvent` | 0x68 |  |
| `IOSurfaceSharedEventListener` | 0x50 |  |
| `IOSurfaceSharedEventNotification` | 0x70 |  |
| `IOSurfaceSharedEventNotificationPort` | 0x90 | IOSurfaceSharedEventListener |
| `IOSurfaceSharedEventReference` | 0x18 |  |
| `IOSurfaceSmaMemoryRegion` | 0x60 | IOSurfaceMemoryRegion |
| `IOSurfaceTransaction` | 0x30 |  |
| `IOSurfaceWiredSendRight` | 0x28 | IOSurfaceSendRight |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000072b0 off=0x00a5ff50-0x00a67200 addr=0xfffffe0007a63f50-0xfffffe0007a6b200 r--/r--   __TEXT            
	sz=0x000033b7 off=0x00a60668-0x00a63a1f addr=0xfffffe0007a64668-0xfffffe0007a67a1f               __TEXT.__cstring          (CstringLiterals)
	sz=0x00003779 off=0x00a63a1f-0x00a67198 addr=0xfffffe0007a67a1f-0xfffffe0007a6b198               __TEXT.__os_log           
	sz=0x00000060 off=0x00a671a0-0x00a67200 addr=0xfffffe0007a6b1a0-0xfffffe0007a6b200               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00032ee4 off=0x033ead60-0x0341dc44 addr=0xfffffe000a3eed60-0xfffffe000a421c44 r-x/r-x   __TEXT_EXEC       
	sz=0x000325a4 off=0x033ead60-0x0341d304 addr=0xfffffe000a3eed60-0xfffffe000a421304          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000940 off=0x0341d304-0x0341dc44 addr=0xfffffe000a421304-0xfffffe000a421c44          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000610 off=0x04a16fc8-0x04a175d8 addr=0xfffffe000ba1afc8-0xfffffe000ba1b5d8 rw-/rw-   __DATA            
	sz=0x00000178 off=0x04a16fc8-0x04a17140 addr=0xfffffe000ba1afc8-0xfffffe000ba1b140               __DATA.__data             
	sz=0x00000460 off=0x00000000-0x00000460 addr=0xfffffe000ba1b140-0xfffffe000ba1b5a0               __DATA.__common           (Zerofill)
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000ba1b5a0-0xfffffe000ba1b5d8               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00006528 off=0x013f5be0-0x013fc108 addr=0xfffffe00083f9be0-0xfffffe0008400108 rw-/rw-   __DATA_CONST      
	sz=0x00000090 off=0x013f5be0-0x013f5c70 addr=0xfffffe00083f9be0-0xfffffe00083f9c70         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000090 off=0x013f5c70-0x013f5d00 addr=0xfffffe00083f9c70-0xfffffe00083f9d00         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000046f8 off=0x013f5d00-0x013fa3f8 addr=0xfffffe00083f9d00-0xfffffe00083fe3f8         __DATA_CONST.__const            
	sz=0x00000d00 off=0x013fa3f8-0x013fb0f8 addr=0xfffffe00083fe3f8-0xfffffe00083ff0f8         __DATA_CONST.__kalloc_type      
	sz=0x00000aa0 off=0x013fb0f8-0x013fbb98 addr=0xfffffe00083ff0f8-0xfffffe00083ffb98         __DATA_CONST.__kalloc_var       
	sz=0x000004a0 off=0x013fbb98-0x013fc038 addr=0xfffffe00083ffb98-0xfffffe0008400038         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000d0 off=0x013fc038-0x013fc108 addr=0xfffffe0008400038-0xfffffe0008400108         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 322 at 0x04af83f8
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     539CEB77-05AA-36C7-B4C4-2CB90BAFB810
008: LC_SOURCE_VERSION           403.1.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac5a68 size=0x6e8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOSurface`
- `CFBundleIdentifier`: `com.apple.iokit.IOSurface`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOSurface`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `403.1`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `403.1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2006-2017 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Console`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
  - `2`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOSurface.kext`
- `_PrelinkExecutableLoadAddr`: `-2198894919856`
- `_PrelinkExecutableRelativePath`: `IOSurface`
- `_PrelinkExecutableSize`: `265420`
- `_PrelinkExecutableSourceAddr`: `-2198894919856`
- `_PrelinkKmodInfo`: `-2198828109880`

## Strings (657) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `12111`
- `11`
- `IOUserClientDefaultLockingSingleThreadExternalMethod`
- `IOSurfaceDescriptorComponent`
- `\"IOSurfaceSharedEvent::free() called with non-empty notification list\" @%s:%d`
- `IOSurfaceScalerTimes`
- `\"IOSurface::prune_transaction_list unexpeted transaction list length\" @%s:%d`
- `IU`
- `Kernel Surfaces`
- `site.IOSurfaceSharedEvent *`
- `IOSurfaceWiredSendRight`
- `site.IOSurfaceWiredSendRight`
- `false`
- `IOSurfaceIsGlobal`
- `IOSurfacePlaneBytesPerRowOfTileData`
- `IOSurfacePlaneExtendedPixelsOnRight`
- `Breaking IOFence deadlock\n`
- `\"%s called with invalid index: %lld\" @%s:%d`
- `IOFence Deadlock Detection Depth`
- `trying to free apparently bogus surface handle %d`
- `\"%s: failed to get IOSurface root\" @%s:%d`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `\"user client not found in map\" @%s:%d`
- `DisablePrepareWiring`
- `com.apple.private.iosurfaceinfo`
- `IOSurfaceRootUserClient.cpp`
- `map_client_shared failed for event_shared_ro`
- `\"IOSurfaceRootUserClient: asked to allocate client shared id %08x not known by IOSurfaceRoot\" @%s:%d`
- `CreationProperties`
- `IOSurfaceElementWidth`
- `IOSurfaceMapCacheAttribute`
- `site.IOSurfaceClient`
- `trying to use apparently bogus event handle %d`
- `====> %s:%d Unable to assemble descriptor of the correct length\n`
- `====> %s:%d IOSurfaceMemoryPool: %s (%d) invalid task (%p) can't access pool id %llu (wrong entitlements)\n`
- `\"os_refcnt: underflow (rc=%p)\\n\" @%s:%d`
- `site.IOSurfaceSharedEventNotificationPort`
- `IOSurfaceSharedEvent`
- `IOSurfaceOffset`
- `IOSurfaceAddressFormat`
- `\"IOSurface released with non-zero client retain count: %p\" @%s:%d`
- `iosurface_id`
- `newWiredMemoryDescriptorWithLength`
- `IOSurfaceBufferTileFormat`
- `IOSurfaceName`
- `IOSurfacePlaneExtendedPixelsOnBottom`
- `create_surface_internal`
- `site.IOSurfaceClient *`
- `site.IOSurfaceMemoryPoolBunch`
- `IOSurfaceSmaMemoryRegion`
- `site.IOSurfaceSmaMemoryRegion`
- `IOSurfaceResetDefaultAttachmentsWhenNotInUse`
- `128111112`
- `IOSurfacePlaneHeight`
- `IOSurface`
- `hw.memsize`
- `LogCompleteNoAssertion`
- `Client Surfaces`
- `B16@?0^{OSObject=^^?i}8`
- `IOSurfaceHeight`
- `IOSurfacePlaneBytesPerRowOfCompressedTileHeaderGroups`
- `AGXUseNearestChromaFiltering`
- `\"IOSurface does not support taggedRelease with when != 1\" @%s:%d`
- `decrement`
- `IOSurfacePlaneCompressedTileHeight`
- `\"fDeviceCacheList is not empty for surface: %p\" @%s:%d`
- `site.IOSurfaceMemoryTag`
- `site.IOSurfaceDescriptor`
- `IOSurface Parameters`
- `\"IOSurface in slot %08x has a mismatched surface ID of %08x\\n\" @%s:%d`
- `trying to free apparently bogus event handle %d`
- `PanicOnAgentMaskSlotExhaustion`
- `IOSurfacePlaneCompressionFootprint`
- `allocate`
- `virtual bool IOSurfaceDeviceMemoryRegion::init(IOSurfaceRoot *, OSDictionary *, const char *, uint32_t, uint32_t)`
- `IOSurfaceRoot::alloc_surface_id: Map said entry free but something was there\n`
- `DeadlockLog`
- `DisableStatisticsProtection`
- `Security: Process %s (%d) relying on global (insecure) IOSurface lookups\n`
- `\"IOSurfaceTransaction::serialize panic because of attempting to write to nullptr.\" @%s:%d`
- `IOFenceAllowTearing`
- `Free`
- `iofence_ddd`
- `IOMalloc failed to alloc handles`
- `IOSurfaceDescriptorContext`
- `IOSurfacePlaneHorizontalPixelOffsetWithinCompressedTileArray`
- `vram`
- `Perf: Process %s (%d) has created %d IOSurfaces out of a limit of %d\n`
- `IONewZero failed to alloc IOSurfaceClientSharedListEntry`
- `IOSurfaceSendRight`
- `IOSurfaceAddressRanges`
- `Active Debug Flags`
- `assignSlotAndCopyAgentMaskMemoryForSignalValue`
- `InUse`
- `IOSurfaceFenceTransaction.cpp`
- `IOSurfacePlaneBytesPerCompressedTileHeader`
- `ColorAndSpatialKeys`
- `\twaitQ:   %p t: %p\n`
- `iofence_backtrace`
- `iofence_current_queue`
- `1211112`
- `IOSurfaceSharedEventNotification`
- `IOSurfacePixelSizeCastingAllowed`
- `IOSurfaceSubsampling`
- `IOSurfacePlaneCompressedTileDataRegionOffset`
- `IOSurfacePlaneDataRegionBytesPerSlice`
- `111111111121`
- `gather_memory_pool_data`
- `map_client_shared failed for client_shared_rw`
- `IOSurfacePlaneVerticalPixelOffsetWithinCompressedTileArray`
- `CEA-861:Type1`
- `non-coherent`
- `EnableStatisticsProtection`
- `com.apple.developer.gpu-restricted`
- `OutOfUse`
- `Descriptors`
- `IOSurfaceEncoderTimes`
- `1211111281111121112`
- `com.apple.private.IOSurface.protected-access`
- `IOSurfaceMemoryPoolBunch`
- `IOSurfaceGPUTimes`
- `init`
- `site.IOSurfaceDeviceCache`
- `site.IOSurface *`
- `Security: Process %s (%d) creating global IOSurfaces accessible to any other process\n`
- `Process caught creating IOFence deadlock`
- `2212211111111112212211111111112212211111111112212211111111112212211111111112212211111111112212211111111112212211111111112`
- `IOSurfaceIsPrivate`
- `s_create_surface`
- `\"IOFence does not support release with when != 1\" @%s:%d`
- `process %s (%d) caught causing IOFence deadlock!\n`
- `bounded_array_ref: Can't construct from a size greater than UINT32_MAX`
- `wired`
- `Size`
- `iosfcrefcnt.c`
- `IOSurfacePlaneComponentBitOffsets`
- `IOSurfaceDisplayDitherCbThresholds`
- `IOSurfaceMemoryPoolCacheModeSwitchEnabled`
- `12222222222221`
- `addAgentMaskForSignalValue`
- `site.IOFence *`
- `iosurface_timestamp_enable`
- `Debug Bits Value`
- `\"IOSurfaceSharedEvent does not support taggedRelease with when != 1\" @%s:%d`
- `BasicInfo`
- `UseCount1`
- `\tcurrent: %p t: %p\n`
- `N`
- `IOSurface count of %d approaching limit of %d\n`
- `\"unexpected client map mismatch\" @%s:%d`
- `IOSurfaceFence.cpp`
- `IOFenceTransaction`
- `IOSurfaceEDRFactor`
- `IOSurfacePlaneComponentNames`
- `IOSurfaceBitsPerBlock`
- `IOSurfacePlaneBitsPerBlock`
- `IOSurfacePlaneCompressedTileWidth`
- `IOSurfacePlaneHTPCVerticalHeaderGroupingMode`
- `IOSurfacePlaneBytesPerTileData`
- `site.IOSurfaceTaskToClientMap`
- `Entry for surface handle %d %p is not equal to %p`
- `1111`
- `IOSurfacePlaneWidth`
- `uint64_t IOSurface::getIndexedTimestamp(uint64_t) const`
- `DisableSupportLowLatencySignal`
- `CSBufferPitch`
- `IOUserClientDefaultLockingSetProperties`
- `Perf: Process %s (%d) IOSurface creation count: %d total count: %d\n`
- `\"%s: Agent mask slot exhaustion detected (event ID %08x, signal value 0x%016llx)\" @%s:%d`
- `IOSurfacePurgeWhenNotInUse`
- `IOSurfaceDeviceMemoryRegion`
- `flush_memory_pool`
- `IOSurfaceRootUserClient: couldn't map shared memory region into client`
- `Contexts`
- `IOSurfacePlaneExtendedPixelsOnLeft`
- `site.IOSurfaceMemoryCallback`
- `IOSurfaceRoot using IOSurfaceRootParavirtMapperInterface %p`
- `site.IOSurfaceShared`
- `IOSurfaceShared.cpp`
- `IOSurfaceMemoryPool.cpp`
- `assignAgentMaskSlot`
- `IOSurfaceSuperbuffer`
- `rewired`
- `iosurface`
- `IOSurface Debug Configuration`
- `Entry for shared event handle %d is not NULL (%p)`
- `\"fence freed before completion: %p\" @%s:%d`
- `IOCoreSurfaceRoot`
- `IOSurfacePlaneInfo`
- `IOSurfacePlaneComponentTypes`
- `read`
- `iofence_waiting_queue`
- `site.IOSurfaceMemoryRegionNode`
- `BreakIOFenceDeadlocks`
- `site.IOSurfaceRootUserClient`
- `1`
- `site.OSSharedPtr<IOSurfaceDeviceCache>`
- `/sma`
- `IOFence`
- `site.IOSurfaceDescriptorContext`
- `====> %s:%d IOSurfaceMemoryPool: %s (%d) can't access pool id %llu (wrong entitlements)\n`
- `site.IOSurfaceSharedEventReference`
- `Layout`
- `IOSurfaceRoot.cpp`
- `%s`
- `IOSurfaceShared`
- `Options`
- `site.IOSurfaceSharedEventListener`
- `site.IOSurfaceSharedEvent`
- `IOSurfacePlaneElementWidth`
- `IOSurfacePlaneHTPCPredictionSelector`
- `IOSurfacePrefetchPages`
- `IOSurfaceGPUGlobalRO`
- `IOSurfaceRoot`
- `create_surface_client_mem`
- `IOSurfaceProhibitUseCount`
- `IOSurfacePlaneSize`
- `display-carveout-inhibitcache`
- `reg`
- `AllowProtectedChildren`
- `Unable to set shared memory region ownership to kernel: %08x\n`
- `\"Bad IOSurfaceClient\" @%s:%d`
- `pid`
- `IOSurfaceSharedEventReference`
- `site.IOSurfaceSharedEventNotification`
- `\"IOFenceTransaction %p freed with non-zero fence count!\\n\" @%s:%d`
- `IOSurfaceSysMemOnly`
- `IOSurfaceProtectionOptions`
- `B24@?0r^{OSSymbol=^^?ib14b18*{smrq_slink={?=^{smrq_slink}}}}8^{OSObject=^^?i}16`
- `1211111112222`
- `LargestFree`
- `\"IOSurfaceSharedEventListener::free(): notification list is not empty\" @%s:%d`
- `IOSurfaceClass`
- `IOSurfaceCacheMode`
- `site.IOSurfaceTransactionSerialized`
- `IOSurfaceAgentMask alloc failed`
- `12111112122212121111111111111128112122111`
- `IOUserClientEntitlements`
- `name`
- `site.IOFenceTransaction`
- `IOSurfaceMemoryRegion`
- `IOSurfacePlaneWidthInCompressedTiles`
- `Unable to prepare shared entry: %08x`
- `\"IOSurfaceRootUserClient::set_surface_handle asked to set handle %08x that was not free: %p\" @%s:%d`
- `%.512s`
- `site.IOFence`
- `111`
- `true`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `site.IOSurfaceFenceTraceData`
- `IOSurface warning: buffer allocation failed.  %llu x %llu fmt: %08x size: %llu bytes\n`
- `Entry for shared event handle %d %p is not equal to %p`
- `copyAgentMaskMemory`
- `IOSurfaceRootUserClient`
- `ensure_memory_pool_memory`
- `IOSurfaceBufferTileMode`
- `IOSurfacePlaneComponentRanges`
- `IOSurfacePlaneCompressedTileHeaderRegionOffset`
- `site.IOSurfacePlaneInfo`
- `iofence_direction`
- `site.IOSurfaceEventNotifierClient`
- `EnablePrepareWiring`
- `KillDeadlockProcesses`
- `OSBoundedPtr.h`
- `IOSurfaceDisplayTimes`
- `IOSurfaceClient`
- `IOSurfaceMemoryTag`
- `IOSurfaceRootParavirtMapperInterface`
- `12`
- `112`
- `create_surface`
- `12222111111112`
- `IOSurfaceDecoderTimes`
- `SidebandVideoPropertiesLookupID`
- `IOSurfacePreallocPages`
- `map_client_shared failed for client_shared_ro`
- `====> %s:%d Memory pool ids exhausted\n`
- `1211228111111111111121`
- `IOSurfacePlaneBytesPerElement`
- `IOSurfaceMemoryPoolEntitlement`
- `IOSurfaceDescriptor`
- `iosurface_debug`
- `Perf: Process %s (%d) has created %d IOSurfaces out of a limit of %d, possible leak?\n`
- `\"IOFence does not support taggedRelease with when != 1\" @%s:%d`
- `12211111`
- `Components`
- `bool IOSurfaceSharedEventListener::init(thread_call_priority_t, IOWorkLoop *, bool, eIOSurfaceSharedEventAgentMask)`
- `121112112211111111`
- `IOSurface.cpp`
- `\"IOFence wait queue is not empty for surface: %p\" @%s:%d`
- `site.IOSurfaceMemoryRegion`
- `site.IOSurfaceRoot`
- `User Clients`
- `set_surface_handle`
- `Killed process %s (%d) for causing IOFence deadlock!\n`
- `IOSurfacePlaneBytesPerRow`
- `UseCount`
- `Memory Regions`
- `\"IOSurfaceRoot::removeEventNotifierClient() invoked with bad client notifier %p\" @%s:%d`
- `append_transaction`
- `Descriptor address`
- `\"IOSurfaceMemoryPool does not support taggedRelease with when != 1\" @%s:%d`
- `IOSurfaceBytesPerElement`
- `IOSurfaceSharedEventListener`
- `IOSurfaceAllocSize`
- `IOSurfacePlaneElementHeight`
- `IOSurfaceDisplayDitherThresholds`
- `IOSurfaceDefaultBulkAttachments`
- `trying to use apparently bogus surface handle %d`
- `AllGlobal`
- `IOSurfaceType`
- `IOSurfaceDisplayDitherYThresholds`
- `IsDisplayable`
- `IOSurfaceNonPurgeable`
- `IOSurfacePlaneComponentBitDepths`
- `CA Framebuffer`
- `iofence_acceleratorid`
- `site.IOSurfaceDeviceMemoryRegion`
- `IOSurfaceUseReserve`
- `IOSurfaceAllocateFromSuperbuffer`
- `iokit.IOSurface`
- `write`
- `Allocated`
- `IOSurface using pageable shmems\n`
- `Pool Id`
- `====> %s:%d Unable to pre-allocate IOSurfaceMemoryPool memory for pool id %llu\n`
- `IOSurfaceMemoryPoolInfo`
- `site.IOSurfaceRootParavirtMapperInterface`
- `IOUserClientDefaultLocking`
- `create_surface_fast_path`
- `site.IOSurfaceDescriptorComponent`
- `1221`
- `site.IOSurfaceMemoryPool`
- `Bucket buffer size`
- `IOSurfaceDisableMapperFlush`
- `121111111212`
- `IOSurface allowing global lookups (with warnings)\n`
- `AllowGlobal`
- `LogPrepareWiring`
- `Buckets`
- `taskCanUsePool`
- `12111211111`
- `IOSurfaceSliceCount`
- `121121111221111111211111111`
- `IOSurfaceMemoryPool`
- `site.IOMemoryDescriptor *`
- `IOSurfaceTransaction.cpp`
- `\"IOSurfaceSharedEvent does not support release with when != 1\" @%s:%d`
- `IOSurfaceDisplayDitherCrThresholds`
- `IOSurfacePlaneBase`
- `Type`
- `1211111212221212121122222212212111212211111112211112221111112111122111121222212222122221222212222122221222212222112111112221112211112112222222222112`
- `IOSurfaceSharedRO alloc failed`
- `DefaultNoSizeCasting`
- `CSBufferHeight`
- `handleAgentMaskRegistration`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `site.IOSurfaceColorAndSpatialKeysStruct`
- `IOSurfaceDeviceCache`
- `Name`
- `iomdEarlyPurge`
- `com.apple.private.gpu-restricted`
- `12112`
- `IOSurfaceBytesPerRow`
- `IOSurfaceSharedEventNotificationPort`
- `site.IOSurfaceNotifyRequest`
- `QuartzCore`
- `IOSurfaceMemoryPoolSize`
- `IOSurfacePixelFormat`
- `IOSurfaceYCbCrMatrix`
- `IOSurface disallowing global lookups\n`
- `\"os_refcnt: attempted resurrection (rc=%p)\\n\" @%s:%d`
- `site.IOSurfaceTransaction`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `IOSurfaceWidth`
- `site.IOSurfaceDescriptorPrivate`
- `site.IOSurfaceSendRight`
- `1212821211211`
- `IOSurfaceAddress`
- `iosurface-non-coherent`
- `\"IOSurfaceRoot::terminateDeviceCachesWithAccelerator() timeout.\" @%s:%d`
- `PageableShmems`
- `IOSurfaceElementHeight`
- `IOSurfaceDefaultAttachments`
- `mapInTask`
- `IOSurface disallowing pixel size casting by default\n`
- `site.IOSurfaceSharedListEntry`
- `11112`
- `site.IOSurfaceClientSharedListEntry`
- `\"os_refcnt: overflow (rc=%p)\\n\" @%s:%d`
- `1211121122`
- `\"failed to allocate memory\" @%s:%d`
- `IOSurfacePlaneOffset`
- `IOSurfaceAddressOffset`
- `IOSurfaceDirection`
- `IOSurfaceMemoryPoolZerofillEnabled`
- `\"IOSurface does not support release with when != 1\" @%s:%d`
- `/vram`
- `IOSurfaceTimingInfo`
- `IOSurfacePlaneCompressionType`
- `IOSurfacePlaneHeaderRegionBytesPerSlice`
- `IOSurfaceHostOnly`
- `Entry for handle %d is not NULL (%p)`
- `setIomdCacheAttribute`
- `IONewZero failed to alloc IOSurfaceSharedListEntry`
- `newMemoryPool`
- `kIOSurfaceTouchEventTimes`
- `IOSurfaceEnableStatistics`
- `122111`
- `/`
- `display-carveout-restricted`
- `IOBufferMemoryDescriptor::inTaskWithOptions failed to allocate a surface shared block.`
- `121111112`
- `====> %s:%d Descriptor length isn't rounded to bucket size\n`
- `121`
- `\tfence: %p\n`
- `IOSurfacePlaneBitsPerElement`
- `IOSurfacePlaneExtendedPixelsOnTop`
- `IOSurfaceSharedRW alloc failed`
- `MetalSharedTexture`
- `hw.cachelinesize`
- `IOFence: blocking wait timed out for surface: %d\n`
- `%s%u`
- `Length`
- `IOSurfaceTransaction`
- `121122`
- `IOSurfaceEvent.cpp`
- `DolbyVisionRPUData`
- `\"IOFence current queue is not empty for surface: %p\" @%s:%d`
- `Data`
- `site.IOSurfaceClientPlaneInfo`
- `IOSurfaceMemoryCallback`
- `sma`
- `Memory Pools`
- `site.IOSurfaceAgentMaskInfo`
- `\"%s\" @%s:%d`
- `IOSurfacePlaneHeightInCompressedTiles`
- `increment`

**[__TEXT.__os_log]**

- `IOSurface::parse_properties() parseAdditionalPlaneInfo failed.\n`
- `IOSurface: allocation size of %llu exceeds limit of %llu bytes\n`
- `IOSurface: address ranges size not multiple of IOAddressRange\n`
- `\t%p: surf: %p dir: %s accelerator: %d callback: %p target: %p ref: %p notified: %d completed: %d\n`
- `Waiting Fences:\n`
- `provider not IOSurfaceRoot\n`
- `%s error - invalid shared event port\n`
- `%s error - failed to alloc surface id\n`
- `IOSurface: plane[%d] extended width exceeds 64bit limit\n`
- `IOSurface: compressed plane[%d] Header region height must fit header group\n`
- `IOSurface: required bytes per line overflow\n`
- `IOSurface: couldn't count /vram's reg tuples; assuming a single carveout\n`
- `IOSurface: compressed plane[%d] HTPCPredictionSelector must be in range\n`
- `IOSurface::createWriteFence: WARNING: IOFence new failure!\n`
- `%s pool off limits for poolId 0x%llX\n`
- `IOSurface: kIOSurfacePlaneBytesPerElement out of range\n`
- `IOSurface: compressed plane[%d] rowOfUncompressedTiles doesn't fit in 32 bits\n`
- `%s: map_surface_client_shared() failed\n`
- `%s error - pool off limits (%llu)\n`
- `IOSurface: plane[%d] calculated size value exceeds 64bit limit\n`
- `IOSurface: sliceCount provided %d is out of bound for maximum / minimum number of required slices.\n`
- `IOSurface: kIOSurfacePlaneDataRegionBytesPerSlice %d is smaller than expected value %d .\n`
- `IOSurface: compressed plane[%d] Data region overlaps header region\n`
- `%s: alloc_handles() failed\n`
- `IOSurface: plane[%d] bytesPerRow exceeds 64bit limit\n`
- `IOSurfaceDeviceMemoryRegion: Couldn't get device memory with index %u for service %s\n`
- `_   /|\n`
- `'o.O'\n`
- `%s: failed to assign slot for event %08x, signal value 0x%016llx: ret 0x%x\n`
- `Cannot map graphics comm page\n`
- `%s error - failed to map shmem\n`
- `IOSurface: kIOSurfacePlaneBitsPerBlock out of range\n`
- `IOSurface: buffer bytes per row value is too small\n`
- `IOSurface: aligned height calculation overflow\n`
- `IOSurface count of %d approaching limit of %d\n`
- `%s error - invalid parentID (0x%llx)\n`
- `IOSurface: plane[%d] base %016llx plus plane size %016llx exceeds 64bit limit\n`
- `IOSurface: compressed plane[%d] CompressedTileWidth must be power of 2\n`
- `IOSurface: compressed plane[%d] CompressedTileHeight must be less than 1024\n`
- `IOSurface %08x: Current device cache changed while purgeability status was changing.\n`
- `IOSurface: %s component count is too small.\n`
- `IOSurface: %s component count mismatch.\n`
- `IOSurface: discovered %u display carveout(s) in /vram\n`
- `=(___)=\n`
- `IOSurface: maximum plane count of %d exceeded.\n`
- `IOSurface: compressed plane[%d] extended top is not supported for compressed iosurfaces\n`
- `IOSurface: required image bytes overflow\n`
- `IOSurface fence debug: surface: %p id: %d\n`
- `%s: slot index %u is not allocated for signal value 0x%016llx on event %08x\n`
- `IOSurface: plane[%d] calculated width in pixels exceeds 64bit limit\n`
- `IOSurface: compressed plane[%d] CompressedTileWidth must be less than 1024\n`
- `IOSurface: compressed plane[%d] kIOSurfacePlaneBytesPerRowOfTileData is %d less than WidthInCompressedTiles %d x BytesPerTileData %d Bytes.\n`
- `%s error - buffer allocation failed (%llu x %llu fmt: %08x size: %llu bytes)\n`
- `IOSurface: /vram declares %u carveout(s) but %u resolved; positions are ambiguous, installing none\n`
- `Cannot allocate IOSurfaceShared\n`
- `Cannot allocate notification array\n`
- `IOSurface: plane[%d] required size for one line exceeds 64bit limit\n`
- `IOSurface: compressed plane[%d] CompressedTileHeaderRegionHeight must exactly cover the height in tiles\n`
- `IOSurface: compressed plane[%d] Header region doesn't fit into plane size\n`
- `IOSurface: Cannot use kIOSurfaceClientAddress with compressed iosurfaces.\n`
- `IOSurface: %s exceeds maximum value\n`
- `Security: Process %s (%d) relying on global (insecure) IOSurface lookups\n`
- `Perf: Process %s (%d) IOSurface creation count: %d total count: %d\n`
- `IONewZero failed to alloc handles\n`
- `  Currently allocated slots:\n`
- `process %s (%d) caught causing IOFence deadlock!\n`
- `IOSurface: HTPC compressed plane[%d] Tile header must be 32-bit or 64-bit\n`
- `IOSurface: compressed plane[%d] kIOSurfacePlaneHorizontalPixelOffsetWithinCompressedTileArray is more than a kIOSurfacePlaneCompressedTileWidth.\n`
- `IOSurface: compressed plane[%d] uncompressedTileSize doesn't fit in 32 bits\n`
- `IOSurface: kIOSurfacePlaneHeaderRegionBytesPerSlice %d exeeds maximum value.\n`
- `%s error - flush failed\n`
- `IOSurface: buffer allocation size is too small to cover valid image area of plane %d: fAllocSize=%llu, planeLimit=%llu\n`
- `IOSurface: Cannot set both global and private properties\n`
- `IOSurface::cleanProcessorCaches memory prepare failed\n`
- `Security: Process %s (%d) failed global (insecure) IOSurface lookup for surface id %08x\n`
- `%s: slot index %u is out of range for event %08x\n`
- `%s: failed to add agent mask for value %llu: 0x%x\n`
- `    Slot[%u]: SignalValue=0x%016llx Timestamp=%llu\n`
- `IOSurface: plane[%d] element width is zero.\n`
- `IOSurface: plane[%d] parseAdditionalPlaneInfo failed.\n`
- `IOSurface: compressed plane[%d] extra width calculation overflow\n`
- `IOSurface: plane[%d] Image data doesn't fit within allocated plane size\n`
- `IOSurface: required allocation size overflow\n`
- `IOSurface::setTimestamp() - timing dictionary create failed\n`
- `IOSurface: plane[%d] bytes per element is zero.\n`
- `IOSurface: compressed plane[%d] CompressedTileWidth must be at least 1\n`
- `IOSurface: compressed plane[%d] Plane width must fit into tiles\n`
- `IOSurface: compressed plane[%d] bytesPerCompressedTileHeaderGroup * planeWidthInCompressedTiles doesn't fit in 32 bits\n`
- `IOSurface: multi-slice interchange compressed plane[%d] (DataRegionBytesPerSlice %d + HeaderRegionBytesPerSlice %d) * sliceCount %d size is greater than total planeSize %lld\n`
- `Cannot create children of protected surfaces\n`
- `Unsupported protection bits set: %016llx\n`
- `IOSurface: bytesPerRow calculation overflow\n`
- `IOSurface::::parse_properties() kIOSurfacePlaneInfo array must not be empty.\n`
- `IOSurface: plane[%d] offset %016llx is less than plane[%d] base %016llx\n`
- `IOSurface: compressed plane[%d] Width + CompressedTileWidth doesn't fit in 32 bits\n`
- `IOSurface: buffer allocation size is too small to cover valid image area: fAllocSize=%llu, requiredSizeInBytes=%llu\n`
- `%s error - Address ranges do not cover requested allocation size\n`
- `IOSurface::copyTimingInfo() - dictionary copy failed\n`
- `IOSurfaceDeviceMemoryRegion: zero-length device memory with index %u for service %s\n`
- `   U     ack!\n`
- `IOSurface: plane[%d] calculated bytesPerRow exceeds 64bit limit\n`
- `IOSurface: compressed plane[%d] extended left is not supported for compressed iosurfaces\n`
- `IOSurface: kIOSurfacePlaneHeaderRegionBytesPerSlice must be present for multi-slice plane %d with sliceCount %d .\n`
- `IOSurface: buffer element width is zero.\n`
- `IOSurface::setTimestamp() - dictionary create failure\n`
- `SID: 0x%X task: %p buffer: %p  buffer->fClientTask = %p not found\n`
- `Cannot allocate IOLock\n`
- `%s error - failed to alloc client buffer\n`
- `%s error - invalid parent (can't be child)\n`
- `IOSurface: plane[%d] total width in elements exceeds 64bit limit\n`
- `IOSurface: compressed plane[%d] CompressedTileHeight must be power of 2\n`
- `IOSurface: compressed plane[%d] extendedHeight overflow\n`
- `IOSurface: HTPC compressed plane[%d] Header region overlaps data region\n`
- `IOSurface: child surface plane[%d] Image data doesn't fit within allocated parent plane size\n`
- `IOSurface: client direction not InOut or Out\n`
- `%s error - no properties\n`
- `IOSurface: kIOSurfacePlaneBitsPerElement out of range\n`
- `IOSurface: plane[%d] minimum extended left bytes per row value exceeds 64bit limit\n`
- `IOSurface: buffer required width in bytes overflow\n`
- `IOSurface: child surfaces must specify an allocation size less than or equal to the parent surface size\n`
- `%s error - invalid address range (0x%llx - 0x%llx) : (0x%llx - 0x%llx)\n`
- `IOSurface::allocate() - requested cache mode %08x incompatible with memory region cache mode %08x\n`
- `Failed to install %s memory region; checking in anyway\n`
- `Cannot allocate IORWLock\n`
- `Killed process %s (%d) for causing IOFence deadlock!\n`
- `IOSurface: plane[%d] base %016llx overlaps with previous plane %d\n`
- `IOSurface: compressed plane[%d] roundedExtendedHeight overflow\n`
- `IOSurface: compressed plane[%d] dataRegionTotalSize doesn't fit in 32 bits\n`
- `IOSurface: buffer bytes per element is zero.\n`
- `%s error - no args\n`
- `%s error - copyObjectForPortNameInTask failed\n`
- `%s error - ensureMemory failed\n`
- `IOSurface: AGX BytesPerCompressedTileHeader of plane[%d] must be 2 or 8 or 32\n`
- `IOSurface: compressed plane[%d] HTPCVerticalHeaderGroupingMode must be in range\n`
- `IOSurface: compressed plane[%d] Plane height must fit into tiles\n`
- `IOSurface: compressed plane[%d] Data region doesn't fit into plane size\n`
- `IOSurface: buffer element height is zero.\n`
- `Unknown cache mode: %08x\n`
- `%s error - unaligned length (0x%llx)\n`
- `%s error - incompatible cache mode (0x%x in 0x%x)\n`
- `IOSurface: plane[%d] illegal compression footprint for type kIOSurfaceCompressionTypeInterchangeLossy %lld \n`
- `sid %08x complete() without assertion. dims: %llux%llu, fmt: %s, name: %s\n`
- `Attempt to %s IOSurface useCount while kIOSurfaceProhibitUseCount is set, ignored (creatorPID=%u currentPID=%u category=%u).\n`
- `%s: mapInTask() failed\n`
- `%s error - exceeded client limit (%d)\n`
- `Perf: Process %s (%d) has created %d IOSurfaces out of a limit of %d\n`
- `%s error - invalid memory range (addr=0x%llx size=0x%llx)\n`
- `IOSurfaceMemoryPool: %s (%d) can't access pool id %llu (wrong entitlements)\n`
- `%s: slot index %u validation failed: allocated=%s, signal value 0x%016llx (expected 0x%016llx) for event %08x\n`
- `IOSurface: aligned allocation size overflow\n`
- `IOSurface: required allocation size overflow\n\n`
- `IOSurface: fClientAlignedOffset >= page_size\n`
- `sid %08x prepare(): %s. format: %s\n`
- `IOSurfaceRoot: Initial shared event memory alloc failed\n`
- `IOSurface: plane[%d] element height is zero.\n`
- `IOSurface: plane[%d] total required size exceeds 64bit limit\n`
- `IOSurface: plane[%d] illegal compression type: %lld\n`
- `IOSurface: compressed plane[%d] CompressedTileHeight must be at least 1\n`
- `IOSurface: compressed plane[%d] kIOSurfacePlaneVerticalPixelOffsetWithinCompressedTileArray is more than a kIOSurfacePlaneCompressedTileHeight.\n`
- `%s error - can't prepare mapping\n`
- `%s error - failed to alloc surface buffer\n`
- `Unable to grow task client map\n`
- `%s error - failed to parse properties\n`
- `IOSurface::setTimestamp() - setValue for timing info failed\n`
- `Breaking IOFence deadlock\n`
- `%s error - invalid parent id (0x%x)\n`
- `Perf: Process %s (%d) has created %d IOSurfaces out of a limit of %d, possible leak?\n`
- `%s error - invalid memory pool port\n`
- `%s error - task does not own memory pool\n`
- `%s error - failed to alloc shmem\n`
- `IOSurface: plane[%d] extended height exceeds 64bit limit\n`
- `IOSurface: compressed plane[%d] extended width calculation overflow\n`
- `IOSurface: required planar allocation size overflow\n`
- `IOSurface: allocation size overflow\n`
- `IOSurface::setTimestamp() - timestamp create failed\n`
- `IOSurface::setTimestamp() - setValue for timing dictionary failed\n`
- `IOSurfaceDeviceMemoryRegion: Couldn't map device memory\n`
- `IOSurfaceRoot: deadlock detection depth limit %d reached\n`
- `IOSurface: plane[%d] calculated offset value exceeds 64bit limit\n`
- `IOSurface: buffer width overflow\n`
- `%s error - invalid range (0x%llx - 0x%llx)\n`
- `%s: createMappingInTask() failed\n`
- `IOSurface: /vram declares %u carveout(s) but none resolved\n`
- `IOSurfaceRoot using IOSurfaceRootParavirtMapperInterface\n`
- `%s error - exceeded client limit (0x%x)\n`
- `%s: No free agent mask slots available for event ID %08x (signal value 0x%016llx)\n`
- `IOSurface::parse_properties() problem with kIOSurfaceSubsampling\n`
- `IOSurface: plane[%d] size is zero\n`
- `IOSurface: kIOSurfacePlaneDataRegionBytesPerSlice must be present for multi-slice plane %d with sliceCount %d .\n`
- `Current Fences:\n`
- `%s error - set surface handle\n`
- `IOSurfaceRootUserClient: duplicate listener refcon %08llx\n`
- `%s error - invalid args\n`
- `%s: failed to assign agent mask slot for value %llu: 0x%x\n`
- `%s: slot index %u out of range or no agent mask info for event %08x (signal value 0x%016llx)\n`
- `IOSurface: plane[%d] extended left exceeds 64bit limit\n`
- `IOSurface: compressed plane[%d] planeHorizontalPixelOffsetWithinCompressedTile exceeds compressedPlaneBytesPerTileRow\n`
- `IOSurface: compressed plane[%d] BytesPerRowOfCompressedTileHeaderGroups needs to be enough for a row of groups of tiles at this width\n`
- `IOSurface: kIOSurfacePlaneDataRegionBytesPerSlice %d exceeds maximum value.\n`
- `IOSurface: Required property %s missing\n`
- `%s error - set surface id\n`
- `IOSurface: plane[%d] required size exceeds 64bit limit\n`
- `IOSurface: compressed plane[%d] CompressedTileHeaderRegionWidth must exactly cover the width in tiles\n`
- `IOSurface: compressed plane[%d] tilesToCoverHeight + headersInGroup doesn't fit in 32 bits\n`
- `IOSurface: kIOSurfacePlaneHeaderRegionBytesPerSlice %d is smaller than expected value %d .\n`
- `IOSurface::flushProcessorCaches memory prepare failed\n`
- `%s error - invalid direction (0x%x vs 0x%x)\n`
- `IOSurface: %s component count is too large.\n`
- `Cannot allocate invalidated surface array\n`
- `IOSurface: compressed plane[%d] Height + CompressedTileHeight doesn't fit in 32 bits\n`
- `IOSurface: compressed plane[%d] full width calculation overflow\n`
- `IOSurface: Planar surfaces must specify a valid buffer width and height.\n`
- `IOSurface: plane limit calculation overflow\n`
- `%s error - unaligned addr (0x%llx)\n`
- `%s: Couldn't allocate range allocator for graphics memory\n`
- `IOSurfaceMemoryPool: %s (%d) invalid task (%p) can't access pool id %llu (wrong entitlements)\n`
- `IOSurface: plane[%d] minimum bytes per row value exceeds 64bit limit\n`
- `IOSurface: plane[%d] bytes per row value of %llu is too small\n`
- `IOSurface: plane[%d] plane width in bytes exceeds 64bit limit\n`
