# `IDSServiceDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 31 instance methods, 0 class methods

## Instance methods

```
-[IDSServiceDelegate service:account:identifier:didSendWithSuccess:error:];
-[IDSServiceDelegate service:devicesChanged:];
-[IDSServiceDelegate service:connectedDevicesChanged:];
-[IDSServiceDelegate service:didSwitchActivePairedDevice:acknowledgementBlock:];
-[IDSServiceDelegate service:account:identifier:hasBeenDeliveredWithContext:];
-[IDSServiceDelegate service:account:incomingResourceAtURL:metadata:fromID:context:];
-[IDSServiceDelegate service:account:identifier:fromID:hasBeenDeliveredWithContext:];
-[IDSServiceDelegate serviceSpaceDidBecomeAvailable:];
-[IDSServiceDelegate service:nearbyDevicesChanged:];
-[IDSServiceDelegate service:account:inviteReceivedForSession:fromID:withContext:];
-[IDSServiceDelegate service:account:incomingMessage:fromID:context:];
-[IDSServiceDelegate service:account:receivedGroupSessionParticipantUpdate:];
-[IDSServiceDelegate service:account:incomingUnhandledProtobuf:fromID:context:];
-[IDSServiceDelegate service:activeAccountsChanged:];
-[IDSServiceDelegate service:account:incomingData:fromID:context:];
-[IDSServiceDelegate service:account:identifier:didSendWithSuccess:error:context:];
-[IDSServiceDelegate service:account:didReceiveLocalNetworkHandshake:fromID:context:];
-[IDSServiceDelegate service:account:inviteDroppedForSessionID:fromID:context:error:];
-[IDSServiceDelegate service:account:identifier:sentBytes:totalBytes:];
-[IDSServiceDelegate service:account:incomingOpportunisticData:withIdentifier:fromID:context:];
-[IDSServiceDelegate service:account:incomingPendingMessageOfType:fromID:context:];
-[IDSServiceDelegate service:account:incomingResourceAtURL:fromID:context:];
-[IDSServiceDelegate service:account:inviteReceivedForSession:fromID:];
-[IDSServiceDelegate service:account:inviteReceivedForSession:fromID:withOptions:];
-[IDSServiceDelegate service:account:pendingResourceWithMetadata:fromID:acknowledgementBlock:context:];
-[IDSServiceDelegate service:account:receivedGroupSessionParticipantDataUpdate:];
-[IDSServiceDelegate service:account:receivedGroupSessionParticipantUpdate:context:];
-[IDSServiceDelegate service:didCancelMessageWithSuccess:error:identifier:];
-[IDSServiceDelegate service:didSendOpportunisticDataWithIdentifier:toIDs:];
-[IDSServiceDelegate service:linkedDevicesChanged:];
-[IDSServiceDelegate serviceAllowedTrafficClassifiersDidReset:];
```
