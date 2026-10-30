# `IOThunderboltVSA`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOThunderboltFamily`](../kexts/com.apple.iokit.IOThunderboltFamily.md)
- Object size: `0xd8` (216 bytes)
- Metaclass: `0xfffffe000ba1c958`; metaclass vtable `0xfffffe000840c488`; class vtable `0xfffffe000840bee8`
- Registration (init): `0xfffffe000a48888c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IOThunderboltVSA` in [`com.apple.iokit.IOThunderboltFamily`](../kexts/com.apple.iokit.IOThunderboltFamily.md): `IOProviderClass` = `IOThunderboltPort`, `IOProbeScore` = `4096`

## Strings in its kext that name it (53)

- `%lldus IOThunderboltVSA(%x@%llx:%x)::start completed - status = 0x%x fHIPort = %p\n`
- `%lldus IOThunderboltVSAService<%p>::publish\n`
- `%lldus IOThunderboltVSAService<%p>::unpublish\n`
- `%lldus IOThunderboltVSAService<%p>::free\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - protocol_idx=0x%x rsvd3=0x%x \n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::finalize - success = %d\n`
- `%lldus IOThunderboltVSAService<%p>::attach\n`
- `%lldus IOThunderboltVSAService(%x@%llx)::finalize\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::2setPowerState - return\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::wake\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::0setPowerState - state = %ld\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - status=0x%x length_offset=0x%x vsec_length=0x%x\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - protocol_idx=0x%x protocol_rev=0x%x \n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - protocol_idx=0x%x rsvd0=0x%x \n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::finalize\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::sleep\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::1setPowerState - state = %ld\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::setPowerState - unkonwn power state %ld\n`
- `%lldus IOThunderboltVSAService<%p>::setProperties\n`
- `%lldus IOThunderboltVSAService<%p>::detach\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::setPowerState - kThunderboltPMWakeState\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::destroyPowerManagement\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::NNNNNfind VSA capability - status=0x%x kVSACapabilityMask=0x%x kVSACapabilityID=0x%x cap_offset=0x%x\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - protocol_idx=0x%x rsvd1=0x%x \n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::setupPowerManagement - status = 0x%x\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - status=0x%08x table_config=0x%x num_of_entries_per_protocol=0x%x num_of_entries_in_table=0x%x\n`
- `%lldus IOThunderboltVSAService(%x@%llx)::finalize - terminate service: unknown service\n`
- `%lldus IOThunderboltVSAService<%p>::initWithPort\n`
- `%lldus IOThunderboltVSAService<%p>::initWithPort - ERROR: fPort = NULL\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::start - VSA Port matched port %p adapterType = 0x%x\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::free\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - protocol_idx=0x%x protocol_setting=0x%x \n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - protocol_idx=0x%x protocol_id=0x%x \n`
- `%lldus IOThunderboltVSAService(%x@%llx)::finalize - terminate service: %s\n`
- `%lldus IOThunderboltVSA::createResources status = 0x%x\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - status=0x%08x\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - protocol_idx=0x%x txMask=0x%x \n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::setPowerState - kThunderboltPMSleepState\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - protocol_idx=0x%x rsvd2=0x%x \n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::start - fHIPort = %p fVSAPort = %p status=0x%x \n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::NNNNNfind VSA capability - status=0x%x kVSACapabilityMask=0x%x kVSACapabilityID=0x%x\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::init\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::setPowerState - kThunderboltPMPauseState\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - protocol_idx=0x%x rxMask=0x%x \n`
- `%lldus IOThunderboltVSAService<%p>::terminate\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::start\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::free\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::start - fHIPort = %p fVSAPort = %p status=0x%x \n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::init\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::setupPowerManagement - status = 0x%x\n`
- `%lldus IOThunderboltVSAService<%p>::terminate\n`
- `%lldus IOThunderboltVSA(%x@%llx:%x)::publishVSAConfigTable - status=0x%08x table_config=0x%x num_of_entries_per_protocol=0x%x num_of_entries_in_table=0x%x\n`
