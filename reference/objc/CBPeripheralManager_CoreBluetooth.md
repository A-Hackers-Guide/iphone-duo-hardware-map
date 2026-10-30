# `CBPeripheralManager`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBManager`
- 16 instance variables, 15 properties, 96 instance methods, 2 class methods

## Instance variables

```
{?="willRestoreState"b1"didAddService"b1"didReceiveReadRequest"b1"didReceiveWriteRequests"b1"centralDidSubscribeToCharacteristic"b1"centralDidUnsubscribeFromCharacteristic"b1"didStartAdvertising"b1"didStartPeriodicAdvertising"b1"didStopPeriodicAdvertising"b1"isReadyToUpdate"b1"centralDidConnect"b1"centralDidUpdateConnectionParameters"b1"didPublishL2CAPChannel"b1"didUnpublishL2CAPChannel"b1"didOpenL2CAPChannel"b1"didStopAdvertisingWithError"b1"didUpdateANCSAuthorization"b1"didUpdateControllerBTClock"b1"didUpdateControllerBTClockDict"b1"didRequestOfflineAdvPayloadRequestedWithReason"b1"didChannelSoundingProcedureEvent"b1"didCloseL2CAPChannel"b1"didReceiveL2CAPData"b1} _delegateFlags;
B _observingKeyPaths;
B _isAdvertising;
B _readyForUpdates;
B _waitingForReady;
@"<CBPeripheralManagerDelegate>" _delegate;
@"NSMapTable" _centrals;
@"NSMutableArray" _services;
@"NSMutableDictionary" _characteristicIDs;
@"NSLock" _updateLock;
@"NSNumber" _multipleAdvertisingSupported;
@"NSHashTable" _l2capChannels;
@? _incomingConnectionRequestCompletion;
Q _attributeIDGenerator;
@? _cisPeripheralConnectEvent;
@? _cisPeripheralDisconnectEvent;
```

## Properties

```
@property (TB,N,V_isAdvertising) isAdvertising;
@property (T@"NSMapTable",R,&,N,V_centrals) centrals;
@property (T@"NSMutableArray",R,&,N,V_services) services;
@property (T@"NSMutableDictionary",R,&,N,V_characteristicIDs) characteristicIDs;
@property (T@"NSLock",R,&,N,V_updateLock) updateLock;
@property (TB,R,N,V_readyForUpdates) readyForUpdates;
@property (TB,R,N,V_waitingForReady) waitingForReady;
@property (T@"NSNumber",&,N,V_multipleAdvertisingSupported) multipleAdvertisingSupported;
@property (T@"NSHashTable",R,&,N,V_l2capChannels) l2capChannels;
@property (T@?,C,N,V_incomingConnectionRequestCompletion) incomingConnectionRequestCompletion;
@property (TQ,V_attributeIDGenerator) attributeIDGenerator;
@property (T@?,C,N,V_cisPeripheralConnectEvent) cisPeripheralConnectEvent;
@property (T@?,C,N,V_cisPeripheralDisconnectEvent) cisPeripheralDisconnectEvent;
@property (TB,R,N,GsupportsMultipleAdvertising) isSupportingMultipleAdvertising;
@property (T@"<CBPeripheralManagerDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[CBPeripheralManager authorizationStatus];
+[CBPeripheralManager supportsFeatures:];
```

## Instance methods

```
-[CBPeripheralManager handleRestoringState:];
-[CBPeripheralManager handleReadyForUpdates:];
-[CBPeripheralManager handleAdvertisingAddressChanged:];
-[CBPeripheralManager startAdvertising:];
-[CBPeripheralManager handleConnectionParametersUpdated:];
-[CBPeripheralManager isMsgAllowedAlways:];
-[CBPeripheralManager initWithDelegate:queue:options:];
-[CBPeripheralManager handleMsg:args:];
-[CBPeripheralManager setOfflineAdvertisingParamsAndData:];
-[CBPeripheralManager l2capChannelForPeer:withPsm:];
-[CBPeripheralManager forEachCentral:];
-[CBPeripheralManager removeAllServices];
-[CBPeripheralManager observeValueForKeyPath:ofObject:change:context:];
-[CBPeripheralManager services];
-[CBPeripheralManager l2capChannelForPeer:withCID:];
-[CBPeripheralManager centralWithIdentifier:];
-[CBPeripheralManager waitingForReady];
-[CBPeripheralManager handleGetAttributeValue:];
-[CBPeripheralManager setConnectionOptions:forPeer:];
-[CBPeripheralManager unpublishL2CAPChannel:];
-[CBPeripheralManager init];
-[CBPeripheralManager isMsgAllowedWhenOff:];
-[CBPeripheralManager initWithDelegate:queue:];
-[CBPeripheralManager publishL2CAPChannel:requiresEncryption:options:];
-[CBPeripheralManager handleServiceAdded:];
-[CBPeripheralManager setCisPeripheralDisconnectEvent:];
-[CBPeripheralManager setIsAdvertising:];
-[CBPeripheralManager addXPCDelayTiming:args:];
-[CBPeripheralManager dealloc];
-[CBPeripheralManager peerWithInfo:];
-[CBPeripheralManager incomingAddress:];
-[CBPeripheralManager retrieveBluetoothUsageStatistics:completion:];
-[CBPeripheralManager handleL2CAPChannelUnpublished:];
-[CBPeripheralManager handlePeriodicAdvertisingStopped:];
-[CBPeripheralManager setCisPeripheralConnectEvent:];
-[CBPeripheralManager l2capChannels];
-[CBPeripheralManager setAttributeIDGenerator:];
-[CBPeripheralManager handleNotificationAdded:];
-[CBPeripheralManager handleSupportedFeatures:];
-[CBPeripheralManager handleAdvertisingStarted:];
-[CBPeripheralManager removeService:];
-[CBPeripheralManager handleL2CAPChannelOpened:];
-[CBPeripheralManager handleSolicitedServicesFound:];
-[CBPeripheralManager refreshNonConnectableIdentity];
-[CBPeripheralManager handleAdvertisingStopped:];
-[CBPeripheralManager updateValue:forCharacteristic:onSubscribedCentrals:];
-[CBPeripheralManager setIncomingConnectionRequestCompletion:];
-[CBPeripheralManager handleSetAttributeValues:];
-[CBPeripheralManager handleL2CAPChannelClosed:];
-[CBPeripheralManager isAdvertising];
-[CBPeripheralManager setDelegate:];
-[CBPeripheralManager handleCSProcedureEventMsg:];
-[CBPeripheralManager attributeIDGenerator];
-[CBPeripheralManager initCISPeripheral:completion:];
-[CBPeripheralManager publishL2CAPChannel:requiresEncryption:priority:];
-[CBPeripheralManager setDesiredConnectionLatency:forCentral:];
-[CBPeripheralManager HandleOfflineAdvPayloadRequestedWithReason:];
-[CBPeripheralManager handleL2CAPChannelDidReceiveData:];
-[CBPeripheralManager incomingConnectionRequestCompletion];
-[CBPeripheralManager centralWithInfo:];
-[CBPeripheralManager respondToRequest:withResult:];
-[CBPeripheralManager publishL2CAPChannel:requiresEncryption:];
-[CBPeripheralManager stopAdvertising];
-[CBPeripheralManager handleCentralDidUpdateANCSAuthorization:];
-[CBPeripheralManager publishPacketL2CAPChannel:requiresEncryption:withIncomingMTU:options:];
-[CBPeripheralManager updateLock];
-[CBPeripheralManager delegate];
-[CBPeripheralManager cisPeripheralConnectEvent];
-[CBPeripheralManager addressRotationState:];
-[CBPeripheralManager getNonConnectableIdentity];
-[CBPeripheralManager handleConnectCISPeripheralComplete:];
-[CBPeripheralManager cisPeripheralDisconnectEvent];
-[CBPeripheralManager removeAllL2CAPChannels];
-[CBPeripheralManager handleDisconnectCISPeripheralComplete:];
-[CBPeripheralManager multipleAdvertisingSupported];
-[CBPeripheralManager setMultipleAdvertisingSupported:];
-[CBPeripheralManager requestStableAddress:];
-[CBPeripheralManager supportsMultipleAdvertising];
-[CBPeripheralManager handleNotificationRemoved:];
-[CBPeripheralManager overrideLocalLeAddress:];
-[CBPeripheralManager disconnectCISPeripheral:];
-[CBPeripheralManager centrals];
-[CBPeripheralManager publishL2CAPChannelWithEncryption:];
-[CBPeripheralManager startPeriodicAdvertising:];
-[CBPeripheralManager respondToCISConnectionRequest:];
-[CBPeripheralManager respondToTransaction:value:attributeID:result:];
-[CBPeripheralManager readyForUpdates];
-[CBPeripheralManager stopPeriodicAdvertising:];
-[CBPeripheralManager handleL2CAPChannelPublished:];
-[CBPeripheralManager publishL2CAPChannelWithEncryption:priority:];
-[CBPeripheralManager handlePeriodicAdvertisingStarted:];
-[CBPeripheralManager characteristicIDs];
-[CBPeripheralManager HandleControllerPeripheralBTClockUpdateMsg:];
-[CBPeripheralManager startAdvertisingForUsecase:withOptions:];
-[CBPeripheralManager handleIncomingCISConnectionRequest:];
-[CBPeripheralManager addService:];
```
