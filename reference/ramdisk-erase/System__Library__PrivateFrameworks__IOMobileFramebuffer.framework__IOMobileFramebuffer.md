# `/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 513,168 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 2632)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (6)

- `/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOSurface.framework/IOSurface (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (955)

```
%s - Post Blend Layer index too large: %d\n
%s: Reference FB count = %d < Enumerated FB count = %d - shouldn't happen - error\n
%s: Local call to iomfb_match_callback\n
dcvrr-d
Parser e: invalid header\n
Parser e: Unsupported type B channel count %d\n
Parser e: unsupported NAC: %u > %u\n
Parser e: invalid acss_config version %u\n
Parser e: processed ALSS EMMP dimensions (temp %u, bright %u)mismatch specified values (temp %u, bright %u)\n
Parser i: set EVLS LUTs succeeded
Parser e: unspecified PP LUT scan plan 0x%x\n
Parser i: set PTUC table config succeeded\n
Parser e: failed to set IRDC data 
Parser e: out of memory for IOMFBRDLCData\n
Parser e: parsing did not consume the full EMMK size\n
Parser e: Unsupported PCS XD config
Parser e: failed to set PDC table rr config
hdcp-hoover-protocol
Parser e: provided min or max durations (%d, %d) invalid\n
Parser e: no memory\n
Parser e: no memory for SPLX data\n
%s - layer index too large: %d\n
Parser e: underflow while reading regions\n
Parser e: out of memory for EMMK table\n
Parser e: failed to set PDC LUT [%d %d %d %d %d] \n
Parser i: set LUS LUTs succeeded
 %s:  failed _ioMobileFramebufferAlloc return %d \n
%s: iomfb_populate_matched_displays\n
Parser e: set CA data failed\n
Parser e: set RXTK data failed\n
%s: All Display Instances enumerated successfully - FB Count = %d\n
Parser e: Unexpected UBCL block version 0x%x\n
Parser e: Could not find PRC tables [%d:%d:%d] [%d:%d:%d]\n
Parser e: bin mix factor must be between 0 and 1\n
Parser e: underflow while reading WgTypeA\n
Parser e: bin tables do not correlate.\n
Parser i: set IRDC device data succeeded\n
Parser e: DBCL num_entries invalid (max: %d): %d\n
Parser e: underflow while reading EMMK spare\n
Parser e: unsupported config version %u for BENL v2\n
Parser e: Failed to sort EMMP tables\n
Parser i: Processing BLTS format version %d data version %d\n
APTPDCEnable
SageUIBrightness
com.apple.TritiumVSHCompensation.CalibStop
Parser e: underflow while reading EM mask\n
Parser i: set PDC LUTs RR succeeded\n
Parser i: set RDLC data succeeded
Parser e: EMMP XD lut not supported
primary
downscale_fail
Parser e: unsupported sync PCS temperature count: %u > %u\n
Parser e: underflow while reading limits\n
AppleDisplayManager
Parser e: Unexpected DBCL block version 0x%x\n
Parser i: set PSFM data succeeded
IOMFB: IOMobileFramebufferProxSensingNeeded API is enabled\n
vblank_duration_us
FFR_raw_index
%d 
Parser e: set QETC data failed
Parser e: Failed to process SPLX v1 data
Parser i: set PRC LUTs succeeded
SwapSetIndicatorBrightness: Brightness control is not enabled\n
AppleTV
display-frame-generation
Parser e: block %s not well formed size %d remaining %d\n
Parser e: DBV taps not in ascending order\n
Parser e: Failed to sort sync PCS tables\n
Parser i: processing prox data version %d\n
Parser e: could not allocate memory for PSFM data
Parser e: set BTHB data failed
%s - Strength value must be between 0.0 and 1.0: %f\n
TimezeroDelta
 %s key : %s not found \n
Parser e: Unsupported version: %u\n
Parser e: null header passed to process_dbcl
Parser e: underflow while reading interp_factor
Parser e: missing PRC LUTs
%s: passed %d surfaces, > %d\n
Parser i: set LUS table config succeeded\n
benchmark
%s - Cannot use zero gamma value for %d layer\n
iomfb_populate_all_display_infos
Found
Parser e: DC or PM LUT size too big\n
Parser i: set PRC table config succeeded
enablePulseWidthMaximization
%s: IOServiceGetMatchingServices for AppleParavirtGPU failed - shouldn't happen - error\n
Parser e: Duplicate PTUC table vers=%d (bright=%d, temp=%d , rr_mode = %d) found in input.\n
Parser e: unsupported region ACSS count: %u \n
Parser i: set user_cal_aft_gain succeeded
Parser e: out of memory for EMMK table
IOMFB framebuffer->transaction.uiEdgeMode[layerIndex] = %d d \n
Parser e: unexpected PBDp block version %d\n
Parser e: set RTPLC data failed
BCBrtControlSetDisplayService
Parser e: missing prox PD table bin %d\n
Parser e: Too many index values for LUT tables
Parser e: unexpected number of backlight sections %d\n
Parser i: skipping GSC block\n
Parser e: failed to set PTUC TLS RR LUT dbv_nits=%d, attempt %u/%u\n
Parser e: Failed to parse PCS block
Parser e: Vector exceeding max j count: %u > %u\n
Parser e: underflow while temperature / brightness
Last_Fence_or_Event_Time
IOReturn kern_SwapSetResTransitionStrength(IOMobileFramebufferRef, float, uint32_t)
%s%d
Parser e: inconsistent PM index\n
Parser e: frame repeat LUT incomplete, only %d/%d provided\n
IOMFB framebuffer->transaction.uiSoftEdgeCoverage[layerIndex] = %f f \n
Parser i: ABGM: edge_gains_enable=%u edge_gains_mode=%u\n
%s: pthread_dependency_wait_np expect: %d current: %d \n
/System/Library/PrivateFrameworks/MediaToolbox.framework/MediaToolbox
Parser e: PCS exceeding max temperature count: %u > %u\n
Parser e: Out of memory
IOMobileFramebufferSetRenderingAngle - kernel rejected the rendering angle trap\n
Parser e: Failed to process SPLX v1 data\n
Parser e: set BLTS data failed
Parser e: underflow while reading limits
Parser e: Failed to parse EMMP Block
Parser e: failed to set PDC table config
Parser i: set EVLS LUTs succeeded\n
Parser e: underflow while reading num_svds and shift_bits\n
Parser e: failed to set PRC LUT [t%d s%d b%d p%d]\n
FigInstallVirtualDisplay
Parser e: Could not allocate space for PCS vectors XD
Parser e: PDC missing at least 1 channel
Parser e: unsupported pdcc emission freq: %u != %u\n
Parser e: underflow while reading num_svds and shift_bits
Parser e: unsupported version: 0x%x != 0x%x\n
Parser e: underflow while reading feature enable flags\n
Parser e: lut sizes should be the same
Parser e: set BTPB data failed
Parser e: Unsupported type A SVDs count %d\n
Parser e: underflow while reading EM band steps\n
Parser e: Unexpected ABGM block version %d\n
Parser i: set PTUC TLS RR LUTs succeeded\n
Parser e: missing PTUC LUTs
/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox
Parser e: lut sizes should be the same\n
Parser e: Unsupported IRDC device data vers=%d\n
Parser i: set ELVS table config succeeded
IOMFB: IOMobileFramebufferRelbufInfo API is not supported\n
IOMobileFramebufferOpen
BCBrtControlGetCapabilities
%s: Found AppleParavirtGPU with DisplayPortCount %u\n
%s dcvrr_a 0x%x dcvrr_b 0x%x dcvrr_c 0x%x dcvrr_d 0x%x\n
Parser e: underflow while reading EM mask delay
BCBrtControlGetMinNits
Parser e: useless PDC table\n
Parser i: set PSFM data succeeded\n
Parser i: set SPLX data succeeded\n
Parser i: set LLMT table config succeeded\n
IOMobileFramebufferSetRenderingAngle - bad argument\n
SwapSetDisplayEdrHeadroom: Brightness control is not enabled\n
Parser e: set BLAH data failed\n
Parser e: ramp down configurations should be nonzero
Error -  IOMobileFrameBufferGetMirroringCapability called on internal framebuffer \n
Parser e: Invalid ACSS Block id\n
Parser e: LLMT DBV Thresholds not in ascending order\n
Parser e: duplicate tables
Parser i: skipping GSC block
Parser e: failed to set PTUC table config
Parser e: too many Brightness tap points %d\n
Parser e: GSC table is NULL
 %s:  success, return %d \n
Parser e: Out of memory\n
IOMobileFramebufferSetDigitalOutMode\n
ext-display-subsystem
Parser e: unsupported PCS brightness count: %u > %u\n
Parser e: PCS tables are NULL
SwapSetBrightnessLimit: Brightness control is not enabled\n
Parser e: data size too large\n
Parser e: could not allocate memory for PSFA data\n
Parser e: PRC table not well formed
%s: Runloop Timer expired: FBs enumerated, no signalling needed from here as Callback would have notified main thread\n
Parser e: set RTPLC data failed\n
IOReturn kern_SwapSetPostBlendLayerEventSignal(IOMobileFramebufferRef, uint32_t, IOSurfaceSharedEventRef, uint64_t)
%s: Spawn separate thread and wait for all FBs to be enumerated\n
Parser e: unsupported HTMP ACSS count: %u \n
Parser e: Could not allocate space for PCS vectors XD\n
Parser e: cannot allocate IOMFBACSSConfig
Parser e: set HGOD data failed
Parser i:  UBCL set data succeeded
Parser i: ACSS_DEBUG: Failed to parse HTMP block
Parser e: underflow while reading sizes\n
Parser i: set ABGM data succeeded\n
Parser e: PDC missing bin\n
Parser e: lerped DCLUT[%d, %d, %d, %d , %d] is all zeros
IOMFBIntDcpUsedForExtWhenLidClose
iomfb_match_callback
Parser e: unsupported NAC: %u != %u\n
Parser e: set user_cal_aft_gain failed
canvas-height
Parser e: unexpected LLMT block size %d\n
Parser e: Duplicate PDC table (bin=%d temp=%d bright=%d sf=%d param=%d chan=%X) found in input.\n
Parser e: Unexpected UFTG block version 0x%x\n
<IOMobileFramebuffer %p refcnt=%d>
Parser e: underflow while temperature / brightness / emission freq\n
Parser i: set DBMA data succeeded
kern_DisplayCapabilitiesGet called \n
IOReturn kern_SwapSetLayerEDRCompensation(IOMobileFramebufferRef, uint32_t, double, _Bool)
%s thresholds[sec:%d][bin:%d] 0x%x\n
Parser i:  DOOC set data succeeded\n
%s: %s service is 0x%x\n
Parser e: no memory to prepare PDC LUTs\n
Parser e: PCS table is NULL
analytics_send_event
Parser e: mismatching versions: %u != 4\n
Parser e: underflow while reading EMMP spare\n
Parser e: set RXTK data failed
IOReturn kern_SwapSetLayer(IOMobileFramebufferRef, uint32_t, IOSurfaceRef, CGRect, CGRect, uint32_t)
IOMFB: %s: using default IOS path for one external display !\n
Parser e: unsupported pdmc temperature count: %u != %u\n
Parser e: EMMP table for ALSS is NULL\n
Parser e: missing PRC LUTs\n
DisableCalClut
underrun
decomp_fail
Parser i: ABGM: gain_bits=%u num_positions=%u gain_size=%u num_runs=%u\n
Parser e: null header passed to process_dbcl\n
Parser i:  DBCL set data succeeded
Parser e: lerped DCLUT[%d, %d, %d, %d, %d] is all zeros
Performance_headroom
Parser i: set BLAH data succeeded\n
DisplayCoexPrioritizeDisplay
Parser e: unsupported number of color channels
Parser e: underflow while reading EM mask delay\n
Parser e: data size too large
IODataQueueAllocateNotificationPort failed\n
iomfb_populate_all_display_infos_block_invoke
Parser i: set QETC data succeeded\n
Parser e: missing PTUC LUTs\n
Parser e: set BLAH data failed
Parser e: Failed copy for EM LUTS\n
Parser e: EMMP table for ACSS is NULL
IODeviceTree:/arm-io
Parser e: unsupported BENL block count: %u > %u\n
Parser e: not enough durations provided for LUS LUTs\n
Parser e: DOOC set data failed
Parser e: underflow while reading EMMK spare
Parser e: underflow while reading feature enable flags
Parser e: ramp down configurations should be nonzero\n
%s For backlight %d: \n         section %d metric 0x%x falls between \n         {thresholds[sec:%d][bin:%d]:0x%x , thresholds[sec:%d][bin:%d]:0x%x} \n         weight = %f\n
Parser e: cannot allocate IOMFBACSSConfig\n
Parser e: LLMT Max DBV Threshold doesn't correspond to 0%% APL\n
SageUIImageType
dcvrr-c
Parser e: underflow while temperature / brightness\n
Parser i:  DOOC set data succeeded
Parser e: underflow while reading indices
paravirtualizedgraphics,gpu
Parser e: no data\n
Parser e: Could not allocate space for PCS vectors\n
Parser e: underflow while reading GSC spare\n
Parser e: parsing did not consume the full RCFG size\n
Parser e: invalid acss_als_rescale_config version %u\n
Parser i: set PTUC table rr config succeeded\n
Parser e: underflow while reading LUT coords
IOMobileFramebufferCalibrationToolboxCommand command_id 0x%x not available on HILO device
DisplayContainerID
Parser e: BTBL Block data and blob size mismatch Expected:%d, actual:%d \n
Parser e: parsing did not consume the full CNST size\n
Parser e: unsupported NBSVD: %u > %u\n
Parser e: null header passed to process_dooc\n
Parser i: set SPLX data succeeded
Parser e: underflow while reading GSC spare
IOMFB: %s: using multiple external display path !\n
IOMFB: `%s' not found in `%s'\n
Blend_CRC
SageSIPTemp
Parser e: ACSS EMMP exceeding max temperature count: %u > %u\n
kern_DisplayWallStatus called \n
Parser e: inconsistent nframes value\n
Parser e: GSC exceeding max brightness count: %u > %u\n
Parser e: missing PTUC RR LUTs\n
Parser e: DBV taps not in ascending order
kern_DisplayWallEnable called \n
Parser e: UFTG num_rows %d exceeds maximum 24\n
Parser i: set PDC table config succeeded\n
Parser e: lut size too big
Parser i: set IRDC device data succeeded
Parser e: unexpected size for CNST %u < %u\n
Parser e: unsupported sync PCS brightness count: %u > %u\n
Parser e: mismatching versions: %u != 1,3,6,7\n
Parser e: Incorrect RTPLC block version %d\n
IOMFB: IOMobileFramebufferRelbufInfo : fb passed is NULL\n
CurrentCode
RGBLayer_MinScaleFraction
IOMFBMaxSrcPixels
Parser e: Duplicate elvs table temperature=%d found in input.\n
Parser e: Failed to parse RCFG block\n
vector
Parser e: ACSS_ALS_RESCALE: set_block_cb failed
kern_SwapSubtitleRegion
SwapSetBrightness: Brightness control is not enabled\n
%s: All display instances are NOT enumerated: Disp_len %d, Ref_FB = %d, Act_FB = %d\n
getParavirtDisplayCount
Parser e: Invalid IRDC version %d\n
Parser e: null header passed to process_uftg\n
Parser e: Vector exceeding max i count: %u > %u\n
Parser e: couldn't read FFR low, using default
Parser i: set QETC data succeeded
Requested_presentation
IOServiceFirstMatch
UserCalibration_SetCalibrationData Power up Failed with %x\n
Parser e: Failed to parse EMMP Block\n
======================================\n
kern_DisplayWallDisable called \n
IOMFB: IOMobileFramebufferProxSensingNeeded : fb passed is NULL\n
SageUpdateStatus
Parser i:  UFTG set data succeeded
Parser e: out of memory for IOMFBBTBLConfig
Parser i: set PDC table config rr succeeded
SageFCMTemp
Parser e: set SPLX data failed\n
%s - Exceeded max number of layers: %d\n
SageVoltDeltaPct
Parser e: UFTG nits_list is not strictly increasing at index %u\n
Parser e: out of memory for EMMP table
Parser e: parsing did not consume the full EMMP size
Parser e: out of memory for IOMFBBTBLConfig\n
Parser e: UPCL set DPCL data failed
kern_DisplayRearrange called \n
Parser i: set RXTK data succeeded
Parser e: underflow while reading EMMP spare
Parser e: PCS exceeding max brightness count: %u > %u\n
IOMobileFramebufferSetPreset\n
Parser e: Illegal channel code %c\n
Parser e: EMMK exceeding max brightness count: %u > %u\n
Parser e: EMMP table for ACSS is NULL\n
dfr
PDC brightnesses
Parser e: actual number of Prox LUTs differ from specified
Parser i: Set ALSS EM config success\n
Parser e: UOOC set data failed
======================================
IOReturn kern_SwapSetBlit(IOMobileFramebufferRef, IOSurfaceRef, CGRect, CGRect, uint32_t)
Parser e: unsupported benl brightness count: %u != %u\n
Parser e: null header passed to process_dooc
totalSwaps
Parser e: failed to set ELVS LUT temperature %d\n
Parser e: Undefined EEPROM version 0x%x, expected 0x%x\n
Parser i: set BLTS data succeeded
IOMobileFramebufferSetRenderingAngle error - angle needs to be a multiple of 90\n
MaxUABoost
Parser e: unsupported NASVD: %u != %u\n
Parser e: underflow while reading EM Counts\n
Parser i: set BLAH data succeeded
Parser e: invalid header
Parser e: underflow while reading regions
%s: IORegistryEntryFromPath unable to find /arm-io node\n
Parser e: actual number of Prox LUTs differ from specified\n
Parser i: set ELVC data succeeded
UserCalibration_WriteEAN EANSize write failed  input_buffer_size 0x%zx ret 0x%x \n
Parser e: out of memory for PRC table\n
======================================\n\n
Parser e: parsing did not consume the full HTMP size\n
Parser e: could not allocate memory for PSFA data
Parser e: Unsupported type B SVDs count %d\n
Parser e: underflow while reading sizes
kern_DisplayResourcesValidateAllocationSet called \n
Parser i: PDC RR inheriting NR bin interp: bin_low=%u t=%g\n
Parser e: unsupported EMMP ALSS brightness count: %u > %u\n
ALSSSupported
Parser e: set ABGM data failed\n
Parser e: null header passed to process_uooc\n
Parser i:  UOOC set data succeeded\n
Parser e: lerped PMLUT[%d, %d, %d, %d , %d] is all zeros
v8@?0
Parser e: unsupported EMMP ACSS brightness count: %u > %u\n
Parser e: parsing did not consume the full EMMP size\n
Parser e: EMMP XD lut not supported\n
Parser e: RTPLCL: body_size %d seems incorrect\n
Parser e: PP LUT missing color channel
Parser i: set ELVS table config succeeded\n
Parser e: missing EMMP (T%d B%d) or gray scales (T%d B%d)\n
Parser e: Unexpected DPCL block version 0x%x\n
Parser e: missing LUS LUTs\n
SageExpectedVoltPerNit
Parser e: unsupported EMMP ACSS count: %u \n
Parser e: out of memory for PCS table copy\n
Parser e: couldn't read FFR high, using default
IOReturn kern_SwapSetPostBlendLayerEventWait(IOMobileFramebufferRef, uint32_t, IOSurfaceSharedEventRef, uint64_t)
enable_ktrace
external
Parser e: could not allocate memory for PSFM data\n
Parser e: Failed to validate pdc rr\n
Parser e: failed to set PDC table rr config\n
Parser e: Prox PP bin tables do no correlate\n
IOMFB: IOMobileFramebufferRelbufInfo API is disabled\n
Parser e: BTHB Block data and header size mismatch by %d too many bytes\n
Parser e: PCS table is NULL\n
Parser e: input data not well-formed
Parser e: failed to process block %s\n
Parser e: unexpected number of bins %d\n
Parser e: cannot read data in CNST\n
Parser e: too many sensor channels %u\n
Parser e: parsing did not consume the full EMMK size
override_panel_width
\n%s: Name is null idx=%d
/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl
Parser e: expected 3 color channels\n
Parser e: Too many index values for LUT tables\n
BCBrtControlGetContainerID
Parser e: unexpected PBDp block size %d\n
totalVBLs
kern_CopyProperty
MaxSrcBufferWidth
Parser e: could not allocate memory for BCAL data\n
Parser i: set HGOD data succeeded\n
Parser e: unspecified PD LUT temperature value %d C\n
IOMFB: IOMobileFramebufferAPTQuantaSwitch API is enabled\n
Parser e: unsupported BENL gray level count: %u > %u\n
Parser e: too many EM color channels %d\n
Parser e: provided data size smaller than expected %d < %d\n
Parser e: underflow while reading interp_factor\n
Parser i: set Prox LUTs succeeded\n
prc_binning_impl
Parser e: inconsistent DC index
\n 
Parser e: cannot read data in CNST
Parser e: unsupported pdcc temperature count: %u != %u\n
VDCL: %s Vendor Specific Calibration Data for idx %d\n
%s Interpolated LUT[temp:%d][subframe:%d][backlight:%d][channel:%d]: 
Parser e: Unsupported heatmap size %d\n
Parser e: failed to set PDC table config\n
Parser i: PDC bin interpolation, bin = %g\n
Parser e: Could not allocate space for PCS vectors
kern_DisplayResourcesAllocationGetV2 called \n
IOMobileFramebufferSetRenderingAngle - can only set rending angle for internal display\n
Parser e: Duplicate IRDC table for RR=%d\n
Parser e: unexpected PRCW block size %d\n
Parser i: set RTPLC data succeeded\n
Parser e: failed to set LUS LUT [%d %d %d]\n
%s no more available region!\n
Parser e: underflow while reading LUT entries\n
kern_DisplayWallValidateConfig called \n
BCBrtControlGetMaxNits
Parser e: out of memory for IOMFBBTBLCurveConfig\n
Parser e: failed to set LLMT table config\n
SupportRelbufInfoCb
Parser e: unexpected PBDS version %d\n
Parser e: cannot read NR and NC
IOMobileFrameBufferGetSizeOfCalibrationToolboxCommand: Invalid command 0x%x\n
Parser e: unsupported async PCS brightness count: %u > %u\n
Parser e: too many EM gray levels %d\n
Parser i: set IRDC data succeeded
Parser e: ACSS: set_block_cb failed
Parser e: unknown backlight section %d\n
Parser e: underflow while reading WgTypeB\n
wireless
Parser e: Failed copy for heatmaps\n
Parser e: Bad size/version for aftg\n
Parser e: Bad size/version for aftg
kern_DisplayResourcesValidateAllocationSetEx called \n
Parser e: unsupported htmp emission freq count: %u != %u\n
Parser e: DBCL set data failed\n
com.apple.TritiumVSHCompensation.Status
%s: pthread_create error %d\n
Parser e: Invalid PCS region index %d\n
Parser i: PDC params version %d\n
Parser e: underflow while reading LUT entries
/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
Parser e: unsupported em line xd ACSS count: %u \n
Parser i:  UBCL set data succeeded\n
Parser e: set IRDC data failed
Parser e: bin mix factor must be between 0 and 1
Didn't find ADM service \n
com.apple.iomfb.underrun
Parser e: too many color channels %u\n
Parser i: ACSS_DEBUG: Failed to parse HTMP block\n
Parser e: unexpected PBDD version %d\n
Parser e: inconsistent nframes value
Parser e: missing EMMP (T%d B%d) or gray scales (sync T%d B%d async T%d B%d)\n
Parser e: underflow while reading PCS spare\n
Parser i: set PDC table config succeeded
Max_FrameTime
UserCalibration_ReadEAN failed: 0x%X
Parser i: all done\n
Parser e: unsupported NBC: %u > %u\n
Parser e: parsing did not consume the full SENS size
Parser e: Invalid RTPLC version %d\n
Parser e: reported PDC tap points (temp/DBV/RR/HGOD status) mismatch actual counts
kern_DisplayMappingSet called \n
Parser e: couldn't read FFR low, using default\n
Parser e: Failed to parse CNST block\n
Parser e: underflow while reading indices\n
Parser e: unsupported NASVD: %u > %u\n
Parser e: underflow while reading LUT steps\n
Parser e: GSC table is NULL\n
Parser i: set prox table config succeeded
Parser i: set PDC LUTs RR succeeded
IOMFB: ProxSensingNeededNotifyFunc, args NULL \n
dcvrr-a
Parser i:  DBCL set data succeeded\n
couldn't set mach port limit\n
kUSBContainerID
Parser i: set BTHB data succeeded\n
Parser e: missing LUS LUTs
Parser e: out of memory for IOMFBBTBLCurveConfig
Parser e: unsupported color ACSS count: %u \n
Parser e: ACSS and ALSS should share either none or all of EMMP data\n
Parser e: underflow while reading EMMK scalers\n
Parser e: prox LUTs should come after config parameters\n
Parser e: null header passed to process_ubcl
Parser e: parsing did not consume the full CNST size
Parser e: Invalid ACSS Block id
Parser i: set Prox LUTs succeeded
Parser i: Copying PDC RR config\n
Parser e: Prox PD bin tables do no correlate\n
Parser e: underflow while reading GSC scalers
Vbl_FrameTime
display-subsystem
Parser e: Could not find PRC tables [%d:%d:%d] for bins [%d:%d]\n
Parser e: Prox PP bin tables do no correlate
SageFCMSIPTempDelta
Parser e: unsupported channel ACSS count: %u \n
Parser e: inconsistent PM index
IOMFB: unknown timestamp type: %d\n
Parser i: Processing BLAH format version %d data version %d\n
Parser e: unsupported sensor channel count: %u > %u\n
Parser e: unsupported PCS temperature count: %u > %u\n
Parser e: GSC exceeding max temperature count: %u > %u\n
Parser e: DOOC set data failed\n
Parser e: out of memory for IOMFBRDLCData
Parser e: parsing did not consume the full GSC size\n
Parser i: ABGM: gain_map_blob_size=0x%x\n
Parser e: underflow while reading R/G/BGLALS
Parser e: Failed to sort async PCS tables
Parser e: Step values should be nonzero\n
Parser e: unsupported AlsH version: 0x%x\n
Parser e: could not allocate memory for ABGM data
Parser e: duplicate tables\n
Parser e: unsupported NHS: %u != %u\n
Parser e: underflow while reading R/G/BGLACSS
Parser e: Unsupported type A XD channel count %d\n
Parser i: set user_cal_aft_gain succeeded\n
Parser e: channel not specified
Parser e: underflow while reading WgTypeB
Parser i: set BTPB data succeeded\n
Parser e: UFTG set data failed\n
Parser e: failed to set prox table config
ReqDCPResetNotifyFunc
Parser e: PMLUT[%d, %d, %d, %d, %d, %d] is all zeros\n
Parser i: ACSS_DEBUG: XD EMMP must be set separately\n
Parser e: no data
<AppleDisplayManager %p refcnt=%d>
Parser e: Bad size/version for HGOD
Parser i:  UPCL set DPCL data succeeded
Parser e: LLMT DBV Thresholds not in ascending order
kern_DisplayWallEnumerate called \n
Parser e: underflow while reading LUT coords\n
canvas_width
Parser e: DCLUT[%d, %d, %d, %d, %d, %d] is all zeros\n
SaturateNegativeCount
Parser e: set BCAL data failed\n
Parser e: UPCL set DPCL data failed\n
\n
Parser i: set HGOD data succeeded
Parser e: failed to set PTUC table rr config
IOMobileFramebufferCalibrationBegin called on external framebuffer \n
TimingElements
PerformanceStatistics
Parser e: failed to set ELVS table config
%s: Timeout: expect: %d current: %d\n
getExternalDisplayCount
Parser e: unsupported AlsR version: 0x%x\n
Parser e: too many EM lines %d\n
Parser e: underflow while reading R/G/BGLACSS\n
Parser e: failed to set LUS table config\n
Parser e: UBCL set data failed
MaxSrcRectTotal
Parser e: unsupported benl ACSS count: %u \n
Parser i: set PDC LUTs succeeded\n
Parser e: data size %d mismatch header %d\n
Parser i: ACSS_DEBUG: XD EMMP requires config XD\n
Parser e: LLMT APL Thresholds not in descending order\n
Parser e: set RDLC data failed
Parser e: Unexpected BLAH block version 0x%x\n
Parser i: processing RTPLC block version %d\n
DisplayCoexPrioritizeProx
Parser e: parsing did not consume the full PCS size
not enough values for callback %d != %d\n
Parser e: could not allocate memory for BCAL data
Parser e: Failed copy for heatmaps
Parser e: PDC missing at least 1 channel\n
Parser e: unspecified PP LUT brightness %d\n
Parser e: lerped DCLUT[%d, %d, %d, %d] is all zeros
Parser e: failed to set LUS table config
Parser e: underflow while reading EM mask
Parser e: Failed copy for EM LUTS
Parser e: bin tables do not correlate.
iomfb_populate_matched_displays
Parser i: set IRDC data succeeded\n
hid-input
Parser i: set RDLC data succeeded\n
Parser e: parsing did not consume the full SENS size\n
Parser e: Unexpected RXTK block version 0x%x\n
Parser e: underflow while reading EM Counts
Parser e: ACSS and ALSS should share either none or all of EMMP data
Parser e: missing PTUC RR LUTs
IOMFB: missing framebuffer for mirorr enable\n
Parser e: ALSS EMMP exceeding max temperature count: %u > %u\n
Parser i: set PTUC TLS LUTs succeeded\n
Parser e: no valid set block callback
ColorElements
Parser e: set BTHB data failed\n
Parser e: underflow while reading PCS scales\n
DisplayPortCount
Parser e: invalid block length for block %s\n
Parser e: too many EM scale intervals %d\n
Parser e: failed to set prox table config\n
Parser e: Failed to sort sync PCS tables
%s - postBlendLayer=%d event=%p waitValue=0x%llx\n
%s - event=%p signalOnGlassValue=0x%llx\n
Parser e: unsupported color count: %u > %u\n
Parser e: null header passed to process_uooc
Parser e: parsing did not consume the full HTMP size
SaturatePositiveCount
%s-%d
Parser e: unsupported color channel count: %u > %u\n
Parser e:  Invalid prox config encountered.\n
%s\n
Parser e: parsing did not consume the full RCFG size
Parser e: Unsupported type A channel count %d\n
SageUIBrightnessDim
Parser e: no valid set block callback\n
Parser e: ACSS EMMP exceeding max brightness count: %u > %u\n
Parser e: no memory for SPLX data
AppleParavirtGPU
%s: Start Runloop for 30 seconds\n
Parser e: input data not well-formed\n
Parser e: ALSS EMMP exceeding max brightness count: %u > %u\n
Parser e: unspecified PP LUT temperature %d C\n
Parser i: set PTUC table config succeeded
Parser e: missing PDC LUTs
Parser e: ACSS_ALS_RESCALE: set_block_cb failed\n
Parser e: unexpected PDC table version %d\n
Parser e: Counted vectors [%d][%d] mismatch expected [%d][%d]\n
Parser e: set SPLX data failed
Parser e: underflow while reading EMMK scalers
Parser e: failed to set PRC table config
Parser i: set PTUC table rr config succeeded
CMDegammaMethod
Parser e: UOOC set data failed\n
Parser i: set PDC LUTs succeeded
kern_DisplayMappingGet called \n
?
Parser e: too many Temp tap points %d\n
Parser i: set BTPB data succeeded
Parser e: out of memory for EMMP table\n
Parser e: unexpected PBDS block size 0x%x != 0x%x\n
Min_FrameTime
MaxSrcBufferHeight
Parser i: set PDC table config rr succeeded\n
Parser e: out of memory for PRC table
IOMFBIsHiloDevice
Parser i: set PSFA data succeeded\n
Parser e: set PSFA data failed\n
Parser e: lerped PMLUT[%d, %d, %d, %d, %d] is all zeros
Parser e: IRDC Block data and header size mismatch by %d too many bytes\n
Parser e: Failed to sort async PCS tables\n
Parser e: could not allocate memory for ABGM data\n
Parser e: Unexpected BLTS block version 0x%x\n
Parser e: PP LUT missing color channel\n
Parser i: set PTUC TLS RR LUTs succeeded
IOMFB: mirror enable kernel failure\n
ELVSSCalDataReversed
Parser e: LLMT APL Thresholds not in descending order
Parser i: PDC mix bin %g and bin %g with %g --> %g\n
Parser e: set PSFM data failed\n
Parser i: Prox PP LUT bin interpolation, bin = %g\n
BCBrtControlSetDisplayInvalidHandler
Parser e: set PSFM data failed
NeedSwapNotifyFunc: dropping notification since messages are pending\n
Parser e: unsupported NBBL: %u > %u\n
Parser i:  UOOC set data succeeded
IOMobileFramebuffer
%s - exceeded max number of blits: %d\n
IOMobileFramebufferCalibrationToolboxCommand command_id 0x%x only available on HILO device
%s: Runloop Timer expired: FB still not enumerated, notify main thread\n
IOMFB: no virtual display context installed\n
Parser e: set IRDC data failed\n
Parser e: useless PDC table
IOMFBScalingLimits
Parser e: UBCL set data failed\n
Dither_CRC
Parser e: reported PDC tap points (temp/DBV/RR/HGOD status) mismatch actual counts\n
Parser i: set ABGM data succeeded
Parser e: no memory
override_display_width
Parser e: parsing did not consume the full PDCC size
Parser e: underflow while reading PCS scales
Parser e: unexpected block size %d\n
%s: AppleParavirtGPU missing DisplayPortCount - shouldn't happen - error\n
Parser i: ABGM: width=%u height=%u start_x=%u start_y=%u\n
Parser i: set BCAL data succeeded
Parser e: set PSFA data failed
IOService
%s: %d\n
Did not find
Parser e: channel not specified\n
Parser e: Unsupported PCS XD config\n
\n \n
Parser i:  UFTG set data succeeded\n
Parser i: set PRC LUTs succeeded\n
Parser i: Prox PD LUT bin interpolation, bin = %g\n
Parser e: Prox PD bin tables do no correlate
kern_DisplayResourcesAllocationGet called \n
canvas_height
IOMFBTemperatureCompensationEnable
Parser e: unexpected LLMT block version %d\n
Parser e: parsing did not consume the full PCS size\n
Parser e: unsupported config: 0x%x\n
Parser e: underflow while temperature / brightness / emission freq
matched IOMFB (%p) to BC (%p) for DFR
com.apple.TritiumVSHCompensation.CumulativeOnTime
Parser i: set ELVC data succeeded\n
dcvrr-b
Parser e: is_xd not supported for this config version %u\n
Parser e: out of memory for PCS table copy
Parser e: Unsupported type B XD channel count %d\n
Parser e: underflow while reading GSC scalers\n
Parser e: EMMK exceeding max temperature count: %u > %u\n
Parser e: ACSS: set_block_cb failed\n
Parser e: underflow while reading WgTypeA
Parser e: underflow while reading PCS spare
IOConnectSetNotificationPort failed, error: %d\n
Parser e: underflow while reading R/G/BGLALS\n
Parser e: illegal frame count %d\n
Parser e: set DBMA data failed\n
Parser i: set PSFA data succeeded
Parser e: null header passed to process_uftg
%s: %s\n
Parser e: lut size too big\n
Parser e: parsing did not consume the full PDCC size\n
Parser e: set BCAL data failed
 %s:  Bad Argument\n
Parser e: Failed to parse PCS block\n
Parser e: Failed to parse RCFG block
%@%d
matched IOMFB (%p) to BC (%p) for embedded panel with display ID (%d)
IOMFB: FigInstallVirtualDisplay not found\n
Parser e: unknown header block name %s\n
Parser e: unsupported gray value count: %u > %u\n
Parser e: unsupported NHS: %u > %u\n
Parser e: failed to set ELVS table config\n
Parser e: no memory to prepare PDC LUTs
Parser e: DBCL set data failed
 %s:  failed, bad argument return %d \n
AppleNVMeEAN
Parser e: set QETC data failed\n
PDC temperatures
Parser i: set BTHB data succeeded
kern_DisplayReconfigComplete called \n
Warning: tried to match BC (%p) to IOMFB (%p) disp type (%d) with container ID (%s) - skip
Parser i: set IRDC vendor data succeeded\n
interpolate_prc_bins
Parser e: Unexpected DOOC block version 0x%x\n
 %s: Framebuffer found=%d return %d Name = %s\n
IOReturn IOMobileFramebufferKernelTests(IOMobileFramebufferRef, struct IOMFBKernelTestsArguments)
IOReturn kern_SwapSetPostBlendLayerEventSignalOnGlass(IOMobileFramebufferRef, IOSurfaceSharedEventRef, uint64_t)
Parser e: unsupported number of color channels\n
Parser e: missing gray scales (sync T%d B%d async T%d B%d)\n
Parser e: too many XD sensor channels %u\n
Parser i: PDC nframes: %d\n
Found ADM service\n
Parser e: Failed to validate pdc rr
RGBLayer_MaxScale
Parser e: unsupported gray step count: %u > %u\n
Parser e: EMMP Alt lut not supported\n
Parser e: Unexpected UOOC block version 0x%x\n
Parser e: mismatching versions: %u != 1,3,6, 7\n
BCBrtControlNewMonitorForAllDisplaysWithHandler
iomfb_populate_thread
IOMFB: ignoring cancelled swap\n
Parser e: out of memory for IOMFBELVCLUTs
Parser i: set RTPLC data succeeded
%s - postBlendLayer=%d event=%p signalValue=0x%llx\n
%s: Did not find a AppleParavirtGPU - shouldn't happen - error\n
Parser i: set LUS table config succeeded
Parser e: underflow while reading EM band steps
 %s:  failed IOServiceOpen. return %d \n
Parser e: duplicate PRC table found in input\n
Parser e: unsupported channel XD ACSS count: %u \n
Parser i: set BLTS data succeeded\n
Parser e: failed to set Prox PD LUT [t %d]\n
IOMFB: IOMobileFramebufferRelbufInfo API is enabled\n
Parser e: unexpected version %d for PDCp block\n
Parser e: mismatching versions: %u != 8\n
kern_DisplayResourcesAllocationSet called \n
IOMFB setting virtual mode: %d %d\n
, 
IOMFB: FrameInfoNotifyFunc dropped notification, numArgs is %u, expected %u
Parser e: could not allocate memory for DBMA data\n
%d
Parser e: could not allocate memory for DBMA data
APTFixedRR
uniformity2D
UserCalibration_SetCalibrationData Failed with %x\n
PRCBinningDebugEnable
Parser e: unsupported em gray level ACSS count: %u \n
Parser e: count %d total_count %d missing PDC LUTs\n
Parser e: failed to set PTUC TLS LUT brightness %d\n
Parser e: DC or PM LUT size too big
BCBrtControlSetNits
Parser e: unsupported region count: %u > %u\n
Parser i: processing SPLX block version %d\n
BCBrtControlGetIsValid
matched IOMFB (%p) to BC (%p) for external display
compatible
Parser e: UFTG set data failed
Parser i: set LLMT table config succeeded
%s: compatible: %s \n
Parser e: unsupported scaling intervals ACSS count: %u \n
Parser e: Incorrect SPLX block version %d (expected 1)\n
Parser e: set user_cal_aft_gain failed\n
Parser e: PRC table not well formed\n
AppleDisplayManagerOpen
override_panel_height
SwapSetIndicatorBrightnessLimit: Brightness control is not enabled\n
Parser e: out of memory for IOMFBELVCLUTs\n
Parser e: failed to set PDC LUT RR [%d %d %d %d] \n
IOMFB: surface lookup failure for id: %d\n
Parser e: unexpected value for polarity %d\n
Parser e: mismatching versions: %u != %u\n
UserCalibration_SetCalibrationData Failed to create parser object\n
Parser i: Processing RXTK format version %d data version %d\n
SwapSetDisplayEdr: Brightness control is not enabled\n
Parser e: unknown block name %s\n
Parser e: Failed to parse CNST block
canvas-width
Time
device_type
Parser e: PCS tables are NULL\n
Parser e: unsupported PCS ACSS count: %u \n
Parser e: unsupported region XD ACSS count: %u \n
Parser i: Copying PDC RR config
Parser e: underflow while reading LUT steps
%s: AppleParavirtGPU DisplayPortCount was not a 32 bit number - shouldn't happen - error\n
display-presentation
Parser e: unsupported pdmc emission freq: %u != %u\n
Parser e: missing prox PP table bin %d\n
SwapSetUserLuminanceAdjustmen: Brightness control is not enabled\n
Parser e: set ELVC data failed\n
Parser e: failed to set PTUC table rr config\n
Parser e: prox LUTs should come after config parameters
Parser e: duplicate PRC table found in input
Parser i: set PTUC TLS LUTs succeeded
FFR_raw_high_index
%s - too many active layers: %d\n
Parser i: set CA data succeeded\n
Parser e: no space to allocate heatmap
Parser i: %s: 
Parser i: set IRDC vendor data succeeded
Parser e: parsing did not consume the full GSC size
Parser i: ACSS_DEBUG: XD EMMP must be set separately
IOMFB: IOMobileFramebufferAPTQuantaSwitch : fb passed is NULL\n
NormalModeEnable
Parser i:  UPCL set DPCL data succeeded\n
Parser i: set prox table config succeeded\n
DisplayID
%s: Runloop Timer expired: FB mismatch but still main thread notified - so avoiding notify here\n
Parser e: cannot read NR and NC\n
IOMFB: SwapSetGainMap: map is NULL\n
Parser e: unsupported async PCS temperature count: %u > %u\n
Parser e: EMMP Alt lut not supported
com.apple.iokit.IOMobileGraphicsFamily
IOMFB: %s not found\n
IOMFB: hdcp reply too small for upstread header\n
dcvrr-version-control
Parser e: set CA data failed
IOMobileFramebufferOpenByName
getDisplayListNumber
IODeviceTree
Parser e: ELVC Block data and header size mismatch by %d too many bytes\n
Parser e: not enough durations provided for LUS LUTs
Parser e: failed to set LLMT table config
MaxSrcRectWidth
%s: Notify main thread as all FB callbacks hit\n
Parser e: UBCL num_entries exceeds maximum (%d): %d\n
Parser e: failed to set PTUC table config\n
Parser e: Failed to parse SENS Block\n
Parser e: Step values should be nonzero
Parser e: set ABGM data failed
Parser: SetBlock %u failed with 0x%x
FrameInfoNotifyFuncIOShqDispatchQueue IO Data Queue not available
Lib:couldn't set mach port limit\n
YUVLayer_MinScaleFraction
ACSSSupported
Parser e: no memory for LUTs
override_display_height
Parser e: inconsistent DC index\n
Parser i: Processing CNST version 0x%x\n
Parser e: lerped PMLUT[%d, %d, %d, %d] is all zeros
Parser i: set CA data succeeded
IOConnectMapMemory failed, error: %d\n
Parser i: set BCAL data succeeded\n
Parser e: set BLTS data failed\n
Parser e: missing PDC LUTs\n
IOReturn kern_SwapSetPostBlendLayer(IOMobileFramebufferRef, uint32_t, IOSurfaceRef, CGRect, CGRect, uint64_t)
SageMeasuredVoltPerNit
Parser e: set HGOD data failed\n
Parser i: ACSS_DEBUG: XD EMMP requires config XD
Parser e: ALSS: set_block_cb_failed
DFR
com.apple.iomfb.underrunType
IOMFB: %s: failed to fetch kIOMFBDisplayExternal property to determine index!\n
Parser e: set ELVC data failed
Parser e: set RDLC data failed\n
Parser e: unexpected version %d for PDCc block\n
Parser e: out of memory for PCS table\n
Parser e:  Invalid prox config encountered.
IOMFB: framebuffer allocation failed\n
Parser i: set LUS LUTs succeeded\n
Parser e: expected 3 color channels
Parser e: Bad size/version for HGOD\n
Parser e: set BTPB data failed\n
Parser e: unexpected PBDD block size 0x%x != 0x%x\n
GainMapVersion
Parser i: set PRC table config succeeded\n
Parser e: set DBMA data failed
IOMobileFramebufferGetMirrorError - no mirror source\n
Issued_time
Parser e: failed to set IRDC data \n
Parser e: no memory for LUTs\n
Parser e: unsupported EMMP ALSS temperature count: %u > %u\n
Parser e: unsupported benl emission freq count: %u != %u\n
Parser e: null header passed to process_ubcl\n
Parser e: couldn't read FFR high, using default\n
Parser e: Duplicate IRDf table for RR=%d\n
Parser e: unsupported em line ACSS count: %u \n
Parser i: set DBMA data succeeded\n
Parser e: failed to set Prox PP LUT [t %d b %d p %d]\n
Parser e: Failed to parse SENS Block
Parser e: Failed to sort EMMP tables
YUVLayer_MaxScale
Parser e: out of memory for PCS table
Parser e: PDC missing bin
Presentation_time
FrameInfoNotifyFunc IO Data Queue not available
UserCalibration_EraseEAN   failed \n
VDCL: %s Global Calibration Data for idx %d\n
Parser e: failed to set PRC table config\n
Parser i: all done
Parser e: EMMP table for ALSS is NULL
Parser e: ALSS: set_block_cb_failed\n
0x%x
PDC subframes
Parser i: Set ALSS EM config success
BuiltIn
Parser e: unexpected block version %d\n
Parser e: unsupported EMMP ACSS temperature count: %u > %u\n
```
