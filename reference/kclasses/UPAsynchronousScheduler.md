# `UPAsynchronousScheduler`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOMobileGraphicsFamily`](../kexts/com.apple.iokit.IOMobileGraphicsFamily.md)
- Object size: `0xb060` (45,152 bytes)
- Metaclass: `0xfffffe000b9fa748`; metaclass vtable `0xfffffe00083afa80`; class vtable `0xfffffe00083af9c8`
- Registration (init): `0xfffffe000a25a51c`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Strings in its kext that name it (15)

- `UPAsynchronousScheduler.cpp`
- `site.UPAsynchronousScheduler`
- `IOMFBStatus UPAsynchronousScheduler_::prepareThread(ArgumentID *, void *, void *, void *, void *)`
- `UPAsynchronousScheduler`
- `void UPAsynchronousScheduler_::releaseArgumentEntry(ArgumentEntry *, bool)`
- `UPAsynchronousScheduler_::ArgumentEntry *UPAsynchronousScheduler_::createArgumentEntry()`
- `IOMFBStatus UPAsynchronousScheduler_::startThreadWithAction(Action, ArgumentID *, void *, void *, void *, void *)`
- `IOMFBStatus UPAsynchronousScheduler_::prepareThreadWithAction(Action, ArgumentID *, void *, void *, void *, void *)`
- `IOMFBStatus UPAsynchronousScheduler_::notifyThread(ArgumentID, void *, void *, void *, void *)`
- `void UPAsynchronousScheduler::performActions_gated()`
- `IOMFBStatus UPAsynchronousScheduler::abortThread(ArgumentID)`
- `virtual void UPAsynchronousScheduler::free()`
- `virtual IOMFBStatus UPAsynchronousScheduler::checkAndQueueArgument(ArgumentEntry *)`
- `virtual bool UPAsynchronousScheduler::init(const char *, uintptr_t, size_t, uint32_t)`
- `IOMFBStatus UPAsynchronousScheduler_::setDefaultAction(Action)`
