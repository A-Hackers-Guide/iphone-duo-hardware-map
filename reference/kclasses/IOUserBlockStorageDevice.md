# `IOUserBlockStorageDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOStorageFamily`](../kexts/com.apple.iokit.IOStorageFamily.md)
- Object size: `0x118` (280 bytes)
- Metaclass: `0xfffffe000ba1ac10`; metaclass vtable `0xfffffe00083f2d58`; class vtable `0xfffffe00083f2750`
- Registration (init): `0xfffffe000a3d2390`
- Superclasses: [`IOBlockStorageDevice`](IOBlockStorageDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (14)

- `virtual void IOUserBlockStorageDevice::stop(IOService *)`
- `virtual IOReturn IOUserBlockStorageDevice::doSynchronize(UInt64, UInt64, IOStorageSynchronizeOptions)`
- `void IOUserBlockStorageDevice::Complete_Impl(uint32_t, kern_return_t)`
- `virtual IOReturn IOUserBlockStorageDevice::doUnmap(IOBlockStorageDeviceExtent *, UInt32, IOStorageUnmapOptions)`
- `void IOUserBlockStorageDevice::CompleteIO_Impl(uint32_t, uint64_t, kern_return_t)`
- `IOUserBlockStorageDevice`
- `kern_return_t IOUserBlockStorageDevice::StartDev_Impl(IOService *, const DeviceParams *)`
- `site.IOUserBlockStorageDevice`
- `virtual bool IOUserBlockStorageDevice::willTerminate(IOService *, IOOptionBits)`
- `virtual bool IOUserBlockStorageDevice::init(OSDictionary *)`
- `virtual bool IOUserBlockStorageDevice::start(IOService *)`
- `virtual IOReturn IOUserBlockStorageDevice::doEjectMedia()`
- `virtual IOReturn IOUserBlockStorageDevice::doAsyncReadWrite(IOMemoryDescriptor *, uint64_t, uint64_t, IOStorageAttributes *, IOStorageCompletion *)`
- `kern_return_t IOUserBlockStorageDevice::RegisterDext_Impl()`
