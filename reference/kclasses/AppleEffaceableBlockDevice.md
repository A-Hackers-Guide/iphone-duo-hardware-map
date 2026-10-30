# `AppleEffaceableBlockDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEffaceableBlockDevice`](../kexts/com.apple.driver.AppleEffaceableBlockDevice.md)
- Object size: `0x298` (664 bytes)
- Metaclass: `0xfffffe000b9418e8`; metaclass vtable `0xfffffe0008068410`; class vtable `0xfffffe0008067eb0`
- Registration (init): `0xfffffe0008bca250`
- Superclasses: [`AppleEffaceableStorage`](AppleEffaceableStorage.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `AppleEffaceableBlockDevice` in [`com.apple.driver.AppleEffaceableBlockDevice`](../kexts/com.apple.driver.AppleEffaceableBlockDevice.md): `IOProviderClass` = `IOEffaceableDevice`
- `AppleEffaceableBlockDevice-NVMe` in [`com.apple.driver.AppleEffaceableBlockDevice`](../kexts/com.apple.driver.AppleEffaceableBlockDevice.md): `IOProviderClass` = `IONVMeEffaceableDevice`

## Strings in its kext that name it (3)

- `site.AppleEffaceableBlockDevice`
- `AppleEffaceableBlockDevice.cpp`
- `AppleEffaceableBlockDevice`
