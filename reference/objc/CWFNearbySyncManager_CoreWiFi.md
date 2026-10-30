# `CWFNearbySyncManager`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 19 instance variables, 9 properties, 51 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _internalQueue;
@"RPCompanionLinkClient" _rapportDiscoveryClient;
i _cloudKeychainSyncStateNotifyToken;
@"NSObject<OS_dispatch_source>" _checkCloudKeychainStateRetryTimer;
@"CWFNearbySyncNetwork" _nearbySyncNetwork;
@"NSMutableDictionary" _nearbySyncRequestHistory;
@"NSMutableDictionary" _failedNearbySyncRequestHistory;
@"NSMutableDictionary" _cachedBBHStateMap;
@"NSMutableDictionary" _cachedBBHTimestampMap;
@"NSOperationQueue" _rapportRequestQueue;
i _eligibilityNotifyToken;
C _cloudKeychainEnabled;
C _associationState;
B _activated;
@"NSObject<OS_dispatch_queue>" _targetQueue;
@? _allowNearbySyncableNetworkHandler;
@? _autoJoinAssistEventHandler;
@? _restoredBackhaulEventHandler;
@? _confirmBrokenBackhaulHandler;
```

## Properties

```
@property (TC,V_cloudKeychainEnabled) cloudKeychainEnabled;
@property (TC,V_associationState) associationState;
@property (TB,V_activated) activated;
@property (T@"NSObject<OS_dispatch_queue>",&,V_targetQueue) targetQueue;
@property (T@"CWFNearbySyncNetwork",C,D) nearbySyncNetwork;
@property (T@?,C,V_allowNearbySyncableNetworkHandler) allowNearbySyncableNetworkHandler;
@property (T@?,C,V_autoJoinAssistEventHandler) autoJoinAssistEventHandler;
@property (T@?,C,V_restoredBackhaulEventHandler) restoredBackhaulEventHandler;
@property (T@?,C,V_confirmBrokenBackhaulHandler) confirmBrokenBackhaulHandler;
```

## Instance methods

```
-[CWFNearbySyncManager setTargetQueue:];
-[CWFNearbySyncManager targetQueue];
-[CWFNearbySyncManager setAllowNearbySyncableNetworkHandler:];
-[CWFNearbySyncManager setActivated:];
-[CWFNearbySyncManager init];
-[CWFNearbySyncManager invalidate];
-[CWFNearbySyncManager activate];
-[CWFNearbySyncManager allowNearbySyncableNetworkHandler];
-[CWFNearbySyncManager activated];
-[CWFNearbySyncManager __rapportClientTargetingDevice:];
-[CWFNearbySyncManager __purgeBBHCache];
-[CWFNearbySyncManager __calloutToCheckIfNetworkIsSyncable:];
-[CWFNearbySyncManager __checkCloudKeychainSyncState];
-[CWFNearbySyncManager __deviceSupportsNearbyBBHConfirmRequests:];
-[CWFNearbySyncManager __deviceSupportsNearbySyncRequests:];
-[CWFNearbySyncManager __failedNearbyNetworkSyncRequestTimestampForDevice:network:];
-[CWFNearbySyncManager __handleAutoJoinAssistPayload:options:];
-[CWFNearbySyncManager __handleBrokenBackhaulRestoreEvent:options:];
-[CWFNearbySyncManager __isCloudKeychainEnabled];
-[CWFNearbySyncManager __nearbyNetworkSyncRequestTimestampForDevice:network:];
-[CWFNearbySyncManager __respondToAutoJoinAssistRequest:options:responseHandler:];
-[CWFNearbySyncManager __respondToConfirmBrokenBackhaulRequest:options:responseHandler:];
-[CWFNearbySyncManager __respondToNeedsConnectivityRequest:options:responseHandler:];
-[CWFNearbySyncManager __sendAutoJoinAssistRequestToAllNearbyDevices];
-[CWFNearbySyncManager __sendAutoJoinAssistRequestToNearbyDevice:retryCount:];
-[CWFNearbySyncManager __sendBrokenBackhaulRestoreEventToAllNearbyDevices];
-[CWFNearbySyncManager __sendBrokenBackhaulRestoreEventToNearbyDevice:];
-[CWFNearbySyncManager __sendConfirmBrokenBackhaulRequestToAllNearbyDevicesWithTimeout:count:network:minimumCacheTimestamp:completion:];
-[CWFNearbySyncManager __sendConfirmBrokenBackhaulRequestToNearbyDevice:timeout:count:network:minimumCacheTimestamp:completion:];
-[CWFNearbySyncManager __sendNeedsConnectivityRequestToAllNearbyDevices];
-[CWFNearbySyncManager __sendNeedsConnectivityRequestToNearbyDevice:retryCount:];
-[CWFNearbySyncManager __setupRapportDiscoveryClient];
-[CWFNearbySyncManager __startMonitoringCloudKeychainSyncStateEvents];
-[CWFNearbySyncManager __startMonitoringOSEligibility];
-[CWFNearbySyncManager __stopMonitoringCloudKeychainSyncStateEvents];
-[CWFNearbySyncManager __stopMonitoringOSEligibility];
-[CWFNearbySyncManager __updateFailedNearbyNetworkSyncRequestTimestampForDevice:network:];
-[CWFNearbySyncManager __updateNearbyNetworkSyncRequestTimestampForDevice:network:];
-[CWFNearbySyncManager associationState];
-[CWFNearbySyncManager autoJoinAssistEventHandler];
-[CWFNearbySyncManager cloudKeychainEnabled];
-[CWFNearbySyncManager confirmBrokenBackhaulHandler];
-[CWFNearbySyncManager nearbyConfirmBrokenBackhaulUsingTimeout:count:network:minimumCacheTimestamp:completion:];
-[CWFNearbySyncManager nearbySyncNetwork];
-[CWFNearbySyncManager restoredBackhaulEventHandler];
-[CWFNearbySyncManager setAssociationState:];
-[CWFNearbySyncManager setAutoJoinAssistEventHandler:];
-[CWFNearbySyncManager setCloudKeychainEnabled:];
-[CWFNearbySyncManager setConfirmBrokenBackhaulHandler:];
-[CWFNearbySyncManager setNearbySyncNetwork:];
-[CWFNearbySyncManager setRestoredBackhaulEventHandler:];
```
