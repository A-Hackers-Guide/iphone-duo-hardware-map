# `AppleWrapperMailbox`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleA7IOP`](../kexts/com.apple.driver.AppleA7IOP.md)
- Object size: `0x160` (352 bytes)
- Metaclass: `0xfffffe000b932340`; metaclass vtable `0xfffffe0007f984c8`; class vtable `0xfffffe0007f97da8`
- Registration (init): `0xfffffe000867138c`
- Superclasses: [`AppleIOP`](AppleIOP.md) → [`IOSlaveCPU`](IOSlaveCPU.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (7)

- `virtual bool AppleWrapperMailbox::start(IOService *)`
- `virtual IOReturn AppleWrapperMailbox::getMailboxBulk(void *, unsigned int *)`
- `virtual bool AppleWrapperMailbox::setDoorbellAction(IOSlaveCPU::DoorbellAction, OSObject *, void *, UInt32)`
- `AppleWrapperMailbox`
- `virtual IOPhysicalAddress AppleWrapperMailbox::getWrapperPhysicalAddress()`
- `site.AppleWrapperMailbox`
- `virtual bool AppleWrapperMailbox::_outboxHandler(IOInterruptEventSource *)`
