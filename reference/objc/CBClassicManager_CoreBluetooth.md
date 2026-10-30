# `CBClassicManager`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBManager`
- 15 instance variables, 15 properties, 69 instance methods, 0 class methods

## Instance variables

```
B _inquiryState;
B _discoverable;
B _connectable;
B _isInquiryRunning;
B _testMode;
@? _connectCallback;
@? _disconnectCallback;
@? _serviceAddedHandler;
@? _inquiryServiceAddedHandler;
@"NSMapTable" _peers;
q _powerState;
@? _classicPeerDiscovered;
@? _sdpRecordAddedHandler;
@? _pairingStatusHandler;
@? _connectionStatusHandler;
```

## Properties

```
@property (T@"NSMapTable",R,&,N,V_peers) peers;
@property (TB,R,N,V_isInquiryRunning) isInquiryRunning;
@property (TB,R,V_inquiryState) inquiryState;
@property (TB,R,V_discoverable) discoverable;
@property (TB,R,V_connectable) connectable;
@property (Tq,R,V_powerState) powerState;
@property (TB,N,V_testMode) testMode;
@property (T@?,C,V_classicPeerDiscovered) classicPeerDiscovered;
@property (T@?,C,V_sdpRecordAddedHandler) sdpRecordAddedHandler;
@property (T@?,C,V_pairingStatusHandler) pairingStatusHandler;
@property (T@?,C,V_connectionStatusHandler) connectionStatusHandler;
@property (T@?,C,V_connectCallback) connectCallback;
@property (T@?,C,V_disconnectCallback) disconnectCallback;
@property (T@?,C,V_serviceAddedHandler) serviceAddedHandler;
@property (T@?,C,V_inquiryServiceAddedHandler) inquiryServiceAddedHandler;
```

## Instance methods

```
-[CBClassicManager peers];
-[CBClassicManager isMsgAllowedAlways:];
-[CBClassicManager connectable];
-[CBClassicManager inquiryState];
-[CBClassicManager handleMsg:args:];
-[CBClassicManager removeAACPClient:];
-[CBClassicManager cancelPeerConnection:force:];
-[CBClassicManager powerState];
-[CBClassicManager setSdpRecordAddedHandler:];
-[CBClassicManager testMode];
-[CBClassicManager removeAllServices];
-[CBClassicManager handleServiceAddedToInquiryList:];
-[CBClassicManager observeValueForKeyPath:ofObject:change:context:];
-[CBClassicManager serviceAddedHandler];
-[CBClassicManager startInquiryWithOptions:classicPeerDiscovered:];
-[CBClassicManager discoverable];
-[CBClassicManager sendLocalDeviceStateRequest];
-[CBClassicManager addServiceWithData:];
-[CBClassicManager isMsgAllowedWhenOff:];
-[CBClassicManager handlePeerDiscovered:];
-[CBClassicManager setInquiryServiceAddedHandler:];
-[CBClassicManager handleLocalDeviceStateUpdatedMsg:];
-[CBClassicManager setDisconnectCallback:];
-[CBClassicManager setPairingStatusHandler:];
-[CBClassicManager removeAllServicesFromInquiryList];
-[CBClassicManager sdpRecordAddedHandler];
-[CBClassicManager stopInquiry];
-[CBClassicManager handleServiceAddedToSDP:];
-[CBClassicManager dealloc];
-[CBClassicManager peerWithInfo:];
-[CBClassicManager orphanClassicPeers];
-[CBClassicManager setBTConnectable:];
-[CBClassicManager addAACPClient:aacpClientAdded:];
-[CBClassicManager handlePeerConnectionStateUpdated:];
-[CBClassicManager removeService:];
-[CBClassicManager classicPeerDiscovered];
-[CBClassicManager initWithQueue:options:];
-[CBClassicManager classicPeerWithInfo:];
-[CBClassicManager connectionStatusHandler];
-[CBClassicManager disconnectCallback];
-[CBClassicManager removeServiceHandle:];
-[CBClassicManager setTestMode:];
-[CBClassicManager cancelPeerConnection:options:];
-[CBClassicManager setConnectCallback:];
-[CBClassicManager handleSDPRecordAdded:];
-[CBClassicManager retrievePairedPeersWithOptions:];
-[CBClassicManager forEachClassicPeer:];
-[CBClassicManager cancelPeerConnection:];
-[CBClassicManager addServiceToInquiryList:];
-[CBClassicManager isInquiryRunning];
-[CBClassicManager secureBluetooth:withAuthData:];
-[CBClassicManager addService:sdpRecord:sdpRecordAddedHandler:];
-[CBClassicManager setClassicPeerDiscovered:];
-[CBClassicManager setBTPowerState:];
-[CBClassicManager getLocalSDPDatabase];
-[CBClassicManager peerWithIdentifier:];
-[CBClassicManager setBTDiscoverable:];
-[CBClassicManager pairingStatusHandler];
-[CBClassicManager connectPeer:options:];
-[CBClassicManager handlePeerDisconnectionCompleted:];
-[CBClassicManager removeServiceFromInquiryList:];
-[CBClassicManager alertUserNotificationIsReady:];
-[CBClassicManager retrievePeerWithAddress:];
-[CBClassicManager setConnectionStatusHandler:];
-[CBClassicManager connectCallback];
-[CBClassicManager inquiryServiceAddedHandler];
-[CBClassicManager setServiceAddedHandler:];
-[CBClassicManager handlePeerConnectionCompleted:];
-[CBClassicManager addService:];
```
