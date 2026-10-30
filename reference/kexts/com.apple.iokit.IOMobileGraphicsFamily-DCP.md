# `com.apple.iokit.IOMobileGraphicsFamily-DCP`

- Name: IOMobileGraphicsFamily-DCP
- Version: `343.0.0`
- UUID: `53CFA2B9-973C-3BAA-AE6C-4AFE6C308284`
- Source version: `700.50.112.6.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleDCP`](com.apple.driver.AppleDCP.md) 1.0, [`com.apple.driver.AppleM2ScalerCSCDriver`](com.apple.driver.AppleM2ScalerCSCDriver.md) 1.0.0, [`com.apple.driver.AppleMobileFileIntegrity`](com.apple.driver.AppleMobileFileIntegrity.md) 1.0.1, [`com.apple.driver.IOSlaveProcessor`](com.apple.driver.IOSlaveProcessor.md) 1.0.0, [`com.apple.driver.RTBuddy`](com.apple.driver.RTBuddy.md) 1.0.0, [`com.apple.iokit.IOAVFamily`](com.apple.iokit.IOAVFamily.md) 1.0.0, [`com.apple.iokit.IOMobileGraphicsFamily`](com.apple.iokit.IOMobileGraphicsFamily.md) 1.0.0, [`com.apple.iokit.IOSurface`](com.apple.iokit.IOSurface.md) 52.7.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.4.1, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 10.0.0d3, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (6) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleDCPLinkService` | 0x5d0 | IOService → IORegistryEntry |
| `DCPLink` | 0x60 |  |
| `DCPPowerManager` | 0x88 |  |
| `IOMFBTTRReport` | 0x88 | IOService → IORegistryEntry |
| `IOMobileFramebufferAP` | 0x5e30 | IOMobileFramebufferService → IOMobileFramebuffer → IOService → IORegistryEntry |
| `SharedEventResourceManager` | 0x50 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00009dd8 off=0x00a02820-0x00a0c5f8 addr=0xfffffe0007a06820-0xfffffe0007a105f8 r--/r--   __TEXT            
	sz=0x000063cb off=0x00a02f38-0x00a09303 addr=0xfffffe0007a06f38-0xfffffe0007a0d303               __TEXT.__cstring          (CstringLiterals)
	sz=0x000032e8 off=0x00a09310-0x00a0c5f8 addr=0xfffffe0007a0d310-0xfffffe0007a105f8               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x0002b1d4 off=0x03219c30-0x03244e04 addr=0xfffffe000a21dc30-0xfffffe000a248e04 r-x/r-x   __TEXT_EXEC       
	sz=0x0002a2d4 off=0x03219c30-0x03243f04 addr=0xfffffe000a21dc30-0xfffffe000a247f04          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000f00 off=0x03243f04-0x03244e04 addr=0xfffffe000a247f04-0xfffffe000a248e04          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00002840 off=0x049f38d0-0x049f6110 addr=0xfffffe000b9f78d0-0xfffffe000b9fa110 rw-/rw-   __DATA            
	sz=0x000000e8 off=0x049f38d0-0x049f39b8 addr=0xfffffe000b9f78d0-0xfffffe000b9f79b8               __DATA.__data             
	sz=0x00002720 off=0x00000000-0x00002720 addr=0xfffffe000b9f79b8-0xfffffe000b9fa0d8               __DATA.__common           (Zerofill)
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b9fa0d8-0xfffffe000b9fa110               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00003160 off=0x013a3cc8-0x013a6e28 addr=0xfffffe00083a7cc8-0xfffffe00083aae28 rw-/rw-   __DATA_CONST      
	sz=0x00000030 off=0x013a3cc8-0x013a3cf8 addr=0xfffffe00083a7cc8-0xfffffe00083a7cf8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000030 off=0x013a3cf8-0x013a3d28 addr=0xfffffe00083a7cf8-0xfffffe00083a7d28         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001e90 off=0x013a3d28-0x013a5bb8 addr=0xfffffe00083a7d28-0xfffffe00083a9bb8         __DATA_CONST.__const            
	sz=0x000008c0 off=0x013a5bb8-0x013a6478 addr=0xfffffe00083a9bb8-0xfffffe00083aa478         __DATA_CONST.__kalloc_type      
	sz=0x000000f0 off=0x013a6478-0x013a6568 addr=0xfffffe00083aa478-0xfffffe00083aa568         __DATA_CONST.__kalloc_var       
	sz=0x00000780 off=0x013a6568-0x013a6ce8 addr=0xfffffe00083aa568-0xfffffe00083aace8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000138 off=0x013a6ce8-0x013a6e20 addr=0xfffffe00083aace8-0xfffffe00083aae20         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x013a6e20-0x013a6e28 addr=0xfffffe00083aae20-0xfffffe00083aae28         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 519 at 0x04af3860
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     53CFA2B9-973C-3BAA-AE6C-4AFE6C308284
008: LC_SOURCE_VERSION           700.50.112.6.0
009: LC_FUNCTION_STARTS          offset=0x004ac18b0 size=0x490
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOMobileGraphicsFamily-DCP`
- `CFBundleIdentifier`: `com.apple.iokit.IOMobileGraphicsFamily-DCP`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOMobileGraphicsFamily-DCP`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `343.0.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `343.0.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91018`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91018`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2009 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOMobileGraphicsFamily-DCP.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895302624`
- `_PrelinkExecutableRelativePath`: `IOMobileGraphicsFamily-DCP`
- `_PrelinkExecutableSize`: `239948`
- `_PrelinkExecutableSourceAddr`: `-2198895302624`
- `_PrelinkKmodInfo`: `-2198828255024`

## Strings (512) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `%s: registerFunctionParent failed with error 0x%x\n`
- `\"IOMFB: carveout memory region \\\"%s\\\" not found\\n\" @%s:%d`
- `\"IOMFB: swap_complete_head_of_line_gated: swap not found: %u\" @%s:%d`
- `121111121222121211111111111111111111111111111121111111211211211212122222111122121212222112212121222211221212122221122121212222112212121222211221212122221122121212222112212121222211212222`
- `%s: Couldn't create ap_lock\n`
- `: set_gain_map_cap_buffer: power assert failed: %d\n`
- `%s: setting 2nd external display state %d in DCP \n`
- `rpc_caller_gated`
- `\"%s: shared buffer overflow [%u]\" @%s:%d`
- `%s: data: in_args->data_size is NULL\n`
- `SharedEventResourceManager.cpp`
- `121212112121212121212121212121212121212121212121212121212121212121212122112121212121212121212121212121212121212121212121212121212121212122112121212121212121212121212121212121212121212121212121212121212122112121212121212121212121212121212121212121212121212121212121212122112121212121212121212121212121`
- `DART error handler registration failed: ret: 0x%08x\n`
- `bool IOMobileFramebufferAP::isDevice(char *)`
- `segData[0].fLength (%d) < pBuffMD[i]->getLength() (%d)\n`
- `hotPlug_notify_gated`
- `site.IOMobileFramebufferAP`
- `121111121222121212121222222222222221221111111111112111111111111111111111111121222222222222222222222222222222222222111111222222222222222111222211122211222222222221111122122222222211112221222122212221222122212221222222222212222222222211222222222222222222222222222222222222222222222222222222222222222222`
- `IOMFB: %s: Failed to update layout for surface = %p. width = %d, height = %d\n`
- `%s: Failed to update default FB on DCP\n`
- `AppleDCPLinkService.cpp`
- `IOMFB: failed to alloc dcp_reset_lock\n`
- `%s: Couldn't create async_remap_lock\n`
- `setParameter`
- `virtual bool IOMobileFramebufferAP::start_client_state()`
- `function-clpc_enabled`
- `IOMFB: Surface %d has cacheMode 0x%x, needs to be 0x%x for display RT fetch\n`
- `rpc_callee_gated`
- `static T *IOMFB::InstanceTracker::instance(tracked_entity_t, uint32_t) [T = IOMFB::ServiceRelay]`
- `IOMFB: failed to create matching service dictionary: %s\n`
- `%s: invalid bytes received from property %s\n`
- `%s: AP instance name %s\n`
- `%s: get_descriptor failed \n`
- `IOMFB: failed to deserialize AFKArray\n`
- `D595_callback__`
- `async_swap_hw forced to false -> layerstate not enabled\n`
- `AppleDCPLinkService`
- `site.CachedState`
- `link_send_message`
- `IOMFB Debug Info`
- `IOMFB_POWER_DART: powerUpDART_v2_assertion enable=%d globalIdx=%u refCount=%d activeCount=%d\n`
- `BBBBBBBBBBGGGGGGGGGGRRRRRRRRRR`
- `dispext`
- `%s: indexes: idx_count (%lu) > out_args.indexes[] count (%lu)\n`
- `site.A494_in_args__`
- `get_buf_block_dcp`
- `propertyHas false Value \n`
- `async_swap_opt_flags`
- `IOMFBCarveoutRegion`
- `IOCoreSurfaceRoot`
- `1`
- `\"IOMFB: Failed to map LPR buffer %u into DispDART: 0x%x\\n\" @%s:%d`
- `IOMFB: replay fence already held!? - SharedEvent path\n`
- `%s: Couldn't create command gate\n`
- `%s: dropped hotPlug_notify message %llu\n`
- `fPendingPower_on_internal started  \n`
- `site.DCPPowerManager`
- `dot-pitch-float`
- `IOMFB: %s : Freeing up Default Temp surface - SwapID = %d, Surface = 0x%p\n`
- `MemDescRelay.cpp`
- `\"unsupported message seq [%u]\" @%s:%d`
- `map_block_buf: pbt=%u temp_buf->map failed\n`
- `virtual bool AppleDCPLinkService::start(IOService *)`
- `IOMFB: external_sync_error_notify_gated: sending to client %p\n`
- `kIOSurfaceTouchEventTimes`
- `\"%s: BufferDescriptor::withOptions options %x, size %llu align %x failed\\n\" @%s:%d`
- `AppleDCPLinkService::check_firmware_hash_crc32() 0x%08X\n`
- `%s: Couldn't create fence_lock\n`
- `use-legacy-DART`
- `virtual void IOMobileFramebufferAP::genlock_error_notify_gated(uint64_t)`
- `surface_complete`
- `iomfb_dcp_power_async`
- `%s: IOSurfaceRoot not available or of the wrong class\n`
- `add_notification`
- `IOMFB: cancel_all_pending_shared_events - ap_lock busy, waiting...\n`
- `IOMFB: %s : layout_buffers - failed for Surface = 0x%p, sid = %d\n`
- `12111112122212121`
- `get_block_dcp`
- `slave_memory`
- `site.IOMobileFramebufferAP::NotifyEventData`
- `\"%s: map_memory failed with 0x%x\\n\" @%s:%d`
- `map`
- `\"OSArray deserialization failed [%p]\" @%s:%d`
- `IOHibernateState`
- `PerformanceStatistics`
- `\"IOMFB: %s Failed to allocate memory descriptor\\n\" @%s:%d`
- `IOMFB: failed to create matching service: %s with role %s\n`
- `iomfb_driver`
- `IOMFB: Failed to map LPR buffer %u into DCP DART: 0x%x\n`
- `IOMobileFramebufferAP`
- `%s: failed to allocate fHDCPContext.lock\n`
- `set_block: pbt=%u rejected, DCP reset in progress\n`
- `link_shared_alloc`
- `IOMFB_POWER_DART: set_device_power on=%d kernelAssertCount=%u ret=%x\n`
- `site.Lock`
- `SCMBuildInfo_AppleDisplayPipe`
- `iomfb_rack_debug`
- `IOMFB: TTR buffer valid, total_size=%u flags=0x%x\n`
- `IOMFB: replay fence already held!?\n`
- `2111`
- `FB%d Api power state transition request from %s to %s for %s\n`
- `OFF`
- `link_workloop`
- `stream_uid`
- `AppleDCPLinkService: %s: failed with 0x%x [%u, %u]\n`
- `DCPEXT`
- `IOMFB: Failed to allocate options dictionary for LPR buffer %u\n`
- `hid-input`
- `\"%s: MemoryDescriptor::map_physical failed\\n\" @%s:%d`
- `AppleDCPLinkService: %s: link_cond_wait_priv failed with 0x%x\n`
- `\"bad stream returned\" @%s:%d`
- `\"stream id overflow: %u\" @%s:%d`
- `site.DCPMemoryDescriptor`
- `IOMFB: LPR buffer %u: dispDva=0x%llx dcpDva=0x%llx size=%llu\n`
- `IOMFBPreserveContents`
- `setIomdCacheAttribute`
- `False`
- `%s: wrong ID: %u\n`
- `IOMFB: %s Failed to prepare memory descriptor\n`
- `ret == kIOReturnSuccess`
- `site.ServiceRelay`
- `iomfb_disable_async_swap`
- `AppleDCPLinkService: link_init_callback failed with 0x%x\n`
- `AppleDCPLinkService: link_init_ready_callback failed with 0x%x\n`
- `\"OSDictionary deserialization failed [%p]\" @%s:%d`
- `deferred_abort_signal`
- `%s: buffer allocation failed\n`
- `IOMFB_POWER_DART: powerUpDART_impl_gated start enable=%d mapper=%p dartRef=%d activeCount=%d\n`
- `IOMFB: TTR raw binary written to %s (%u bytes)\n`
- `AppleDCPExpert`
- `%s::start() Initialization of fClientUpdateLock failed.\n`
- `%s: Can't send need swap notification since notify queue empty!\n`
- `default_fb_surface_gated`
- `: set_gain_map_cap_buffer: prepare failed: %d\n`
- `%s: hdcp reply is not ready\n`
- `\"%s: overflow detected, paylod too big: (%zu + %u + %u)\" @%s:%d`
- `link_shared_free`
- `\"Remote stream %d failed to become idle\\n\" @%s:%d`
- `IOMFB: service matched: %s (pipe:%u)\n`
- `%s: AP %s IOMFB_Notification_hotplug\n`
- `%s: AP %s trigger pending HPD notification hpdState %llu\n`
- `static T *IOMFB::InstanceTracker::instance(tracked_entity_t, uint32_t) [T = IOMFB::DCPPowerManager]`
- `IOMFB: TTR buffer total_size %u exceeds capacity %d\n`
- `%s: invalid blitID: %d\n`
- `IOMFB: LPR buffer %u: surfaceID=%u cacheMode=0x%x\n`
- `IOMFB: TTR buffer magic mismatch: 0x%x\n`
- `IOMFB: [%s] SurfaceID 0x%x GP Decompression Error Debug - Detected 16 bytes of zero values in metadata buffer \n`
- `stream_eventsource[ i ]`
- `AppleDCPLinkService: power_state_handler failed with 0x%x\n`
- `\"unsupported message type [%u]\" @%s:%d`
- `IOMFB: failed to alloc lock\n`
- `disp`
- `site.Record`
- `IOMFB: %s MemoryDescriptor::withAddressRange failed with options %x\n`
- `121222222222222222222222222222222111`
- `\"%s: shared_to_ptr_memcpy failed with 0x%x\" @%s:%d`
- `IOMFB: failed to deserialize AFKDictionary\n`
- `site.DCPBufferDescriptor`
- `site.A491_in_args__`
- `iomd`
- `IOMFB ERROR: dcp_expert not initialized, incorrect use_psd_dcp_power2 value`
- `map_block_buf: pbt=%u allocateBufferWithOptions failed user_size=%u\n`
- `True`
- `\"IOMFB: swap_complete_ap_gated: swap not found: %u\" @%s:%d`
- `AppleDCPLinkService: %s: shared buffer underflow [%u]\n`
- `IOMFBLaunchFDR`
- `void IOMobileFramebufferAP::blit_surface_complete(IOMFBSwapIORequest *, uint32_t)`
- `void IOMobileFramebufferAP::surface_complete(IOMFBSwapIORequest *, uint32_t)`
- `SharedEventResourceManager`
- `: set_gain_map_cap_buffer: calling dcp with dva=0x%llx len=%llu\n`
- `ERROR: mSharedEventListener is NULL`
- `call_code`
- `AppleDCPLinkService: %s: ptr_to_shared_memcpy failed with 0x%x\n`
- `CoreAnalyticsHub`
- `set_dcp_clamshell_state ClamshellState %d \n`
- `iomdEarlyPurge`
- `%s: block: block_size (%lu) > out_args.block[] count (%lu)\n`
- `3D7A5E91-0B2C-4F8D-A6E3-180274267000`
- `%s: no map or size passed\n`
- `ERROR: event is NULL`
- `\"IOMFB: LPR buffer %u surface_map succeeded but dispDva=0!\\n\" @%s:%d`
- `totalVBLs`
- `bool IOMFB::MemDescRelay::release_descriptor(desc_id_t)`
- `\"rpc_callee_wrap failed with 0x%x\" @%s:%d`
- `112`
- `IOMFB_POWER_DART: set_power_state done powerState=%lu state=%d ret=%x earlyReturn=1\n`
- `Async swap implementation, we should not enter here\n`
- `AppleDCPLinkService: endpoint power-down entered with driver_power set, this wait cannot complete: this=%p power2=%d`
- `%s: more than %d current instances of IOMobileFramebuffer!\n`
- `IOMFB: Enable low latency shared events mapping: %d, doorbell: %d\n`
- `IOMFB: Failed to set LPR buffers on DCP\n`
- `\"IOMFB: swap_complete_head_of_line_gated: invalid request to \" \"update and complete %u\" @%s:%d`
- `stream_workloop[ i ]`
- `dcp_reset_loop_panic`
- `\"IOMFB SharedEvent: Replay Signal missing for event ID %u surface %u\\n\" @%s:%d`
- `site.AppleDCPLinkService`
- `virtual bool IOMobileFramebufferAP::init(OSDictionary *)`
- `IOMFB: %s: Disable ASync Swap Value = %d\n`
- `dcp_reset_req`
- `async_swap_hw forced to false -> YUV layer with surface\n`
- `void IOMobileFramebufferAP::blit_surface_complete(IOMFBDisplayedData *, uint32_t, uint32_t)`
- `%s: AP %s HPD notification not registered yet, hpdPending %d hpdState %llu\n`
- `HwStatus= 0x%08X\n`
- `Address= 0x%08X\n`
- `ext`
- `IOMFB: TTR ttr_allocate_and_map: allocation failed\n`
- `display-frame-generation`
- `IOMFB: update HDCP protection status 0x%llx\n`
- `\"MemDescRelay records linked list mal-formed\\n\" @%s:%d`
- `%s, no mapper on this platform\n`
- `AppleDCPLinkService: hibernate-resume re-start of link service failed`
- `name`
- `site.IOMFBTTRReport`
- `AppleDCPLinkService: link_state_init failed with 0x%x\n`
- `IOMFB: failed to create matching dictionary: %s\n`
- `IOMFB: failed to create DART extensible panic log`
- `IOMFB: %s : getMemoryRegion Failed for Surface = 0x%p, sid = %d\n`
- `AppleDCPLinkService: link_init_ack_callback failed with 0x%x\n`
- `IOMFB: external_sync_error_notify_gated: delivered successfully to client %p\n`
- `result`
- `link_gate`
- `mapper`
- `link_handle_message`
- `%s: data: in_args->data_size (%lu) > in_args->data[] count (%lu)\n`
- `%s: data: in_args->count (%lu) > in_args->data[] count (%lu)\n`
- `%s: Couldn't create start_lock\n`
- `IOMFB: external_sync_error_notify_gated: state=0x%llx (late=%d expected_clock=%d incorrect_params=%d)\n`
- `IOMFB: external_sync_error_notify_gated: no listeners registered, storing pending state=0x%llx\n`
- `%s: invalid layerID: %d\n`
- `display-complete`
- `\"IOMFB: %s: no instance for instance ID: %u\\n\" @%s:%d`
- `allow-pte-remap`
- `IOMFB: external_sync: userspace client registered for notifications\n`
- `1212221111`
- `static T *IOMFB::InstanceTracker::instance(tracked_entity_t, uint32_t) [T = IOMobileFramebufferAP]`
- `%s: dropped external_sync_error_notify message %llu\n`
- `IOMFB: TTR buffer allocated and DART-mapped, dva=0x%llx\n`
- `DART error handler registration skipped: fMapper is NULL\n`
- `site.DCPLink`
- `get_clamshell_state fAPClamshellState %d from_kernel %d fReceivedClamshellStateFromSkyLight %d \n`
- `HwError= %s\n`
- `virtual IOMFBStatus IOMobileFramebufferAP::hdcp_get_reply(IOMemoryMap *, size_t *)`
- `%s: blobs: in_args->blob_count (%lu) > in_args->blobs[] count (%lu)\n`
- `propertyHas default Value \n`
- `IOMFBSkipSpinner`
- `\"Reference remap initiated with null descriptor\\n\" @%s:%d`
- `MemDescRelay::desc_id_t IOMFB::MemDescRelay::withAddressRange(uint64_t, uint64_t, uint32_t, MemDescRelay::task_t, dva_t *, uint64_t *)`
- `AppleDCPLinkService: default_ack failed with 0x%x\n`
- `\"IOMFB: Firmware hash checksum mismatched: local=0x%08X, remote=0x%08X\" @%s:%d`
- `site.struct record`
- `IOSurfaceDisplayTimes`
- `AppleDCPLinkService: %s: link_send_message failed with 0x%x\n`
- `\"%s: broken message 0x%llx\" @%s:%d`
- `site._shared_event_maps`
- `DART Exception @ 0x%08X\n`
- `\"%s Failed to parse registry for device\" @%s:%d`
- `%s: heap allocation of arguments failed\n`
- `heap_iomd`
- `%s, failed to allocate surface callback lock\n`
- `IOMFB: allocate_lpr_buffers_gated: enable=%d\n`
- `%s: no hdcp reply available while not pending\n`
- `AppleDCPLinkService: driver_signal failed with 0x%x\n`
- `iomfb_proxy`
- `: set_gain_map_cap_buffer: allocateDescWithAddressRange failed\n`
- `start`
- `set_block: map_block_buf failed, pbt=%u, block=%p, block_size=%zu, ret=0x%x\n`
- `d52`
- `InstanceTracker.h`
- `DCPResetLoopMaxCount`
- `IOMFB: TTR ttr_allocate_and_map: DART-map failed 0x%x\n`
- `Unknown display name, defaulting to 0 (disp0).\n`
- `IOMFB: %s failed with options 0x%x\n`
- `IOMFB: failed to alloc DART paniclog lock`
- `%s: Dropped need_swap_notify notification!\n`
- `/var/mobile/Library/Logs/iomfb_ttr_dump.bin`
- `displayOnTimestamp`
- `IOMFB: dropped apt mode switch message from DCP`
- `dcp_reset_display_id`
- `site.NotifyEventData`
- `MemDescRelay::desc_id_t IOMFB::MemDescRelay::allocate_buffer(uint32_t, uint64_t, uint32_t, dva_t *, uint64_t *)`
- `%s: vals: count (%lu) > out_args.vals[] count (%lu)\n`
- `\"link_message_handler failed with 0x%x\" @%s:%d`
- `setActive`
- `MemDescRelay::desc_id_t IOMFB::MemDescRelay::map_physical(uint64_t, uint64_t, uint32_t, dva_t *, uint64_t *)`
- `iomfb_version_check`
- `com.apple.driver.iomfb.nested_rpc_telemetry`
- `AppleDCPLinkService: %s: shared_to_ptr_memcpy failed with 0x%x\n`
- `\"%s: link_rpc_lookup callback not found: '%s'\" @%s:%d`
- `get_record_by_id`
- `IOMFB: cancel_all_pending_shared_events - fence_lock timeout, proceeding without lock\n`
- `\"IOMFB: swap_complete_intent_gated: unsupported intent %u\" @%s:%d`
- `\"callback failed with: 0x%x\" @%s:%d`
- `IOMFB:: DCPExpert::setPowerAssertion returned 0x%x\n`
- `DCPResetLoopWindowSec`
- `IOMFB_DART_STATE`
- `com.apple.private.allow-explicit-graphics-priority`
- `L2Index= 0x%08X\n`
- `L3Index= 0x%08X\n`
- `\"IOMFB SharedEvent: Replay Signal missing event ID for surface %u (Wait value 0x%llx)\\n\" @%s:%d`
- `\"cannot find stream for message\" @%s:%d`
- `222222122222222222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `site.IOMFBSwap`
- `function-frame_swap`
- `%s: property %s not found in EDT, assumed false.\n`
- `IOMFB: driver commit: %s\n`
- `dcp_reset_notify`
- `IOMFB_POWER_DART: set_power_state done powerState=%lu state=%d ret=%x earlyReturn=0\n`
- `    AXI_ID[%d]= 0x%08X\n`
- `IOMFB: resizing canvas: %d %d\n`
- `io_fence_callback`
- `endpoint_service`
- `\"IOMFB: fCommandPool is NULL - cannot map LPR buffers\\n\" @%s:%d`
- `IOMFB: dropped release buffer info message from DCP for swapID = 0x%x\n`
- `virtual void IOMobileFramebufferAP::hotPlug_notify_gated(uint64_t, IOMFB_TiledDisplayInfo *, bool)`
- `IOMFB: dcp_reset_recovery_complete\n`
- `layout_buffers`
- `AppleDCPLinkService: link_handle_message failed with 0x%x\n`
- `%s: Couldn't create a work loop for instantiating command pool\n`
- `BICSMigrationLastExpiry`
- `map_block_buf: pbt=%u withAddressRange failed user_addr=0x%llx, user_size=%u, buf_flags=0x%x\n`
- `IOMFB: LPR buffers already enabled\n`
- `IOMFB: dcp_reset_notify() called - DCP reset triggered\n`
- `registerErrorHandler`
- `IOMFB:: wait_for_kernel_power returned 0x%x\n`
- `compatible`
- `allocate_buffer`
- `IOMFB: mapDeviceMemoryWithIndex memory descriptor allocation failed (0x%x)\n`
- `map_block_buf: pbt=%u temp_buf->prepare failed ret=0x%x`
- `: set_gain_map_cap_buffer: dcp returned %d\n`
- `IOMFB: external_sync: pending notification found, delivering state=0x%llx\n`
- `IsWrite= %s\n`
- `21122`
- `DCPLink`
- `%s: has_data: in_args->count (%lu) > in_args->has_data[] count (%lu)\n`
- `dart_flush_by_smmu = %u\n`
- `map_block_buf: pbt=%u set_kernel_power_assert failed ret=0x%x\n`
- `display-presentation`
- `IOMFB: %s IOMemoryDescriptor::prepare failed with 0x%x\n`
- `external-index`
- `iomfb_dis_fwhash_check`
- `IOMFB_POWER_DART: set_power_state powerState=%lu powerCallbackDcp=%d\n`
- `iomfb_swap_wait_timeout_s`
- `iop_nub`
- `iomfb_add_heap_in_ios`
- `\"%s: callee link failure: 0x%x\" @%s:%d`
- `DCPPowerManager`
- `%s: fRackDebugSwapWaitTimeoutSec = %d`
- `map_block_buf: pbt=%u block_size=%zu too small for addr_offs=%u size_offs=%u`
- `IOMobileFramebufferAP.cpp`
- `IOMFB_POWER_DART: powerUpDART_impl_gated done enable=%d mapper=%p dartRef=%d ret=%x\n`
- `internal`
- `%s: DCP map_memory failed with 0x%x\n`
- `\"swap wait timedout for %d seconds waiting for fence 0x%08x\" @%s:%d`
- `endpoint`
- `ptr_to_shared_memcpy`
- `IOMFB: Firmware hash checksum mismatched: local=0x%08X, remote=0x%08X`
- `12122112222111111`
- `%s::start() Initialization of Userspace state failed.\n`
- `stream_tid`
- `\"link version mismatch: AP is %u, DCP is %u\" @%s:%d`
- `IOMFB: Failed to map LPR buffer %u into DispDART: 0x%x\n`
- `DART error handler unregister in recovery_complete: ret: 0x%08x\n`
- `static T *IOMFB::InstanceTracker::instance(tracked_entity_t, uint32_t) [T = IOMFB::MemDescRelay]`
- ` fIsSharedDisplay is %d \n`
- `ON`
- `SystemConsoleMode`
- `create_default_fb_surface`
- `2112211`
- `stream_gate[ i ]`
- `heap_slave_memory`
- `\"IOMFB: link_shutdown_signal stalled after %u waits, kernel_assertion_count: %d\\n\" @%s:%d`
- `1211`
- `IOMFB: TTR vn_rdwr failed: %d\n`
- `site.MemDescRelay`
- `set_parameter_dcp`
- `nub`
- `\"%s: payload too big: %u + %u > %u\" @%s:%d`
- `IOMFBSetConsoleMode`
- `dcp_reset_reason`
- `\"%s: Unable to request dcp reset since notify queue empty!\\n\" @%s:%d`
- `Conversions.h`
- `\"IOMFB: buffer too small for property data\" @%s:%d`
- `\"swap wait timedout 0x%08x\" @%s:%d`
- `need_swap_notify`
- `HwClass= %s\n`
- `shared_to_ptr_memcpy`
- `DCPPowerManager.cpp`
- `%s: Couldn't add command gate to work loop.\n`
- `map_block_buf: pbt=%u buf->prepare failed ret=0x%x, buf_flags=0x%x\n`
- `IOMFB_POWER_DART: powerUpDART enable=%d dcp_power_off=%d dartRef=%d activeCount=%d\n`
- `\"IOMFB SharedEvent: Replay Wait missing for event ID %u surface %u\\n\" @%s:%d`
- `iomfb_disable_debug_info`
- `totalSwaps`
- `IOMFBStatus IOMobileFramebufferAP::updateBufferMappingCount_gated(bool)`
- `122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `IOMFB: swap_wait: IOLockSleep[Deadline]: unexpected return value: 0x%x\n`
- `d16`
- `iomfb_trace_nested_rpc_calls`
- `framebuffer-width`
- `AppleDCPLinkService: %s: shared buffer overflow [%u]\n`
- `\"%s: payload size too small: %u < %lu\" @%s:%d`
- `\"Local stream %d failed to become idle\\n\" @%s:%d`
- `tlbi-flushes-smmu`
- `%s:  failed to map surface %d\n`
- `SwapIdleBuffer received with no idle caching surface; dropping swap %u`
- `propertyHas true Value \n`
- `IOMFB: LPR buffer size: %llu bytes (%ux%u, rowBytes=%u)\n`
- `\"IOMFB: fCoreSurfaceRoot is NULL\\n\" @%s:%d`
- `ServiceRelay.cpp`
- `IOMFB: TTR vnode_open failed: %d\n`
- `\"bad IOFence callback\" @%s:%d`
- `slave_processor`
- `IOMFB: mapDeviceMemoryWithIndex DCP memory descriptor allocation failed (0x%x)\n`
- `D400_callback__`
- `IOMFB: dropped prox sensing needed message from DCP`
- `SID= 0x%08X\n`
- `void IOMobileFramebufferAP::surface_complete(IOMFBDisplayedData *, uint32_t, uint32_t)`
- `IOMFB: AppleDCPLinkService heap size increment: 0x%x\n`
- `@`
- `Type= %s\n`
- `Spinner surface alloc with w: %d x h: %d\n`
- `propertyExists \n`
- `set_clamshell_state fAPClamshellState %d \n`
- `AppleDCPLinkService: failed to allocate memory descriptor relay\n`
- `CollectStatistics`
- `map_block_buf: pbt=%u buf->map failed, buf_flags=0x%x\n`
- ` * IOMFB: Could not set the memory descriptor for theDMA command (error:%d)\n`
- `IOReturn IOMobileFramebufferAP::spinner_surface_alloc(IOSurface **, uint32_t, uint32_t, bool)`
- `AppleDCPLinkService: %s:%u REQUIRE failed: %s`
- `\"%s: payload size mismatch: %u != %lu\" @%s:%d`
- `static bool IOMobileFramebufferAP::readDataInEDT(IOService *, bool, const char *, const uint32_t, uint32_t *)`
- `IOMFB: cancel_all_pending_shared_events - ap_lock timeout, proceeding without lock\n`
- `\"SharedEventResourceManager: Exceeded maximum of %u shared event maps (requested index: %llu)\" @%s:%d`
- `121111121222`
- `%s`
- `%s: Powering off external and powering on Internal from hpd notification\n`
- `DART error handler unregister: fMapper is null\n`
- `dot-pitch`
- `void IOMobileFramebufferAP::setSystemConsoleMode_gated(bool)`
- `: set_gain_map_cap_buffer: data=%p data_len=%u\n`
- `IOMFB SharedEvent: Replay abort Signal value %llu for surface %d pending Wait complete\n`
- `%s%x`
- `%s: swapID: in_args->count (%lu) > in_args->swapID[] count (%lu)\n`
- `IOMFB: AP DRIVER START!\n`
- `async_swap_pte_remap`
- `IOMFBTTREventType`
- `\"%s: message is not ok: 0x%llx\" @%s:%d`
- `armio_device`
- `\"IOMFB: %u DCP resets within %llu seconds - reset loop detected\\n\" @%s:%d`
- `framebuffer-height`
- `AppleClamshellState`
- `dart_allows_pte_remap = %u\n`
- `withAddressRangeAligned`
- `\"%s: record book mismatch\\n\" @%s:%d`
- `iomfb_low_latency_shared_events_doorbell`
- `IOMFB SharedEvent: Replay abort Signal value %llu for surface %d in callback\n`
- `%s::start() Initialization of fNotifyQueuesLock failed.\n`
- `site.A492_out_args__`
- `site.SharedEventResourceManager`
- `IOMFB: service matched: %s\n`
- `IOMFB: TTR report nub published for event %u\n`
- `swap_apply_fences`
- `displayOnContinuousTimestamp`
- `%s: Couldn't create a work loop\n`
- `iomfb_low_latency_shared_events_mapping`
- `IOMFB: User Power Assertion Request %d\n`
- `Unexpected behavior: enabling cursor as head of line\n`
- `RecordTracker.cpp`
- `\"%s: Dropped request dcp_reset notification!\\n\" @%s:%d`
- `IOMFB: cancel_all_pending_shared_events - fence_lock busy, waiting...\n`
- `%s: unmap_memory failed with 0x%x\n`
- `site.RecordTracker`
- `IOMFB: failed to alloc sched\n`
- `AppleSEPManager`
- `virtual bool IOMobileFramebufferAP::start(IOService *)`
- `iommu-parent`
- `com.apple.iomfb.dcp_reset_req`
- `\"%s, fDartActiveCount is zero when disable is specified\" @%s:%d`
- `IOMFBTTRReport`
- `AppleDCPLinkService: %s: overflow detected, payload too big: (%zu + %u + %u)\n`
- `\"IOMFB: service not found for ID: '%s'\" @%s:%d`
- `IOMFB: call to addMatchingNotification failed\n`
- `IOMFB: powerUpDART_impl_gated(%d) callPlatformFunction setActive failed: 0x%x dart_ref=%d\n`
- `IOReturn IOMobileFramebufferAP::surface_map_dcp(IOSurface *, IODMACommand **, dva_t *, bool)`
- `iomfb_swap_fn`
- `%s: size_override = %d > max = %d, proceeding with default size = %d\n`
- `iomd-early-reclaim`
- `virtual IOSurfaceID IOMobileFramebufferAP::default_fb_surface_gated(uint32_t, uint32_t)`
- `\"%s: no available record\" @%s:%d`
- `AppleDCPLinkService: %s: payload too big: %u bytes\n`
- `IOMFB: failed to alloc power_state_lock\n`
- `\"IOMFB: Failed to allocate _service_count_lock\" @%s:%d`
- `TTBRIndex= 0x%08X\n`
- `ERROR: timestamp create failed\n `
- `%s: data: out_args->data_size (%lu) > out_args->data[] count (%lu)\n`
- `%s: Rack Debug Enable Value = %d`
- `%s: Boot-arg %s found: set fRackDebugSwapWaitTimeoutSec = %d`
- `\"IOMFB: fMapper (DispDART) is NULL - cannot map LPR buffers\\n\" @%s:%d`
- `IOMFB: Failed to create IOSurface for LPR buffer %u\n`
- `IOMFB: deferred abort signal queue full, dropping signal value 0x%llx for surface %d\n`
- `set_block_dcp`
- `122222222222222222222222222222211`
- `DCP`
- `\"IOMFB: Failed to map LPR buffer %u into DCP DART: 0x%x\\n\" @%s:%d`
- `\"IOMFB: LPR buffer %u surface_map_dcp succeeded but dcpDva=0!\\n\" @%s:%d`
- `IOMFB: Unsupported format for spinner \n`
- `internal-index`
- `link_protocol_priv.h`
- `D594_callback__`
- `IOMFB: failed to alloc service_lock\n`
- `property doesnt Exists \n`
- `role`
