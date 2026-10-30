# `ACCiAP2ShimServer`

- Image: [`/System/Library/PrivateFrameworks/AccessoryiAP2Shim.framework/AccessoryiAP2Shim`](../userland/System__Library__PrivateFrameworks__AccessoryiAP2Shim.framework__AccessoryiAP2Shim.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 12 properties, 63 instance methods, 7 class methods

## Instance variables

```
B _isShuttingDown;
{__serverFlags="deathBecomesUs"b1"serverExiting"b1"reserved"b30} _serverFlags;
i _iap2AvailableNotifyToken;
@"NSMutableDictionary" _delegateList;
@"NSMutableDictionary" _accessoryViaKeyUIDList;
@"NSMutableDictionary" _accessoryViaConnectionIDList;
@"NSObject<OS_dispatch_queue>" _listQueue;
@"NSObject<OS_xpc_object>" _listener;
@"NSObject<OS_dispatch_queue>" _iap2dhighPriorityRootQueue;
@"NSObject<OS_dispatch_queue>" _internalListenerQueue;
@"NSMutableDictionary" _clients;
@"NSLock" _clientLock;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_delegateList) delegateList;
@property (T@"NSMutableDictionary",&,N,V_accessoryViaKeyUIDList) accessoryViaKeyUIDList;
@property (T@"NSMutableDictionary",&,N,V_accessoryViaConnectionIDList) accessoryViaConnectionIDList;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_listQueue) listQueue;
@property (T@"NSObject<OS_xpc_object>",R,N,V_listener) listener;
@property (TB,R,N,V_isShuttingDown) isShuttingDown;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_iap2dhighPriorityRootQueue) iap2dhighPriorityRootQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_internalListenerQueue) internalListenerQueue;
@property (T{__serverFlags=b1b1b30},R,V_serverFlags) serverFlags;
@property (T@"NSMutableDictionary",R,V_clients) clients;
@property (T@"NSLock",R,V_clientLock) clientLock;
@property (Ti,R,V_iap2AvailableNotifyToken) iap2AvailableNotifyToken;
```

## Class methods

```
+[ACCiAP2ShimServer sharedInstance];
+[ACCiAP2ShimServer markClientAsInterestedInBleNotifications:];
+[ACCiAP2ShimServer notifyInterestedClientsOfACCBLEAccessoryEvent:withPayload:];
+[ACCiAP2ShimServer postNotifydNotificationType:];
+[ACCiAP2ShimServer resetServerState];
+[ACCiAP2ShimServer postNSDistributeNotificationType:notifyDict:];
+[ACCiAP2ShimServer stringForClientID:];
```

## Instance methods

```
-[ACCiAP2ShimServer clients];
-[ACCiAP2ShimServer removeDelegate:];
-[ACCiAP2ShimServer removeAllClients];
-[ACCiAP2ShimServer addDelegate:];
-[ACCiAP2ShimServer init];
-[ACCiAP2ShimServer dealloc];
-[ACCiAP2ShimServer addAccessory:];
-[ACCiAP2ShimServer listener];
-[ACCiAP2ShimServer _addDelegate:];
-[ACCiAP2ShimServer _startServer];
-[ACCiAP2ShimServer serverFlags];
-[ACCiAP2ShimServer removeAccessory:];
-[ACCiAP2ShimServer stopServer];
-[ACCiAP2ShimServer _removeDelegate:];
-[ACCiAP2ShimServer isShuttingDown];
-[ACCiAP2ShimServer startServer];
-[ACCiAP2ShimServer delegateList];
-[ACCiAP2ShimServer setDelegateList:];
-[ACCiAP2ShimServer listQueue];
-[ACCiAP2ShimServer clientLock];
-[ACCiAP2ShimServer _addAccessory:];
-[ACCiAP2ShimServer _removeAccessory:];
-[ACCiAP2ShimServer findAccessoryForAccessoryUID:andKeyTag:];
-[ACCiAP2ShimServer addClientWithCapabilities:auditToken:currentClientID:xpcConnection:eaProtocols:notifyOfAlreadyConnectedAccessories:andBundleId:];
-[ACCiAP2ShimServer _attachAccessory:];
-[ACCiAP2ShimServer _detachAccessory:];
-[ACCiAP2ShimServer _findAccessoryForAccessoryUID:andKeyTag:];
-[ACCiAP2ShimServer _findAccessoryForConnectionID:];
-[ACCiAP2ShimServer _findAccessoryForConnectionID:andKeyTag:];
-[ACCiAP2ShimServer _iterateAccessories:];
-[ACCiAP2ShimServer _iterateDelegates:];
-[ACCiAP2ShimServer _pollForDeathAfterPromptCompletes];
-[ACCiAP2ShimServer _resetServerState];
-[ACCiAP2ShimServer _stopServer];
-[ACCiAP2ShimServer _takeClientAssertionsForAccessoryConnection];
-[ACCiAP2ShimServer _takeClientAssertionsForAccessoryDisconnection];
-[ACCiAP2ShimServer accessoryViaConnectionIDList];
-[ACCiAP2ShimServer accessoryViaKeyUIDList];
-[ACCiAP2ShimServer findAccessoryForConnectionID:];
-[ACCiAP2ShimServer findAccessoryForConnectionID:andKeyTag:];
-[ACCiAP2ShimServer findClientWithID:];
-[ACCiAP2ShimServer findClientWithXPCConnection:];
-[ACCiAP2ShimServer generateClientID];
-[ACCiAP2ShimServer iap2AvailableNotifyToken];
-[ACCiAP2ShimServer iap2dhighPriorityRootQueue];
-[ACCiAP2ShimServer internalListenerQueue];
-[ACCiAP2ShimServer iterateAccessoriesAsync:];
-[ACCiAP2ShimServer iterateAccessoriesSync:];
-[ACCiAP2ShimServer iterateDelegatesAsync:];
-[ACCiAP2ShimServer iterateDelegatesSync:];
-[ACCiAP2ShimServer notifyEAClient:ofAccessoryEvent:accessory:];
-[ACCiAP2ShimServer notifyEAClientsOfAccessoryConnection:];
-[ACCiAP2ShimServer notifyEAClientsOfAccessoryDisconnection:];
-[ACCiAP2ShimServer notifyEAClientsOfAccessoryEvent:accessory:];
-[ACCiAP2ShimServer notifyEAClientsOfAccessoryReconnection:];
-[ACCiAP2ShimServer processDetachXPCConnection:];
-[ACCiAP2ShimServer processXPCMessage:connection:];
-[ACCiAP2ShimServer removeClientForXPCConnection:];
-[ACCiAP2ShimServer removeClientWithID:];
-[ACCiAP2ShimServer sendToClient:notification:withPayload:];
-[ACCiAP2ShimServer sendToInterestedClientsACCBLENotification:withPayload:];
-[ACCiAP2ShimServer setAccessoryViaConnectionIDList:];
-[ACCiAP2ShimServer setAccessoryViaKeyUIDList:];
```
