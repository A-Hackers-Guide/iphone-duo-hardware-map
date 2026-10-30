# `AppleThunderboltIPService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltIP`](../kexts/com.apple.driver.AppleThunderboltIP.md)
- Object size: `0x100` (256 bytes)
- Metaclass: `0xfffffe000b9d2230`; metaclass vtable `0xfffffe0008284970`; class vtable `0xfffffe0008284418`
- Registration (init): `0xfffffe000996cd44`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `XDomainServiceDriver` in [`com.apple.driver.AppleThunderboltIP`](../kexts/com.apple.driver.AppleThunderboltIP.md): `IOProviderClass` = `IOThunderboltLocalNode`, `IOResourceMatch` = `IOKit`, `IOMatchCategory` = `AppleThunderboltIPService`, `IOProbeScore` = `4096`

## Strings in its kext that name it (60)

- `%lldus AppleThunderboltIPService<%p>::publishIPService - ERROR: fProvider = NULL\n`
- `AppleThunderboltIPService<%p>::publishIPService - ERROR: fProvider = NULL\n`
- `%lldus AppleThunderboltIPService<%p>::publishIPService - publishing IP service vers %d.%d, protocol ID %d, settings = 0x%x\n`
- `%lldus AppleThunderboltIPService<%p>::getIPPortForThunderboltPort - tbtPort (updated) = %p\n`
- `%lldus AppleThunderboltIPService<%p>::protocolListenerCallback - WARNING: isInactive() = true, aborting\n`
- `AppleThunderboltIPService<%p>::finalize - ERROR: publishIPService failed with 0x%08x\n`
- `AppleThunderboltIPService<%p>::finalize - releasing objects\n`
- `%lldus AppleThunderboltIPService<%p>::getIPPortForThunderboltPort - tbtPort = %p\n`
- `%lldus AppleThunderboltIPService<%p>::getIPPortForThunderboltPort - ERROR: lane = %d\n`
- `AppleThunderboltIPService<%p>::reserveForLogin - WARNING: isInactive() = true, aborting\n`
- `AppleThunderboltIPService<%p>::publishIPService - unpublishing IP service\n`
- `%lldus AppleThunderboltIPService<%p>::createPorts - total_ports_count = %d\n`
- `AppleThunderboltIPService<%p>::createPorts - new_ip_port = %p\n`
- `AppleThunderboltIPService<%p>::handleXDomainPacket - WARNING: connection not found, dropping XD packet\n`
- `%lldus AppleThunderboltIPService<%p>::reserveForLogin - setting fCurrentLoginRequest = %p\n`
- `AppleThunderboltIPService<%p>::getIPPortForThunderboltPort - tbtPort = %p\n`
- `%lldus AppleThunderboltIPService<%p>::getIPPortForThunderboltPort - ERROR: dual link port not found\n`
- `AppleThunderboltIPService<%p>::finalize\n`
- `AppleThunderboltIPService<%p>::getIPPortForThunderboltPort - tbtPort (dual link) = %p\n`
- `AppleThunderboltIPService<%p>::getIPPortForThunderboltPort - using primary lane\n`
- `%lldus AppleThunderboltIPService<%p>::handleXDomainPacket - forwarding packet to ip_connection %p\n`
- `AppleThunderboltIPService<%p>::finalize - ERROR: fDispatchQueue = NULL\n`
- `%lldus AppleThunderboltIPService<%p>::handleXDomainPacket - ERROR: context = %p, fProvider = %p\n`
- `AppleThunderboltIPService<%p>::getIPPortForThunderboltPort - WARNING: isInactive() = true, aborting\n`
- `AppleThunderboltIPService<%p>::createPorts - ERROR: no suitable TBT ports found\n`
- `AppleThunderboltIPService<%p>::protocolListenerCallback - WARNING: isInactive() = true, aborting\n`
- `%lldus AppleThunderboltIPService<%p>::protocolListenerCallback - inspecting command\n`
- `%lldus AppleThunderboltIPService<%p>::reserveForLogin - ERROR: attempt to release a reservation held by another object (%p)\n`
- `%lldus AppleThunderboltIPService<%p>::start - calling registerService\n`
- `%lldus AppleThunderboltIPService<%p>::createPorts - new_ip_port = %p\n`
- `AppleThunderboltIPService<%p>::createPorts - creating AppleThunderboltIPPort object for TBT port %d\n`
- `AppleThunderboltIPService<%p>::getIPPortForThunderboltPort - ERROR: lane = %d\n`
- `%lldus AppleThunderboltIPService<%p>::getIPPortForThunderboltPort - tbtPort (dual link) = %p\n`
- `AppleThunderboltIPService<%p>::reserveForLogin - reserve = %d, client = %p\n`
- `%lldus AppleThunderboltIPService<%p>::reserveForLogin - reserve = %d, client = %p\n`
- `%lldus AppleThunderboltIPService<%p>::handleXDomainPacket - WARNING: isInactive() = true, aborting\n`
- `AppleThunderboltIPService<%p>::handleXDomainPacket - ERROR: ExtractFromThunderboltIPProtocolHeader failed\n`
- `AppleThunderboltIPService<%p>::finalize - waiting on fDispatchQueue\n`
- `%lldus AppleThunderboltIPService<%p>::getIPPortForThunderboltPort - looking for upstream TBT ports\n`
- `%lldus AppleThunderboltIPService<%p>::start\n`
- `AppleThunderboltIPService<%p>::start - calling registerService\n`
- `AppleThunderboltIPService<%p>::publishIPService - ERROR: failed with 0x%08x\n`
- `%lldus AppleThunderboltIPService<%p>::start - ERROR: failed to startup\n`
- `%lldus AppleThunderboltIPService<%p>::protocolListenerCallback - dispatchAsync( handleXDomainPacket )\n`
- `AppleThunderboltIPService<%p>::handleXDomainPacket - WARNING: isInactive() = true, aborting\n`
- `AppleThunderboltIPService<%p>::getIPPortForThunderboltPort - tbtPort (updated) = %p\n`
- `AppleThunderboltIPService<%p>::getIPPortForThunderboltPort - switching to upstream tbtPort at depth %d\n`
- `%lldus AppleThunderboltIPService<%p>::reserveForLogin - WARNING: login request (%p) already in progress, please try again\n`
- `%lldus AppleThunderboltIPService<%p>::getIPPortForThunderboltPort - on secondary lane, switching to dual link port\n`
- `AppleThunderboltIPService<%p>::handleXDomainPacket - ERROR: context = %p, fProvider = %p\n`
- `AppleThunderboltIPService<%p>::handleXDomainPacket - packetType = %s\n`
- `%lldus AppleThunderboltIPService<%p>::reserveForLogin - no reservation to release\n`
- `AppleThunderboltIPService<%p>::createPorts - port_number = %d, adapter_type = 0x%x, lane = %d\n`
- `%lldus AppleThunderboltIPService<%p>::createPorts - ERROR: fRootSwitch = NULL\n`
- `AppleThunderboltIPService<%p>::start - ERROR: fDispatchQueue = NULL\n`
- `%lldus AppleThunderboltIPService<%p>::reserveForLogin - WARNING: isInactive() = true, aborting\n`
- `site.AppleThunderboltIPService`
- `AppleThunderboltIPService<%p>::protocolListenerCallback - dispatchAsync( handleXDomainPacket )\n`
- `AppleThunderboltIPService<%p>::protocolListenerCallback - ERROR: fDispatchQueue not running, aborting\n`
- `AppleThunderboltIPService<%p>::handleXDomainPacket - forwarding packet to ip_connection %p\n`
