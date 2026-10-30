# `ApplePPMUserClient`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleiPhoneACSKPPM`](../kexts/com.apple.driver.AppleiPhoneACSKPPM.md)
- Object size: `0x110` (272 bytes)
- Metaclass: `0xfffffe000b9dbe78`; metaclass vtable `0xfffffe00082bcf88`; class vtable `0xfffffe00082bc878`
- Registration (init): `0xfffffe0009b93924`
- Superclasses: [`IOUserClient`](IOUserClient.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (8)

- `site.ApplePPMUserClient`
- `bool ApplePPMUserClient::associateClientId(UniqueClientID_t)`
- `ApplePPMUserClient`
- `virtual bool ApplePPMUserClient::initWithTask(task_t, void *, UInt32, OSDictionary *)`
- `ApplePPMUserClient.cpp`
- `virtual IOReturn ApplePPMUserClient::registerMultiClient(CPMSPPMClientDescription *)`
- `void ApplePPMUserClient::dissociateClientId(UniqueClientID_t)`
- `virtual void ApplePPMUserClient::cleanUpPPMUserClient()`
