# `DCPDPControllerProxy`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.DCPDPFamilyProxy`](../kexts/com.apple.driver.DCPDPFamilyProxy.md)
- Object size: `0x618` (1,560 bytes)
- Metaclass: `0xfffffe000b9dfa00`; metaclass vtable `0xfffffe00082d6970`; class vtable `0xfffffe00082d6298`
- Registration (init): `0xfffffe0009c2f61c`
- Superclasses: [`DCPAVProxy`](DCPAVProxy.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `DCPDPControllerProxy` in [`com.apple.driver.DCPDPFamilyProxy`](../kexts/com.apple.driver.DCPDPFamilyProxy.md): `IOProviderClass` = `AFKEndpointInterface`, `IOPropertyMatch` = `{'EPICName': 'dcpdp-controller-epic'}`

## Strings in its kext that name it (6)

- `<rdar://problem/67769074> Re-enable DCPDPControllerProxy::setMaxLaneCount() (fix 'displayPort -maxlc')\n`
- `DCPDPControllerProxy`
- `DCPDPControllerProxyUserClient`
- `site.DCPDPControllerProxyUserClient`
- `site.DCPDPControllerProxy`
- `IOAV[%d] %s<0x%llx>::%s: <rdar://problem/67769074> Re-enable DCPDPControllerProxy::setMaxLaneCount() (fix 'displayPort -maxlc')\n`
