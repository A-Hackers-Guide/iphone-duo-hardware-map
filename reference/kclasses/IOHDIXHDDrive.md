# `IOHDIXHDDrive`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.DiskImages`](../kexts/com.apple.driver.DiskImages.md)
- Object size: `0x120` (288 bytes)
- Metaclass: `0xfffffe000b9f5208`; metaclass vtable `0xfffffe0008385268`; class vtable `0xfffffe0008384c40`
- Registration (init): `0xfffffe000a16ad18`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`IOHDIXHDDriveInKernel`](IOHDIXHDDriveInKernel.md) — `com.apple.driver.DiskImages.KernelBacked`

## Strings in its kext that name it (6)

- `IOHDIXHDDriveNub`
- `IOHDIXHDDrive`
- `site.IOHDIXHDDriveNub`
- `site.IOHDIXHDDrive`
- `IOHDIXHDDrive::sanitizeIOResult: Mapping DI error %d to EIO\n`
- `IOHDIXHDDrive::doAsyncReadWrite(): failed to allocate command\n`
