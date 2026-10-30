# `RTBuddyCoredumpMap`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md)
- Object size: `0x30` (48 bytes)
- Metaclass: `0xfffffe000ba238b0`; metaclass vtable `0xfffffe000848ffa0`; class vtable `0xfffffe000848ff10`
- Registration (init): `0xfffffe000a918d64`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Strings in its kext that name it (10)

- `IOMemoryMap *RTBuddyCoredumpMap::readwriteMapForIopVirtual(IOVirtualAddress, IOVirtualAddress *)`
- `site.RTBuddyCoredumpMap`
- `RTBuddyCoredumpMap.cpp`
- `bool RTBuddyVisibleMemoryImpl::initWithMemoryDescriptor(IOMemoryDescriptor *, RTBuddyCoredumpMap *, IOMapper *, IOPhysicalAddress, uint8_t)`
- `RTBuddyCoredumpMapEntry`
- `RTBuddySlaveMemoryDescriptor *RTBuddyCoredumpMap::slaveMemoryForPhysicalRange(IOPhysicalAddress, IOByteCount, IODirection)`
- `RTBuddyCoredumpMap`
- `IOVirtualAddress RTBuddyCoredumpMap::physToVirt(IOPhysicalAddress, IOByteCount)`
- `site.RTBuddyCoredumpMapEntry`
- `int RTBuddyCoredumpMap::indexOfVirt(IOPhysicalAddress)`
