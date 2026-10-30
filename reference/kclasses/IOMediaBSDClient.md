# `IOMediaBSDClient`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOStorageFamily`](../kexts/com.apple.iokit.IOStorageFamily.md)
- Object size: `0xb0` (176 bytes)
- Metaclass: `0xfffffe000ba1ada0`; metaclass vtable `0xfffffe00083f6658`; class vtable `0xfffffe00083f60e8`
- Registration (init): `0xfffffe000a3e624c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 2 in total)

- [`AppleAPFSMediaBSDClient`](AppleAPFSMediaBSDClient.md) — `com.apple.filesystems.apfs`
- [`AppleAPFSVolumeBSDClient`](AppleAPFSVolumeBSDClient.md) — `com.apple.filesystems.apfs`

## IOKit personalities that instantiate it (1)

- `IOMediaBSDClient` in [`com.apple.iokit.IOStorageFamily`](../kexts/com.apple.iokit.IOStorageFamily.md): `IOProviderClass` = `IOMedia`, `IOResourceMatch` = `IOBSD`, `IOMatchCategory` = `IOMediaBSDClient`, `IOProbeScore` = `30000`

## Strings in its kext that name it (2)

- `site.IOMediaBSDClient`
- `IOMediaBSDClient`
