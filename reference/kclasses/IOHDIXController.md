# `IOHDIXController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.DiskImages`](../kexts/com.apple.driver.DiskImages.md)
- Object size: `0x118` (280 bytes)
- Metaclass: `0xfffffe000b9f51b8`; metaclass vtable `0xfffffe00083844a0`; class vtable `0xfffffe0008383f20`
- Registration (init): `0xfffffe000a16804c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IOHDIXController` in [`com.apple.driver.DiskImages`](../kexts/com.apple.driver.DiskImages.md): `IOProviderClass` = `IOResources`, `IOResourceMatch` = `IOKit`, `IOMatchCategory` = `IOHDIXController`

## Strings in its kext that name it (10)

- `IOHDIXController: NOTE: administrator is creating non-ejectable disk image\n`
- `IOHDIXController::checkPermission: WARNING: UID spoofing detected (and defeated) (%ld, %ld)\n`
- `IOHDIXController::_di_root_image: returning 0x%x (%d)\n`
- `IOHDIXController`
- `IOHDIXController::createDriveInKernel: returning error 0x%x\n`
- `IOHDIXControllerUserClient`
- `site.IOHDIXController`
- `IOHDIXController::_di_root_image: find*IOMediaObject() returned 0x%x\n`
- `IOHDIXController::_di_root_image: createDriveInKernel() returned 0x%x (%d)\n`
- `site.IOHDIXControllerUserClient`
