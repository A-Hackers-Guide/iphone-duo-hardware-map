# `AppleAPFSVolumeBSDClient`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.filesystems.apfs`](../kexts/com.apple.filesystems.apfs.md)
- Object size: `0xb0` (176 bytes)
- Metaclass: `0xfffffe000ba3afd0`; metaclass vtable `0xfffffe00084aa318`; class vtable `0xfffffe00084a9da8`
- Registration (init): `0xfffffe000aa06a04`
- Superclasses: [`IOMediaBSDClient`](IOMediaBSDClient.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleAPFSVolumeBSDClient` in [`com.apple.filesystems.apfs`](../kexts/com.apple.filesystems.apfs.md): `IOProviderClass` = `AppleAPFSVolume`, `IOResourceMatch` = `IOBSD`, `IOMatchCategory` = `IOMediaBSDClient`, `IOProbeScore` = `31000`

## Strings in its kext that name it (1)

- `site.AppleAPFSVolumeBSDClient`
