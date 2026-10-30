# `AppleCentauriManagerHelper`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleCentauriManager`](../kexts/com.apple.driver.AppleCentauriManager.md)
- Object size: `0x88` (136 bytes)
- Metaclass: `0xfffffe000b93af58`; metaclass vtable `0xfffffe0008026570`; class vtable `0xfffffe0008026018`
- Registration (init): `0xfffffe0008aec59c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleCentauriManagerHelperMatch` in [`com.apple.driver.AppleCentauriManager`](../kexts/com.apple.driver.AppleCentauriManager.md): `IOProviderClass` = `IOService`, `IONameMatch` = `centauri`, `IOMatchCategory` = `AppleCentauriManagerHelper`

## Device-tree nodes it binds (1) [DT]

- [`/centauri`](../devicetree/root__centauri.md) on `centauri`

## Strings in its kext that name it (4)

- `site.AppleCentauriManagerHelper`
- `AppleCentauriManagerHelper`
- `%s::%s: AppleCentauriManagerHelper %s started, ret = %x \n`
- `AppleCentauriManagerHelper.cpp`
