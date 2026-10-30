# `AppleQiAuthProtocol`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleC26Charger`](../kexts/com.apple.driver.AppleC26Charger.md)
- Object size: `0xb8` (184 bytes)
- Metaclass: `0xfffffe000b938430`; metaclass vtable `0xfffffe00080030e8`; class vtable `0xfffffe0008002b40`
- Registration (init): `0xfffffe0008a26774`
- Superclasses: [`IOAccessoryAuthProtocolInterface`](IOAccessoryAuthProtocolInterface.md) → [`IOAccessoryPort`](IOAccessoryPort.md) → [`IOAccessoryTransport`](IOAccessoryTransport.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleQiAuthProtocol` in [`com.apple.driver.AppleC26Charger`](../kexts/com.apple.driver.AppleC26Charger.md): `IOProviderClass` = `AppleC26DeviceStream`, `IOMatchCategory` = `AppleQiAuthProtocol`

## Strings in its kext that name it (7)

- `site.AppleQiAuthProtocol`
- `AppleQiAuthProtocol`
- `%s: AppleQiAuthProtocol provider is not AppleC26DeviceStream\n`
- `AppleQiAuthProtocol::stop()\n`
- `%s: ===== AppleQiAuthProtocol::start() SUCCESS =====\n`
- `%s: AppleQiAuthProtocol got device stream (number=%d, type=%d, protocol=%d)\n`
- `%s: AppleQiAuthProtocol super::start() failed\n`
