# `IOBlockStorageDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOStorageFamily`](../kexts/com.apple.iokit.IOStorageFamily.md)
- Object size: `0x90` (144 bytes)
- Metaclass: `0xfffffe000ba1ac60`; metaclass vtable `0xfffffe00083f3a88`; class vtable `0xfffffe00083f3480`
- Registration (init): `0xfffffe000a3d3d90`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (6; 10 in total)

- [`AppleARMNORPanicLogDevice`](AppleARMNORPanicLogDevice.md) — `com.apple.driver.AppleARMPlatform`
- [`AppleDiskImageDevice`](AppleDiskImageDevice.md) — `com.apple.driver.AppleDiskImages2`
- [`IOBlockStorageServices`](IOBlockStorageServices.md) — `com.apple.iokit.IOSCSIBlockCommandsDevice`
- [`IOHDIXHDDriveNub`](IOHDIXHDDriveNub.md) — `com.apple.driver.DiskImages`
- [`IONVMeBlockStorageDevice`](IONVMeBlockStorageDevice.md) — `com.apple.iokit.IONVMeFamily`
- [`IOUserBlockStorageDevice`](IOUserBlockStorageDevice.md) — `com.apple.iokit.IOStorageFamily`

## Strings in its kext that name it (3)

- `IOBlockStorageDevice`
- `virtual IOReturn IOUserBlockStorageDevice::doUnmap(IOBlockStorageDeviceExtent *, UInt32, IOStorageUnmapOptions)`
- `site.IOBlockStorageDevice`
