# `RTBuddySlaveMemory`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md)
- Object size: `0x10` (16 bytes)
- Metaclass: `0xfffffe000ba239a0`; metaclass vtable `0xfffffe0008491428`; class vtable `0xfffffe0008491350`
- Registration (init): `0xfffffe000a91d6b8`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Direct subclasses (3; 4 in total)

- [`RTBuddySlaveBuffer`](RTBuddySlaveBuffer.md) — `com.apple.driver.RTBuddy`
- [`RTBuddySlaveMemoryDescriptor`](RTBuddySlaveMemoryDescriptor.md) — `com.apple.driver.RTBuddy`
- [`RTBuddyVisibleSlaveBuffer`](RTBuddyVisibleSlaveBuffer.md) — `com.apple.driver.RTBuddy`

## Strings in its kext that name it (10)

- `RTBuddySlaveMemoryDescriptor`
- `site.RTBuddySlaveMemoryBuffer`
- `virtual IOReturn RTBuddy::_slaveMemoryFromIOPPhysGated(const IOPhysicalAddress *, const IOByteCount *, RTBuddySlaveMemory **)`
- `site.RTBuddySlaveMemory`
- `RTBuddySlaveMemory.cpp`
- `RTBuddySlaveMemoryDescriptor *RTBuddyCoredumpMap::slaveMemoryForPhysicalRange(IOPhysicalAddress, IOByteCount, IODirection)`
- `RTBuddySlaveMemory *RTBuddy::slaveMemoryFromIOPPhys(IOPhysicalAddress, IOByteCount)`
- `RTBuddySlaveMemory`
- `RTBuddySlaveMemoryBuffer`
- `site.RTBuddySlaveMemoryDescriptor`
