# `IOApplePartitionScheme`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOStorageFamily`](../kexts/com.apple.iokit.IOStorageFamily.md)
- Object size: `0xc0` (192 bytes)
- Metaclass: `0xfffffe000ba1ac38`; metaclass vtable `0xfffffe00083f33e8`; class vtable `0xfffffe00083f2df0`
- Registration (init): `0xfffffe000a3d389c`
- Superclasses: [`IOPartitionScheme`](IOPartitionScheme.md) → [`IOStorage`](IOStorage.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IOApplePartitionScheme` in [`com.apple.iokit.IOStorageFamily`](../kexts/com.apple.iokit.IOStorageFamily.md): `IOProviderClass` = `IOMedia`, `IOPropertyMatch` = `[{'Whole': True}, {'Content Hint': 'CD_ROM_Mode_1', 'Writable': False}, {'Conten`, `IOMatchCategory` = `IOStorage`, `IOProbeScore` = `2000`

## Strings in its kext that name it (2)

- `IOApplePartitionScheme`
- `site.IOApplePartitionScheme`
