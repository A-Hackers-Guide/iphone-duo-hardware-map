# `com.apple.driver.AppleMobileDispH19P-DCP`

- Name: AppleMobileDispH19P-DCP
- Version: `140.0`
- UUID: `BBF8AC14-9B37-3CCF-8A04-14BE0CE846AF`
- Source version: `700.50.112.6.0`
- Depends on: [`com.apple.AUC`](com.apple.AUC.md) 1.0, [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleM2ScalerCSCDriver`](com.apple.driver.AppleM2ScalerCSCDriver.md) 1.0.0, [`com.apple.driver.AppleSEPManager`](com.apple.driver.AppleSEPManager.md) 1.0.0, [`com.apple.driver.IOSlaveProcessor`](com.apple.driver.IOSlaveProcessor.md) 1.0.0, [`com.apple.driver.RTBuddy`](com.apple.driver.RTBuddy.md) 1.0.0, [`com.apple.iokit.IOAVFamily`](com.apple.iokit.IOAVFamily.md) 1.0.0, [`com.apple.iokit.IOMobileGraphicsFamily`](com.apple.iokit.IOMobileGraphicsFamily.md) 1.0, [`com.apple.iokit.IOMobileGraphicsFamily-DCP`](com.apple.iokit.IOMobileGraphicsFamily-DCP.md) 1.0, [`com.apple.iokit.IOSurface`](com.apple.iokit.IOSurface.md) 52.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.4.1, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (3) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) | `AppleCLCD2` | `disp0,t8160` |
| [`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) | `AppleCLCD2` | `dispsec,t8160` |
| [`/arm-io/dispext0`](../devicetree/root__arm-io__dispext0.md) | `AppleCLCD2` | `dispext0,t8160` |

## IOKit personalities (2) [KC]

### AppleADBE0-8970X
- `BacklightMatching`:
  - `IOPropertyMatch`:
    - `backlight-control`: `True`
- `CFBundleIdentifier`: `com.apple.driver.AppleMobileDispH19P-DCP`
- `IOClass`: `AppleCLCD2`
- `IONameMatch`:
  - `disp0,t8160`
  - `dispext0,t8160`
  - `dispsec,t8160`
- `IOPersonalityPublisher`: `com.apple.driver.AppleMobileDispH19P-DCP`
- `IOProviderClass`: `AppleARMIODevice`

### AppleDCPLinkServiceSoC
- `CFBundleIdentifier`: `com.apple.driver.AppleMobileDispH19P-DCP`
- `IOClass`: `AppleDCPLinkServiceSoC`
- `IONameMatch`:
  - `DCPEndpoint24`
  - `DCPEXTEndpoint24`
  - `DCPSECEndpoint24`
- `IOPersonalityPublisher`: `com.apple.driver.AppleMobileDispH19P-DCP`
- `IOProviderClass`: `RTBuddyEndpointService`


## C++ classes (5) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleCLCD2` | 0x61b8 | UnifiedPipeline2 → IOMobileFramebufferAP → IOMobileFramebufferService → IOMobileFramebuffer → IOService → IORegistryEntry |
| `AppleDCPLinkServiceSoC` | 0x5d0 | AppleDCPLinkService → IOService → IORegistryEntry |
| `IOMobileFramebufferShim` | 0x65e8 | UnifiedPipeline2 → IOMobileFramebufferAP → IOMobileFramebufferService → IOMobileFramebuffer → IOService → IORegistryEntry |
| `IOMobileFramebufferTilingMgr` | 0x710 |  |
| `UnifiedPipeline2` | 0x61b8 | IOMobileFramebufferAP → IOMobileFramebufferService → IOMobileFramebuffer → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000099c9 off=0x00667490-0x00670e59 addr=0xfffffe000766b490-0xfffffe0007674e59 r--/r--   __TEXT            
	sz=0x00001920 off=0x00667b60-0x00669480 addr=0xfffffe000766bb60-0xfffffe000766d480               __TEXT.__const            
	sz=0x000079d9 off=0x00669480-0x00670e59 addr=0xfffffe000766d480-0xfffffe0007674e59               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00027118 off=0x0226ec30-0x02295d48 addr=0xfffffe0009272c30-0xfffffe0009299d48 r-x/r-x   __TEXT_EXEC       
	sz=0x000262b8 off=0x0226ec30-0x02294ee8 addr=0xfffffe0009272c30-0xfffffe0009298ee8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000e60 off=0x02294ee8-0x02295d48 addr=0xfffffe0009298ee8-0xfffffe0009299d48          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00004000 off=0x04979790-0x0497d790 addr=0xfffffe000b97d790-0xfffffe000b985ce5 rw-/rw-   __DATA            
	sz=0x000002e0 off=0x04979790-0x04979a70 addr=0xfffffe000b97d790-0xfffffe000b97da70               __DATA.__data             
	sz=0x00000100 off=0x00000000-0x00000100 addr=0xfffffe000b97da70-0xfffffe000b97db70               __DATA.__common           (Zerofill)
	sz=0x00008175 off=0x00000000-0x00008175 addr=0xfffffe000b97db70-0xfffffe000b985ce5               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000060f8 off=0x0116d7c8-0x011738c0 addr=0xfffffe00081717c8-0xfffffe00081778c0 rw-/rw-   __DATA_CONST      
	sz=0x00000018 off=0x0116d7c8-0x0116d7e0 addr=0xfffffe00081717c8-0xfffffe00081717e0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000018 off=0x0116d7e0-0x0116d7f8 addr=0xfffffe00081717e0-0xfffffe00081717f8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00005118 off=0x0116d7f8-0x01172910 addr=0xfffffe00081717f8-0xfffffe0008176910         __DATA_CONST.__const            
	sz=0x000006c0 off=0x01172910-0x01172fd0 addr=0xfffffe0008176910-0xfffffe0008176fd0         __DATA_CONST.__kalloc_type      
	sz=0x000000f0 off=0x01172fd0-0x011730c0 addr=0xfffffe0008176fd0-0xfffffe00081770c0         __DATA_CONST.__kalloc_var       
	sz=0x00000730 off=0x011730c0-0x011737f0 addr=0xfffffe00081770c0-0xfffffe00081777f0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000d0 off=0x011737f0-0x011738c0 addr=0xfffffe00081777f0-0xfffffe00081778c0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 486 at 0x04adf6f8
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     BBF8AC14-9B37-3CCF-8A04-14BE0CE846AF
008: LC_SOURCE_VERSION           700.50.112.6.0
009: LC_FUNCTION_STARTS          offset=0x004aaa7c0 size=0x700
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleMobileDispH19P-DCP`
- `CFBundleIdentifier`: `com.apple.driver.AppleMobileDispH19P-DCP`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleMobileDispH19P-DCP`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `140.0`
- `CFBundleSignature`: `appl`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `140.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91018`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91018`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2013 Apple Inc. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleMobileDispH19P-DCP.kext`
- `_PrelinkExecutableLoadAddr`: `-2198899084144`
- `_PrelinkExecutableRelativePath`: `AppleMobileDispH19P-DCP`
- `_PrelinkExecutableSize`: `258350`
- `_PrelinkExecutableSourceAddr`: `-2198899084144`
- `_PrelinkKmodInfo`: `-2198828755056`

## Strings (617) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `IOMFBTestBacklightDimValue`
- `\"%s: dva mismatch for record id: %u\\n\" @%s:%d`
- `lMaxPanel`
- `( \"Lock acquired in %d itr (fallback)\\n\" ) @%s:%d`
- `%s: Display Wall: Primary VFTG enable timedout due to unplug\n`
- `AED %s: could not resolve secondary for primary fb %u`
- `Max_FrameTime`
- `virtual IOMFBStatus IOMFB::UPPipe2::callPlatformFunction(const OSSymbol *, bool, void *, void *, void *, void *)`
- `%s: Primary fid is invalid\n`
- `timeout %d power %d %d\n`
- `InstanceTracker.h`
- `iomfb_backlight`
- `bool UnifiedPipeline2::start_hardware_boot()`
- `BICS_history_corrupt`
- `IOMFB arm_fn_search: Couldn't allocate AppleARMFunction for %s\n`
- `AED establish-pairing: no peer pipe for primary fb %u`
- `IOMFBTimebaseDenom`
- `lMaxProduct`
- `IdleState`
- `Swap queue drained before power state change\n`
- `Display Wall: Primary modeset failed with status 0x%x\n`
- `%s: given OSObject is not an OSDictionary\n`
- `%s: Found %d timings and %d colors on primary\n`
- `Dual pipe: fb %u issuing secondary modeset on fb %u (timing %u color %u)\n`
- `%s: commandSleep was SleepStatusRestart\n`
- `DW_LOG::%s:%d: Replugging back fb %u plug_state %u\n`
- `IOMFBFrameInfoBuffer.cpp`
- `isp-alss-zone-x`
- `%s: Dual pipe tear down is already processed\n`
- `%s: AED established dual-pipe shim state (primary fb %u secondary fb %u)`
- `Dual pipe secondary modeset failed with status 0x%x\n`
- `DCP`
- `IOMFB: Found key %s value %d\n`
- `static MemoryMap *IOMFB::UPPipe2::mapMemory(uint64_t, uint32_t, uint32_t)`
- `IOMFBBrightnessLevel`
- `HPD notification on display wall registered on fbid=%u, this=%p, external_pipe=%d, fTilingMgr=%p, state=%llu\n`
- `%s: Skipping redundant modeset (timing=%u, color=%u)\n`
- `%s: Secondary tile=%p colorModeKeyID=%u, timingModeKeyID=%u\n`
- `virtual void IOMFB::PropRelay::publish(RuntimeProperty, uint32_t, uint64_t)`
- `( \"Swap queue drain timed out (500ms)\\n\" ) @%s:%d`
- `Display Wall setup cannot be supported! Not `
- `static T *IOMFB::InstanceTracker::instance(tracked_entity_t, uint32_t) [T = IOMFB::MemDescRelay]`
- `Building mode tables for dual pipe\n`
- `Merge Config: Primary VFTG enable timedout\n`
- `deferred notification for dual pipe HPD\n`
- `DW_LOG::%s:%d: Done tearing down Display Wall.\n`
- `%s: Display Wall config is set\n`
- `AppleDCPLinkServiceSoC`
- `isp-alss-lum-weight`
- `no-dcp-driver`
- `Swapping client did start %p\n`
- `virtual IOMFBStatus IOMobileFramebufferShim::get_display_area(DisplayArea *)`
- `%s: SwapIDs: %d vs %d\n`
- `%s: DisplayWall available framebuffer are:`
- `setDisplayWall`
- `dual pipe notified earlier = %d\n`
- `Error: Tiled mode addition failed\n`
- `VGA`
- `DW_LOG::%s:%d:  tparams[0].id %u\n`
- `\"OSDictionary serialization failed [%p] [%p]\" @%s:%d`
- `virtual bool UnifiedPipeline2::init(OSDictionary *)`
- `%s: ---- New mode inserted ----\n`
- ` DRM CHECK not done for transparent_surf \n`
- `%s: Setting power state to %lu\n`
- `AED %s: primary fb %u not paired, nothing to do`
- `GP2_Max_BW`
- `%s: Dual pipe secondary modeset failed with status 0x%x\n`
- `AP DRIVER: Display disabled using boot-arg %s\n`
- `AED %s: no tiling manager`
- `virtual bool IOMobileFramebufferTilingMgr::initTilingMgr(IOMobileFramebufferShim *)`
- `%s: DisplayWall invalid input grid config\n`
- `0000000`
- `IOMFBSecureIndicatorSDRFactor`
- `master %d %d\n`
- `%s: Display Wall logs are %s\n`
- `%s : init_ca_pmu failed with 0x%x\n `
- `get_record_by_id`
- `void IOMFB::UPPipe2::unmap_buf(BufferDescriptor *, uint32_t, dva_t, bool, bool)`
- `DW_LOG::%s:%d: Building mode list for DisplayWall Group %u Master FB %u \n`
- `D124_callback__`
- `getTiledModes`
- `iomfb_prep_dcp_power`
- `%s: late_init failed\n`
- `site.IOMobileFramebufferShim`
- `%s: Entry to process hpd\n`
- `Color : %d\n`
- `start`
- `Display Wall secondary or primary modesets failed with statuses sec = 0x%x prim = 0x%x\n`
- `UnifiedPipeline2`
- `max_user_reachable_brightness`
- `Done setting power state state lock %lu lockAquired=%d\n`
- `11121`
- `DW_LOG::%s:%d: inserting: %ux%u@%u.%u\n`
- `%s: data: in_args->len (%lu) > in_args->data[] count (%lu)\n`
- `UPPipeAP_H19P.cpp`
- `static T *IOMFB::InstanceTracker::instance(tracked_entity_t, uint32_t) [T = IOMFB::PropRelay]`
- `site.Buffer`
- `IOMFBTimebaseNumer`
- `external`
- `kern.darkboot`
- ` DRM CHECK not done for fDefaultFramebufferSurface \n`
- `( \"Merge Config: Primary VFTG enable timedout\\n\" ) @%s:%d`
- `DW_LOG::%s:%d: DisplayWall framebuffers in the setup do not correlate to requested grid. DW_ID %u FB count is %u requested grid %u x %u\n`
- `site.UPPipeAP_H19P`
- `221111`
- `%s: failed to map physical address 0x%llx\n`
- `IOMFBLaunchFDRUserCal`
- `%s: dual pipe notified earlier = %d\n`
- `Dither_CRC`
- `Bright_ScalingFactor`
- `Update Ext Pipe state: is_plug %u total count %u limited %u Apple Display %u pipes %u \n`
- `IOPMPowerSource`
- `Requested_presentation`
- `IOMFBSecureContentFactor`
- `mismatched shim_id %u swapID's %d vs %d\n`
- `set_config_requires_dual_pipe`
- `Dual pipe primary modeset failed with status 0x%x`
- `APTPDCBrightness`
- `site.AppleCLCD2`
- `AED %s: null secondary, cannot pair`
- `Other tile ID is invalid %d\n`
- `%s: Swap queue drained before power state change\n`
- ` capa.sliceCapabilityMask 0x%x\n`
- `Conversions.h`
- `IOMFB: exclaves_display_healthcheck_rate failed with status 0x%x\n`
- `( \"mTiledColorsCount exceeded max possible\\n\" ) @%s:%d`
- `%s: Should not be entering here - async_swap = %d, swapID = %d!!\n`
- `%s: fTilingMgr is NULL\n`
- `Secondary tile=%p colorModeKeyID=%u, timingModeKeyID=%u\n`
- `%s:  capa bpp %d\n`
- `tearing down display wall in shutdown`
- `auto IOMobileFramebufferShim::set_matrix(uint32_t, const IOMFBMatrix *)::(anonymous class)::operator()(Gate::owner_t *, void *, void *, void *, void *) const`
- `%s: IOCommandPool::withWorkLoop failed\n`
- `%s: unable to find record for id: %u\n`
- ` DRM CHECK FAILED FOR DUAL PIPE SWAP protection_option 0x%llx bits 0x%llx\n`
- `MIPI`
- `%s: DisplayWall SettingUp the tile %u fbid %u size (%ux%u) with offset (x, y)= (%u, %u)\n`
- `%s: val: in_args->len (%lu) > in_args->val[] count (%lu)\n`
- `HTPC Compressed surface not okay!\n`
- `%s: Invalid Property type \n`
- `GCPStrength`
- `Doube HPD. Ignoring\n`
- `%s: Other tile ID is invalid %d\n`
- `121212112121212121212121212121212121212121212121212121212121212121212122112121212121212121212121212121212121212121212121212121212121212122112121212121212121212121212121212121212121212121212121212121212122112121212121212121212121212121212121212121212121212121212121212122112121212121212121212121212121`
- `Frame_APCE`
- `did_boot`
- `%s: function allocation failed\n`
- `Plug`
- `%s: Dual pipe: fb %u waiting for primary VFTG link check, timeout %u ms\n`
- `%s: Merge Config: Primary modeset failed with status 0x%x\n`
- `%s: Dual pipe: fb %u primary modeset thread finished in %u ms, status 0x%x\n`
- `%s: Display Wall secondary or primary modesets failed with statuses sec = 0x%x prim = 0x%x\n`
- `DCPSEC`
- `dispsec`
- `FFR_table_index`
- `121111121222121212121222222222222221221111111111112111111111111111111111111121222222222222222222222222222222222222111111222222222222222111222211122211222222222221111122122222222211112221222122212221222122212221222222222212222222222211222222222222222222222222222222222222222222222222222222222222222222`
- `FullFrameRequired`
- `DCPEXT`
- `Setting power state to %lu\n`
- `111222`
- `site.AppleDCPLinkServiceSoC`
- `virtual void IOMFB::PropRelay::set_delegate(PropMgr *)`
- `IOMFB: DCPLink::start failed with 0x%x (pipe:%u)\n`
- `%s: Index for tiled mode was not found\n`
- `SwapIDs: %d vs %d\n`
- `virtual bool IOMobileFramebufferTilingMgr::applyProperty(RuntimeProperty, uint32_t)`
- `AED establish-pairing: invalid primary fb %u`
- `%s: Delayed Plug notification called for Display Wall Tear Down done fb: %u\n`
- `Performance_headroom`
- `FB %u Request api power state of %lu on %p\n`
- `IOMobileFramebufferTilingMgr`
- `%s: DisplayWall invalid input timing config\n`
- `isDisplayWallConfigSupported`
- `0123456789ABCDEF`
- `IOMFB: reported 0x%llx (ns) as Time period to exclaves_display_healthcheck_rate \n`
- `%s: %d x %d at %d\n`
- `Presentation_delta`
- `\" Ycbcr Media Format supported only for 8/10/12 bits \" @%s:%d`
- `IOMFB FCAM stats: unexpected window count %d\n`
- `Dualpipe tear down with %d and %d\n`
- `AED %s: fb already in VFTG merge, skipping re-pair`
- `iomfb_swap_submit_split_enable`
- `%s: block: block_size (%lu) > out_args.block[] count (%lu)\n`
- `site.IOMobileFramebufferTilingMgr`
- `%s: Failed to find matching corresponding timing in all the displays in the wall setup\n`
- `%s: copyMapperForDeviceWithIndex failed\n`
- `IOMFBSecureIndicatorFactor`
- `dvfs-disp`
- `isp-alss-zone-y`
- `dfr-brightness-control`
- `%s: max_user_reachable_brightness 0x%x`
- `update_notify_clients`
- `%s: failed to schedule dump\n`
- `trigger_user_cal_loader`
- `PurpleGfxMem%u`
- `IOFMB: %s: setProperty failed\n`
- `Submitting swap after power down at entry. Returning failure, cancelling swap\n`
- ` %p state: %d; `
- `Running SDO therad\n`
- `2112211`
- `IOMFB: DCPPowerManager::start failed with 0x%x\n`
- `%s: Swapping clinet stop %p \n`
- `%s: Internal error\n`
- `Panel_ID`
- `IOMFBIndicatorNitsCap`
- `%s: no available records...\n`
- `IOFMB: %s: failed to create buffer\n`
- `Layer_0_CRC`
- `function-bw_req_interrupt0`
- `dispext`
- `SurfaceSharedEventAgentMask`
- `establish_dual_pipe_shim_state`
- `FFR_raw_high_index`
- `set_ffr_index`
- `IOMFBIndicatorBrightnessNits`
- `IOMFB FCAM stats: read %s failed\\n`
- `%s: Found %d timings and %d colors on secondary\n`
- `%s: this=%p TILE w = %u, h = %u w_total=%d\n`
- `Dual pipe mode set for %s\n`
- `Internal Error: Simple FB this=%p is called with DisplayWall timingID=%u\n`
- `tearing down dual pipe in shutdown`
- `GP0_Obs_BW`
- `\"%s: record book mismatch\\n\" @%s:%d`
- `Entry to process hpd\n`
- `%s: surf_alloc %d surf %p surfID %d\n`
- `IOMFBSwapAppleLookSupported`
- `enabled`
- `%s: displayarea %d * %d\n`
- `this=%p colorID=%u, timingID=%u\n`
- `setDisplayWall: invalid display wall group id %u (max %u)\n`
- `\"IOMFB: unexpected or missing EDT node: edt: '%s', prefix: '%s'\" @%s:%d`
- `IOReturn UnifiedPipeline2::dart_map_mdesc_gated(IOMemoryDescriptor *, IODMACommand **, dva_t *, bool)`
- `iomfb_disable_async_swap_hw`
- `%s: modeset: fb %u set_digital_out_mode returning 0x%x (timing %u color %u dual %d)\n`
- `rt_bandwidth_setup_ap`
- `ammoliteStrength`
- `%s: Delayed Plug notification called for Display Wall Tear Down start\n`
- `isp-alss-zone-count`
- `Dual pipe tear down is already processed\n`
- `Secondary color ID found\n`
- `tiling_mgr_sched`
- `%s found \n`
- `%s: log_write called but trace not enabled\n`
- `setDCPAVPropStart`
- `%s: master %d %d\n`
- `( \"Display Wall: Primary VFTG enable timedout\\n\" ) @%s:%d`
- `%s: deferred notification for dual pipe HPD\n`
- `%s: ERROR: more than %d current instances of IOMobileFramebuffer!\n`
- `11211`
- `IOMFB : Failed to set property  %s , is_valid_property = %d \n`
- `Cleaned up local states for dual pipe\n`
- `get_buf_block_dcp`
- `Updating role on an invalid tile ID %d\n`
- `DP`
- `DW_LOG::%s:%d: DisplayWall Group %u Master FB %u Count %u Timing %ux%u@%u.%u\n`
- `Presentation_time`
- `121111121222121212121222222222222221221111111111112111111111111111111111111121222222222222222222222222222222222222111111222222222222222111222211122211222222222221111122122222222211112221222122212221222122212221222222222212222222222211222222222222222222222222222222222222222222222222222222222222222222`
- `is_hpd_dual_pipe`
- `MaxNumLayers`
- `IOMFB %s: failed (no carveout)\n`
- `modeset called on secondary this=%p\n`
- `%s: vals: in_args->nvals (%lu) > in_args->vals[] count (%lu)\n`
- `function-mcc_dataset`
- `first-frame-response-threshold`
- `IOMFB %s: read failed\n`
- ` capa bpp %d\n`
- `site.Allocator`
- `site.A120_out_args__`
- `IOMFB %s: Value underrun for CRC ref counter %d\n`
- `processing dual pipe plug state of %x on FB%d\n`
- `dual plug status checked on invalid framebuffer %d\n`
- `FrameInfoBuffer`
- `virtual IOMFBStatus IOMobileFramebufferShim::set_matrix(uint32_t, const IOMFBMatrix *)`
- `powering down %p from %p\n`
- `Aborting set_digital_out_mode.\n`
- `Aborting set_digital_out_mode. Setting Dual pipe timing on single pipe.\n`
- `00`
- `\"%s: Failed to allocate _upload_trace_lock\" @%s:%d`
- `IOMFB %s: missing EDT data %s\n`
- `Primary fid is invalid\n`
- `mTiledModesCount exceeded max possible\n`
- `start this=%p colorID=%u, timingID=%u, tiledModesCount=%u, mTiledColorsCount=%u\n`
- `site.A122_in_args__`
- `D205_callback__`
- `%s`
- `coverglass-serial-number`
- `isp-alss-zone-weight`
- `read_edt_data`
- `%s: Dual pipe mode set for %s\n`
- `%s: lock held %llu us\n`
- `DisplayWall mode list created for Group %u with %u modes\n`
- `BacklightMatching`
- ` DRM CHECK not done for IOMFBSwapRequestIntent_SwapIdleBuffer \n`
- `%s: Force convert FU -> sync swap. SWID=%d Mismatch code=0x%x\n`
- `---- New display wall timing mode inserted ----\n`
- `%s: Delayed Plug notification called for Display Wall start fb: %u\n`
- `%s: dest: in_args->bytes (%lu) > in_args->dest[] count (%lu)\n`
- `%s: productName: productNameLengthMax (%lu) > out_args.productName[] count (%lu)\n`
- `Brightness_Scale`
- `IOMFB %s: Got data for prop: %s with length: %uB but expected length is %uB!\n`
- `external-normal-mode`
- `static IOMobileFramebufferTilingMgr *IOMobileFramebufferTilingMgr::instance()`
- `%s: Building mode tables for dual pipe\n`
- `%s: FB %u Request api power state of %lu on %p\n`
- `target timing`
- `BLNitsCap`
- `lMaxReachable`
- `iomfb_tiling_sched`
- `%s: Aborting set_digital_out_mode. getVideoDataForIDs failed\n`
- `callPlatformFunction`
- `sim`
- `primary`
- `3.1`
- `IOMFBLaunchFDR`
- `%s: Dual pipe: fb %u issuing secondary modeset on fb %u (timing %u color %u)\n`
- `NormalModeActive`
- `Failed to created DisplayWall mode list\n`
- `auto IOMobileFramebufferTilingMgr::setDisplayWall(uint8_t, uint32_t, bool)::(anonymous class)::operator()(void *, void *, void *, void *) const`
- `GP1_Obs_BW`
- `site.Lock`
- `%s: Couldn't create DCP Power Manager\n`
- `%s: Aborting set_digital_out_mode.\n`
- `Merge Config: Primary modeset failed with status 0x%x\n`
- `Int`
- `Platform limits applied %u overall limited %u\n`
- ` %u`
- `Dual pipe allocated for merge\n`
- `%s: %s PMC Bandwidth dashboard not found (error %d)\n`
- `PixelDef.cpp`
- `iomfb_pending_poweron_sched`
- `%d x %d at %d\n`
- ` DRM CHECK should not enter this case \n`
- `Aborting set_digital_out_mode after dual pipe teardown on %d. HPD dropped during teardown, dual pipe timing cannot run on one pipe.`
- `%s:  commandSleep was interrupted\n`
- `AED teardown-pairing: no shim for primary fb %u`
- `%s: %s: HPD notification not registered yet\n`
- `iomfb_rack_debug`
- `%s: state: %d ret1 %x\n`
- `modeset: fb %u set_digital_out_mode returning 0x%x (timing %u color %u dual %d)\n`
- `site.ServiceRelay`
- `%s: DisplayWall FBs %u\n`
- `virtual bool IOMobileFramebufferTilingMgr::isDisplayWallConfigSupported(uint8_t)`
- `AED establish-pairing: no shim for primary fb %u`
- `000000`
- `\"IOMFB: cannot call %s on the remote side\" @%s:%d`
- `read_carveout`
- `Unplug`
- `setParameter`
- `hasAlpha`
- `IOMFBWindowedVsyncOffDisableDetachingKey`
- `Found %d timings and %d colors on secondary\n`
- `Swap queue drain timed out (500ms)\n`
- `\"OSDictionary deserialization failed [%p]\" @%s:%d`
- `IOReturn IOMFB::FrameInfoBuffer::stop_tracing(uint32_t)`
- `first-frame-response`
- `%s: Dualpipe tear down with %d and %d\n`
- `Skipping shutdown notification on secondary DCP for stitched config\n`
- `%s: idxs: nidx (%lu) > out_args.idxs[] count (%lu)\n`
- `AED teardown-pairing: invalid primary fb %u`
- `%s: tparams: tmax (%lu) > out_args.tparams[] count (%lu)\n`
- `site.Record`
- `%s: Could not set the memory descriptor for the DMA command (%X)\n`
- `%s: Error: Tiled mode addition failed\n`
- `%s: this=%p power_state=%lu tile=%p ret2=%d\n`
- `Aborting set_digital_out_mode. getVideoDataForIDs failed\n`
- `IOReturn getPropVal(RuntimeProperty, OSObject *, uint32_t *)`
- `0000`
- `OSUnserializeXML failed`
- `%s on non dual pipe device\n`
- `Swapping clinet stop %p \n`
- `enablePulseWidthMaximization`
- `APP`
- `failed to get IONVRAM\n`
- `modeset: fb %u is_dual=%d adm_forced=%d vftg_cfg=%d paired=%d hpd_dual_ok=%d timing=%u color=%u (%ux%u@%uHz)\n`
- `%s:  capa.sliceCapabilityMask 0x%x\n`
- `virtual bool IOMobileFramebufferTilingMgr::buildDisplayWallModeConfig(uint8_t, uint8_t)`
- `teardown_dual_pipe_pairing`
- `IOMFB %s: Unexpected pixel layout found`
- `IOMFB %s: Couldn't allocate scheduler object\n`
- `%s: Color : %d\n`
- `swap_submit`
- `%s: Aborting set_digital_out_mode. Setting Dual pipe timing on single pipe.\n`
- `DisplayWall invalid input, only 2, 3 or 4 framebuffers can be selected\n`
- `DW_LOG::%s:%d: DisplayWall requested timing is invalid %u x %u\n`
- `D125_callback__`
- `000`
- `%s: Inserted mTiledModesCount %d new modes\n`
- `IODeviceTree:/arm-io/pmp/iop-pmp-nub`
- `RTPLC_Bright_Capped`
- `channelBits`
- `iomfb_api_pstate_sched`
- `%s: async_swap_hw forced to false -> config mismatch - swap creation failed\n`
- `%s: Aborting set_digital_out_mode after dual pipe teardown on %d. HPD dropped during teardown, dual pipe timing cannot run on one pipe.`
- `( \"Dual pipe primary modeset timed out. Merge Config = %s\\n\" ) @%s:%d`
- `1221212222222222212222222222212222222222212222222222212222222222212222222222212222222222212222222222212222222222212222222222212222222222212222222222212222222222212222222222212222222222212222222222222222222222222222222222222212`
- `BrightOut_NoScale`
- `function-link_enable`
- `Dual pipe: fb %u primary VFTG link check done in %u ms, localStatus %u\n`
- `Layer_2_CRC`
- `GP0_Max_BW`
- `OffTimestamp`
- `Ext`
- `%s: processing dual pipe plug state of %x on FB%d\n`
- `%s: Done setting power state state lock %lu lockAquired=%d\n`
- `TBICSSupported`
- `%s: DisplayWall value %u\n`
- `virtual bool IOMobileFramebufferTilingMgr::buildDisplayWallModeConfig(uint8_t, uint8_t, IOMFB_DisplayWallModeMap *, IOMFB_DisplayWallColorMap *, uint32_t *)`
- `is plugged checked for invalid framebuffer %d\n`
- `AED grow: primary fb %u -> secondary fb %u (ext idx %u) from peer count %u pipe0 %u\n`
- `static T *IOMFB::InstanceTracker::instance(tracked_entity_t, uint32_t) [T = IOMobileFramebufferAP]`
- `twilightStrength`
- `%s: %p state=%llu\n`
- `%s: cparams: cmax (%lu) > out_args.cparams[] count (%lu)\n`
- `target-type`
- `( \"mTiledModesCount exceeded max possible\\n\" ) @%s:%d`
- `Dual pipe: fb %u primary modeset thread finished in %u ms, status 0x%x\n`
- `set_block_dcp`
- `AED %s: shim pairing failed for primary fb %u (0x%x)`
- `ext-display-subsystem`
- `%s: can't allocate scheduler\n`
- `%s: Setting kIOMFBDisplayWallAvailFBs %d\n`
- `IONVRAM`
- `not enabled`
- `%s: ERROR - DisplayWall invalid input parameters group %u master FB %u\n`
- `/var/mobile/iomfb_frame_info`
- `%s: DisplayWall SettingUp the tile %u fbid %u with grid location (x, y)= (%u, %u)\n`
- `%s: val: in_args->len is NULL\n`
- `%s: Delayed Plug notification called for Display Wall done fb: %u\n`
- `iomfb_ffr`
- `IODeviceTree:/`
- `%s: HPD notification not registered yet\n`
- `surf_alloc %d surf %p surfID %d\n`
- `No`
- `RTPLC_RT_Trig`
- `mTiledColorsCount exceeded max possible\n`
- `ColorManager_CRC`
- `setDCPAVPropEnd`
- `%s: Cleaned up local states for dual pipe\n`
- `%s: Lock acquired in %d itr (fallback)\n`
- `migrate_status`
- `virtual bool IOMobileFramebufferTilingMgr::setDisplayWall(uint8_t, uint32_t, bool)`
- `loadDisplayWallConfig: invalid display wall group id %u (max %u)\n`
- `UnifiedPipeline.cpp`
- `%s: powering down from %p\n`
- `powering down from %p\n`
- `AED`
- `DW_LOG::%s:%d: DisplayWall is not supported for this product\n`
- `D127_callback__`
- `RecordTracker.cpp`
- `IOMFBStatus IOMFB::UPPipe2::map_buf(BufferDescriptor *, uint32_t *, dva_t *, bool)`
- `%s: Display Wall config tearing down is complete\n`
- `111212222222222222222222222222222221222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `IOMFBNumLayers`
- `IOMFB: %s: Disable HW ASync Swap / VSync OFF Value = %d\n`
- `first-frame-response-high`
- `IOMFB_KTRACE_API_VERSION`
- `Insert merge modes into primary failed. Failing modeset\n`
- `site.StaticElement<T>`
- `0`
- `imb`
- `Dual pipe primary modeset timed out. Merge Config = %s\n`
- `%d\n`
- `DW_LOG::%s:%d: Teardown is completed\n`
- `%s: failed to compute stride of surface\n`
- `UPPipe.cpp`
- `iomfb_disable_display`
- `GPBandwidth`
- `IOFMB: %s: invalid chunk requested\n`
- `%s: otherID: %d Dual pipe HPD notified!\n`
- `IOMFB %s: Disabling overdrive (missing EDT data)\n`
- `%s: other : %d Tiled not notified previosly. Config is complete\n`
- `otherID: %d Dual pipe HPD notified!\n`
- `powering down from %p primary %p\n`
- `%s: Display Wall config failed to get set\n`
- `Dual cables are on seperate die's\n`
- `Last_Fence_or_Event_Time`
- `%s not found \n`
- `site.UnifiedPipeline2`
- `%s: type mismatch for property %s\n`
- `%s: DisplayWall applied framebuffers for a display wall:`
- `Handling dual pipe HPD on %d with state %lld\n`
- `%s: plug state %x is same. Ignoring processHPD\n`
- `%s: val: out_args->len (%lu) > out_args->val[] count (%lu)\n`
- `RTPLC_Nits_Cap`
- `Multi pipe tear down %p\n`
- `Lock acquired in %d itr (fallback)\n`
- `Power state ret1=%d: otherTiles:`
- `Vbl_FrameTime`
- `SharedEventAgentSignalEnabled`
- `hotPlug_notify_gated`
- `other : %d Tiled not notified previosly. Config is complete\n`
- `---- New mode inserted ----\n`
- `dual pipe: rejected swap_start on secondary fb %u (client %p)`
- `%s: Display Wall Area Inch (w x h) = (%f x %f) \n`
- `AED %s: peer pipe index %u invalid (expected 1-based) for primary fb %u`
- `Issued_time`
- `iomd-early-reclaim`
- `RTPLCBLNitsScaler`
- `site.A119_in_args__`
- `%s: DisplayWall timing %ux%u@%u.%u \n`
- `buildDisplayWallModeConfig`
- `AED %s: no shim for secondary fb %u`
- `%s: modeset: fb %u is_dual=%d adm_forced=%d vftg_cfg=%d paired=%d hpd_dual_ok=%d timing=%u color=%u (%ux%u@%uHz)\n`
- `Dual pipe: fb %u waiting for primary modeset thread, timeout %u ms\n`
- `IOMFB %s: %s PMC support: RTBW: 0x%llx, PS: 0x%llx\n`
- `raw-panel-serial-number`
- `IOMFB AP: use_psd_dcp_power2: %d\n`
- `IODTNVRAM`
- `AED tore down dual-pipe shim state (primary fb %u)`
- `\"mismatched swapID's %d vs %d\\n\" @%s:%d`
- `%s: Power state: otherTile %p\n`
- `function-clock_req_interrupt`
- `BWRHandler::BWRSurface *IOMFB::getBWRSurface(Surface *, BWRHandler::BWRSurface *)`
- `%s: Doube HPD. Ignoring\n`
- `plug state %x is same. Ignoring processHPD\n`
- `Found %d timings and %d colors on primary\n`
- `%s: ERROR: Could not allocate fTilingMgrLock\n`
- `iomfb_display_wall_logs_enable`
- `%s: chunk: in_args->chunk_size (%lu) > in_args->chunk[] count (%lu)\n`
- `\"ERROR: Pipe index to shared event mask mapping not supported\\n\" @%s:%d`
- `GP1_Max_BW`
- `OnTimestamp`
- `Power state: otherTile %p\n`
- `IOMFBSupportsHeadOfLineSwaps`
- `HDMI`
- `\"ERROR: agent_mask cannot be null\\n\" @%s:%d`
- `site.RecordTracker`
- `ExternalAppleLook`
- `AED %s: primary fb %u not plugged, refusing to pair`
- `IOMFBPropertyRelay.cpp`
- `AED established dual-pipe shim state (primary fb %u secondary fb %u)`
- `%s: Merge Config: Primary VFTG enable timedout due to unplug\n`
- `%s: Requested DisplayWall config cannot be enabled\n`
- `Min_FrameTime`
- `%s: %s PMC Bandwidth dashboard mal-formed\n`
- `getMatchingMode`
- `failed to get IODTNVRAM\n`
- `%s: Dual pipe: fb %u waiting for primary modeset thread, timeout %u ms\n`
- `AED %s: paired primary fb %u with secondary fb %u`
- `%s: %s PMC perf state dashboard not found (error %d)\n`
- `%s: Secondary color ID found\n`
- `%s: %s all %u wall displays are identical: mfg: %s pid: 0x%x die: 0x%x maxPixClk: 0x%x dwnstrmType: %s\n`
- `PurpleGfxMem`
- `%s: modeset called on secondary this=%p\n`
- `IOMFBTestBacklightFastRamp`
- `iomfb_ffr_high`
- `isp-alss-zone-width`
- `AED: fb %u could not read ADM pipe-count intent (0x%x); modesetting as single pipe\n`
- `get_block`
- `FFR_raw_index`
- `backlight-calibration-parameters`
- `\n`
- `%s: powering down %p from %p\n`
- `%s: Dual pipe primary modeset failed with status 0x%x`
- `%s: %s PMC perf state dashboard mal-formed\n`
- `Layer_1_CRC`
- `Blend_CRC`
- `IOMFBHotplugKeysChangedKey`
- `%s: AED tore down dual-pipe shim state (primary fb %u)`
- `Inserted mTiledModesCount %d new modes\n`
- `Display Wall: Primary VFTG enable timedout\n`
- `isp-alss-zone-height`
- `virtual IOReturn UnifiedPipeline2::setProperties(OSObject *)`
- `virtual void IOMobileFramebufferShim::get_display_size(uint32_t *, uint32_t *) const`
- `Yes`
- `Display Wall: Primary VFTG enable timedout due to unplug\n`
- `\"IOMFB: %s: no instance for instance ID: %u\\n\" @%s:%d`
- `%s: init failed\n`
- `DisplayWallAvailFBs`
- `gSetContrastEnhancerStrength`
- `%s: Handling dual pipe HPD on %d with state %lld\n`
- `00000`
- `%s%x`
- `IOMobileFramebufferShim`
- `HPD notification registered on fbid=%u, this=%p, external_pipe=%d, fTilingMgr=%p, state=%llu\n`
- `%s: offset %d primary %d second %d\n`
- `%s: start this=%p colorID=%u, timingID=%u, tiledModesCount=%u, mTiledColorsCount=%u\n`
- `DW_LOG::%s:%d:  dw_mode_valid %u found_modes %u master_fb %u\n`
- `D118_callback__`
- `offset %d primary %d second %d\n`
- `Dual pipe: fb %u waiting for primary VFTG link check, timeout %u ms\n`
- `IOMFBLTPOFlashMitigationNeeded`
- `%s: heap allocation of arguments failed\n`
- `%s: DisplayWall grid_config %ux%u\n`
- `GP2_Obs_BW`
- `getDisplayProductId`
- `%s: triggering user cal`
- `IOFMB: %s: setDCPAVPropStart not called or failed\n`
- `state: %d ret1 %x\n`
- `%s:  commandSleep was SleepStatusTimeout attempt is %d\n`
- `IOMFB %s: failed (region not in carveout)\n`
- `%s: %s on non dual pipe device\n`
- `Merge Config: Primary VFTG enable timedout due to unplug\n`
- `%s: Display Wall: Primary modeset failed with status 0x%x\n`
- `121111121222121211111111111111111111111111111121111111211211211212122222111122121212222112212121222211221212122221122121212222112212121222211221212122221122121212222112212121222211212222`
- `IOMFBSupportsRotation`
- `1`
- `set_panel_id`
- `AppleCLCD2`
- `this=%p power_state=%lu tile=%p ret2=%d\n`
- `establish_dual_pipe_pairing`
- `void IOMFB::FrameInfoBuffer::log_write(const FrameInfoData *)`
- `site.PropRelay`
- `setDCPAVPropChunk`
- `%s: timeout %d power %d %d\n`
- `Skipping redundant modeset (timing=%u, color=%u)\n`
- `%s: Dual pipe: fb %u primary VFTG link check done in %u ms, localStatus %u\n`
- `%s: Failed to properly install the stitched display wall timing\n`
- `\" IOMFB: Unable to find a mapping of index to DCP role to match against DCP expert\" @%s:%d`
- `IOMFB %s: %s platform functions missing: %s %s\n`
- `122222222222222222222222222222211`
- `%s: HPD notification registered on fbid=%u, this=%p, external_pipe=%d, fTilingMgr=%p, state=%llu\n`
- `Index for tiled mode was not found\n`
- `get_display_area`
- `%s: DisplayWall DisplayWallTiming  %u p %u . %u\n`
- `%ux%u@%u.%u\n`
- `virtual bool IOMFB::UPPipeAP_H19P::late_init()`
