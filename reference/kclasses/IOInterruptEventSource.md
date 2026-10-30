# `IOInterruptEventSource`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: `com.apple.kernel` (kernel core)
- Object size: `0x68` (104 bytes)
- Metaclass: `0xfffffe000b835628`; metaclass vtable `0xfffffe0007f0a810`; class vtable `0xfffffe0007f0b018`
- Registration (init): `0xfffffe000b3b8304`
- Superclasses: [`IOEventSource`](IOEventSource.md)

## Direct subclasses (4; 4 in total)

- [`AppleUSBCableChangeEventSource`](AppleUSBCableChangeEventSource.md) — `com.apple.driver.AppleEmbeddedUSB`
- [`AppleUSBHostPortInterruptEventSource`](AppleUSBHostPortInterruptEventSource.md) — `com.apple.iokit.IOUSBHostFamily`
- [`IOFilterInterruptEventSource`](IOFilterInterruptEventSource.md) — `com.apple.kernel`
- [`IOInterruptQueueEventSource`](IOInterruptQueueEventSource.md) — `com.apple.driver.AudioDMAController-Gen5p0`
