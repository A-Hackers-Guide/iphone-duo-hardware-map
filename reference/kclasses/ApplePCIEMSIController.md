# `ApplePCIEMSIController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedPCIE`](../kexts/com.apple.driver.AppleEmbeddedPCIE.md)
- Object size: `0xe0` (224 bytes)
- Metaclass: `0xfffffe000b943800`; metaclass vtable `0xfffffe0008087d70`; class vtable `0xfffffe0008087770`
- Registration (init): `0xfffffe0008c47c50`
- Superclasses: [`IOPCIMessagedInterruptController`](IOPCIMessagedInterruptController.md) → [`IOInterruptController`](IOInterruptController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (31)

- `virtual void ApplePCIEMSIController::deallocateInterrupt(UInt32)`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s numVectors=%u, firstVector=%u, parentController=%p\n`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s vectorNumber=%d, vector=%p\n`
- `ApplePCIEMSIController`
- `virtual bool ApplePCIEMSIController::allocateInterruptVectors(IOService *, uint32_t, IORangeScalar *)`
- `ApplePCIEMSIController.cpp`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s Attempting to allocate %u reserved MSI vector(s), starting at vector %u, for port %d\n`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s failed to register interrupt: device=%p, source=%d\n`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s Warning: the EP driver requested fewer MSIs (%u) than were reserved (%u)\n`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s _vectorPorts[%d]=%p\n`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s device=%p, controllerIndex=%u, interruptFlags=0x%x, deviceIndex=%p\n`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s Failed to allocate %d MSI vector(s) for port %d\n`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s failed to initialize\n`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s device=%p, numVectors=%u, firstVector=%d\n`
- `site.ApplePCIEMSIController`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s device=%p, source=%d, target=%p, handler=%p, refCon=%p\n`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s device=%p, source=%d\n`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s aicVector=%u, _vectorPorts[%d]=%p\n`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s aicVector=%u, _vectorPorts[%d]=%p\n`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s device=%p, source=%d\n`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s device=%p, controllerIndex=%u, interruptFlags=0x%x, deviceIndex=%p\n`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s vectorNumber=%d, vector=%p\n`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s device=%p, numVectors=%u, firstVector=%d\n`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s failed to initialize\n`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s Warning: the EP driver requested fewer MSIs (%u) than were reserved (%u)\n`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s _vectorPorts[%d]=%p\n`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s failed to register interrupt: device=%p, source=%d\n`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s Failed to allocate %d MSI vector(s) for port %d\n`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s Attempting to allocate %u reserved MSI vector(s), starting at vector %u, for port %d\n`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s numVectors=%u, firstVector=%u, parentController=%p\n`
- `[PCIe:%u %llu ns] ApplePCIEMSIController::%s device=%p, source=%d, target=%p, handler=%p, refCon=%p\n`
