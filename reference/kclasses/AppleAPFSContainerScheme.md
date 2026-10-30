# `AppleAPFSContainerScheme`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.filesystems.apfs`](../kexts/com.apple.filesystems.apfs.md)
- Object size: `0x150` (336 bytes)
- Metaclass: `0xfffffe000ba3b038`; metaclass vtable `0xfffffe00084ab570`; class vtable `0xfffffe00084aafb8`
- Registration (init): `0xfffffe000aa0c85c`
- Superclasses: [`IOStorage`](IOStorage.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (3)

- `AppleAPFSContainerScheme` in [`com.apple.filesystems.apfs`](../kexts/com.apple.filesystems.apfs.md): `IOProviderClass` = `IOMedia`, `IOPropertyMatch` = `[{'Content Hint': '7C3457EF-0000-11AA-AA11-00306543ECAC'}]`, `IOMatchCategory` = `IOStorage`, `IOProbeScore` = `2000`
- `AppleAPFSContainerSchemeWholeDisk` in [`com.apple.filesystems.apfs`](../kexts/com.apple.filesystems.apfs.md): `IOProviderClass` = `IOMedia`, `IOPropertyMatch` = `[{'Whole': True}]`, `IOMatchCategory` = `IOStorage`, `IOProbeScore` = `2000`
- `AppleAPFSRecovery` in [`com.apple.filesystems.apfs`](../kexts/com.apple.filesystems.apfs.md): `IOProviderClass` = `IOMedia`, `IOPropertyMatch` = `[{'Content Hint': '52637672-7900-11AA-AA11-00306543ECAC'}]`, `IOMatchCategory` = `IOStorage`, `IOProbeScore` = `2000`

## Strings in its kext that name it (2)

- `site.AppleAPFSContainerScheme`
- `AppleAPFSContainerScheme`
