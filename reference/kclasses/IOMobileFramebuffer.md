# `IOMobileFramebuffer`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOMobileGraphicsFamily`](../kexts/com.apple.iokit.IOMobileGraphicsFamily.md)
- Object size: `0x90` (144 bytes)
- Metaclass: `0xfffffe000b9fa5c8`; metaclass vtable `0xfffffe00083ade60`; class vtable `0xfffffe00083ad5b0`
- Registration (init): `0xfffffe000a2538dc`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 6 in total)

- [`IOMobileFramebufferService`](IOMobileFramebufferService.md) — `com.apple.iokit.IOMobileGraphicsFamily`

## Strings in its kext that name it (38)

- `void IOMobileFramebufferLegacy::surface_complete(IOMFBDisplayedData *, uint32_t)`
- `IOReturn IOMobileFramebufferLegacy::hdcp_send_request_gated(const uint8_t *, size_t, IOMFBNotifyRequestArgs *)`
- `virtual void IOMobileFramebufferUserClient::stop(IOService *)`
- `virtual IOMFBStatus IOMobileFramebufferLegacy::swap_submit(IOMFBSwap *, IOUserClient *, uint32_t *)`
- `virtual bool IOMobileFramebufferLegacy::start(IOService *)`
- `site.IOMobileFramebufferLegacy`
- `void IOMobileFramebufferLegacy::disp_has_no_clients_gated()`
- `%s: more than %d current instances of IOMobileFramebuffer!\n`
- `site.IOMobileFramebufferService`
- `IOMobileFramebufferLegacy`
- `static IOReturn IOMobileFramebufferUserClient::s_hdcp_send_request(IOMobileFramebufferUserClient *, void *, IOExternalMethodArguments *)`
- `IOReturn IOMobileFramebufferLegacy::spinner_surface_alloc(IOSurface **)`
- `IOReturn IOMobileFramebufferUserClient::hdcp_get_reply(const uint8_t *, size_t *)`
- `IOMobileFramebuffer`
- `IOMobileFramebufferRuntimeProperties.cpp`
- `bool IOMobileFramebufferLegacy::verifyKeepOnScreen_gated(IOMFBSwapIORequest *)`
- `void IOMobileFramebufferLegacy::record_swap_info_gated(IOMFBSwapIORequest *, IOMFBSwapCompletionState)`
- `void IOMobileFramebufferLegacy::surface_complete(IOMFBSwapIORequest *, uint32_t, bool)`
- `site.IOMobileFramebuffer`
- `IOMobileFramebufferService`
- `virtual bool IOMobileFramebufferLegacy::init(OSDictionary *)`
- `virtual IOMFBStatus IOMobileFramebufferLegacy::hdcp_get_reply(IOMemoryMap *, size_t *)`
- `static IOReturn IOMobileFramebufferUserClient::s_hdcp_get_reply(IOMobileFramebufferUserClient *, void *, IOExternalMethodArguments *)`
- `bool IOMobileFramebufferLegacy::setDisplayRefreshProperties()`
- `void IOMobileFramebufferLegacy::getCurrentActiveRegions_gated(uint32_t, const IOMFBRect **, uint32_t *) const`
- `site.IOMobileFramebufferUserClient`
- `virtual void IOMobileFramebufferLegacy::writeDebugInfo_gated(OSDictionary *)`
- `void IOMobileFramebufferLegacy::parse_RTP_boot_args()`
- `IOMobileFramebufferUserClient.cpp`
- `IOMobileFramebufferLegacy.cpp`
- `void IOMobileFramebufferLegacy::setSystemConsoleMode_gated(bool)`
- `IOReturn IOMobileFramebufferLegacy::updateBufferMappingCount_gated(bool)`
- `static IOReturn IOMobileFramebufferUserClient::s_map_display_type(IOMobileFramebufferUserClient *, void *, IOExternalMethodArguments *)`
- `bool IOMobileFramebufferLegacy::isDevice(char *)`
- `IOMobileFramebufferUserClient`
- `virtual IOMFBStatus IOMobileFramebufferLegacy::get_color_remap_mode(DisplayColorRemapMode *) const`
- `bool IOMobileFramebufferLegacy::isLayerValidForSwap(uint32_t, IOMFBSwapIORequest *)`
- `static bool IOMobileFramebufferLegacy::readDataInEDT(IOService *, bool, const char *, const uint32_t, uint32_t *)`
