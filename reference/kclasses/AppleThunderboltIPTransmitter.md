# `AppleThunderboltIPTransmitter`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltIP`](../kexts/com.apple.driver.AppleThunderboltIP.md)
- Object size: `0x168` (360 bytes)
- Metaclass: `0xfffffe000b9d2288`; metaclass vtable `0xfffffe0008285740`; class vtable `0xfffffe00082851e8`
- Registration (init): `0xfffffe0009980ad8`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `XDomainServiceConsumer` in [`com.apple.driver.AppleThunderboltIP`](../kexts/com.apple.driver.AppleThunderboltIP.md): `IOProviderClass` = `IOThunderboltXDomainService`, `IOPropertyMatch` = `{'Protocol Version': 1, 'Service Key': 'network'}`, `IOResourceMatch` = `IOKit`, `IOProbeScore` = `4096`

## Strings in its kext that name it (60)

- `AppleThunderboltIPTransmitter<%p>::setPowerState - kThunderboltIPPowerStatePause\n`
- `AppleThunderboltIPTransmitter<%p>::ipServiceNotificationCallback\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::processTimeout - deactivating fTxPath, prev_state = %d\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::processIPServiceNotification - fIPConnection = %p, fTBTRouteString = 0x%llx, fTBTPortNumber = 0x%x\n`
- `AppleThunderboltIPTransmitter<%p>::timerCommandCallback - ERROR: dispatchAsync failed with 0x%08x\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::systemWillShutdown - fState = %s\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::processTimeout - WARNING: sendLogoutRequest returned kIOReturnOffline (link down?)\n`
- `AppleThunderboltIPTransmitter<%p>::logout - in the process of logging in, aborting & starting logout\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::finalize - ERROR: fDispatchQueue = NULL\n`
- `AppleThunderboltIPTransmitter<%p>::processIPServiceNotification - this is not the node we're looking for...\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::processTimeout - WARNING: out of login retries, giving up\n`
- `AppleThunderboltIPTransmitter<%p>::processLoginResponsePacket - setting remote MAC address\n`
- `AppleThunderboltIPTransmitter<%p>::sendLoginRequest - WARNING: reserveForLogin returned kIOReturnExclusiveAccess\n`
- `AppleThunderboltIPTransmitter<%p>::setTimer - submitting new timer\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::logout - ERROR: fTerminationComplete = true, aborting\n`
- `AppleThunderboltIPTransmitter<%p>::sendLoginRequest - ERROR: unexpected state: 0x%x\n`
- `AppleThunderboltIPTransmitter<%p>::processLogoutResponsePacket - ERROR: ExtractFromThunderboltIPLogoutResponsePacket failed\n`
- `AppleThunderboltIPTransmitter<%p>::timerCommandCallback - ERROR: fTerminationComplete = true, aborting\n`
- `AppleThunderboltIPTransmitter<%p>::processLoginResponsePacket - ERROR: failed with 0x%08x, waiting for timeout to fire\n`
- `AppleThunderboltIPTransmitter<%p>::login - calling configureTxPath\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::configureTxPath - DST: dst_port = %p, dst_hop_range = { %d, %d }\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::prepareForTermination - stopping power management\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::ipServiceNotificationCallback - ERROR: dispatchAsync failed with 0x%08x\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::processLogoutResponsePacket - ERROR: ExtractFromThunderboltIPLogoutResponsePacket failed\n`
- `AppleThunderboltIPTransmitter<%p>::login - WARNING: still in state %s, please try again\n`
- `AppleThunderboltIPTransmitter<%p>::logout - WARNING: sendLogoutRequest returned kIOReturnOffline (link down?)\n`
- `AppleThunderboltIPTransmitter<%p>::sendLoginRequest - WARNING: sendRequestPacket returned kIOReturnOffline (link down?)\n`
- `AppleThunderboltIPTransmitter<%p>::finalize - stopping fDispatchQueue\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::processTimeout - ERROR: logout failed with 0x%08x\n`
- `AppleThunderboltIPTransmitter<%p>::setupPowerManagement\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::prepareForTermination - WARNING: fIPService = NULL\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::dispatchProcessLogoutResponsePacket - ERROR: fDispatchQueue = NULL\n`
- `AppleThunderboltIPTransmitter<%p>::txCommandCallback - ERROR: incomingStatus = 0x%x\n`
- `AppleThunderboltIPTransmitter<%p>::processTimeout - calling sendLogoutRequest\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::processLoginResponsePacket - ERROR: fTxPath->activateSynchronous failed with 0x%08x\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::login - ERROR: unexpected state: 0x%x\n`
- `AppleThunderboltIPTransmitter<%p>::finalize - fDispatchQueue finished, setting fTerminationComplete = true\n`
- `AppleThunderboltIPTransmitter<%p>::sendLogoutRequest - calling sendRequestPacket( %s )\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::dispatchLogoutWithRequest - ERROR: fDispatchQueue = NULL\n`
- `AppleThunderboltIPTransmitter<%p>::setPowerState - WARNING: fTerminationStarted = true, aborting\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::processTimeout - ERROR: unexpected state: 0x%x\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::loginWithRequest - fState = %s\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::createTxPath - creating fTxCommandPool\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::txCommandCallback - commandWakeup( fTerminationWaitingForCommands )\n`
- `AppleThunderboltIPTransmitter<%p>::login - WARNING: fIPConnection = NULL, aborting login\n`
- `AppleThunderboltIPTransmitter<%p>::login - ERROR: unexpected state: 0x%x\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::dispatchLogoutWithRequest - fState = %s\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::dispatchLogoutWithRequest - ERROR: dispatch failed with 0x%08x\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::logout - fState = %s, sendRequest = %d\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::processLoginResponsePacket - ERROR: fIPConnection = NULL\n`
- `AppleThunderboltIPTransmitter<%p>::login - ERROR: failed to login (0x%08x), logging out\n`
- `AppleThunderboltIPTransmitter<%p>::processTimeout - callbackType = %d\n`
- `AppleThunderboltIPTransmitter<%p>::dispatchLogoutWithRequest - dispatchSync( logoutWithRequest )\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::start - ERROR: failed to fetch properties from the service dictionary\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::prepareForTermination - fState = %s\n`
- `AppleThunderboltIPTransmitter<%p>::prepareForTermination - releasing login reservation\n`
- `AppleThunderboltIPTransmitter<%p>::login - ERROR: failed configure Tx Path (0x%08x)\n`
- `AppleThunderboltIPTransmitter<%p>::finalize - fState = %s\n`
- `AppleThunderboltIPTransmitter<%p>::setPowerState - restarting fTxQueue\n`
- `%lldus AppleThunderboltIPTransmitter<%p>::configureTxPath - allocating fTxPath\n`
