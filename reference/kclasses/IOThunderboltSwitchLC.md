# `IOThunderboltSwitchLC`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOThunderboltFamily`](../kexts/com.apple.iokit.IOThunderboltFamily.md)
- Object size: `0x260` (608 bytes)
- Metaclass: `0xfffffe000ba1cf50`; metaclass vtable `0xfffffe0008416c58`; class vtable `0xfffffe0008415e70`
- Registration (init): `0xfffffe000a54d6b8`
- Superclasses: [`IOThunderboltSwitchLegacy`](IOThunderboltSwitchLegacy.md) → [`IOThunderboltSwitch`](IOThunderboltSwitch.md) → [`IOThunderboltNub`](IOThunderboltNub.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 2 in total)

- [`IOThunderboltSwitchType2`](IOThunderboltSwitchType2.md) — `com.apple.iokit.IOThunderboltFamily`
- [`IOThunderboltSwitchType3`](IOThunderboltSwitchType3.md) — `com.apple.iokit.IOThunderboltFamily`

## Strings in its kext that name it (26)

- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::isPortInDPMode - port %d dp_mode %d\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::getPortSetForBus - port_set = %p\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::enablePlugEvents - set notify retry, packet = 0x%08x\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::finalize\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::discoverMicroForPort\n`
- `%lldus IOThunderboltSwitchLC(%x@%llx)::lateSleepPhase3 - send new sleep request\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::sendPrepareToSleepMessageToMicro - Skipping Setting for IceLake\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::free\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::discoverMicroForPort - ERROR: status = 0x%08x\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::isPortConnected - port %d connected %d\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::addPortForMicro - port %d micro_address 0x%x micro_type = %d\n`
- `%lldus IOThunderboltSwitchLC(%x@%llx)::lateSleepPhase3 - ERROR: status = 0x%08x\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::setupI2CCommandQueue - find LC capability for switch at route = 0x%llx\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::updateConfiguredStateForPort - eeprom_version = 0x%x eeprom_revision = %d chip_type = 0x%04x\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::sendPrepareToSleepMessageToMicro - lc_address = 0x%08x wake enables = 0x%08x\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::determineWakeReason - fLCOffset = 0x%x reason 0x%04x\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::setupI2CCommandQueue - find I2C capability for switch at route = 0x%llx\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::updateConfiguredStateForPort - do_correct_xdomain_sleep = %d\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::sendPrepareToSleepMessageToMicro - address = 0x%02x, micro_type = 0x%x, mode = %d, status = 0x%08x\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::setPortSetReady - ready = %d\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::sendPrepareToSleepMessageToMicro - lc_address = 0x%08x the_port = %p peer_port = %p peer_switch = %p\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::sendPrepareToSleepMessageToMicro - write LC_SX_CTRL lc_address = 0x%08x data = 0x%08x\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::sendPrepareToSleepMessageToMicro - lc_address = 0x%08x no pci tunnel, clearing configured\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::free\n`
- `%lldus IOThunderboltSwitchLC<%p>(0x%llx)::sendPrepareToSleepMessageToMicro - lc_address = 0x%08x wake enables = 0x%08x\n`
- `%lldus IOThunderboltSwitchLC(%x@%llx)::lateSleepPhase3 - ERROR: status = 0x%08x\n`
