# `PLClientLogger`

- Image: [`/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog`](../userland/System__Library__PrivateFrameworks__PowerLog.framework__PowerLog.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 26 instance variables, 26 properties, 79 instance methods, 2 class methods

## Instance variables

```
B _clientDebug;
B _talkToPowerlogHelper;
B _batchedTimerInFlight;
B _forceBatching;
B _batchDropMessages;
B _hasSeenFirstDrop;
i _batchMessagesSentCount;
i _batchedDropMessageCount;
i _hourlyDropCount;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"NSObject<OS_dispatch_queue>" _batchFlushQueue;
@"NSString" _processName;
@"NSMutableDictionary" _permissionCache;
@"NSMutableDictionary" _pendingTaskCache;
@"NSMutableArray" _batchedTaskCache;
@"NSMutableDictionary" _dynamicCache;
@"NSMutableDictionary" _eventFilterSaved;
@"NSObject<OS_dispatch_queue>" _xpcConnectionQueue;
@"NSObject<OS_dispatch_queue>" _xpcConnectionHelperQueue;
@"NSObject<OS_xpc_object>" _xpcConnection;
@"NSObject<OS_xpc_object>" _xpcConnectionHelper;
@"NSSet" _batchingClientAllowlist;
@"NSSet" _curatedBatchingList;
@"NSSet" _batchingKeysAllowlist;
d _hourlyWindowStart;
@"NSObject<OS_dispatch_queue>" _adaptivePermissionWorkQueue;
```

## Properties

```
@property (TB,V_clientDebug) clientDebug;
@property (T@"NSObject<OS_dispatch_queue>",&,V_workQueue) workQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,V_batchFlushQueue) batchFlushQueue;
@property (T@"NSString",&,V_processName) processName;
@property (T@"NSMutableDictionary",&,V_permissionCache) permissionCache;
@property (T@"NSMutableDictionary",&,V_pendingTaskCache) pendingTaskCache;
@property (T@"NSMutableArray",&,V_batchedTaskCache) batchedTaskCache;
@property (T@"NSMutableDictionary",&,V_dynamicCache) dynamicCache;
@property (T@"NSMutableDictionary",&,V_eventFilterSaved) eventFilterSaved;
@property (T@"NSObject<OS_dispatch_queue>",&,V_xpcConnectionQueue) xpcConnectionQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,V_xpcConnectionHelperQueue) xpcConnectionHelperQueue;
@property (T@"NSObject<OS_xpc_object>",&,N,V_xpcConnection) xpcConnection;
@property (T@"NSObject<OS_xpc_object>",&,N,V_xpcConnectionHelper) xpcConnectionHelper;
@property (TB,V_talkToPowerlogHelper) talkToPowerlogHelper;
@property (TB,V_batchedTimerInFlight) batchedTimerInFlight;
@property (TB,V_forceBatching) forceBatching;
@property (TB,V_batchDropMessages) batchDropMessages;
@property (Ti,V_batchMessagesSentCount) batchMessagesSentCount;
@property (T@"NSSet",R,V_batchingClientAllowlist) batchingClientAllowlist;
@property (T@"NSSet",R,V_curatedBatchingList) curatedBatchingList;
@property (T@"NSSet",R,V_batchingKeysAllowlist) batchingKeysAllowlist;
@property (Ti,V_batchedDropMessageCount) batchedDropMessageCount;
@property (TB,V_hasSeenFirstDrop) hasSeenFirstDrop;
@property (Ti,V_hourlyDropCount) hourlyDropCount;
@property (Td,N,V_hourlyWindowStart) hourlyWindowStart;
@property (T@"NSObject<OS_dispatch_queue>",&,V_adaptivePermissionWorkQueue) adaptivePermissionWorkQueue;
```

## Class methods

```
+[PLClientLogger sharedInstance];
+[PLClientLogger isMessageOnDeviceDisabled];
```

## Instance methods

```
-[PLClientLogger clearCache];
-[PLClientLogger setWorkQueue:];
-[PLClientLogger setProcessName:];
-[PLClientLogger setEventFilterSaved:];
-[PLClientLogger cacheForKey:];
-[PLClientLogger cachedPermissionForClientID:withKey:withType:];
-[PLClientLogger shouldLogNowForClientID:withKey:withPayload:withFilterInterval:];
-[PLClientLogger setBatchedTimerInFlight:];
-[PLClientLogger xpcSendMessage:withClientID:withKey:withPayload:];
-[PLClientLogger powerlogStateChanged];
-[PLClientLogger setForceBatching:];
-[PLClientLogger setPendingTaskCache:];
-[PLClientLogger init];
-[PLClientLogger clearBatchedTaskCachePPS];
-[PLClientLogger setXpcConnection:];
-[PLClientLogger sendBatchToPPS];
-[PLClientLogger setXpcConnectionHelper:];
-[PLClientLogger adaptivePermissionWorkQueue];
-[PLClientLogger permissionCache];
-[PLClientLogger hourlyDropCount];
-[PLClientLogger workQueue];
-[PLClientLogger logLaterForClientID:withKey:withFilterInterval:];
-[PLClientLogger setHasSeenFirstDrop:];
-[PLClientLogger batchFlushQueue];
-[PLClientLogger setHourlyWindowStart:];
-[PLClientLogger blockedPermissionForClientID:withKey:withType:withTimeout:];
-[PLClientLogger batchMessagesSentCount];
-[PLClientLogger logForClientID:withKey:withPayload:];
-[PLClientLogger sendHourlyDropSummaryWithTotalDrops:processName:];
-[PLClientLogger setClientDebug:];
-[PLClientLogger setXpcConnectionQueue:];
-[PLClientLogger setXpcConnectionHelperQueue:];
-[PLClientLogger getWorkQueueForClientID:];
-[PLClientLogger setDynamicCache:];
-[PLClientLogger xpcConnection];
-[PLClientLogger setBatchedDropMessageCount:];
-[PLClientLogger logStateCaches];
-[PLClientLogger permissionForClientID:withKey:withType:completion:];
-[PLClientLogger trackHourlyClientDrops];
-[PLClientLogger batchingKeysAllowlist];
-[PLClientLogger batchedTimerInFlight];
-[PLClientLogger xpcConnectionWithClientID:withKey:withPayload:];
-[PLClientLogger xpcSendMessageWithReply:withClientID:withKey:withPayload:];
-[PLClientLogger setBatchedTaskCache:];
-[PLClientLogger forceBatching];
-[PLClientLogger processName];
-[PLClientLogger xpcSendMessageWithRateLimitingforClient:withKey:withPayload:];
-[PLClientLogger setHourlyDropCount:];
-[PLClientLogger batchingClientAllowlist];
-[PLClientLogger addToPendingTaskCacheForType:forClientID:forKey:withPayload:];
-[PLClientLogger batchedTaskCache];
-[PLClientLogger addToBatchedTaskCacheForType:forClientID:forKey:withPayload:];
-[PLClientLogger setBatchDropMessages:];
-[PLClientLogger hasSeenFirstDrop];
-[PLClientLogger batchedDropMessageCount];
-[PLClientLogger xpcConnectionQueue];
-[PLClientLogger setBatchMessagesSentCount:];
-[PLClientLogger talkToPowerlogHelper];
-[PLClientLogger curatedBatchingList];
-[PLClientLogger batchDropMessages];
-[PLClientLogger buildMessageForClientID:withKey:withPayload:];
-[PLClientLogger pendingTasksForType:forClientID:forKey:];
-[PLClientLogger setPermissionCache:];
-[PLClientLogger setBatchFlushQueue:];
-[PLClientLogger batchSizeForClientID:];
-[PLClientLogger eventFilterSaved];
-[PLClientLogger clientDebug];
-[PLClientLogger xpcConnectionHelperQueue];
-[PLClientLogger xpcConnectionHelper];
-[PLClientLogger setCachePermission:ForClientID:withKey:withType:];
-[PLClientLogger setAdaptivePermissionWorkQueue:];
-[PLClientLogger hourlyWindowStart];
-[PLClientLogger logWithCurrentDateForClientID:withKey:withPayload:];
-[PLClientLogger queryForClientID:withKey:withPayload:];
-[PLClientLogger dynamicCache];
-[PLClientLogger setTalkToPowerlogHelper:];
-[PLClientLogger clearBatchedTaskCache];
-[PLClientLogger batchTasksCacheFlush];
-[PLClientLogger pendingTaskCache];
```
