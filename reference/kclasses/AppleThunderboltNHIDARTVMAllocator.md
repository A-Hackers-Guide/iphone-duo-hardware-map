# `AppleThunderboltNHIDARTVMAllocator`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltNHI`](../kexts/com.apple.driver.AppleThunderboltNHI.md)
- Object size: `0x78` (120 bytes)
- Metaclass: `0xfffffe000b9d2988`; metaclass vtable `0xfffffe000828c8e0`; class vtable `0xfffffe000828c7c8`
- Registration (init): `0xfffffe00099d7538`
- Superclasses: [`IODARTVMAllocatorGeneric`](IODARTVMAllocatorGeneric.md) → [`IODARTVMAllocator`](IODARTVMAllocator.md)

## Strings in its kext that name it (21)

- `%lldus AppleThunderboltNHIDARTVMAllocator::init\n`
- `%lldus AppleThunderboltNHIDARTVMAllocator::init - DART reported minDVA %p and maxDVA %p and page size %p and thus fSupportsFixedAllocations = %d\n`
- `%lldus AppleThunderboltNHIDARTVMAllocator::vmAlloc - ERROR: IOMemoryDescriptor asked for a fixed DART offset, but fixed DART offsets are not supported on this device\n`
- `site.AppleThunderboltNHIDARTVMAllocator`
- `%lldus AppleThunderboltNHIDARTVMAllocator::vmAlloc - ERROR: failed to get VM space for allocation at page 0x%08x and DVA %p\n`
- `AppleThunderboltNHIDARTVMAllocator.cpp`
- `%lldus AppleThunderboltNHIDARTVMAllocator::init - IODARTVMAllocatorGeneric failed to initialize\n`
- `/Library/Caches/com.apple.xbs/AB76979E-E216-4029-9F29-4667DBC65AB9/TemporaryDirectory.yEhsoY/Sources/AppleThunderboltNHI/AppleThunderboltNHIDARTVMAllocator.cpp`
- `%lldus AppleThunderboltNHIDARTVMAllocator::vmAlloc - ERROR: IOMemoryDescriptor asked for a fixed DART offset but did not supply one via setContext\n`
- `AppleThunderboltNHIDARTVMAllocator`
- `%lldus AppleThunderboltNHIDARTVMAllocator::vmAlloc - ERROR: requested DVA %p not between minDVA %p and maxDVA %p\n`
- `\"AppleThunderboltNHIDARTVMAllocator::init - slide cannot be non-zero (found %d)\" @%s:%d`
- `%lldus AppleThunderboltNHIDARTVMAllocator::forMapper\n`
- `%lldus AppleThunderboltNHIDARTVMAllocator::vmAlloc - ERROR: cannot make requested allocation at 0x%08x/%d\n`
- `%lldus AppleThunderboltNHIDARTVMAllocator::init - IODARTVMAllocatorGeneric could not fetch DART capability\n`
- `%lldus AppleThunderboltNHIDARTVMAllocator::vmAlloc - ERROR: tailPadding %d not supported when allocating at a specific offset\n`
- `%lldus AppleThunderboltNHIDARTVMAllocator::init - IODARTVMAllocatorGeneric failed to initialize\n`
- `%lldus AppleThunderboltNHIDARTVMAllocator::init\n`
- `%lldus AppleThunderboltNHIDARTVMAllocator::init - IODARTVMAllocatorGeneric could not fetch DART capability\n`
- `%lldus AppleThunderboltNHIDARTVMAllocator::forMapper\n`
- `%lldus AppleThunderboltNHIDARTVMAllocator::init - DART reported minDVA %p and maxDVA %p and page size %p and thus fSupportsFixedAllocations = %d\n`
