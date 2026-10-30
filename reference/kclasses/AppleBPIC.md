# `AppleBPIC`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.ApplePhoneBTM`](../kexts/com.apple.driver.ApplePhoneBTM.md)
- Object size: `0xe0` (224 bytes)
- Metaclass: `0xfffffe000b989020`; metaclass vtable `0xfffffe00081a6e40`; class vtable `0xfffffe00081a67b0`
- Registration (init): `0xfffffe00093d9f80`
- Superclasses: [`IOHIDDevice`](IOHIDDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleBPIC` in [`com.apple.driver.ApplePhoneBTM`](../kexts/com.apple.driver.ApplePhoneBTM.md): `IOProviderClass` = `AppleARMSPMIDevice`, `IONameMatch` = `btm,bpic`, `IOMatchCategory` = `AppleBPIC`

## Strings in its kext that name it (10)

- `virtual bool AppleBPIC::start(IOService *)`
- `bool AppleBTMBPICAgent::initWithParent(AppleBPIC *, IOService *)`
- `AppleBPIC.cpp`
- `virtual IOReturn AppleBPIC::newReportDescriptor(IOMemoryDescriptor **) const`
- `static AppleStonehengeBPIC *AppleStonehengeBPIC::withParent(AppleBPIC *, IOService *)`
- `bool AppleBPIC::getDTProperty(const char *, uint32_t *, IOService *)`
- `AppleBPIC::free\n`
- `AppleBPIC::start\n`
- `AppleBPIC`
- `site.AppleBPIC`
