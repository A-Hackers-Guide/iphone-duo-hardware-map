# `AppleThunderboltPCIDownAdapter`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltPCIDownAdapter`](../kexts/com.apple.driver.AppleThunderboltPCIDownAdapter.md)
- Object size: `0x128` (296 bytes)
- Metaclass: `0xfffffe000b9d2b50`; metaclass vtable `0xfffffe000828f970`; class vtable `0xfffffe000828f240`
- Registration (init): `0xfffffe00099dd978`
- Superclasses: [`IOThunderboltTunnelDriver`](IOThunderboltTunnelDriver.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AppleThunderboltPCIDownAdapterType5`](AppleThunderboltPCIDownAdapterType5.md) — `com.apple.driver.AppleThunderboltPCIDownAdapter`

## IOKit personalities that instantiate it (1)

- `AppleThunderboltPCIDownAdapter` in [`com.apple.driver.AppleThunderboltPCIDownAdapter`](../kexts/com.apple.driver.AppleThunderboltPCIDownAdapter.md): `IOProviderClass` = `IOThunderboltPort`, `IOProbeScore` = `4096`

## Strings in its kext that name it (51)

- `%lldus AppleThunderboltPCIDownAdapter<%p>::setupRootPCICorrelationPath - eeprom - status = 0x%0x port number = %d\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::lateSleep\n`
- `AppleThunderboltPCIDownAdapterType5`
- `%lldus AppleThunderboltPCIDownAdapterType5(%x:%llx:%x)::setupRootPCICorrelationPath - phandle_func_object = %p\n`
- `%lldus AppleThunderboltPCIDownAdapterType5(%x:%llx:%x)::setupRootPCICorrelationPath - phandle_dictionary = %p status = 0x%08x\n`
- `%lldus AppleThunderboltPCIDownAdapter::setupRootPCICorrelationPath - Disabled?!?\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::setupRootPCICorrelationPath - status = 0x%0x\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::upstreamPCIDeviceNotification - newService = %p name = %s - FOUND!\n`
- `%lldus AppleThunderboltPCIDownAdapter(%x:%llx:%x)::deactivateRemoveLegacyProperty - remove legacy property from correlated PCI\n`
- `%lldus AppleThunderboltPCIDownAdapterType5(%x:%llx:%x)::setupRootPCICorrelationPath: No RootBridge\n`
- `%lldus AppleThunderboltPCIDownAdapterType5(%x:%llx:%x)::setupRootPCICorrelationPath - phandle_key = %p\n`
- `%lldus AppleThunderboltPCIDownAdapterType5(%x:%llx:%x)::setupRootPCICorrelationPath - Disabled by boot-arg\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::setupPCICorrelationPathFromAdapter - status = 0x%08x parent_path = %p\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::createResources status = 0x%x\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::setupPCICorrelationPathFromAdapter - status = 0x%08x parent_pci_device = %p\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::setupPCICorrelationFromPCIDevice\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::finishPCICorrelation (2) - set pci correlation properties, status = 0x%08x\n`
- `site.AppleThunderboltPCIDownAdapterType5`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::start\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::upstreamPCIDeviceNotification - newService = %p name = %s\n`
- `%lldus AppleThunderboltPCIDownAdapter(%x:%llx:%x)::activateSetLegacyProperty - switch needs extended link training, add legacy property to correlated PCI\n`
- `%lldus AppleThunderboltPCIDownAdapterType5(%x:%llx:%x)::setupBootArgs\n`
- `%lldus AppleThunderboltPCIDownAdapterType5<%p>::postAdapterEnable - tmp_status = 0x%08x\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::earlyWake\n`
- `%lldus AppleThunderboltPCIDownAdapter::setupRootPCICorrelationPath\n`
- `%lldus AppleThunderboltPCIDownAdapter::setupPCICorrelationFromPCIDevice: dev %d func %d portnum %d\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::setThunderboltClient = %p success = %d\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::start - status = 0x%08x\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::setupPCICorrelationFromPCIDevice - status = 0x%0x\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::findPCIChildFromDeviceFunction - status = 0x%08x\n`
- `%lldus AppleThunderboltPCIDownAdapterType5(%x:%llx:%x)::setupRootPCICorrelationPath - phandle_object = %p\n`
- `%lldus AppleThunderboltPCIDownAdapterType5(%x:%llx:%x)::setupRootPCICorrelationPath - ERROR: failed to find service for \"%s\" phandle.\n`
- `site.AppleThunderboltPCIDownAdapter`
- `%lldus AppleThunderboltPCIDownAdapterType5<%p>::postAdapterEnable - port_control_prop = %p\n`
- `%lldus AppleThunderboltPCIDownAdapterType5<%p>::postAdapterEnable - port_control = %p\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::finalize\n`
- `%lldus AppleThunderboltPCIDownAdapter(%x:%llx:%x)::activateSetLegacyProperty - the_switch = %p\n`
- `%lldus AppleThunderboltPCIDownAdapterType5<%p>::postAdapterEnable - hal = %p\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::free\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::findPCIChildFromDeviceFunction - parent_device = %p, dev = %x, fn = %x\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::finishPCICorrelation (1) - status = 0x%08x\n`
- `%lldus AppleThunderboltPCIDownAdapterType5<%p>::postAdapterEnable - nhi = %p\n`
- `%lldus AppleThunderboltPCIDownAdapterType5<%p>::postAdapterEnable - nhi_device = %p\n`
- `%lldus AppleThunderboltPCIDownAdapterType5(%x:%llx:%x)::setupRootPCICorrelationPath\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::setupPCICorrelationFromPCIDevice - eeprom - status = 0x%0x port number = %d\n`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::finishPCICorrelation (2) - status = 0x%08x\n`
- `%lldus AppleThunderboltPCIDownAdapter(%x:%llx:%x)::activateSetLegacyProperty - fCorrelatedPCIDevice = %p, fProviderPort = %p\n`
- `%lldus AppleThunderboltPCIDownAdapterType5(%x:%llx:%x)::setupRootPCICorrelationPath - status = 0x%0x\n`
- `AppleThunderboltPCIDownAdapter`
- `%lldus AppleThunderboltPCIDownAdapter<%p>::setupPCICorrelationPathFromAdapter - parent_adapter = %p\n`
- `%lldus AppleThunderboltPCIDownAdapterType5(%x:%llx:%x)::setupRootPCICorrelationPath - matching_dictionary = %p\n`
