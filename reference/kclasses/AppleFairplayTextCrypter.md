# `AppleFairplayTextCrypter`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.IOTextEncryptionFamily`](../kexts/com.apple.IOTextEncryptionFamily.md)
- Object size: `0xa0` (160 bytes)
- Metaclass: `0xfffffe000ba1b708`; metaclass vtable `0xfffffe0008400de0`; class vtable `0xfffffe0008400868`
- Registration (init): `0xfffffe000a423294`
- Superclasses: [`IOTextCrypter`](IOTextCrypter.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleFairplayTextCrypter` in [`com.apple.IOTextEncryptionFamily`](../kexts/com.apple.IOTextEncryptionFamily.md): `IOProviderClass` = `IOResources`, `IOResourceMatch` = `IOBSD`, `IOMatchCategory` = `AppleFairplayTextCrypter`

## Strings in its kext that name it (6)

- `AppleFairplayTextCrypter`
- `site.AppleFairplayTextCrypter`
- `\"AppleFairplayTextCrypter::sessionDidEnd(): no session!\" @%s:%d`
- `AppleFairplayTextCrypterSession`
- `site.AppleFairplayTextCrypterSession`
- `AppleFairplayTextCrypterSession::fairplayOpen() failed, error %ld\n`
