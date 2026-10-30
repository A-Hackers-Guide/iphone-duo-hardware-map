# `RTBuddyCoredump`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md)
- Object size: `0x868` (2,152 bytes)
- Metaclass: `0xfffffe000ba23e08`; metaclass vtable `0xfffffe0008496510`; class vtable `0xfffffe0008496460`
- Registration (init): `0xfffffe000a93aaa8`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Direct subclasses (1; 1 in total)

- [`RTBuddyCoprocDrivenCoredump`](RTBuddyCoprocDrivenCoredump.md) — `com.apple.driver.RTBuddy`

## Strings in its kext that name it (16)

- `IOMemoryMap *RTBuddyCoredumpMap::readwriteMapForIopVirtual(IOVirtualAddress, IOVirtualAddress *)`
- `RTBuddyCoredump`
- `RTBuddyCoredumpDecoder`
- `site.RTBuddyCoredumpMap`
- `site.RTBuddyCoredump`
- `bool RTBuddyCoredump::initWithOptions(RTBuddy *, RTBuddyCoredumpArch)`
- `RTBuddyCoredumpMap.cpp`
- `bool RTBuddyVisibleMemoryImpl::initWithMemoryDescriptor(IOMemoryDescriptor *, RTBuddyCoredumpMap *, IOMapper *, IOPhysicalAddress, uint8_t)`
- `RTBuddyCoredumpMapEntry`
- `RTBuddySlaveMemoryDescriptor *RTBuddyCoredumpMap::slaveMemoryForPhysicalRange(IOPhysicalAddress, IOByteCount, IODirection)`
- `RTBuddyCoredump.cpp`
- `RTBuddyCoredumpMap`
- `IOVirtualAddress RTBuddyCoredumpMap::physToVirt(IOPhysicalAddress, IOByteCount)`
- `site.RTBuddyCoredumpMapEntry`
- `int RTBuddyCoredumpMap::indexOfVirt(IOPhysicalAddress)`
- `site.RTBuddyCoredumpDecoder`
