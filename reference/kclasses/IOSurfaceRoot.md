# `IOSurfaceRoot`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOSurface`](../kexts/com.apple.iokit.IOSurface.md)
- Object size: `0x4a0` (1,184 bytes)
- Metaclass: `0xfffffe000ba1b3b8`; metaclass vtable `0xfffffe00083fb990`; class vtable `0xfffffe00083fb438`
- Registration (init): `0xfffffe000a410888`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `FirstPersonality` in [`com.apple.iokit.IOSurface`](../kexts/com.apple.iokit.IOSurface.md): `IOProviderClass` = `IOResources`, `IOResourceMatch` = `IOBSD`, `IOMatchCategory` = `IOSurfaceRoot`

## Strings in its kext that name it (21)

- `IOSurfaceRootUserClient.cpp`
- `\"IOSurfaceRootUserClient: asked to allocate client shared id %08x not known by IOSurfaceRoot\" @%s:%d`
- `virtual bool IOSurfaceDeviceMemoryRegion::init(IOSurfaceRoot *, OSDictionary *, const char *, uint32_t, uint32_t)`
- `IOSurfaceRoot::alloc_surface_id: Map said entry free but something was there\n`
- `IOSurfaceRootUserClient: couldn't map shared memory region into client`
- `IOSurfaceRoot using IOSurfaceRootParavirtMapperInterface %p`
- `site.IOSurfaceRootUserClient`
- `IOSurfaceRoot.cpp`
- `IOSurfaceRoot`
- `\"IOSurfaceRootUserClient::set_surface_handle asked to set handle %08x that was not free: %p\" @%s:%d`
- `IOSurfaceRootUserClient`
- `IOSurfaceRootParavirtMapperInterface`
- `site.IOSurfaceRoot`
- `\"IOSurfaceRoot::removeEventNotifierClient() invoked with bad client notifier %p\" @%s:%d`
- `site.IOSurfaceRootParavirtMapperInterface`
- `\"IOSurfaceRoot::terminateDeviceCachesWithAccelerator() timeout.\" @%s:%d`
- `provider not IOSurfaceRoot\n`
- `IOSurfaceRoot: Initial shared event memory alloc failed\n`
- `IOSurfaceRoot: deadlock detection depth limit %d reached\n`
- `IOSurfaceRoot using IOSurfaceRootParavirtMapperInterface\n`
- `IOSurfaceRootUserClient: duplicate listener refcon %08llx\n`
