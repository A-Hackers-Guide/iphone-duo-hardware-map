# `AppleJPEGDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleJPEGDriver`](../kexts/com.apple.driver.AppleJPEGDriver.md)
- Object size: `0x170` (368 bytes)
- Metaclass: `0xfffffe000b955760`; metaclass vtable `0xfffffe000812d210`; class vtable `0xfffffe000812cca0`
- Registration (init): `0xfffffe0009078cd8`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `s5l8920x` in [`com.apple.driver.AppleJPEGDriver`](../kexts/com.apple.driver.AppleJPEGDriver.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['jpeg,s5l8920x']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/jpeg`](../devicetree/root__arm-io__jpeg.md) on `jpeg,s5l8920x`

## Strings in its kext that name it (60)

- `void AppleJPEGDriver::begin_io_gated(bool)`
- `virtual IOService *AppleJPEGDriver::probe(IOService *, SInt32 *)`
- `IOReturn AppleJPEGDriver::finish_io_gated(JpegRequest *, IOReturn, uint32_t, bool)`
- `site.AppleJPEGDriver`
- `bool AppleJPEGDriver::isSurfaceMultiPlane(IOSurface *)`
- `IOReturn AppleJPEGDriver::setupBuffersForCoding_gated(JpegRequest *)`
- `void AppleJPEGDriver::interruptOccurred_gated(JpegRequest *, uint32_t)`
- `AppleJPEGDriverUserClient`
- `IOReturn AppleJPEGDriver::startDecoderExt(AppleJPEGDriverIOStructExt *, AppleJPEGDriverIOStructExt *, mach_port_t, IOUserClient *, task_t)`
- `IOReturn AppleJPEGDriver::startDecoder(AppleJPEGDriverIOStruct *, AppleJPEGDriverIOStruct *, mach_port_t, IOUserClient *, task_t)`
- `AppleJPEGDriver`
- `IOReturn AppleJPEGDriver::attachCoreAnalyticsService(void *, IOService *, IONotifier *)`
- `IOReturn AppleJPEGDriver::setPowerState_gated(unsigned long, IOService *)`
- `void AppleJPEGDriver::release_codec_gated(uint32_t)`
- `IOReturn AppleJPEGDriver::startEncoder2024(AppleJPEGDriverIOStruct2024 *, AppleJPEGDriverIOStruct2024 *, mach_port_t, IOUserClient *, task_t)`
- `virtual bool AppleJPEGDriver::start(IOService *)`
- `IOReturn AppleJPEGDriver::queue_io_gated(JpegRequest *)`
- `void AppleJPEGDriver::getMCUSize(AppleJPEGSubsampling, unsigned int &, unsigned int &, unsigned int &)`
- `virtual IOReturn AppleJPEGDriver::newUserClient(task_t, void *, UInt32, OSDictionary *, IOUserClient **)`
- `virtual bool AppleJPEGDriver::init(OSDictionary *)`
- `static IOReturn AppleJPEGDriver::IODARTErrorHandler(void *, const IODARTErrorInfo *)`
- `IOReturn AppleJPEGDriver::startDecoder2024(AppleJPEGDriverIOStruct2024 *, AppleJPEGDriverIOStruct2024 *, mach_port_t, IOUserClient *, task_t)`
- `IOReturn AppleJPEGDriver::doRestOfBufferSetupForEncode_gated(JpegRequest *)`
- `void AppleJPEGDriver::convertToRequestSubSampleMode(AppleJPEGSubsampling, JpegRequest *)`
- `site.AppleJPEGDriverUserClient`
- `IOReturn AppleJPEGDriver::startEncoderExt(AppleJPEGDriverIOStructExt *, AppleJPEGDriverIOStructExt *, mach_port_t, IOUserClient *, task_t)`
- `IOReturn AppleJPEGDriver::startEncoder(AppleJPEGDriverIOStruct *, AppleJPEGDriverIOStruct *, mach_port_t, IOUserClient *, task_t)`
- `uint32_t AppleJPEGDriver::assign_codec_gated(JpegRequest *)`
- `virtual IOReturn AppleJPEGDriverUserClient::registerNotificationPort(mach_port_t, UInt32, UInt32)`
- `void AppleJPEGDriver::showRequestInfo(JpegRequest *)`
- `IOReturn AppleJPEGDriver::dumpBitstream(JpegRequest *)`
- `void AppleJPEGDriver::checkDARTException()`
- `bool AppleJPEGHal::init(uint32_t, AppleJPEGDriver *, IOService *, IOWorkLoop *, uint32_t, bool, bool, uint32_t)`
- `IOReturn AppleJPEGDriver::doRestOfBufferSetupForDecode_gated(JpegRequest *)`
- `virtual void AppleJPEGDriver::clientClosedGated(AppleJPEGDriverUserClient *)`
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
