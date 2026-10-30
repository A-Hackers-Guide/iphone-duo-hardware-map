# `com.apple.driver.AppleJPEGDriver`

- Name: AppleJPEGDriver
- Version: `8.1.8`
- UUID: `0114CB17-D438-38F5-939F-620F79249447`
- Source version: `8.1.8.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.iokit.CoreAnalyticsFamily`](com.apple.iokit.CoreAnalyticsFamily.md) 1.0.0, [`com.apple.iokit.IOSurface`](com.apple.iokit.IOSurface.md) 52.6.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.2.2, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.2.2, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.2.2, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.2.2, [`com.apple.kpi.private`](com.apple.kpi.private.md) 22.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/jpeg`](../devicetree/root__arm-io__jpeg.md) | `AppleJPEGDriver` | `jpeg,s5l8920x` |

## IOKit personalities (1) [KC]

### s5l8920x
- `CFBundleIdentifier`: `com.apple.driver.AppleJPEGDriver`
- `IOClass`: `AppleJPEGDriver`
- `IONameMatch`:
  - `jpeg,s5l8920x`
- `IOPersonalityPublisher`: `com.apple.driver.AppleJPEGDriver`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (25) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleJPEGDriver` | 0x170 | IOService → IORegistryEntry |
| `AppleJPEGDriverUserClient` | 0x110 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |
| `AppleJPEGHal` | 0x118 |  |
| `AppleJPEGWrapperControlLegacy` | 0x30 |  |
| `AppleJPEGWrapperControlV11` | 0x30 |  |
| `AppleJPEGWrapperControlV14` | 0x30 |  |
| `AppleJPEGWrapperControlV8` | 0x30 |  |
| `AppleJPEGWrapperControlV9` | 0x30 |  |
| `BorageFunctions` | 0x48 |  |
| `CatnipFunctions` | 0x48 |  |
| `ClaryFunctions` | 0x48 |  |
| `CloverFunctions` | 0x48 |  |
| `DahliaFunctions` | 0x48 |  |
| `DaisyFunctions` | 0x48 |  |
| `DandelionFunctions` | 0x48 |  |
| `HibiscusFunctions` | 0x48 |  |
| `IxoraFunctions` | 0x48 |  |
| `KopsiaFunctions` | 0x48 |  |
| `LegacyFunctions` | 0x18 |  |
| `LotusFunctions` | 0x48 |  |
| `NerineFunctions` | 0x48 |  |
| `StockFunctions` | 0x48 |  |
| `TansyFunctions` | 0x48 |  |
| `ThymeFunctions` | 0x48 |  |
| `TulipaFunctions` | 0x48 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00010b4c off=0x0053e400-0x0054ef4c addr=0xfffffe0007542400-0xfffffe0007552f4c r--/r--   __TEXT            
	sz=0x00002b2e off=0x0053eac8-0x005415f6 addr=0xfffffe0007542ac8-0xfffffe00075455f6               __TEXT.__cstring          (CstringLiterals)
	sz=0x00009ab7 off=0x005415f6-0x0054b0ad addr=0xfffffe00075455f6-0xfffffe000754f0ad               __TEXT.__os_log           
	sz=0x00003e9c off=0x0054b0b0-0x0054ef4c addr=0xfffffe000754f0b0-0xfffffe0007552f4c               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x0002cf4c off=0x02068270-0x020951bc addr=0xfffffe000906c270-0xfffffe00090991bc r-x/r-x   __TEXT_EXEC       
	sz=0x0002c8cc off=0x02068270-0x02094b3c addr=0xfffffe000906c270-0xfffffe0009098b3c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000680 off=0x02094b3c-0x020951bc addr=0xfffffe0009098b3c-0xfffffe00090991bc          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00003251 off=0x0494e8d0-0x04951b21 addr=0xfffffe000b9528d0-0xfffffe000b955b21 rw-/rw-   __DATA            
	sz=0x00002e58 off=0x0494e8d0-0x04951728 addr=0xfffffe000b9528d0-0xfffffe000b955728               __DATA.__data             
	sz=0x000003f8 off=0x00000000-0x000003f8 addr=0xfffffe000b955728-0xfffffe000b955b20               __DATA.__common           (Zerofill)
	sz=0x00000001 off=0x00000000-0x00000001 addr=0xfffffe000b955b20-0xfffffe000b955b21               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00006118 off=0x011283b8-0x0112e4d0 addr=0xfffffe000812c3b8-0xfffffe00081324d0 rw-/rw-   __DATA_CONST      
	sz=0x000000c8 off=0x011283b8-0x01128480 addr=0xfffffe000812c3b8-0xfffffe000812c480         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x000000c8 off=0x01128480-0x01128548 addr=0xfffffe000812c480-0xfffffe000812c548         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00004df0 off=0x01128548-0x0112d338 addr=0xfffffe000812c548-0xfffffe0008131338         __DATA_CONST.__const            
	sz=0x00000dc0 off=0x0112d338-0x0112e0f8 addr=0xfffffe0008131338-0xfffffe00081320f8         __DATA_CONST.__kalloc_type      
	sz=0x00000340 off=0x0112e0f8-0x0112e438 addr=0xfffffe00081320f8-0xfffffe0008132438         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000098 off=0x0112e438-0x0112e4d0 addr=0xfffffe0008132438-0xfffffe00081324d0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 227 at 0x04addf7c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     0114CB17-D438-38F5-939F-620F79249447
008: LC_SOURCE_VERSION           8.1.8.0.0
009: LC_FUNCTION_STARTS          offset=0x004aa6110 size=0x848
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleJPEGDriver`
- `CFBundleGetInfoString`: `Copyright © 2016-2025 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.AppleJPEGDriver`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleJPEGDriver`
- `CFBundleNumericVersion`: `135823360`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `8.1.8`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `8.1.8`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleJPEGDriver.kext`
- `_PrelinkExecutableLoadAddr`: `-2198900300800`
- `_PrelinkExecutableRelativePath`: `AppleJPEGDriver`
- `_PrelinkExecutableSize`: `290305`
- `_PrelinkExecutableSourceAddr`: `-2198900300800`
- `_PrelinkKmodInfo`: `-2198828930864`

## Strings (531) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `site.BorageFunctions`
- `DandelionFunctions`
- `site.AppleJPEGPU`
- `site.TansyFunctions`
- `format_444_12bit_linear_count`
- `AppleJPEGNumCores`
- `void AppleJPEGDriver::begin_io_gated(bool)`
- `size_decode_exlarge_count`
- `format_422_10bit_tiled_count`
- `format_400_10bit_packed_count`
- `core_0_requests_count`
- `virtual void AppleJPEGWrapperControl::set_jw_axi_tlimit(uint32_t)`
- `virtual bool HibiscusFunctions::setupAXIRegisterOffset(uint32_t, uint64_t)`
- `virtual IOService *AppleJPEGDriver::probe(IOService *, SInt32 *)`
- `IOReturn AppleJPEGDriver::finish_io_gated(JpegRequest *, IOReturn, uint32_t, bool)`
- `format_420_8bit_linear_count`
- `uint32_t AppleJPEGHal::checkHardwareVersion()`
- `site.CloverFunctions`
- `parseBootArgs`
- `site.ClaryFunctions`
- `IOReturn AppleJPEGHal::startEncoderGated(ajpeg_setup_t *)`
- `AppleJPEGWrapperControlV8`
- `site.AppleJPEGDriver`
- `bool AppleJPEGDriver::isSurfaceMultiPlane(IOSurface *)`
- `OSBoundedPtr.h`
- `size_encode_4m_count`
- `size_decode_1m_count`
- `IxoraFunctions`
- `AppleJPEGSupportsDCTScaling`
- `size_encode_1m_count`
- `format_400_8bit_tiled_count`
- `virtual bool TulipaFunctions::setupAXIRegisterOffset(uint32_t, uint64_t)`
- `NerineFunctions`
- `site.QueueManager`
- `IOReturn AppleJPEGCoreAnalyzer::start(IOService *, IOServiceMatchingNotificationHandler)`
- `format_400_encode_count`
- `ClaryFunctions`
- `enableDeviceClockLowLevel`
- `singleClockIndexDevice`
- `IOReturn AppleJPEGDriver::setupBuffersForCoding_gated(JpegRequest *)`
- `format_argb_10bit_tiled_count`
- `format_444_8bit_tiled_count`
- `virtual bool CatnipFunctions::setupAXIRegisterOffset(uint32_t, uint64_t)`
- `setParameter`
- `site.JpegRequest`
- `AppleJPEGRequiresMCUAlignment`
- `getCPUType`
- `TulipaFunctions`
- `virtual bool NerineFunctions::detectFastsim()`
- `1211111212221212111111111111111212`
- `void AppleJPEGDriver::interruptOccurred_gated(JpegRequest *, uint32_t)`
- `AppleJPEGWrapperControlV9`
- `virtual uint32_t AppleJPEGWrapperControl::read_jw_axi_tlimit()`
- `AppleJPEGSupportsAppleInterchangeFormats`
- `IOUserClientEntitlements`
- `enableDeviceClockWrapper`
- `LotusFunctions`
- `1111111`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `format_420_decode_count`
- `format_422_10bit_linear_count`
- `setIomdCacheAttribute`
- `virtual bool KopsiaFunctions::setupAXIRegisterOffset(uint32_t, uint64_t)`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `ThymeFunctions`
- `AppleJPEGDriverUserClient`
- `AppleJPEGSupportsRSTLogging`
- `IOReturn AppleJPEGDriver::startDecoderExt(AppleJPEGDriverIOStructExt *, AppleJPEGDriverIOStructExt *, mach_port_t, IOUserClient *, task_t)`
- `format_420_encode_count`
- `site.CatnipFunctions`
- `bool AppleJPEGPU::_getPUPower()`
- `site.LotusFunctions`
- `virtual bool StockFunctions::setupAXIRegisterOffset(uint32_t, uint64_t)`
- `site.AppleJPEGCoreAnalyzer`
- `IOReturn AppleJPEGDriver::startDecoder(AppleJPEGDriverIOStruct *, AppleJPEGDriverIOStruct *, mach_port_t, IOUserClient *, task_t)`
- `%s_%d_%d*%d_[%u]_%x`
- `size_decode_4m_count`
- `format_420_10bit_packed_count`
- `decode_requests_count`
- `virtual bool DahliaFunctions::setupAXIRegisterOffset(uint32_t, uint64_t)`
- `format_411_encode_count`
- `format_444_10bit_linear_count`
- `com.apple.jpegdriverevents.codecRequests`
- `site.AppleJPEGWrapperControlLegacy`
- `121`
- `com.apple.jpegdriverevents.jpegFormat`
- `deQueue`
- `AppleJPEGDriver`
- `121121`
- `site.RequestHandling`
- `IOReturn AppleJPEGDriver::attachCoreAnalyticsService(void *, IOService *, IONotifier *)`
- `IOReturn AppleJPEGDriver::setPowerState_gated(unsigned long, IOService *)`
- `site.NerineFunctions`
- `jpeg-disableWorkaround`
- `format_444_10bit_tiled_count`
- `encode_requests_count`
- `com.apple.applejpegdriver.ajpegtestapp`
- `AppleJPEGWrapperControlLegacy`
- `LegacyFunctions`
- `DahliaFunctions`
- `AppleJPEGWrapperControlV14`
- `void AppleJPEGDriver::release_codec_gated(uint32_t)`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `site.AppleJPEGWrapperControlV8`
- `IOReturn AppleJPEGWrapperControl::encoderHWSetup(ajpeg_setup_t *)`
- `format_444_8bit_linear_count`
- `format_400_12bit_linear_count`
- `IOReturn AppleJPEGDriver::startEncoder2024(AppleJPEGDriverIOStruct2024 *, AppleJPEGDriverIOStruct2024 *, mach_port_t, IOUserClient *, task_t)`
- `void AppleJPEGCoreAnalyzer::submitAnalyticData()`
- `format_444_decode_count`
- `com.apple.applejpegdriver.poweron`
- `virtual bool AppleJPEGDriver::start(IOService *)`
- `IOReturn AppleJPEGDriver::queue_io_gated(JpegRequest *)`
- `Fast Clock frames_%d`
- `format_420_12bit_linear_count`
- `void AppleJPEGHal::interruptOccurred_gated(IOInterruptEventSource *, int)`
- `virtual uint32_t AppleJPEGWrapperControl::read_idle2bcg_trigger()`
- `void AppleJPEGDriver::getMCUSize(AppleJPEGSubsampling, unsigned int &, unsigned int &, unsigned int &)`
- `die-id`
- `iomdEarlyPurge`
- `site.KopsiaFunctions`
- `virtual IOReturn AppleJPEGDriver::newUserClient(task_t, void *, UInt32, OSDictionary *, IOUserClient **)`
- `format_411_decode_count`
- `format_undefined_count`
- `IOUserClientDefaultLockingSetProperties`
- `virtual bool AppleJPEGDriver::init(OSDictionary *)`
- `axi2af_parity_enable`
- `AppleJPEGSupportsCompressedInterchangeFormats`
- `format_argb_10bit_linear_count`
- `format_422_8bit_tiled_count`
- `IOReturn AppleJPEGHal::createInterruptEventSource(IOWorkLoop *)`
- `cacheFlushInactive`
- `virtual void AppleJPEGWrapperControl::set_jw_axi_tcount(uint32_t)`
- `virtual void AppleJPEGWrapperControl::set_idle2bcg_trigger(uint32_t)`
- `static IOReturn AppleJPEGDriver::IODARTErrorHandler(void *, const IODARTErrorInfo *)`
- `IOReturn AppleJPEGDriver::startDecoder2024(AppleJPEGDriverIOStruct2024 *, AppleJPEGDriverIOStruct2024 *, mach_port_t, IOUserClient *, task_t)`
- `iomdEarlyReclaim`
- `1211111212221212121111111222112222122222211111`
- `IOCoreSurfaceRoot`
- `site.ThymeFunctions`
- `site.AppleJPEGWrapperControlV14`
- `size_decode_256k_count`
- `format_400_10bit_linear_count`
- `void AppleJPEGHal::showErrorRequestInfo(ajpeg_setup_t *)`
- `IOReturn RequestHandling::decodeRequestValidation(JpegRequest *)`
- `virtual bool DaisyFunctions::setupAXIRegisterOffset(uint32_t, uint64_t)`
- `IOReturn AppleJPEGWrapperControl::reset_jpeg_block()`
- `iomd-cache-size`
- `AppleJPEGSupports12BitsFormat`
- `IOReturn AppleJPEGDriver::doRestOfBufferSetupForEncode_gated(JpegRequest *)`
- `void AppleJPEGDriver::convertToRequestSubSampleMode(AppleJPEGSubsampling, JpegRequest *)`
- `size_encode_exlarge_count`
- `com.apple.jpegdriverevents.coreRequests`
- `core_1_requests_count`
- `StockFunctions`
- `11112111121`
- `112221111111112212112222222221222222222222222222222222222222222222222222222222222222222111122222112222222222222222222222222222222222222222222222212222222121112222222222222`
- `format_400_10bit_tiled_count`
- `format_422_12bit_linear_count`
- `DaisyFunctions`
- `site.AppleJPEGHal`
- `site.AppleJPEGWrapperControlV11`
- `AppleJPEGSupportsMissingEOI`
- `com.apple.jpegdriverevents.frameBufferFormatEncode`
- `virtual bool IxoraFunctions::setupAXIRegisterOffset(uint32_t, uint64_t)`
- `site.DandelionFunctions`
- `TansyFunctions`
- `virtual uint32_t AppleJPEGWrapperControl::read_jw_axi_tcount()`
- `virtual uint32_t AppleJPEGWrapperControl::read_idle2bcg_en()`
- `site.DahliaFunctions`
- `virtual bool CloverFunctions::setupAXIRegisterOffset(uint32_t, uint64_t)`
- `site.AppleJPEGPM`
- `sleepCommandGate`
- `turnOnJPEGHW_gated`
- `virtual void AppleJPEGWrapperControl::set_idle2bcg_en(uint32_t)`
- `/tmp/jpegtest_`
- `format_420_8bit_tiled_count`
- `site.AppleJPEGDriverUserClient`
- `HibiscusFunctions`
- `AppleJPEGIsLegacyDevice`
- `format_422_encode_count`
- `format_422_decode_count`
- `virtual bool BorageFunctions::setupAXIRegisterOffset(uint32_t, uint64_t)`
- `virtual bool DandelionFunctions::setupAXIRegisterOffset(uint32_t, uint64_t)`
- `AppleJPEGWrapperControlV11`
- `virtual void AppleJPEGWrapperControlLegacy::ajpeg_drv_set_decode_submode(ajpeg_setup_t *)`
- `IOReturn AppleJPEGDriver::startEncoderExt(AppleJPEGDriverIOStructExt *, AppleJPEGDriverIOStructExt *, mach_port_t, IOUserClient *, task_t)`
- `ajpeg_drv_set_image_boundary`
- `format_444_encode_count`
- `format_400_decode_count`
- `IOReturn AppleJPEGDart::mapMemoryDescriptor(IOMemoryDescriptor *, uint32_t, IODMACommand **, IOPhysicalAddress *, s_debug_info *)`
- `%s_%d_%d*%d_%x`
- `\"%s\" @%s:%d`
- `size_encode_256k_count`
- `format_argb_12bit_tiled_count`
- `format_422_10bit_packed_count`
- `IOReturn RequestHandling::encodeHWRequestSetup(JpegRequest *)`
- `iomd-cache-ttl`
- `IOReturn AppleJPEGDriver::startEncoder(AppleJPEGDriverIOStruct *, AppleJPEGDriverIOStruct *, mach_port_t, IOUserClient *, task_t)`
- `uint32_t AppleJPEGDriver::assign_codec_gated(JpegRequest *)`
- `AppleJPEGHal`
- `site.StockFunctions`
- `registerErrorHandler`
- `size_decode_12m_count`
- `121111111`
- `virtual IOReturn AppleJPEGDriverUserClient::registerNotificationPort(mach_port_t, UInt32, UInt32)`
- `site.LegacyFunctions`
- `bool AppleJPEGHal::checkForInterrupt(IOFilterInterruptEventSource *)`
- `void AppleJPEGDriver::showRequestInfo(JpegRequest *)`
- `com.apple.jpegdriverevents.frameBufferFormat`
- `format_420_10bit_linear_count`
- `site.DaisyFunctions`
- `IOReturn AppleJPEGDriver::dumpBitstream(JpegRequest *)`
- `format_444_10bit_packed_count`
- `KopsiaFunctions`
- `void RequestHandling::matrixConvYUVtoRGBA(ajpeg_setup_t *)`
- `init`
- `virtual bool NerineFunctions::setupAXIRegisterOffset(uint32_t, uint64_t)`
- `12211111111111112221122222222122222`
- `hw-type`
- `void AppleJPEGCoreAnalyzer::collectCoreDataFromRequest(JpegRequest *)`
- `IOUserClientDefaultLockingSingleThreadExternalMethod`
- `CatnipFunctions`
- `IOReturn RequestHandling::decodeHWRequestSetup(JpegRequest *)`
- `IOReturn AppleJPEGHal::executeOperation_gated(ajpeg_setup_t *)`
- `QueueManager`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `site.IxoraFunctions`
- `virtual bool TansyFunctions::setupAXIRegisterOffset(uint32_t, uint64_t)`
- `void AppleJPEGDriver::checkDARTException()`
- `format_argb_linear_count`
- `BorageFunctions`
- `CloverFunctions`
- `start`
- `IOReturn AppleJPEGHal::startDecoderGated(ajpeg_setup_t *)`
- `IOReturn AppleJPEGDart::registerMapper(uint32_t, uint32_t, IOService *)`
- `site.AppleJPEGDart`
- `bool AppleJPEGHal::init(uint32_t, AppleJPEGDriver *, IOService *, IOWorkLoop *, uint32_t, bool, bool, uint32_t)`
- `site.HibiscusFunctions`
- `IOReturn AppleJPEGDriver::doRestOfBufferSetupForDecode_gated(JpegRequest *)`
- `Norm Clock frames_%d`
- `format_argb_12bit_linear_count`
- `virtual bool ClaryFunctions::setupAXIRegisterOffset(uint32_t, uint64_t)`
- `IOReturn AppleJPEGHal::finishCoding_gated(ajpeg_setup_t *)`
- `virtual void AppleJPEGDriver::clientClosedGated(AppleJPEGDriverUserClient *)`
- `virtual bool ThymeFunctions::setupAXIRegisterOffset(uint32_t, uint64_t)`
- `IOUserClientDefaultLocking`
- `function-set_perf_state_floor`
- `IOReturn AppleJPEGDart::unmapMemoryDescriptor(IOMemoryDescriptor *, uint32_t, IODMACommand *, uint32_t)`
- `IOReturn RequestHandling::encodeRequestValidation(JpegRequest *)`
- `jpeg-log`
- `setActive`
- `jpeg-fsim`
- `format_argb_tiled_count`
- `format_422_8bit_linear_count`
- `void AppleJPEGHal::pollingForAXI()`
- `void AppleJPEGPM::setPUPowerState(uint32_t, bool, bool)`
- `virtual bool LotusFunctions::setupAXIRegisterOffset(uint32_t, uint64_t)`
- `IOReturn AppleJPEGCoreAnalyzer::checkFrameBufferFormat(uint32_t, uint32_t)`
- `bool AppleJPEGWrapperControl::getIsFsim() const`
- `222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111`
- `size_encode_12m_count`
- `112`
- `%s_%d_%d*%d_[%u_%u]_%x`
- `format_400_8bit_linear_count`
- `format_420_10bit_tiled_count`
- `site.TulipaFunctions`
- `site.AppleJPEGWrapperControlV9`
- `com.apple.jpegdriverevents.picSize`
- `CoreAnalyticsHub`

**[__TEXT.__os_log]**

- `AppleJPEGDriver: %s: codec=%d, buffer overflow on write dma error triggered\n`
- `AppleJPEGDriver: %s : dartAddress NULL`
- `AppleJPEGDriver: ** AppleJPEGDriver detects type 0x%x CPU!!!\n`
- `AppleJPEGDriver: ** %s[%p] : 'jpeg-disableWorkaround' boot-arg detected: %u\n`
- `AppleJPEGDriver: %s, ERROR: returned codec is %d not valid!!!!!!\n`
- `AppleJPEGDriver: ** %s : failed, returns %x\n`
- `AppleJPEGDriver: %s : Dimension Info: %d x %d`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Illegal rddma p0 metadata base address at compress mode %d\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Encode cannot handle IMG_YUV10_420_2P to CMP_YUV_444\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Encode cannot handle IMG_pYUV12_420_2P to CMP_YUV_444\n`
- `AppleJPEGDriver: %s(): NULL mCoreAnalyzer!\n`
- `AppleJPEGDriver: ** %s[%p] : die-id = %u\n`
- `AppleJPEGDriver: %s : fail to alloc mPlatformFunc\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Encode cannot handle IMG_YUV_422_1P to CMP_YUV_444\n`
- `AppleJPEGDriver: %s(): Forcing clock speed to %u\n`
- `AppleJPEGDriver: %s unknown subsampling mode %d\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : setup->stride_p1 = 0x%x. MUST BE 8B MULTIPLE FOR MODE 0x%x!\n`
- `AppleJPEGDriver: ** %s : Source address is not 32 byte aligned\n`
- `AppleJPEGDriver: ** %s : failed to mapping rst header start address\n`
- `AppleJPEGDriver: %s : vn_rdwr() returned %d\n`
- `AppleJPEGDriver: ** %s : dim out of range pixelsX=%u pixelsY=%u decW=%u decH=%u cropW=%u cropH=%u cropOffX=%u cropOffY=%u\n`
- `AppleJPEGDriver: %s : dest surface [%d] bad luma plane size. Plane Size : %d, Min Plane Size : %llu; Plane Width : %d, Height : %d;  Min Plane Width : %d, Height : %d\n`
- `AppleJPEGDriver: ** %s[%p] : 'jpeg-log' boot-arg detected: 0x%x\n`
- `AppleJPEGDriver: %s [%p] : provider %p, instance %p, result %x FAILED.\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Illegal Decode Submode %d at line %d\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : PACKED IMG_pYUV10_444_2P on chroma AVG sub-sample must have even width %x at line %d\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Encode cannot handle any CMP_YUV_411\n`
- `AppleJPEGDriver: %s : log file is %s\n`
- `AppleJPEGDriver: %s: encode tiled mode: %d, quality: %d, restart: %d`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Decode cannot handle any IMG_YUV10_444_1P\n`
- `AppleJPEGDriver: %s[%p] : cannot initialize the initLock, mpInitlock=%p`
- `AppleJPEGDriver: FATAL ERROR: Check setup : BAD IMAGE Encode MODE %x at line %d\n`
- `AppleJPEGDriver: %s(): HW version read from register 0x%x does not match EDT value 0x%x\n`
- `AppleJPEGDriver: ** %s : [%d] plane count %d, stride %d, plane stride [%d,%d], allocation size 0x%x\n`
- `AppleJPEGDriver: %s : vnode_open() returned %d\n`
- `AppleJPEGDriver: * %s: no codec registerated for this power unit`
- `AppleJPEGDriver: ** %s wrong codec number %d\n`
- `AppleJPEGDriver: ** %s : mapMemoryDescriptor 0x%x\n`
- `AppleJPEGDriver: %s: failed to map fuse descriptor at 0x%llx\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Encode cannot handle IMG_YUV_420_2P to CMP_YUV_422\n`
- `AppleJPEGDriver: ** AppleJPEGDriver type from register 0x%x\n`
- `AppleJPEGDriver: ** %s [%p] : user client failed to attach to driver's IORegistry!!!\n`
- `AppleJPEGDriver: %s: fail to read hw-type from EDT!\n`
- `AppleJPEGDriver: %s : codec %d is not busy!!!\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Encode cannot handle IMG_pYUV10_420_2P to CMP_YUV_444\n`
- `AppleJPEGDriver: %s: codec, tlimit [%p], tlimit_outstanding [%p]\n`
- `AppleJPEGDriver: ** %s[%p] : JPEG HCLK Frequency %llu MHz, wrapper Frequency %llu Mhz\n`
- `AppleJPEGDriver: * %s mPendingSetup is NULL - ignoring interrupt`
- `AppleJPEGDriver: ** %s : input/output size too small. Bailing out. input jpeg file size %d, output buffer size %d,\n`
- `AppleJPEGDriver: %s : fail to init mPlatformFunc\n`
- `AppleJPEGDriver: * %s expecting event source: %p, got: %p`
- `AppleJPEGDriver: ** %s : why is the assigned codec %d for req %p, this codec %d !!!!!!\n`
- `AppleJPEGDriver: %s : mHal unexpectedly NULL\n`
- `AppleJPEGDriver: %s: ERROR: Width larger than stride, P1: %x > %x\n is packed format %d `
- `AppleJPEGDriver: FATAL ERROR: Check setup : Encode cannot handle IMG_YUV_422_2P to CMP_YUV_444\n`
- `AppleJPEGDriver: %s(): IOService start() method failed!\n`
- `AppleJPEGDriver: %s: running on specified core: %d\n`
- `AppleJPEGDriver: * %s : Could not add the interrupt source.\n`
- `AppleJPEGDriver: %s : Codec %d, Task ID %u Async %d`
- `AppleJPEGDriver: ** %s : ERROR, setMemoryDesc failed with code 0x%x\n`
- `AppleJPEGDriver: %s(): Successfully added codec num %u [%p]\n`
- `AppleJPEGDriver: %s : codec %d, RegisterMemoryMap %p, Device Memory Count = %u\n`
- `AppleJPEGDriver: ** AppleJPEGHal detects non-defined type 0x%x\n`
- `AppleJPEGDriver: %s : fail to set mPlatformFunc axi offset\n`
- `AppleJPEGDriver: %s: unknown pixeformat 0x%x (%c%c%c%c)`
- `AppleJPEGDriver: %s: ERROR: Width larger than stride, P1: %x > %x\n`
- `AppleJPEGDriver: Setting up notifier for %s\n`
- `AppleJPEGDriver: %s : codec %d base %p phy_add %p length %u, freq %lluMHz\n`
- `AppleJPEGDriver: ** %s : bytesPerRow and width incompatible %d %d %d %d\n`
- `AppleJPEGDriver: ** %s : Source Address 0x%08llx is not 4096 byte aligned\n`
- `AppleJPEGDriver: ** %s : unsupported encoding quality %d detcted, quality limit is %d \n`
- `AppleJPEGDriver: ** %s : [%d] mode %d, w*h [%d * %d], input format %c%c%c%c , output format %c%c%c%c\n`
- `AppleJPEGDriver: %s : Error Request Info\n`
- `AppleJPEGDriver: ** %s[%p] : intForPM with provider=%p\n`
- `AppleJPEGDriver: ** %s : sourceMemoryDesc prepare failed\n`
- `AppleJPEGDriver: %s(): NULL power provider!\n`
- `AppleJPEGDriver: ** %s : ERROR, mMapper kIODARTIOMDCacheTTLKey fail with code %d`
- `AppleJPEGDriver: ** %s : ERROR, address is NULL`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Encode cannot handle IMG_pYUV12_420_2P to CMP_YUV_422\n`
- `AppleJPEGDriver: * %s : Virtual function, shall not be called`
- `AppleJPEGDriver: ** %s : HW is busy waiting for idle, %d codecs busy\n`
- `AppleJPEGDriver: %s:[%d] std_done %x, dma done %x error=0x%x, pendingRequst=%p\n`
- `AppleJPEGDriver: %s : Input IOSurface illegal dimensions (Width %d x Height %d), specified dimensions (Width %d x Height %d), bailing ! ! !\n`
- `AppleJPEGDriver: %s(): DART registerMapper() failed with %d!\n`
- `AppleJPEGDriver: * %s: Failed to cast CoreAnalyticsHub`
- `AppleJPEGDriver: ** %s : ERROR: request is null!\n`
- `AppleJPEGDriver: ** %s: too many dart exceptions from malicious file in 1sec, total exception open %lld, close %lld\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Encode cannot handle IMG_YUV12_422_2P to CMP_YUV_420\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Illegal rddma p0 address at compress mode %d\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Illegal Encode Submode %d at line %d\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : setup->rddma_base_adr_p0 = 0x%x. MUST BE 4B ALIGNED FOR MODE 0x%x!\n`
- `AppleJPEGDriver: %s : dartHwStatus NULL`
- `AppleJPEGDriver: ** %s: newHeaderSize %u exceeds MARKERRAM_MEM_SIZE %u, rejecting\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Encode cannot handle IMG_YUV12_420_2P to CMP_YUV_422\n`
- `AppleJPEGDriver: %s: unknown bit depth %d`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Encode cannot handle IMG_pYUV12_422_2P to CMP_YUV_420\n`
- `AppleJPEGDriver: * %s: mCoreAnalyzer is null`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Illegal width and height setting, pixel_width_x: %d, pixel_height_y: %d\n`
- `AppleJPEGDriver: ** %s : Source Address is not 32 byte aligned, jpegAddress=0x%llx, offset=%d\n`
- `AppleJPEGDriver: ** %s: sourceSurface failed to prepare, return value 0x%x\n`
- `AppleJPEGDriver: ** ERROR: did not find request 0x%p in the queue, result is 0x%p\n`
- `AppleJPEGDriver: %s : codec=%d, Compressed jpeg size %d > output buffer size, input [%dw x% dh], encoding quality setting %u\n`
- `AppleJPEGDriver: ** %s : ERROR, mapper is NULL, code %d`
- `AppleJPEGDriver: %s(): NULL mIOSurfaceRoot!\n`
- `AppleJPEGDriver: %s : Error! NULL JPEG request, returnFromInterrupt = %d\n`
- `AppleJPEGDriver: * %s Driver is not supporting RGB 565 anymore! \n`
- `AppleJPEGDriver: FATAL ERROR: encode codec=%d\n`
- `AppleJPEGDriver: * %s: unexpect format for analyzing %d.`
- `AppleJPEGDriver: %s(): Core Analyzer start() failed with %d!\n`
- `AppleJPEGDriver: %s [%p] : Failed to get user client  pUserClient=%p, or client already gone\n`
- `AppleJPEGDriver: ** %s[%p] : perf state handler %p`
- `AppleJPEGDriver: %s(): NULL JPEG register memory map!\n`
- `AppleJPEGDriver: %s : dartAXIId = 0x%x\n`
- `AppleJPEGDriver: %s(): Power manager registerPU() failed with %d!\n`
- `AppleJPEGDriver: * %s : failed to pass the request validation return 0x%x`
- `AppleJPEGDriver: %s: codec, tlimit vir [%p], tlimit_outstanding vir [%p]\n`
- `AppleJPEGDriver: %s: codec=%d, AXI bus error triggered\n`
- `AppleJPEGDriver: * %s : codec %d failed in decoderHWSetup return 0x%x`
- `AppleJPEGDriver: * %s: WARNING: not all codecs are registerated for this power unit`
- `AppleJPEGDriver: %s : SW Reset failed (2) at line %d, failed values 0x%x\n`
- `AppleJPEGDriver: %s : dartAXIId NULL\n`
- `AppleJPEGDriver: %s : fail to alloc AppleJPEGWrapperControl\n`
- `AppleJPEGDriver: AppleJPEGDriver::startDecoderGated(), x/y scale is not supported %d : %d, width: [%d]/[%d], height [%d]/[%d]\n`
- `AppleJPEGDriver: %s : dartHwError = %s\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Encode cannot handle IMG_YUV10_420_2P to CMP_YUV_422\n`
- `AppleJPEGDriver: ** %s : Source Address 0x%08llx is not 4 byte aligned\n`
- `AppleJPEGDriver: ** %s: crop offset out of bounds: offsetX %u * MCUWidth %u = %u > pixelsX %u, offsetY %u * MCUHeight %u = %u > pixelsY %u\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Decode cannot handle any IMG_pYUV12_4XX_2P modes!\n`
- `AppleJPEGDriver: %s(): NULL mJpegDart!\n`
- `AppleJPEGDriver: %p %p %p %x\n`
- `AppleJPEGDriver: %s : handle the unwanted JPEG interrupts\n`
- `AppleJPEGDriver: FATAL ERROR: decode codec=%d\n`
- `AppleJPEGDriver: ** %s : can't get source surface memory descriptor\n`
- `AppleJPEGDriver: %s(): Device Memory Count is 0!\n`
- `AppleJPEGDriver: %s: decode v2c:%d, cropping %d, scaling %d`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Encode cannot handle IMG_pYUV12_422_2P to CMP_YUV_444\n`
- `AppleJPEGDriver: ** %s : Dest Address is not 4096 byte aligned\n`
- `AppleJPEGDriver: %s : dartHwError NULL`
- `AppleJPEGDriver: ** %s : bytesPerRow and width incompatible %d %d, bytesPerElement %d, expected %d\n`
- `AppleJPEGDriver: %s, executeOperation failed with 0x%x\n`
- `AppleJPEGDriver: * %s: checkJpegFormat error 0x%x`
- `AppleJPEGDriver: ** %s : ERROR, mMapper kIODARTIOMDCacheSizeKey fail with code %d`
- `AppleJPEGDriver: %s(): NULL mWorkLoop!\n`
- `AppleJPEGDriver: %s(): NULL mCommandQueueManager!\n`
- `AppleJPEGDriver: %s(): NULL mRequestHandler!\n`
- `AppleJPEGDriver: ** %s: destinanationSurface failed to prepare, return value 0x%x\n`
- `AppleJPEGDriver: * %s: picture size error 0x%x`
- `AppleJPEGDriver: %s: codec, desc=%p, map=%p\n`
- `AppleJPEGDriver: * %s : Could not get the interrupt source.\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Illegal rddma p1 address at compress mode %d\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Decode cannot handle any IMG_RGB101010_1P\n`
- `AppleJPEGDriver: %s(): Error! enableDeviceClock(en = %u, idx = %u) returned %d\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : BAD IMAGE Decode MODE %x at line %d\n`
- `AppleJPEGDriver: %s: fail to read the hw-type from EDT, unrecognized char %d!\n`
- `AppleJPEGDriver: %s : Software Reset of codec %d Failed\n`
- `AppleJPEGDriver: ** %s : codec index %d is larger than maximum allowed value %d`
- `AppleJPEGDriver: ** %s : ERROR, mCommandPool[%d] is NULL`
- `AppleJPEGDriver: ** %s : xOffset %u / yOffset %u / pixelsX %u / pixelsY %u out of range\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Encode cannot handle IMG_pYUV10_422_2P to CMP_YUV_444\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : setup->wrdma_base_adr_p1 = 0x%x. MUST BE 8B ALIGNED FOR MODE 0x%x!\n`
- `AppleJPEGDriver: %s(): NULL mJpegPM!\n`
- `AppleJPEGDriver: %s(): TIMEOUT %dms\n`
- `AppleJPEGDriver: %s(): Device has only 1 clock index in the EDT (type = 0x%x, hardware version = 0x%x)\n`
- `AppleJPEGDriver: ** %s : pixelX %d, pixelY %d, decodeWidth %d, decodeHeight %d, xOffset %d, yOffset %d\n`
- `AppleJPEGDriver: %s : dartIsWrite = 0x%x\n`
- `AppleJPEGDriver: %s(): Fastsim detected via platform fuses\n`
- `AppleJPEGDriver: + %s [%p] :  task 0x%p, securityID %p, type %u, properties %p, handler %p`
- `AppleJPEGDriver: ** %s : ERROR, dart fail to gen segments with error code 0x%x\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Illegal rddma p1 metadata base address address at compress mode %d\n`
- `AppleJPEGDriver: %s(): getNodeIndex() failed with %d!\n`
- `AppleJPEGDriver: %s(): ERROR: start function failed for codec num %u [provider = %p this = %p]\n`
- `AppleJPEGDriver: * %s : interrupt after error detected!\n`
- `AppleJPEGDriver: ** %s : codec %d is version 0x%x\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Encode cannot handle IMG_YUV12_420_2P to CMP_YUV_444\n`
- `AppleJPEGDriver: ** %s : Destination Address 0x%08llx is not 32 byte aligned\n`
- `AppleJPEGDriver: %s : error: mJPEGAXIRegisterDescriptor=%p\n`
- `AppleJPEGDriver: %s : mIsActive=%d,  mIsInterruptEventSourceEnabled=%d\n`
- `AppleJPEGDriver: FATAL ERROR: ajpeg_drv_setx_encode_CMP_YUV_422 illegal mode!\n`
- `AppleJPEGDriver: %s(): NULL mCommandGate!\n`
- `AppleJPEGDriver: ** %s [%p] : provider %p probing again!  Inconceivable!\n`
- `AppleJPEGDriver: %s : dartHwStatus = 0x%x\n`
- `AppleJPEGDriver: %s(): Invalid codec number %u >= %u!\n`
- `AppleJPEGDriver: %s wait for idle done, powering off\n`
- `AppleJPEGDriver: ** %s : destMemoryDesc prepare failed\n`
- `AppleJPEGDriver: %s: codec, vir=%p, phy=%p, length=%u\n`
- `AppleJPEGDriver: ** %s : ERROR, mMapper IODARTErrorHandler fail with code %d`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Encode cannot handle IMG_YUV12_422_2P to CMP_YUV_444\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Decode cannot handle CMP_YUV_420 to IMG_YUV_444_2P\n`
- `AppleJPEGDriver: * %s invalid NULL surface`
- `AppleJPEGDriver: jpeg_huffman_set() - Invalid input\n`
- `AppleJPEGDriver: %s: failed to create fuse descriptor at 0x%llx\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Encode cannot handle IMG_YUV_420_2P to CMP_YUV_444\n`
- `AppleJPEGDriver: ** %s : can't get dest surface memory descriptor\n`
- `AppleJPEGDriver: ** %s : ERROR, command is NULL`
- `AppleJPEGDriver: %s(): Skipping HW version check [0x%x (reg), 0x%x (EDT)]\n`
- `AppleJPEGDriver: ** AppleJPEGDriver[%p]::startDecoder :  inputJPEGStruct %p, outputJPEGStruct %p\n`
- `AppleJPEGDriver: %s: codec, axi register=%p\n`
- `AppleJPEGDriver: %s : image_mode %d, submode %d`
- `AppleJPEGDriver: FATAL ERROR: ajpeg_drv_setx_encode_CMP_YUV_444 illegal mode!\n`
- `AppleJPEGDriver: * %s : failed to pass the request setup return 0x%x`
- `AppleJPEGDriver: ** %s base_addr: %llx  does not match any physical address. \n`
- `AppleJPEGDriver: * %s : xOffset = %d, yOffset = %d, hdr_width=%d, hdr_height=%d, stride=%d, height=%d, failure %d\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Encode cannot handle IMG_pYUV10_422_2P to CMP_YUV_420\n`
- `AppleJPEGDriver: ** %s[%p] : 'axi2af_parity_enable' boot-arg detected: %u\n`
- `AppleJPEGDriver: ** %s : cn=%d WaitingIdle && BusyCodecs==0: mCodecHal[%d] still active! loadScore = %llu\n`
- `AppleJPEGDriver: %s: pre-silicon platform (PV_RUNTIME_ENV=0x%x, JPEG_PRESENT=0x%x), fastsim=%d\n`
- `AppleJPEGDriver: %s : codec=%d, BitStream Corruption type [ %d ] was detected during body decoding\n`
- `AppleJPEGDriver: FATAL ERROR: ajpeg_drv_setx_encode_CMP_YUV_400 illegal mode!\n`
- `AppleJPEGDriver: **%s : dest lookup or lock failed %d %p\n`
- `AppleJPEGDriver: %s, ERROR: specified core %d doesn't exist on this device\n`
- `AppleJPEGDriver: %s:[%d] Error: Still has pending transaction. May have issue when reset.\n`
- `AppleJPEGDriver: %s : SW Reset failed (1) at line %d, failed value 0x%x\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Encode cannot handle IMG_YUV10_422_2P to CMP_YUV_420\n`
- `AppleJPEGDriver: ** %s[%p] : 'jpeg-fsim' boot-arg detected: %u\n`
- `AppleJPEGDriver: ** %s [%p] : %lld clients in queue, Open=%lld, Close=%lld, Open-Close=%lld\n`
- `AppleJPEGDriver: %s(): unknown %dms - status: 0x%x\n`
- `AppleJPEGDriver: jpeg_qtbl_set() - Invalid input\n`
- `AppleJPEGDriver: %s: codec=%d, buffer overflow from codec IP error triggered\n`
- `AppleJPEGDriver: %s(): Error! enablePsdService(en = %u, ltr = %u, dieId = %u) returned %d\n`
- `AppleJPEGDriver: ** %s: newHeaderSize %u is not a multiple of 12 bytes, rejecting\n`
- `AppleJPEGDriver: %s : ajpeg_drv_set_encode() failed, bailing ! ! !\n`
- `AppleJPEGDriver: * %s : xOffset = %d, yOffset = %d, pixelsX=%d, pixelsY=%d, stride=%d, height=%d, failure %d\n`
- `AppleJPEGDriver: %s(): Failed to alloc mpQueueLock!\n`
- `AppleJPEGDriver: ** %s : error 0x%x\n`
- `AppleJPEGDriver: ** %s :  Error sending async result 0x%x\n`
- `AppleJPEGDriver: %s : errorInfo->IsWrite NULL`
- `AppleJPEGDriver: ** %s: elementCount %u exceeds partialDecodeFakeHeader capacity %zu, rejecting\n`
- `AppleJPEGDriver: FATAL ERROR: ajpeg_drv_setx_encode_CMP_YUV_420 illegal mode!\n`
- `AppleJPEGDriver: * %s: No Available CoreAnalyticsHub`
- `AppleJPEGDriver: %s : error: mJPEGAXIRegisterMemoryMap=%p\n`
- `AppleJPEGDriver: ** %s[%p] : codecNumber %d, parent %p, provider %p, power %p\n`
- `AppleJPEGDriver: %s: codec=%d, buffer overflow on read dma error triggered\n`
- `AppleJPEGDriver: %s(): Error! function-set_perf_state_floor failed to set perf to %d! (result = %d)\n`
- `AppleJPEGDriver: %s(): NULL mCodecHal[%u]!\n`
- `AppleJPEGDriver: * %s: Failed to match the notifier`
- `AppleJPEGDriver: ** %s [%p] user client failed to start!!!\n`
- `AppleJPEGDriver: %s: Client active, cannot switch port\n`
- `AppleJPEGDriver: %s : Input JPEG stream size %llu less than miniumum of %u bytes, bailing \n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : setup->stride_p0 = 0x%x. MUST BE 4B MULTIPLE FOR MODE 0x%x!\n`
- `AppleJPEGDriver: ** %s [%p] : ERROR: total codec num %d, limiting to %d`
- `AppleJPEGDriver: * %s [%p] : task [0x%p] client close %p\n`
- `AppleJPEGDriver: ** %s : Dest Address is not 4 byte aligned\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Decode cannot handle CMP_YUV_411 to IMG_YUV_444_2P\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Encode cannot handle IMG_pYUV10_420_2P to CMP_YUV_422\n`
- `AppleJPEGDriver: %s: ERROR: Width larger than stride, P0: %x > %x\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Illegal scale factor %d\n`
- `AppleJPEGDriver: %s: JPEG not found in EDT!\n`
- `AppleJPEGDriver: ** %s : i/o sizes are illegal (inputSize %d, req->outputSize %d)! or Horz (%d) and Vert (%d) Resolutions are not set\n`
- `AppleJPEGDriver: %s : createInterruptEventSource failed!\n`
- `AppleJPEGDriver: ** %s: startOfRawBitStream %u >= sourceSurface allocSize %llu, rejecting\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : setup->wrdma_base_adr_p0 = 0x%x. MUST BE 4B ALIGNED FOR MODE 0x%x!\n`
- `AppleJPEGDriver: %s : dartAddress = 0x%llx\n`
- `AppleJPEGDriver: ** %s : failed, returns %x\n\n`
- `AppleJPEGDriver: %s: ERROR: Width larger than stride, P0: %x > %x, is packed format %d \n`
- `AppleJPEGDriver: %s(): queue[%d] is empty\n`
- `AppleJPEGDriver: ** %s : source lookup or lock failed %d %p\n`
- `AppleJPEGDriver: ** %s :  inputJPEGStruct %p, outputJPEGStruct %p\n`
- `AppleJPEGDriver: FATAL ERROR: Check setup : Decode cannot handle CMP_YUV_422 to IMG_YUV_444_2P\n`
- `AppleJPEGDriver: %s(): Failed to initialize mCodecHal[%u]!\n`
- `AppleJPEGDriver: %s, ERROR: specified core doesn't exist on this platform\n`
- `AppleJPEGDriver: %s : codec=%d, Hardware Timeout error triggered\n`
