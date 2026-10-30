# `CWFCloudSyncManager`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 9 properties, 40 instance methods, 0 class methods

## Instance variables

```
@"CWFKeyValueStore" _cloudKVS;
@"NSObject<OS_dispatch_queue>" _internalQueue;
i _cloudKeychainSyncStateNotifyToken;
@"NSObject<OS_dispatch_source>" _checkCloudKeychainStateRetryTimer;
i _keychainChangedNotifyToken;
@"NSObject<OS_dispatch_source>" _checkKeychainTimer;
Q _keychainChangeCounter;
B _waitingForNextKeychainChangeEvent;
Q _checkKeychainTimestamp;
@"NSMutableDictionary" _waitingForKeychainCounterMap;
@"NSMutableDictionary" _waitingForKeychainNetworkMap;
C _cloudKeychainEnabled;
@"NSObject<OS_dispatch_queue>" _targetQueue;
@? _allowCloudSyncableNetworkHandler;
@? _rememberLocalNetworkHandler;
@? _forgetLocalNetworkHandler;
@? _fetchAllLocalNetworksHandler;
@? _hasKeychainPasswordHandler;
```

## Properties

```
@property (TC,V_cloudKeychainEnabled) cloudKeychainEnabled;
@property (T@"NSObject<OS_dispatch_queue>",&,V_targetQueue) targetQueue;
@property (T@"NSDictionary",R,C) cloudKVS;
@property (T@"NSArray",R,C) cloudNetworks;
@property (T@?,C,V_allowCloudSyncableNetworkHandler) allowCloudSyncableNetworkHandler;
@property (T@?,C,V_rememberLocalNetworkHandler) rememberLocalNetworkHandler;
@property (T@?,C,V_forgetLocalNetworkHandler) forgetLocalNetworkHandler;
@property (T@?,C,V_fetchAllLocalNetworksHandler) fetchAllLocalNetworksHandler;
@property (T@?,C,V_hasKeychainPasswordHandler) hasKeychainPasswordHandler;
```

## Instance methods

```
-[CWFCloudSyncManager cloudNetworks];
-[CWFCloudSyncManager allowCloudSyncableNetworkHandler];
-[CWFCloudSyncManager setAllowCloudSyncableNetworkHandler:];
-[CWFCloudSyncManager setTargetQueue:];
-[CWFCloudSyncManager targetQueue];
-[CWFCloudSyncManager init];
-[CWFCloudSyncManager invalidate];
-[CWFCloudSyncManager activate];
-[CWFCloudSyncManager __localDeviceVersionDescription];
-[CWFCloudSyncManager setRememberLocalNetworkHandler:];
-[CWFCloudSyncManager __calloutToCheckForKeychainPasswordWithNetworkProfile:error:];
-[CWFCloudSyncManager __calloutToCheckIfNetworkIsSyncable:];
-[CWFCloudSyncManager __calloutToFetchAllLocalNetworksAndReturnError:];
-[CWFCloudSyncManager __checkCloudKeychainSyncState];
-[CWFCloudSyncManager __checkWaitingForKeychainPasswordList];
-[CWFCloudSyncManager __cloudKeyForNetworkProfile:];
-[CWFCloudSyncManager __cloudNetworkProfiles];
-[CWFCloudSyncManager __handleCloudKVSChangedKeys:];
-[CWFCloudSyncManager __handleKeychainChangeEvent];
-[CWFCloudSyncManager __isCloudKeychainEnabled];
-[CWFCloudSyncManager __localDeviceModel];
-[CWFCloudSyncManager __resetCheckKeychainCounterForRecentlyJoinedNetworks];
-[CWFCloudSyncManager __startMonitoringCloudKeychainSyncStateEvents];
-[CWFCloudSyncManager __startMonitoringKeychainChangeEvents];
-[CWFCloudSyncManager __stopMonitoringCloudKeychainSyncStateEvents];
-[CWFCloudSyncManager __stopMonitoringKeychainChangeEvents];
-[CWFCloudSyncManager __synchronizeWithLocalNetworks];
-[CWFCloudSyncManager __updateCloudNetwork:error:];
-[CWFCloudSyncManager cloudKVS];
-[CWFCloudSyncManager cloudKeychainEnabled];
-[CWFCloudSyncManager fetchAllLocalNetworksHandler];
-[CWFCloudSyncManager forgetCloudNetwork:error:];
-[CWFCloudSyncManager forgetLocalNetworkHandler];
-[CWFCloudSyncManager hasKeychainPasswordHandler];
-[CWFCloudSyncManager rememberCloudNetwork:error:];
-[CWFCloudSyncManager rememberLocalNetworkHandler];
-[CWFCloudSyncManager setCloudKeychainEnabled:];
-[CWFCloudSyncManager setFetchAllLocalNetworksHandler:];
-[CWFCloudSyncManager setForgetLocalNetworkHandler:];
-[CWFCloudSyncManager setHasKeychainPasswordHandler:];
```
