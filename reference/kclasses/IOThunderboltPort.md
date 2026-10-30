# `IOThunderboltPort`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOThunderboltFamily`](../kexts/com.apple.iokit.IOThunderboltFamily.md)
- Object size: `0x1a0` (416 bytes)
- Metaclass: `0xfffffe000ba1cbb0`; metaclass vtable `0xfffffe00084102d0`; class vtable `0xfffffe000840f9f0`
- Registration (init): `0xfffffe000a4f24c4`
- Superclasses: [`IOThunderboltNub`](IOThunderboltNub.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (52)

- `%lldus IOThunderboltPort(FF@FF:%x)::configureStandardProperties - fSwitch = 0x0\n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::configureLinkMode\n`
- `%lldus IOThunderboltPort(%x@%llx:%x)::setPortState - old state = %d new state = %d\n`
- `%lldus IOThunderboltPort<%p>::lowSpeedPeerPort - port = %d has a dual link port at route 0x%llx port %d\n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::isEnhancedUniDirTMUEnabled - offset = 0x%x data = 0x%08x is_enable = %d status = 0x%08x\n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::configureLinkMode - ufp = (%x@%llx:0x%x), dfp = (%x@%llx:0x%x)\n`
- `%lldus IOThunderboltPort(FF@FF:%x)::getChipType - fSwitch = 0x0\n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::getMaxHardwareBandwidth - max bw = %u\n`
- `%lldus IOThunderboltPort<%p>::lowSpeedPeerPort - port = %d has no peer\n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::configureSharedBuffers enable=0x%x shared_credits=0x%lx\n`
- `%lldus IOThunderboltPort<%p>::free\n`
- `%lldus IOThunderboltPort<%p>::finalize - port number = %d upstream = %d\n`
- `%lldus IOThunderboltPort<%p>::setSWObjectionCLxStates - waitForCLxChange to 0x%x\n`
- `%lldus IOThunderboltPort(%x@%llx:%x)::configureFromDesciption - vendor_id = 0x%x device_id = 0x%x revision = 0x%x spec_version = 0x%x fMaxInHopID = 0x%x max_out_hop_id = 0x%x fMaxCredits = 0x%x fAdapterType = 0x%x fPortNumber = 0x%x fByteCounterSupported = 0x%x fLockByeCounterSupported = 0x%x status`
- `%lldus IOThunderboltPort<%p>::ensureRegistered - registerService\n`
- `%lldus IOThunderboltPort<%p>::deallocateNonFlowControlledCredits - requested = %d, allocated = %d, max = %d, status = 0x%08x\n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::getSupportedCLxStates - data = 0x%08x clx_states = 0x%x hw_clx_states = 0x%x link_clx_supported = %d status = 0x%08x\n`
- `%lldus IOThunderboltPort<%p>::cmReadDWord - out_data = 0x%08x status = 0x%08x\n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::configureLinkMode - done, status = 0x%08x\n`
- `%lldus IOThunderboltPort<%p>::setPeerPort - port_number = 0x%x alt_port = %p 0x%x\n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::isEnhancedUniDirTMUEnabled - is_enable = %d status = 0x%08x\n`
- `%lldus IOThunderboltPortMicro<%p>::initWithController\n`
- `%lldus IOThunderboltPort<%p>::linkPorts - r 0x%llx p %d provider_port = %p r 0x%llx p %d fOutHopSet %p fInHopSet %p\n`
- `%lldus IOThunderboltPort(FF@FF:%x)::configureStandardProperties - eeprom->getPCIDeviceFunction\n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::setEnabledCLxStates - set CLx data = 0x%08x mask = 0x%08x\n`
- `%lldus IOThunderboltPort<%p>::setSWObjectionCLxStates - settting objection to 0x%x\n`
- `%lldus IOThunderboltPortMicro<%p>::free\n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::configureLinkMode - ufp required bw allocated = %u, ufp hw bw = %u, ufp max hw bw = %u, dfp required bw allocated = %u, dfp hw bw = %u, dfp max hw bw = %u, bw thresh = %u\n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::enableUniDirTMU - offset = 0x%x data = 0x%08x mask = 0x%08x enable = %d status = 0x%08x\n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::getMaxHardwareBandwidth - per lane bw = %u, supported link modes = 0x%08x\n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::setEnabledCLxStates - data = 0x%08x clx_states = 0x%x status = 0x%08x\n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::isUniDirTMUEnabled - offset = 0x%x data = 0x%08x is_enable = %d status = 0x%08x\n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::setUpstreamTMUParameters - offset = 0x%x data = 0x%08x mask = 0x%08x replenish_n = %d status = 0x%08x\n`
- `%lldus IOThunderboltPort<%p>::lowSpeedPeerPort - port = %d has a dual link peer at route 0x%llx port %d\n`
- `%lldus IOThunderboltPort(FF@FF:%x)::getRouteString - fSwitch = 0x0\n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::enableEnhancedUniDirTMU - offset = 0x%x data = 0x%08x mask = 0x%08x enable = %d status = 0x%08x\n`
- `%lldus IOThunderboltPort<%p>::allocateNonFlowControlledCredits - requested = %d, allocated = %d, max = %d, status = 0x%08x\n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::setMinimumRequiredTMUMode - fMinRequiredTMUMode = 0x%08x tmu_mode = 0x%08x\n`
- `%lldus IOThunderboltPort<%p>::setDualLinkPort - port_number = 0x%x alt_port = %p 0x%x rid = %d\n`
- `%lldus IOThunderboltPort<%p>::setSWObjectionCLxStates - didUpdateCLx = %d waitForCLxChange to 0x%x Done \n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::getEnabledCLxStates - data = 0x%08x clx_states = 0x%x status = 0x%08x\n`
- `%lldus IOThunderboltPort<%p>::setSWObjectionCLxStates - updating CLx mode for states 0x%x\n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::setUpstreamTMUParameters - offset = 0x%x data = 0x%08x mask = 0x%08x replenish_timeout = %d replenish_threshold = %d status = 0x%08x\n`
- `%lldus IOThunderboltPort<%p>::cmReadDWord - route = 0x%llx address = 0x%x offset = 0x%02x\n`
- `%lldus IOThunderboltPort(FF@FF:%x)::getThunderboltDepth - fSwitch = 0x0\n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::enableTimeSync - offset = 0x%x data = 0x%08x mask = 0x%08x enable = %d status = 0x%08x\n`
- `site.OSSharedPtr<IOThunderboltPortMicro>`
- `%lldus IOThunderboltPort<%p>::setPeerPort - port_number = 0x%x alt_port = %p 0x%x\n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::configureLinkMode - done, status = 0x%08x\n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::setEnabledCLxStates - data = 0x%08x clx_states = 0x%x status = 0x%08x\n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::setEnabledCLxStates - set CLx data = 0x%08x mask = 0x%08x\n`
- `%lldus IOThunderboltPort(%x@%llx:0x%x)::configureLinkMode - ufp = (%x@%llx:0x%x), dfp = (%x@%llx:0x%x)\n`
