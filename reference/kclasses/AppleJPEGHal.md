# `AppleJPEGHal`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleJPEGDriver`](../kexts/com.apple.driver.AppleJPEGDriver.md)
- Object size: `0x118` (280 bytes)
- Metaclass: `0xfffffe000b955940`; metaclass vtable `0xfffffe000812eb50`; class vtable `0xfffffe000812eac0`
- Registration (init): `0xfffffe0009084654`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Strings in its kext that name it (14)

- `uint32_t AppleJPEGHal::checkHardwareVersion()`
- `IOReturn AppleJPEGHal::startEncoderGated(ajpeg_setup_t *)`
- `void AppleJPEGHal::interruptOccurred_gated(IOInterruptEventSource *, int)`
- `IOReturn AppleJPEGHal::createInterruptEventSource(IOWorkLoop *)`
- `void AppleJPEGHal::showErrorRequestInfo(ajpeg_setup_t *)`
- `site.AppleJPEGHal`
- `AppleJPEGHal`
- `bool AppleJPEGHal::checkForInterrupt(IOFilterInterruptEventSource *)`
- `IOReturn AppleJPEGHal::executeOperation_gated(ajpeg_setup_t *)`
- `IOReturn AppleJPEGHal::startDecoderGated(ajpeg_setup_t *)`
- `bool AppleJPEGHal::init(uint32_t, AppleJPEGDriver *, IOService *, IOWorkLoop *, uint32_t, bool, bool, uint32_t)`
- `IOReturn AppleJPEGHal::finishCoding_gated(ajpeg_setup_t *)`
- `void AppleJPEGHal::pollingForAXI()`
- `AppleJPEGDriver: ** AppleJPEGHal detects non-defined type 0x%x\n`
