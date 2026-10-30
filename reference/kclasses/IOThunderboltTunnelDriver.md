# `IOThunderboltTunnelDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOThunderboltFamily`](../kexts/com.apple.iokit.IOThunderboltFamily.md)
- Object size: `0xd0` (208 bytes)
- Metaclass: `0xfffffe000ba1d3b0`; metaclass vtable `0xfffffe000841c750`; class vtable `0xfffffe000841c0d8`
- Registration (init): `0xfffffe000a584e28`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (7; 20 in total)

- [`AppleThunderboltDPAdapterFamily`](AppleThunderboltDPAdapterFamily.md) — `com.apple.driver.AppleThunderboltDPAdapterFamily`
- [`AppleThunderboltDPAdapterFamilyBase`](AppleThunderboltDPAdapterFamilyBase.md) — `com.apple.driver.AppleThunderboltDPAdapterFamily`
- [`AppleThunderboltPCIDownAdapter`](AppleThunderboltPCIDownAdapter.md) — `com.apple.driver.AppleThunderboltPCIDownAdapter`
- [`AppleThunderboltPCIUpAdapter`](AppleThunderboltPCIUpAdapter.md) — `com.apple.driver.AppleThunderboltPCIUpAdapter`
- [`AppleThunderboltUSBDownAdapter`](AppleThunderboltUSBDownAdapter.md) — `com.apple.driver.AppleThunderboltUSBDownAdapter`
- [`AppleThunderboltUSBUpAdapter`](AppleThunderboltUSBUpAdapter.md) — `com.apple.driver.AppleThunderboltUSBUpAdapter`
- [`IOThunderboltTunnelDriverType2`](IOThunderboltTunnelDriverType2.md) — `com.apple.iokit.IOThunderboltFamily`

## Strings in its kext that name it (55)

- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)::tunnelDidDeallocate - interface = %p\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::earlyWakeBegin - WARNING: fController == NULL\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::addAvailableTBTPorts - interface = %p srcPort = %p dstPort = %p\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::tunnelWillActivate - interface = %p\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::earlyWakeComplete - decremented early wake scan count to %u\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::earlyWakeBegin - incremented early wake scan count to %u\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::tunnelWillDeactivate - interface = %p\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::decrementScanCount\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::lateSleepBegin - incremented late sleep scan count to %u\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::earlyWakeComplete\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::countActiveClients - interface = %p\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::incrementClientScanCount - incremented client scan count id %u to %u\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::incrementClientScanCount\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::tunnelDidActivate - interface = %p\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::decrementScanCount - decremented scan count id %u to %u\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::setTunnelSourcePort - interface = %p tbtPort = %p transportPort = 0x%x\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)::getTunnelDriverInterface - interface_manager = %p\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)::tunnelDidActivate - interface = %p\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::incrementScanCount - incremented scan count id %u to %u\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)::checkPathsDisabledByProtocol - paths_disabled = %d for port type 0x%06x\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)::setTunnelFlags - interface = %p flags = %u\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::waitForClientStop - interface = %p\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::lateSleepComplete - decremented late sleep scan count to %u\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::lateSleepComplete\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::lateSleepBegin\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)::isTunnelInUse - interface = %p\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)::setTunnelDestinationPort - interface = %p port = %p\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)::isClientAsleep - interface = %p\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::decrementClientScanCount\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)::getTunnelDriverInterface - port is on root switch\n`
- `%lldus IOThunderboltTunnelDriver<%p>::free\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)::getTunnelDriverInterface - tbt_port = %p\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)::getTunnelDriverInterface - interface = %p\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::lateSleepBegin - WARNING: fController == NULL\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)::getTunnelFlags - interface = %p\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)::setTunnelSourcePort - interface = %p port = %p\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)::tunnelWillActivate - interface = %p\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)::getTunnelDriverInterface - fController = %p\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::getAvailablePort - interface = %p transportPort = 0x%x\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::incrementScanCount\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::earlyWakeBegin\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::getAvailablePort - interface = %p\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::isTunnelInitializedWithTransportPort - interface = %p transportPort = 0x%x\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::areAllClientsForTransportAsleep - interface = %p transportPort = 0x%x\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::tunnelDidDeallocate - interface = %p\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::decrementClientScanCount - decremented client scan count id %u to %u\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::setTunnelDestinationPort - interface = %p tbtPort = %p transportPort = 0x%x\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::finalize - ERROR: late sleep scan count = %u\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::decrementScanCount - ERROR: fController == NULL\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::incrementScanCount - ERROR: increment id %u must be between 0 and %u inclusive\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::decrementClientScanCount\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::lateSleepComplete - decremented late sleep scan count to %u\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::finalize - ERROR: early wake scan count = %u\n`
- `%lldus IOThunderboltTunnelDriver(%x:%llx:%x)<0x%08x>::incrementScanCount\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::tunnelDidActivate - interface = %p\n`
