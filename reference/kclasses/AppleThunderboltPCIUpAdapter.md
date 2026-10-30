# `AppleThunderboltPCIUpAdapter`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltPCIUpAdapter`](../kexts/com.apple.driver.AppleThunderboltPCIUpAdapter.md)
- Object size: `0x208` (520 bytes)
- Metaclass: `0xfffffe000b9d2dd0`; metaclass vtable `0xfffffe0008290cf0`; class vtable `0xfffffe0008290440`
- Registration (init): `0xfffffe00099f5dec`
- Superclasses: [`IOThunderboltTunnelDriver`](IOThunderboltTunnelDriver.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleThunderboltPCIUpAdapter` in [`com.apple.driver.AppleThunderboltPCIUpAdapter`](../kexts/com.apple.driver.AppleThunderboltPCIUpAdapter.md): `IOProviderClass` = `IOThunderboltPort`, `IOProbeScore` = `4096`

## Strings in its kext that name it (60)

- `%lldus AppleThunderboltPCIUpAdapter(%x:%llx:%x)::preAdapterEnable\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::destroyPowerManagement\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getNextPortsArray - first port, link is lateral\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::waitForDownAdapters - route = 0x%llx port = 0x%x - waiting\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::destroyPaths\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::pathActivationCallback - fRxPath status = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::startActivatingFindDownAdapterPCICapability\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findUpstreamParentPCIDevice - status = 0x%08x parent_pci_device = %p\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::beginPathRouting - status = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath - use new path, same bandwidth but a better source port\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::pathActivationCallback - fTxPath status = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter(%x:%llx:%x)::preAdapterEnable - enable extended encapsulation on downstream port - status = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::processDownAdapterEnableWriteResults - status = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::startPCICorrelation (2) - status = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::startDeactivatingFindDownAdapterPCICapability\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::processUpAdapterResetEnableWriteResults - status = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::start - (1) fRxRequiredBandwidth = %d fRxMaximumBandwidth = %d fTxRequiredBandwidth = %d fTxMaximumBandwidth = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getNextPortsArray - port is too far upstream - discard\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath - free_upstream_bandwidth = %d free_downstream_bandwidth = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter::preAdapterEnable - lc2 offset = 0x%llx link_control_2 = 0x%x\n`
- `AppleThunderboltPCIUpAdapter - route = 0x%llx PCI link active time %llu ms status = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter(%x:%llx:%x)::finishDeactivateContext - we're deactivated\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getNextPortsArray - found a loop, ignoring next port\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::start - the_switch->getPathsDisabledForUpdate() returned %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::finalize - success = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath ------------------------- \n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::setupPaths - status = 0x%x fState = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::activatePaths - status = 0x%x fState = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::startPCICorrelation (1) - set correlation properties - status = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>[%u:0x%llx:0x%x]::wake - fState = %d\n`
- `AppleThunderboltPCIUpAdapter.cpp`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::start - IONVRAM not available\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::waitForDownAdapters\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::processActivatingFindDownAdapterPCICapabilityResults - fPCIDownAdapter->getPCICapabilityOffset() = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::postAdapterEnable - waiting for PCI link active indication\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::lateSleep - fState = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::earlyWakeDelay - delay %lld ms\n`
- `%lldus AppleThunderboltPCIUpAdapter::postAdapterEnable\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::pathDeactivationCallback - fTxPath status = 0x%x \n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::wake\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::syncActivate - waiting on activation\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::start - (2) fRxRequiredBandwidth = %d fRxMaximumBandwidth = %d fTxRequiredBandwidth = %d fTxMaximumBandwidth = %d\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::configCommandCallback - status = 0x%x, command = %p\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findExistingPaths - ERROR only found some paths\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getNextPortsArray - port is downstream - discard\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findUpstreamParentPCIDevice - fPCIDownAdapter = %p\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::startDeactivatingFindUpAdapterPCICapability\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findExistingPaths - fPCIDownAdapter = %p, status = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getNextPortsArray - even port index\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::waitForDownAdapters - route = 0x%llx port = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath - downstream\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::findBestPath - use new path, longest\n`
- `%lldus AppleThunderboltPCIUpAdapter::startPreAdapterEnable\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getNextPortsArray - add port route = 0x%llx port = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::getNextPortsArray - next_switch = 0x%llx check_switch = 0x%llx\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::createPaths - fTxPath %p\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::startPCICorrelation (1) - status = 0x%08x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::processDeactivatingFindUpAdapterPCICapabilityResults - status = 0x%x\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::setPowerState - kThunderboltPMSleepState\n`
- `%lldus AppleThunderboltPCIUpAdapter<%p>::start - status = 0x%x\n`
