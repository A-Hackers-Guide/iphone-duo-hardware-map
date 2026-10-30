# `ApplePMPv2`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.ApplePMP`](../kexts/com.apple.driver.ApplePMP.md)
- Object size: `0x118` (280 bytes)
- Metaclass: `0xfffffe000b987c38`; metaclass vtable `0xfffffe00081975b0`; class vtable `0xfffffe0008197058`
- Registration (init): `0xfffffe0009362d3c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `ApplePMPv2` in [`com.apple.driver.ApplePMP`](../kexts/com.apple.driver.ApplePMP.md): `IOProviderClass` = `RTBuddyEndpointService`, `IONameMatch` = `['PMPEndpoint1', 'PMP0Endpoint1', 'PMP1Endpoint1']`

## Strings in its kext that name it (8)

- `site.ApplePMPv2RegistryEntry`
- `/ApplePMP/ApplePMPv2UserClient.cpp`
- `site.ApplePMPv2UserClient`
- `ApplePMPv2.cpp`
- `site.ApplePMPv2`
- `ApplePMPv2UserClient`
- `ApplePMPv2RegistryEntry`
- `ApplePMPv2`
