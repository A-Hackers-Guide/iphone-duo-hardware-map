# `IOAVHandler`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOMobileGraphicsFamily`](../kexts/com.apple.iokit.IOMobileGraphicsFamily.md)
- Object size: `0x40` (64 bytes)
- Metaclass: `0xfffffe000b9fa6d0`; metaclass vtable `0xfffffe00083af4d8`; class vtable `0xfffffe00083af418`
- Registration (init): `0xfffffe000a256eb4`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Direct subclasses (1; 1 in total)

- [`IOAVHandlerInternalDisplay`](IOAVHandlerInternalDisplay.md) — `com.apple.iokit.IOMobileGraphicsFamily`

## Strings in its kext that name it (12)

- `site.IOAVHandlerInternalDisplay`
- `IOAVHandler`
- `site.IOAVHandler`
- `static IOReturn IOAVHandler::IOAVEvent_async(void *, void *, void *)`
- `IOAVHandler.cpp`
- `IOAVHandlerInternalDisplay`
- `IOReturn IOAVHandler::linkShutdown_gated()`
- `virtual void IOAVHandlerInternalDisplay::plugEvent_async_gated(IOAVVideoInterface *)`
- `IOAVHandlerInternalDisplay.cpp`
- `\"%s: could not cast pointer to IOAVHandler *\" @%s:%d`
- `bool IOAVHandler::IOAVEvent(IOAVEventType, IOService *)`
- `void IOAVHandler::IOAVEvent_async_gated(void *, void *)`
