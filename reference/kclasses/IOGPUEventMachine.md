# `IOGPUEventMachine`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOGPUFamily`](../kexts/com.apple.iokit.IOGPUFamily.md)
- Object size: `0x1450` (5,200 bytes)
- Metaclass: `0xfffffe000b9f43d0`; metaclass vtable `0xfffffe0008373c08`; class vtable `0xfffffe0008373b28`
- Registration (init): `0xfffffe000a1046c8`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Direct subclasses (1; 1 in total)

- [`AGXEventMachine`](AGXEventMachine.md) — `com.apple.AGXG19P`

## Strings in its kext that name it (5)

- `virtual int32_t IOGPUEventMachine::requestStampIndexForChannel(IOGPUChannel *, IOGPUDevice *)`
- `site.IOGPUEventMachine`
- `IOGPUEventMachine.cpp`
- `\"IOGPUEventMachine::waitForStamp: Stamp test failed, but all submitted stamps are finished.  stamp[%08x]: %08x gpu_stamp: %08x\" @%s:%d`
- `IOGPUEventMachine`
