# `AFKEPKextV2`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleFirmwareKit`](../kexts/com.apple.driver.AppleFirmwareKit.md)
- Object size: `0x1b8` (440 bytes)
- Metaclass: `0xfffffe000b945d50`; metaclass vtable `0xfffffe00080ab188`; class vtable `0xfffffe00080aab78`
- Registration (init): `0xfffffe0008cd9cb8`
- Superclasses: [`AFKEPKextBaseV2`](AFKEPKextBaseV2.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 2 in total)

- [`AFKACIPCEndpoint`](AFKACIPCEndpoint.md) — `com.apple.driver.AppleFirmwareKit`
- [`DCPEndpointV2`](DCPEndpointV2.md) — `com.apple.driver.AppleDCP`

## IOKit personalities that instantiate it (1)

- `AOP2Endpoints` in [`com.apple.driver.AppleAOP2`](../kexts/com.apple.driver.AppleAOP2.md): `IOProviderClass` = `RTBuddyEndpointService`, `IONameMatch` = `['AOP2Endpoint1', 'AOP2Endpoint2', 'AOP2Endpoint3', 'AOP2Endpoint4', 'AOP2Endpoi`

## Strings in its kext that name it (3)

- `AFKEPKextV2`
- `AFKEPKextV2.cpp`
- `site.AFKEPKextV2`
