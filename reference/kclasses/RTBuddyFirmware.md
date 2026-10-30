# `RTBuddyFirmware`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md)
- Object size: `0xe8` (232 bytes)
- Metaclass: `0xfffffe000ba23db0`; metaclass vtable `0xfffffe0008496218`; class vtable `0xfffffe0008495c88`
- Registration (init): `0xfffffe000a9377cc`
- Superclasses: [`IOSlaveFirmware`](IOSlaveFirmware.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (15)

- `virtual IOReturn RTBuddy::loadFirmware(RTBuddyFirmware *)`
- `RTBuddyFirmwareService`
- `RTBuddySegment *RTBuddyFirmware::getSegmentForIopVirtual(IOVirtualAddress)`
- `void RTBuddyFirmware::writeBackPatchBay()`
- `const void *RTBuddyFirmware::iopVirtualToApVirtual(IOVirtualAddress, size_t)`
- `RTBuddyFirmware.cpp`
- `OSData *RTBuddyFirmware::copy32FromIopVirtual(IOVirtualAddress, size_t)`
- `void RTBuddy::callPatchbayCallback(RTBuddyFirmware *)`
- `site.RTBuddyFirmwareService`
- `RTBuddyFirmware`
- `void RTBuddyFirmware::copyToTarget(RTBuddy *)`
- `site.RTBuddyFirmware`
- `IOReturn RTBuddyFirmware::copySegmentDescriptorWithName(const char *, RTBuddySegmentDescriptor *)`
- `site.RTBuddyFirmwareBundle`
- `RTBuddyFirmwareBundle`
