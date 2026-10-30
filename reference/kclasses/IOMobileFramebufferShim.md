# `IOMobileFramebufferShim`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleMobileDispH19P-DCP`](../kexts/com.apple.driver.AppleMobileDispH19P-DCP.md)
- Object size: `0x65e8` (26,088 bytes)
- Metaclass: `0xfffffe000b97db10`; metaclass vtable `0xfffffe0008175c08`; class vtable `0xfffffe0008174e98`
- Registration (init): `0xfffffe000928ffcc`
- Superclasses: [`UnifiedPipeline2`](UnifiedPipeline2.md) → [`IOMobileFramebufferAP`](IOMobileFramebufferAP.md) → [`IOMobileFramebufferService`](IOMobileFramebufferService.md) → [`IOMobileFramebuffer`](IOMobileFramebuffer.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (7)

- `virtual IOMFBStatus IOMobileFramebufferShim::get_display_area(DisplayArea *)`
- `virtual bool IOMobileFramebufferTilingMgr::initTilingMgr(IOMobileFramebufferShim *)`
- `site.IOMobileFramebufferShim`
- `auto IOMobileFramebufferShim::set_matrix(uint32_t, const IOMFBMatrix *)::(anonymous class)::operator()(Gate::owner_t *, void *, void *, void *, void *) const`
- `virtual IOMFBStatus IOMobileFramebufferShim::set_matrix(uint32_t, const IOMFBMatrix *)`
- `virtual void IOMobileFramebufferShim::get_display_size(uint32_t *, uint32_t *) const`
- `IOMobileFramebufferShim`
