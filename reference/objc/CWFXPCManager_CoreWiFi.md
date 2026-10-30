# `CWFXPCManager`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CWFXPCListenerDelegate`, `CWFXPCRequestProxyDelegate`
- 13 instance variables, 15 properties, 52 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _mutexQueue;
@"NSMutableArray" _mutableXPCListeners;
@"CWFXPCRequestProxy" _XPCRequestProxy;
@"RBSProcessMonitor" _processMonitor;
@"NSMutableSet" _processMonitorPIDs;
@"NSMutableSet" _processMonitorBundleIDs;
i _notifyKeybagLockStatusToken;
@"CWFWiFiUserAgent" _wifiUserAgent;
@"<CWFXPCManagerDelegate>" _delegate;
@"NSSet" _supportedRequestTypes;
@? _allowCloudSyncableNetworkHandler;
@? _allowNearbySyncableNetworkHandler;
@? _getAdaptiveInterfaceRankDurationHandler;
```

## Properties

```
@property (T@"<CWFXPCManagerDelegate>",&,V_delegate) delegate;
@property (T@"NSSet",C,V_supportedRequestTypes) supportedRequestTypes;
@property (T@"CWFAutoJoinManager",R) autoJoinManager;
@property (T@"CWFAutoJoinManager",R) autoJoinManagerCached;
@property (T@"CWFPrivateMACManager",R,D) privateMACManager;
@property (T@"CWFWiFiNetworkSharingManager",R) wifiNetworkSharingManager;
@property (T@"CLLocation",C) location;
@property (T@"CWFScanResult",C) associatedNetwork;
@property (T@?,C,V_allowCloudSyncableNetworkHandler) allowCloudSyncableNetworkHandler;
@property (T@?,C,V_allowNearbySyncableNetworkHandler) allowNearbySyncableNetworkHandler;
@property (T@?,C,V_getAdaptiveInterfaceRankDurationHandler) getAdaptiveInterfaceRankDurationHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CWFXPCManager sendXPCEvent:reply:];
-[CWFXPCManager setDurationForJoinPMAssertion:];
-[CWFXPCManager setTargetQueue:requestType:interfaceName:];
-[CWFXPCManager wifiNetworkSharingManager];
-[CWFXPCManager autoJoinManagerCached];
-[CWFXPCManager registeredEventIDs];
-[CWFXPCManager associatedNetwork];
-[CWFXPCManager privateMACManager];
-[CWFXPCManager autoJoinManager];
-[CWFXPCManager setAssociatedNetwork:];
-[CWFXPCManager registeredActivities];
-[CWFXPCManager setSupportedRequestTypes:];
-[CWFXPCManager allowCloudSyncableNetworkHandler];
-[CWFXPCManager setAllowCloudSyncableNetworkHandler:];
-[CWFXPCManager setAllowNearbySyncableNetworkHandler:];
-[CWFXPCManager __wifiNetworkSharingAppXPCConnectionWithBundleID:];
-[CWFXPCManager suspend];
-[CWFXPCManager XPCListener:XPCConnection:receivedXPCRequest:];
-[CWFXPCManager __updateProcessMonitorConfiguration];
-[CWFXPCManager init];
-[CWFXPCManager __checkKeybagLockStatus];
-[CWFXPCManager location];
-[CWFXPCManager __stopMonitoringKeybagLockStatus];
-[CWFXPCManager XPCRequestProxy:getAdaptiveInterfaceRankDurationAndReply:];
-[CWFXPCManager XPCRequestProxy:sendXPCEvent:reply:];
-[CWFXPCManager __startMonitoringKeybagLockStatus];
-[CWFXPCManager XPCListener:XPCConnection:completedXPCRequest:];
-[CWFXPCManager XPCRequestProxy:invalidatedXPCConnection:];
-[CWFXPCManager setGetAdaptiveInterfaceRankDurationHandler:];
-[CWFXPCManager invalidate];
-[CWFXPCManager XPCListener:addedXPCConnection:];
-[CWFXPCManager setDelegate:];
-[CWFXPCManager initWithServiceTypes:];
-[CWFXPCManager setLocation:];
-[CWFXPCManager XPCRequestProxy:XPCConnection:receivedXPCRequest:];
-[CWFXPCManager endpointWithServiceType:];
-[CWFXPCManager XPCListener:invalidatedXPCConnection:];
-[CWFXPCManager XPCRequestProxy:XPCConnection:canceledXPCRequestsWithUUID:];
-[CWFXPCManager activate];
-[CWFXPCManager localXPCClientWithServiceType:];
-[CWFXPCManager delegate];
-[CWFXPCManager __wifiNetworkSharingUIServiceXPCConnection];
-[CWFXPCManager __wifiUserAgentXPCConnection];
-[CWFXPCManager __wifiNetworkSharingAppexXPCConnections];
-[CWFXPCManager allowNearbySyncableNetworkHandler];
-[CWFXPCManager getAdaptiveInterfaceRankDurationHandler];
-[CWFXPCManager supportedRequestTypes];
-[CWFXPCManager XPCListener:XPCConnection:updatedRegisteredEventIDs:];
-[CWFXPCManager XPCListener:XPCConnection:canceledXPCRequestsWithUUID:];
-[CWFXPCManager XPCListener:XPCConnection:updatedProcessState:];
-[CWFXPCManager __updateProcessStateForXPCConnection:];
-[CWFXPCManager resume];
```
