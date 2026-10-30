# `IOThunderboltSwitchOS`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOThunderboltFamily`](../kexts/com.apple.iokit.IOThunderboltFamily.md)
- Object size: `0x2c0` (704 bytes)
- Metaclass: `0xfffffe000ba1cca0`; metaclass vtable `0xfffffe0008412138`; class vtable `0xfffffe0008411330`
- Registration (init): `0xfffffe000a51a2cc`
- Superclasses: [`IOThunderboltSwitch`](IOThunderboltSwitch.md) → [`IOThunderboltNub`](IOThunderboltNub.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 7 in total)

- [`IOThunderboltSwitchOS2`](IOThunderboltSwitchOS2.md) — `com.apple.iokit.IOThunderboltFamily`
- [`IOThunderboltSwitchUSB4`](IOThunderboltSwitchUSB4.md) — `com.apple.iokit.IOThunderboltFamily`

## Strings in its kext that name it (60)

- `%lldus IOThunderboltSwitchOS2<%p>::configureUpstreamAsymmetricMode - dispatchAsync( IOThunderboltSwitchOS2<%p>::configureUpstreamAsymmetricModeInternal )\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::publishAdapterData - port %x dev %x func %x\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::configureRouter - upstream port = %d\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::configureUpstreamAsymmetricMode - wake sleeping threads\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::overrideDROMProperties - InUSB4Mode\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::readEEPROMInternal - thistime %x remaining %x offset %x\n`
- `%lldus IOThunderboltSwitchOS(%d@0x%llx)::routerOperation - packet_data[%d] = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::updateUpstreamLinkModeSupport - final values: ufp_asymmetric_support = 0x%08x, dfp_asymmetric_support = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::wakeAllPortsInternal - LC 1 set SLI bit - status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::lateSleepPhase3 - waited for sleep ready indication, data = 0x%08x - status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::readEEPROMInternal DROM Length %x \n`
- `%lldus IOThunderboltSwitchOS(%d@0x%llx)::routerOperation - opcode write status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS(%d@0x%llx)::routerOperation - write data and metadata, status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x:%llx)::checkPathsDisabledByPortType - paths_disabled = %d for port type 0x%08x\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::changeTMUMode\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::resetChild - fChildResetPort = %d\n`
- `%lldus IOThunderboltSwitchOS(%d@0x%llx)::routerOperation - operation not supported - status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::setupTMU - Time Synchronization Protocol Not Supported (TSNS) bit is set.\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::configureRouter - data = 0x%08x should_configure = %d - status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS<%p>(0x%llx)::free\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::setupTMU - enable bidir mode early\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::finishTMUSetup\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::configureRouter - inUSB4Mode = %d status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::updateUpstreamLinkModeSupport - done, status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::updateUpstreamLinkModeSupport - ufp_supported_link_modes = 0x%08x, dfp_supported_link_modes = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::configureRouter - PORT_CS_18 = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::configureUpstreamAsymmetricMode - start waiting for in-progress asymmetric transition (if any)\n`
- `%lldus IOThunderboltSwitchOS<%p>(0x%llx)::finalize\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::setTMUParameters - set avg constant to %d. data = 0x%08x mask = 0x%08x status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::updateWakeEnables - write device offset = 0x%x data = 0x%08x mask = 0x%08x - status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::readEEPROMInternal set fEEPROMRead\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::updateWakeEnables - port %d is a primary NULL port\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::wakeAllPortsInternal\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::checkCanEnterLinkModeForPort - port = (%x@%llx:0x%x), mode = %d, link_mode_entry_possible = %u, status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::readEEPROMInternal First RO status %x rstatus %x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::updateUpstreamLinkModeSupport - read UFP, ufp_asymmetric_support = 0x%08x, status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::readSupportedRouterCapabilities - status = 0x%08x fRouterCapabilities[0] = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::publishAdapterData - Buffer Allocation Operation - metadata = 0x%08x, robuffer[0] = 0x%08x, operation_status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS(%d@0x%llx)::routerOperation - metadata = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::configureRouter - config ready - status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::checkUIDMatch - new_uid=0x%016llx old_uid=0x%016llx result=%d\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::isPortConnected - port_number = 0x%02x - offset = %x connected = %d status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::updateUpstreamLinkModeSupport - read DFP, dfp_asymmetric_support = 0x%08x, status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS(%d@0x%llx)::routerOperation - packet_data[%d] (metadata) = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS(%d@0x%llx)::routerOperation - write offset = 0x%x opcode_dword = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::publishAdapterData - publish Buffer Allocation Request = %p count = %d\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::getUIDFromDeviceSpace - uid = 0x%016llx\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::configureCLx - status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::changeTMUMode\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::disableTMU\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::publishAdapterData - recvd %d buffer allocation parameters\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::assignLanes\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::checkCanEnterLinkModeForPort - ufp = (%x@%llx:0x%x), dfp = (%x@%llx:0x%x)\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::readEEPROMInternal - << %x\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::overrideDROMProperties - Not InUSB4Mode\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::setRouterCapability - status = 0x%08x enabled = %d\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::updateWakeEnables - status = 0x%08x\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::publishAdapterData - got param_index = 0x%02x, requested_allocation = 0x%04x, key = \"%s\"\n`
- `%lldus IOThunderboltSwitchOS<%p>(0x%llx)::discoverMicroForPort - port = %d\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::sendPrepareToSleepMessageToMicro - address = 0x%02x micro_type = 0x%02x mode = 0x%02x - status = 0x%08x\n`
