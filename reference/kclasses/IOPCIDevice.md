# `IOPCIDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOPCIFamily`](../kexts/com.apple.iokit.IOPCIFamily.md)
- Object size: `0xb8` (184 bytes)
- Metaclass: `0xfffffe000ba18e80`; metaclass vtable `0xfffffe00083d6eb8`; class vtable `0xfffffe00083d6860`
- Registration (init): `0xfffffe000a341bec`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`IOAGPDevice`](IOAGPDevice.md) — `com.apple.iokit.IOPCIFamily`

## Strings in its kext that name it (60)

- `[PCIe:%u %llu ns] IOPCIDevice::deviceMemoryWrite8: index %u could not get mapping\n`
- `IOReturn IOPCIDevice::reprobeThreadCall(thread_call_t)`
- `[PCIe:%u %llu ns] IOPCIDevice::%s: invalid index %llu for client %s\n`
- `IOPCIDevice requestProbe failed insufficient privileges\n`
- `[PCIe:%u %llu ns] IOPCIDevice::%s:%s invalid bar index %u\n`
- `IOPCIDevicePublishRetryTimeout`
- `site.IOPCIDeviceExpansionData`
- `[PCIe:%u %llu ns] IOPCIDevice::deviceMemoryRead32: failed to get memory for index %u\n`
- `[PCIe:%u %llu ns] IOPCIDevice::deviceMemoryRead8: index %u is not MMIO space\n`
- `[PCIe:%u %llu ns] IOPCIDevice::ClientCrashed_Impl() for client %s done\n`
- `[PCIe:%u %llu ns] IOPCIDevice::deviceMemoryRead8: index %u could not get mapping\n`
- `IOPCIDeviceMemoryMapSize`
- `IOPCIDeviceMemoryMapBase`
- `[PCIe:%u %llu ns] IOPCIDevice::deviceMemoryWrite64: index %u could not get mapping\n`
- `[PCIe:%u %llu ns] IOPCIDevice::deviceMemoryRead64: index %u could not get mapping\n`
- `[PCIe:%u %llu ns] IOPCIDevice::deviceMemoryWrite32: index %u could not get mapping\n`
- `[PCIe:%u %llu ns] [IOPCIDevice::%s()] client %s (isOpen(forClient) == %u)\n`
- `[PCIe:%u %llu ns] IOPCIDevice::relocate at [i%x]%u:%u:%u(0x%x:0x%x)\n`
- `[PCIe:%u %llu ns] IOPCIDevice::%s:%s unable to access device memory\n`
- `[PCIe:%u %llu ns] IOPCIDevice::%s: device not open for client %s\n`
- `site.IOPCIDevice`
- `\"getVectorType: failed to cast vector %d's nub to IOPCIDevice\\n\" @%s:%d`
- `IOPCIDeviceChanged`
- `[PCIe:%u %llu ns] IOPCIDevice::deviceMemoryRead32: index %u could not get mapping\n`
- `IOPCIDevice`
- `[PCIe:%u %llu ns] IOPCIDevice::deviceMemoryRead16: index %u is not MMIO space\n`
- `getInterruptType: failed to cast nub to IOPCIDevice\n`
- `[PCIe:%u %llu ns] IOPCIDevice::deviceMemoryWrite16: index %u could not get mapping\n`
- `IOPCIDeviceCrashResetType`
- `[PCIe:%u %llu ns] IOPCIDevice::deviceMemoryRead64: index %u is not MMIO space\n`
- `IOReturn IOPCIBridge::childClientCrashRecoveryGated(IOPCIDevice *)`
- `kern_return_t IOPCIDevice::SetProperties_Impl(OSDictionary *)`
- `IOPCIDeviceDeviceTreeEntry`
- `\"IOPCIDevice(%p) linked (linkFinish)\" @%s:%d`
- `kern_return_t IOPCIDevice::ClientCrashed_Impl(IOService *, uint64_t)`
- `[PCIe:%u %llu ns] IOPCIDevice::deviceMemoryRead16: index %u could not get mapping\n`
- `[PCIe:%u %llu ns] IOPCIDevice::%s: no-user-memory-mapping property prevents copying device memory\n`
- `[PCIe:%u %llu ns] IOPCIDevice::deviceMemoryRead8: failed to get memory for index %u\n`
- `[PCIe:%u %llu ns] IOPCIDevice::%s: invalid index %u for client %s\n`
- `[PCIe:%u %llu ns] IOPCIDevice::deviceMemoryRead32: index %u is not MMIO space\n`
- `\"IOPCIDevice(%p) linked\" @%s:%d`
- `IOPCIDevice.cpp`
- `[PCIe:%u %llu ns] IOPCIDevice::ClientCrashed_Impl() for client %s\n`
- `[PCIe:%u %llu ns] IOPCIDevice::%s:%s NULL config entry\n`
- `IOPCIDeviceMapperPageSize`
- `[PCIe:%u %llu ns] IOPCIDevice::deviceMemoryRead64: failed to get memory for index %u\n`
- `IOPCIDeviceDeadOnRestore`
- `[PCIe:%u %llu ns] IOPCIDevice::deviceMemoryRead16: failed to get memory for index %u\n`
- `IOReturn IOPCIBridge::waitForDeviceReady(IOPCIDevice *)`
- `[PCIe:%u %llu ns] [IOPCIDevice::%s()] disabling memory%s for client %s\n`
- `[PCIe:%u %llu ns] IOPCIDevice::deviceMemoryRead16: failed to get memory for index %u\n`
- `[PCIe:%u %llu ns] IOPCIDevice::deviceMemoryRead64: failed to get memory for index %u\n`
- `[PCIe:%u %llu ns] IOPCIDevice::%s: device not open for client %s\n`
- `[PCIe:%u %llu ns] [IOPCIDevice::%s()] client %s (isOpen(forClient) == %u)\n`
- `[PCIe:%u %llu ns] IOPCIDevice::deviceMemoryRead8: index %u is not MMIO space\n`
- `[PCIe:%u %llu ns] IOPCIDevice::deviceMemoryWrite32: index %u could not get mapping\n`
- `[PCIe:%u %llu ns] IOPCIDevice::%s:%s invalid bar index %u\n`
- `[PCIe:%u %llu ns] IOPCIDevice::deviceMemoryRead32: index %u is not MMIO space\n`
- `[PCIe:%u %llu ns] IOPCIDevice::%s: no-user-memory-mapping property prevents copying device memory\n`
- `[PCIe:%u %llu ns] IOPCIDevice::deviceMemoryWrite64: index %u could not get mapping\n`
