# `AppleAPFSContainer`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.filesystems.apfs`](../kexts/com.apple.filesystems.apfs.md)
- Object size: `0x748` (1,864 bytes)
- Metaclass: `0xfffffe000ba3aec0`; metaclass vtable `0xfffffe00084a7b28`; class vtable `0xfffffe00084a7558`
- Registration (init): `0xfffffe000aa068dc`
- Superclasses: [`IOPartitionScheme`](IOPartitionScheme.md) → [`IOStorage`](IOStorage.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleAPFSContainer` in [`com.apple.filesystems.apfs`](../kexts/com.apple.filesystems.apfs.md): `IOProviderClass` = `IOMedia`, `IOPropertyMatch` = `[{'Content Hint': 'EF57347C-0000-11AA-AA11-00306543ECAC'}]`, `IOMatchCategory` = `IOStorage`, `IOProbeScore` = `1000`

## Strings in its kext that name it (3)

- `site.AppleAPFSContainerScheme`
- `AppleAPFSContainerScheme`
- `AppleAPFSContainer`
