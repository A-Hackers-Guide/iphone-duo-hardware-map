# `RTKitNetKernelSharedMemory`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.RTKitNet`](../kexts/com.apple.iokit.RTKitNet.md)
- Object size: `0xa0` (160 bytes)
- Metaclass: `0xfffffe000ba24248`; metaclass vtable `0xfffffe000849c210`; class vtable `0xfffffe000849bcb8`
- Registration (init): `0xfffffe000a9563f0`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IORTKitNetSharedMemory` in [`com.apple.iokit.RTKitNet`](../kexts/com.apple.iokit.RTKitNet.md): `IOProviderClass` = `AFKSharedMemoryRegionBase`, `IONameMatch` = `aop2.network.aop2apkernel`, `IOResourceMatch` = `IOBSD`

## Strings in its kext that name it (4)

- `site.RTKitNetKernelSharedMemory`
- `RTKitNetKernelSharedMemory`
- `/Library/Caches/com.apple.xbs/236004E1-A52B-48CC-92D8-0A3096B3CEC6/TemporaryDirectory.BreRZD/Sources/RTKitNet_AP_Libraries/src/AlwaysOnNetworking/RTKitNet/RTKitNetKernelSharedMemory.cpp`
- `%30s:%d RTKitNetKernelSharedMemory::start, shared memory size %llu less than required %zu\n`
