# `VCPDRMService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.VideoProcessing`](../kexts/com.apple.driver.VideoProcessing.md)
- Object size: `0x98` (152 bytes)
- Metaclass: `0xfffffe000ba39db8`; metaclass vtable `0xfffffe00084a6208`; class vtable `0xfffffe00084a5cb0`
- Registration (init): `0xfffffe000a9aded0`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `VideoProcessingDRM` in [`com.apple.driver.VideoProcessing`](../kexts/com.apple.driver.VideoProcessing.md): `IOProviderClass` = `IOResources`, `IOResourceMatch` = `IOBSD`, `IOMatchCategory` = `VCPDRMService`

## Strings in its kext that name it (3)

- `site.VCPDRMService`
- `VCPDRMService`
- `virtual IOReturn VCPDRMService::newUserClient(task_t, void *, UInt32, IOUserClient **)`
