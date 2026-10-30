# `IOThunderboltSwitch`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOThunderboltFamily`](../kexts/com.apple.iokit.IOThunderboltFamily.md)
- Object size: `0x220` (544 bytes)
- Metaclass: `0xfffffe000ba1cb60`; metaclass vtable `0xfffffe000840f748`; class vtable `0xfffffe000840e9a0`
- Registration (init): `0xfffffe000a4e3104`
- Superclasses: [`IOThunderboltNub`](IOThunderboltNub.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 13 in total)

- [`IOThunderboltSwitchLegacy`](IOThunderboltSwitchLegacy.md) — `com.apple.iokit.IOThunderboltFamily`
- [`IOThunderboltSwitchOS`](IOThunderboltSwitchOS.md) — `com.apple.iokit.IOThunderboltFamily`

## Strings in its kext that name it (60)

- `%lldus IOThunderboltSwitchOS2<%p>::configureUpstreamAsymmetricMode - dispatchAsync( IOThunderboltSwitchOS2<%p>::configureUpstreamAsymmetricModeInternal )\n`
- `%lldus IOThunderboltSwitchI2CCommandQueue<%p>::sendI2CSync - start read phase\n`
- `%lldus IOThunderboltSwitchType1<%p>(0x%llx)::identifyHWRevision - could not write cc95 of port 0x%x\n`
- `%lldus IOThunderboltSwitch(%x@%llx)::fullScan - ERROR: status = 0x%x\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::publishAdapterData - port %x dev %x func %x\n`
- `%lldus IOThunderboltSwitch<%p>(0x%llx)::childDeviceScanForPort - waiting %u milliseconds for invalid config port\n`
- `%lldus IOThunderboltSwitch(%x@%llx)::acquireDPActivationSemaphore - adapter %p waiting on fDPActivationSemaphore\n`
- `%lldus IOThunderboltSwitchType6<%p>(0x%llx)::createResources - exit special mode kIOThunderboltSpecialModeSTMC\n`
- `%lldus IOThunderboltSwitch(%x@%llx)::configureFromStaticData - status = 0x%08x\n`
- `%lldus IOThunderboltSwitchType3<%p>(0x%llx)::acquireI2CLock\n`
- `%lldus IOThunderboltSwitchType1<%p>(0x%llx)::sendPrepareToSleepMessageToMicro - micro_address = 0x%08x port_set count = %d\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::isPortInDPMode - port %d dp_mode %d\n`
- `%lldus IOThunderboltSwitch(%x@%llx)::dropDPActivationSemaphore - adapter %p signaling fDPActivationSemaphore\n`
- `%lldus IOThunderboltSwitch<%p>(0x%llx)::enableTimeSyncSlaveForPortSynchronous - find port time sync capability for port 0x%x at route = 0x%llx\n`
- `%lldus IOThunderboltSwitch<%p>(0x%llx)::processXDomainChild - depth = %d peer_route_string = 0x%llx\n`
- `%lldus IOThunderboltSwitchI2CCommandQueue<%p>::sendI2CSync -  start write phase\n`
- `%lldus IOThunderboltSwitch<%p>(0x%llx)::disableUnusedLinks - port = %d has a dual link port at route 0x%llx port %d\n`
- `%lldus IOThunderboltSwitch<%p>(0x%llx) - Phase 7 (Static Link) done\n`
- `%lldus IOThunderboltSwitch<%p>(0x%llx) - Phase 1 (Discover Switch) done\n`
- `%lldus IOThunderboltSwitchType3<%p>(0x%llx)::acquireDPAdapterSynchronous\n`
- `%lldus IOThunderboltSwitch<%p>(0x%llx)::childDeviceScanForPort - wait %u milliseconds for training on port %d\n`
- `%lldus IOThunderboltSwitch<%p>(0x%llx)::readEEPROM - NVM not loaded! EEC=0x%x\n`
- `%lldus IOThunderboltSwitch(%x@%llx)::terminateInvalidClientsOnPort - terminate invalid child port %d\n`
- `%lldus IOThunderboltSwitchType3<%p>(0x%llx)::releaseLock - cannot unlock!\n`
- `%lldus IOThunderboltSwitch<%p>(0x%llx)::childDeviceScanForPort - link is up, but dual link was not, recheck\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::configureRouter - upstream port = %d\n`
- `%lldus IOThunderboltSwitchType1<%p>(0x%llx)::isPortConnected - port %d connected %d\n`
- `%lldus IOThunderboltSwitchType6<%p>(0x%llx)::free\n`
- `%lldus IOThunderboltSwitch(%x@%llx)::portAllowsDeviceScan - device identification prohibited.\n`
- `%lldus IOThunderboltSwitchType1<%p>(0x%llx)::sendPrepareToSleepMessageToMicro - micro_address = 0x%08x the_port = %p peer_port = %p peer_switch = %p\n`
- `%lldus IOThunderboltSwitchType6(%x@%llx)::configureRouter - router ready - status = 0x%08x\n`
- `%lldus IOThunderboltSwitchLegacy(%x@%llx)::setupTMU - disable TMU\n`
- `%lldus IOThunderboltSwitchDelegateACIO(%x@%llx)::enterSpecialMode - port %d about to enable and reset registered state!\n`
- `%lldus IOThunderboltSwitch<%p>(0x%llx)::childDeviceScanForPort - port %d\n`
- `%lldus IOThunderboltSwitchType5(%x@%llx)::resetChild - done\n`
- `%lldus IOThunderboltSwitch<%p>(0x%llx)::childDeviceScanForPort - retry = %d - child port %d phy state = %d\n`
- `%lldus IOThunderboltSwitch(%x@%llx)::portAllowsDeviceScan - device scan prohibited.\n`
- `%lldus IOThunderboltSwitch<%p>(0x%llx)::startPortScan - scan_port = %d\n`
- `%lldus IOThunderboltSwitchI2CCommandQueue<%p>::readBytesSync - read byte\n`
- `%lldus IOThunderboltSwitchType7<%p>(0x%llx)::free\n`
- `%lldus IOThunderboltSwitchLegacy(%x@%llx)::isLinkUpInternal - child port %d phy state = %d\n`
- `%lldus IOThunderboltSwitchType6(%x@%llx)::setupSpecialModesInternal - fSupportedSpecialMode = 0x%08x\n`
- `%lldus IOThunderboltSwitch(%x@%llx:0x%x)::childDeviceScanForPort - wait_for_training = %d prior_link = %d status = 0x%08x\n`
- `%lldus IOThunderboltSwitchType3<%p>(0x%llx)::acquireDPAdapter - ERROR: dropDPSemaphore failed with 0x%08x\n`
- `%lldus IOThunderboltSwitch<%p>(0x%llx)::updateTopologyID - fRouteString = 0x%016llx hi = 0x%08x lo = 0x%08x valid = 0x%x\n`
- `%lldus IOThunderboltSwitch<%p>(0x%llx)::publishLinkProperties - port = 0x%x\n`
- `%lldus IOThunderboltSwitch(%x@%llx)::controllerWillPowerDown\n`
- `%lldus IOThunderboltSwitchOS2(%x@%llx)::configureUpstreamAsymmetricMode - wake sleeping threads\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::overrideDROMProperties - InUSB4Mode\n`
- `%lldus IOThunderboltSwitch<%p>(0x%llx)::i2cRead - route = 0x%llx, address = 0x%02x, offset = 0x%02x, size = 0x%x\n`
- `%lldus IOThunderboltSwitch<%p>(0x%llx)::linkPartnerReset - reset success = %d - took %d milliseconds\n`
- `%lldus IOThunderboltSwitch(%x@%llx)::listenerCallback - listener callback - not idle - switch = %p\n`
- `%lldus IOThunderboltSwitchDelegateACIO<%p>(0x%llx)::initWithController - acioPortDisable: 0x%08x\n`
- `%lldus IOThunderboltSwitchOS(%x@%llx)::readEEPROMInternal - thistime %x remaining %x offset %x\n`
- `%lldus IOThunderboltSwitchDelegateACIO(%x@%llx)::identifyHWRevision - return status = 0x%08x\n`
- `%lldus IOThunderboltSwitchDelegateACIO(%x@%llx)::exitSpecialMode invalidating port %d\n`
- `%lldus IOThunderboltSwitchI2CCommandQueue<%p>::sendI2CSync - send stop\n`
- `%lldus IOThunderboltSwitchDelegateACIO(%x@%llx)::updateWakeEnables - port_group_offset = 0x%x\n`
- `%lldus IOThunderboltSwitch(%x@%llx)::verifierCallback - CRC error - crc = 0x%08x, calc_crc = 0x%08x\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::getPortSetForBus - port_set = %p\n`
