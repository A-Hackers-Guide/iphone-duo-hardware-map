# `IOTBTTunnelDriverInterface`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOThunderboltFamily`](../kexts/com.apple.iokit.IOThunderboltFamily.md)
- Object size: `0x78` (120 bytes)
- Metaclass: `0xfffffe000ba1c680`; metaclass vtable `0xfffffe00084088a8`; class vtable `0xfffffe0008408698`
- Registration (init): `0xfffffe000a44fe00`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Direct subclasses (2; 2 in total)

- [`IOTBTTunnelDriverInterfaceType2`](IOTBTTunnelDriverInterfaceType2.md) — `com.apple.iokit.IOThunderboltFamily`
- [`IOTBTTunnelDriverInterfaceType3`](IOTBTTunnelDriverInterfaceType3.md) — `com.apple.iokit.IOThunderboltFamily`

## Strings in its kext that name it (60)

- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::allocateActivationStatePerPort - entered\n`
- `%lldus IOTBTTunnelDriverInterface(%d)<%p>::installClientInterface - return status = 0x%08x\n`
- `%lldus IOTBTTunnelDriverInterface(%d)<%p>::tunnelDidWake - fIsSleeping = %d\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::setTunnelStartWithTransportPort - activationState = %p transportPort=0x%x fTunnelIsStarted = %d fPendingPorts->getCount() = 0x%x\n`
- `%lldus IOTBTTunnelDriverInterface(%d)<%p>::copyDestinationPort - return port = %p\n`
- `%lldus IOTBTTunnelDriverInterface(%d)<%p>::tunnelDidActivate - return\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::tunnelDidActivateWithTransportPort - transportPort=0x%x changed=%d return\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::setAllocatedAndActivatedWithTransportPort - transportPort=0x%x fActualTunnelIsAllocated = %d fActualTunnelIsActivated = %d\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::setAllocatedAndActivatedWithTransportPort - transportPort=0x%x fTunnelIsAllocated = %d fTunnelIsActivated = %d\n`
- `%lldus IOTBTTunnelDriverInterface(%d)<%p>::setTunnelFlags - return flags = %u\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::messagePortClientsWithTransportPort - msg = 0x%08x activationState=%p \n`
- `%lldus IOTBTTunnelDriverInterface(%d)<%p>::waitForTunnelSleep - fReadyToReleaseClient = %d\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::areAllClientsAsleep isAsleep=%d\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::tunnelWillSleepPerTransportPort transportPort=0x%x - waiting for clients to sleep\n`
- `%lldus IOTBTTunnelDriverInterface(%d)<%p>::installClientInterface - interface = %p\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::waitForTunnelDeallocateWithTransportPort - transportPort=0x%x woke up fActualTunnelIsAllocated = %d\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::waitForTunnelSleepWithTransportPort - transportPort=0x%x sleep on fReadyToReleaseClient = %d\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::messagePortClientsWithTransportPort - sending message to destination port at (%x:%llx:%x)\n`
- `%lldus IOTBTTunnelDriverInterface(%d)<%p>::setDestinationPort - port = %p\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::waitForTunnelDeallocateWithTransportPort transportPort=0x%x\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::tunnelDidDeallocateWithTransportPort transportPort=0x%x - clear allocated and activated\n`
- `%lldus IOTBTTunnelDriverInterface(%d)<%p>::sendStateChangeNotification\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::sendStateChangeNotificationWithTransportPort - transportPort=0x%x ioportIndex=0x%x isAllocateOp=%d\n`
- `%lldus IOTBTTunnelDriverInterface(%d)<%p>::setAllocatedAndActivated - fTunnelIsAllocated = %d fTunnelIsActivated = %d\n`
- `%lldus IOTBTTunnelDriverInterface(%d)<%p>::setAllocatedAndActivated - changed = %d\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::waitForTunnelWakeWithTransportPort - transportPort=0x%x fTunnelIsAllocated = %d fTunnelIsActivated = %d\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::countActiveClients activeClients=0x%x\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::waitForTunnelWakeWithTransportPort transportPort=0x%x\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::tunnelWillSleepPerTransportPort transportPort=0x%x - changed=%d return\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::tunnelDidActivateWithTransportPort - set activated and allocated\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::tunnelWillDeactivateWithTransportPort - transportPort=0x%x changed=%d return\n`
- `%lldus IOTBTTunnelDriverInterface(%d)<%p>::tunnelDidWake - We're awake. Tell the current tunnel state.\n`
- `%lldus IOTBTTunnelDriverInterface(%d)<%p>::tunnelDidDeallocate - return\n`
- `%lldus IOTBTTunnelDriverInterface<%p>::initWithManager\n`
- `%lldus IOTBTTunnelDriverInterface<%p>::free\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::tunnelDidActivateWithTransportPort transportPort=0x%x\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::getAvailableTBTPorts - srcPort=%p dstPort = %p\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::unsetTransportPortToIOPortIndex  status=0x%x - transportPort=0x%x \n`
- `%lldus IOTBTTunnelDriverInterface(%d)<%p>::tunnelDidActivate\n`
- `%lldus IOTBTTunnelDriverInterface(%d)<%p>::createResources - return status = 0x%08x\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::waitForTunnelDeallocateWithTransportPort - transportPort=0x%x sleep on fActualTunnelIsAllocated = %d\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::setAllocatedAndActivatedWithTransportPort - transportPort=0x%x changed = %d\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::allocateActivationStatePerPort - exiting status=0x%x\n`
- `%lldus IOTBTTunnelDriverInterface(%d)<%p>::copySourcePort - return port = %p\n`
- `%lldus IOTBTTunnelDriverInterface(%d)<%p>::tunnelDidActivate - set activated and allocated\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::waitForTunnelSleepWithTransportPort transportPort=0x%x\n`
- `%lldus IOTBTTunnelDriverInterface(%d)<%p>::isTunnelInUse\n`
- `%lldus IOTBTTunnelDriverInterface(%d)<%p>::waitForTunnelSleep\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::addAvailableTBTPorts - success = %d srcPort=%p dstPort = %p\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::countActiveClients fTunnelActivationStatePerPort=%p\n`
- `%lldus IOTBTTunnelDriverInterface(%d)<%p>::waitForTunnelWake - sleep on fTunnelIsActivated = %d\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::tunnelDidWake - transportPort=0x%x  fIsSleeping = %d\n`
- `%lldus IOTBTTunnelDriverInterface(%d)::createClientInterface - client = %p type = 0x%08x transportPort=0x%x\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::setTransportPortToIOPortIndex  status=0x%x - transportPort=0x%x ioPortIndex=0x%x\n`
- `%lldus IOTBTTunnelDriverInterfaceType2(%d)<%p>::waitForClientStop - fTunnelIsStarted = %d\n`
- `%lldus IOTBTTunnelDriverInterface(%d)<%p>::tunnelDidDeallocate\n`
- `%lldus IOTBTTunnelDriverInterface(%d)<%p>::waitForTunnelWake - return status = 0x%08x\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::copyDestinationPortWithTransportPort - return tbtPort = %p\n`
- `%lldus IOTBTTunnelDriverInterface(%d)<%p>::waitForTunnelDeallocate - fTunnelIsAllocated = %d fTunnelIsActivated = %d\n`
- `%lldus IOTBTTunnelDriverInterfaceType3(%d)<%p>::allocateActivationStatePerPort - allocated succssfully\n`
