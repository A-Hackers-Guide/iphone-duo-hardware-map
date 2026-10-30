# `AccessoryTransportPluginNFC`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/NFC.transport/NFC`](../userland/System__Library__CoreAccessories__PlugIns__Transports__NFC.transport__NFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ACCTransportPlugin`
- Protocols: `ACCTransportPluginProtocol`
- 21 instance variables, 6 properties, 39 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _tagForConnectionUuid;
@"NSMutableDictionary" _connectionUuidForEndpointUuid;
{timespec="tv_sec"q"tv_nsec"q} _tagsArrivalTime;
@"NFAccessoryReaderSession" _readerSession;
@"NSArray" _polledTags;
@"NSObject<OS_dispatch_semaphore>" _polledSem;
@"NFACTag" _connectedTag;
@"NSData" _connectedTagId;
@"NSString" _connectedTagEndpointUuid;
@"NSMutableArray" _requestedOpenEndpointUUID;
@"NSDate" _lastRequestPowerPauseTime;
i _screenStateToken;
i _screenState;
i _proximityOcclusionState;
{timespec="tv_sec"q"tv_nsec"q} _proxRequestTime;
^{__IOHIDEventSystemClient=} _hidEventClient;
B _waitProxState;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_xpc_object>" _listenerConnection;
@"NSMutableArray" _peers;
B _isRunning;
```

## Properties

```
@property (TB,N,V_isRunning) isRunning;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,N) pluginName;
```

## Instance methods

```
-[AccessoryTransportPluginNFC isRunning];
-[AccessoryTransportPluginNFC stopPlugin];
-[AccessoryTransportPluginNFC pluginName];
-[AccessoryTransportPluginNFC sendOutgoingData:forEndpointWithUUID:connectionUUID:];
-[AccessoryTransportPluginNFC startPlugin];
-[AccessoryTransportPluginNFC initPlugin];
-[AccessoryTransportPluginNFC setIsRunning:];
-[AccessoryTransportPluginNFC readerSession:didDetectTags:];
-[AccessoryTransportPluginNFC readerSessionDidEndUnexpectedly:];
-[AccessoryTransportPluginNFC propertiesDidChange:forEndpointWithUUID:previousProperties:connectionUUID:];
-[AccessoryTransportPluginNFC _checkProductTypeCompatibility:];
-[AccessoryTransportPluginNFC _checkLRC:];
-[AccessoryTransportPluginNFC _connectPeer:];
-[AccessoryTransportPluginNFC _setProximityMonitoringEnabled:];
-[AccessoryTransportPluginNFC _animationDelayMs:];
-[AccessoryTransportPluginNFC _closeReaderSession];
-[AccessoryTransportPluginNFC _connectToTagId:];
-[AccessoryTransportPluginNFC _createEndpointsForTags:skipWalletAuth:];
-[AccessoryTransportPluginNFC _decodeTagIdentifier:];
-[AccessoryTransportPluginNFC _didNfcTagsListChange:];
-[AccessoryTransportPluginNFC _didScreenStateChange:];
-[AccessoryTransportPluginNFC _getAccessoryFamily:];
-[AccessoryTransportPluginNFC _getAccessoryType:];
-[AccessoryTransportPluginNFC _getNfcStateMachineState];
-[AccessoryTransportPluginNFC _getTimeSinceLastRequestPowerPauseMs];
-[AccessoryTransportPluginNFC _getpowerPauseStatus];
-[AccessoryTransportPluginNFC _handleIOHIDEvent:];
-[AccessoryTransportPluginNFC _handleNearFieldAccessoryEventNotification:];
-[AccessoryTransportPluginNFC _handleSessionOpen:forEndpointWithUUID:connectionUUID:];
-[AccessoryTransportPluginNFC _hasWalletOnClearCase2020:];
-[AccessoryTransportPluginNFC _initXPC];
-[AccessoryTransportPluginNFC _notifyAuthReadyAfterPowerPauseComplete];
-[AccessoryTransportPluginNFC _pollTags:];
-[AccessoryTransportPluginNFC _requestPowerPause];
-[AccessoryTransportPluginNFC _requiresLegacyAuth:];
-[AccessoryTransportPluginNFC _requiresMfi40Auth:];
-[AccessoryTransportPluginNFC _setScreenStateMonitoringEnabled:];
-[AccessoryTransportPluginNFC _tagsHavePowerBits:uuid:];
-[AccessoryTransportPluginNFC _updateAccessoryPower:];
```
