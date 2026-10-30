# `AFKRemoteSMCClient`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleFirmwareKit`](../kexts/com.apple.driver.AppleFirmwareKit.md)
- Object size: `0xc8` (200 bytes)
- Metaclass: `0xfffffe000b945ee0`; metaclass vtable `0xfffffe00080aea70`; class vtable `0xfffffe00080ae500`
- Registration (init): `0xfffffe0008ce106c`
- Superclasses: [`AFKIOServiceClientBase`](AFKIOServiceClientBase.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AFKRemoteSMCClient` in [`com.apple.driver.AppleFirmwareKit`](../kexts/com.apple.driver.AppleFirmwareKit.md): `IOProviderClass` = `AFKEndpointInterface`, `IONameMatch` = `afk-smc-client`

## Strings in its kext that name it (5)

- `site.AFKRemoteSMCClient`
- `AFKRemoteSMCClient`
- `%s(%s:%#llx): AFKRemoteSMCClient writeKey_rpc(%x):%x\n`
- `%s(%s:%#llx): AFKRemoteSMCClient readPKey_rpc(%x):%x\n`
- `%s(%s:%#llx): AFKRemoteSMCClient readKey_rpc(%x):%x\n`
