# `DCPEndpointV2`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md)
- Object size: `0x1c8` (456 bytes)
- Metaclass: `0xfffffe000b940530`; metaclass vtable `0xfffffe000804bdf0`; class vtable `0xfffffe000804b7e0`
- Registration (init): `0xfffffe0008b60498`
- Superclasses: [`AFKEPKextV2`](AFKEPKextV2.md) → [`AFKEPKextBaseV2`](AFKEPKextBaseV2.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `DCPEndpointsV2` in [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md): `IOProviderClass` = `RTBuddyEndpointService`, `IONameMatch` = `['DCPEndpoint1', 'DCPEndpoint2', 'DCPEndpoint3', 'DCPEndpoint4', 'DCPEndpoint5',`, `IOProbeScore` = `1`

## Strings in its kext that name it (5)

- `DCPEndpointV2`
- `virtual bool DCPEndpointV2::start(IOService *)`
- `site.DCPEndpointV2`
- `DCPEndpointV2.cpp`
- `virtual IOReturn DCPEndpointV2::setPowerState(unsigned long, IOService *)`
