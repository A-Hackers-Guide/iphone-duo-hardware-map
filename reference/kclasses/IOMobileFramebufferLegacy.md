# `IOMobileFramebufferLegacy`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOMobileGraphicsFamily`](../kexts/com.apple.iokit.IOMobileGraphicsFamily.md)
- Object size: `0x1de0` (7,648 bytes)
- Metaclass: `0xfffffe000b9feb10`; metaclass vtable `0xfffffe00083b12d8`; class vtable `0xfffffe00083b06e8`
- Registration (init): `0xfffffe000a2697bc`
- Superclasses: [`IOMobileFramebufferService`](IOMobileFramebufferService.md) → [`IOMobileFramebuffer`](IOMobileFramebuffer.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (24)

- `void IOMobileFramebufferLegacy::surface_complete(IOMFBDisplayedData *, uint32_t)`
- `IOReturn IOMobileFramebufferLegacy::hdcp_send_request_gated(const uint8_t *, size_t, IOMFBNotifyRequestArgs *)`
- `virtual IOMFBStatus IOMobileFramebufferLegacy::swap_submit(IOMFBSwap *, IOUserClient *, uint32_t *)`
- `virtual bool IOMobileFramebufferLegacy::start(IOService *)`
- `site.IOMobileFramebufferLegacy`
- `void IOMobileFramebufferLegacy::disp_has_no_clients_gated()`
- `IOMobileFramebufferLegacy`
- `IOReturn IOMobileFramebufferLegacy::spinner_surface_alloc(IOSurface **)`
- `bool IOMobileFramebufferLegacy::verifyKeepOnScreen_gated(IOMFBSwapIORequest *)`
- `void IOMobileFramebufferLegacy::record_swap_info_gated(IOMFBSwapIORequest *, IOMFBSwapCompletionState)`
- `void IOMobileFramebufferLegacy::surface_complete(IOMFBSwapIORequest *, uint32_t, bool)`
- `virtual bool IOMobileFramebufferLegacy::init(OSDictionary *)`
- `virtual IOMFBStatus IOMobileFramebufferLegacy::hdcp_get_reply(IOMemoryMap *, size_t *)`
- `bool IOMobileFramebufferLegacy::setDisplayRefreshProperties()`
- `void IOMobileFramebufferLegacy::getCurrentActiveRegions_gated(uint32_t, const IOMFBRect **, uint32_t *) const`
- `virtual void IOMobileFramebufferLegacy::writeDebugInfo_gated(OSDictionary *)`
- `void IOMobileFramebufferLegacy::parse_RTP_boot_args()`
- `IOMobileFramebufferLegacy.cpp`
- `void IOMobileFramebufferLegacy::setSystemConsoleMode_gated(bool)`
- `IOReturn IOMobileFramebufferLegacy::updateBufferMappingCount_gated(bool)`
- `bool IOMobileFramebufferLegacy::isDevice(char *)`
- `virtual IOMFBStatus IOMobileFramebufferLegacy::get_color_remap_mode(DisplayColorRemapMode *) const`
- `bool IOMobileFramebufferLegacy::isLayerValidForSwap(uint32_t, IOMFBSwapIORequest *)`
- `static bool IOMobileFramebufferLegacy::readDataInEDT(IOService *, bool, const char *, const uint32_t, uint32_t *)`
