# `IOMobileFramebufferAP`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOMobileGraphicsFamily-DCP`](../kexts/com.apple.iokit.IOMobileGraphicsFamily-DCP.md)
- Object size: `0x5e30` (24,112 bytes)
- Metaclass: `0xfffffe000b9f79c8`; metaclass vtable `0xfffffe00083a8a40`; class vtable `0xfffffe00083a7ee0`
- Registration (init): `0xfffffe000a232cc4`
- Superclasses: [`IOMobileFramebufferService`](IOMobileFramebufferService.md) → [`IOMobileFramebuffer`](IOMobileFramebuffer.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 3 in total)

- [`UnifiedPipeline2`](UnifiedPipeline2.md) — `com.apple.driver.AppleMobileDispH19P-DCP`

## Strings in its kext that name it (22)

- `bool IOMobileFramebufferAP::isDevice(char *)`
- `site.IOMobileFramebufferAP`
- `virtual bool IOMobileFramebufferAP::start_client_state()`
- `virtual void IOMobileFramebufferAP::genlock_error_notify_gated(uint64_t)`
- `site.IOMobileFramebufferAP::NotifyEventData`
- `IOMobileFramebufferAP`
- `void IOMobileFramebufferAP::blit_surface_complete(IOMFBSwapIORequest *, uint32_t)`
- `void IOMobileFramebufferAP::surface_complete(IOMFBSwapIORequest *, uint32_t)`
- `virtual bool IOMobileFramebufferAP::init(OSDictionary *)`
- `void IOMobileFramebufferAP::blit_surface_complete(IOMFBDisplayedData *, uint32_t, uint32_t)`
- `static T *IOMFB::InstanceTracker::instance(tracked_entity_t, uint32_t) [T = IOMobileFramebufferAP]`
- `virtual IOMFBStatus IOMobileFramebufferAP::hdcp_get_reply(IOMemoryMap *, size_t *)`
- `virtual void IOMobileFramebufferAP::hotPlug_notify_gated(uint64_t, IOMFB_TiledDisplayInfo *, bool)`
- `IOMobileFramebufferAP.cpp`
- `IOMFBStatus IOMobileFramebufferAP::updateBufferMappingCount_gated(bool)`
- `void IOMobileFramebufferAP::surface_complete(IOMFBDisplayedData *, uint32_t, uint32_t)`
- `IOReturn IOMobileFramebufferAP::spinner_surface_alloc(IOSurface **, uint32_t, uint32_t, bool)`
- `static bool IOMobileFramebufferAP::readDataInEDT(IOService *, bool, const char *, const uint32_t, uint32_t *)`
- `void IOMobileFramebufferAP::setSystemConsoleMode_gated(bool)`
- `virtual bool IOMobileFramebufferAP::start(IOService *)`
- `IOReturn IOMobileFramebufferAP::surface_map_dcp(IOSurface *, IODMACommand **, dva_t *, bool)`
- `virtual IOSurfaceID IOMobileFramebufferAP::default_fb_surface_gated(uint32_t, uint32_t)`
