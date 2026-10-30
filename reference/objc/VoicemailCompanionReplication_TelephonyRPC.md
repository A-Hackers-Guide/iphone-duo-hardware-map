# `VoicemailCompanionReplication`

- Image: [`/System/Library/PrivateFrameworks/TelephonyRPC.framework/TelephonyRPC`](../userland/System__Library__PrivateFrameworks__TelephonyRPC.framework__TelephonyRPC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PSYInitialSyncStateObserverDelegate`, `SYServiceDelegate`, `PSYSyncCoordinatorDelegate`, `NPHVMSyncSessionManagerDelegate`
- 13 instance variables, 20 properties, 47 instance methods, 0 class methods

## Instance variables

```
B _syncPermitted;
@"SYService" _syncService;
@"NPSDomainAccessor" _domainAccessor;
@"_TtC12TelephonyRPC21VoicemailManager_ObjC" _voicemailManager;
@"NSCondition" _voicemailsLoadedCondition;
@"NPHVMSyncSessionManager" _syncSessionManager;
@"NSCondition" _notSyncingCondition;
@"NSObject<OS_os_transaction>" _transaction;
@"NSMutableArray" _syncingVoicemails;
@"NSObject<OS_dispatch_queue>" _syncServiceQueue;
@"PSYSyncCoordinator" _initialSyncCoordinator;
@"PSYInitialSyncStateObserver" _initialSyncStateObserver;
@"NSObject<OS_dispatch_semaphore>" _initialSyncComplete;
```

## Properties

```
@property (T@"NPSDomainAccessor",R,N,V_domainAccessor) domainAccessor;
@property (T@"NSMutableArray",&,N) remoteVoicemails;
@property (Tq,N) currentMigrationVersion;
@property (T@"_TtC12TelephonyRPC21VoicemailManager_ObjC",R,N,V_voicemailManager) voicemailManager;
@property (T@"NSCondition",R,N,V_voicemailsLoadedCondition) voicemailsLoadedCondition;
@property (TB,GisSyncPermitted,V_syncPermitted) syncPermitted;
@property (T@"NPHVMSyncSessionManager",R,N,V_syncSessionManager) syncSessionManager;
@property (T@"NSCondition",R,N,V_notSyncingCondition) notSyncingCondition;
@property (TB,N,G_isSyncing) syncing;
@property (T@"NSObject<OS_os_transaction>",&,N,V_transaction) transaction;
@property (T@"NSMutableArray",&,N,V_syncingVoicemails) syncingVoicemails;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_syncServiceQueue) syncServiceQueue;
@property (T@"PSYSyncCoordinator",R,N,V_initialSyncCoordinator) initialSyncCoordinator;
@property (T@"PSYInitialSyncStateObserver",R,N,V_initialSyncStateObserver) initialSyncStateObserver;
@property (T@"NSObject<OS_dispatch_semaphore>",R,N,V_initialSyncComplete) initialSyncComplete;
@property (T@"SYService",R,N,V_syncService) syncService;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[VoicemailCompanionReplication domainAccessor];
-[VoicemailCompanionReplication setTransaction:];
-[VoicemailCompanionReplication voicemails];
-[VoicemailCompanionReplication syncService];
-[VoicemailCompanionReplication transaction];
-[VoicemailCompanionReplication sync:];
-[VoicemailCompanionReplication init];
-[VoicemailCompanionReplication syncCoordinator:beginSyncSession:];
-[VoicemailCompanionReplication dealloc];
-[VoicemailCompanionReplication _isSyncing];
-[VoicemailCompanionReplication initialSyncStateObserver:syncDidCompleteForPairingIdentifier:];
-[VoicemailCompanionReplication service:encounteredError:context:];
-[VoicemailCompanionReplication service:sessionEnded:error:];
-[VoicemailCompanionReplication service:startSession:error:];
-[VoicemailCompanionReplication serviceDidPairDevice:];
-[VoicemailCompanionReplication syncSession:applyChanges:completion:];
-[VoicemailCompanionReplication syncSession:didEndWithError:];
-[VoicemailCompanionReplication syncSession:resetDataStoreWithError:];
-[VoicemailCompanionReplication setSyncing:];
-[VoicemailCompanionReplication changesBetween:and:];
-[VoicemailCompanionReplication syncCoordinator:didInvalidateSyncSession:];
-[VoicemailCompanionReplication syncCoordinatorDidChangeSyncRestriction:];
-[VoicemailCompanionReplication voicemailManager];
-[VoicemailCompanionReplication initialSyncCoordinator];
-[VoicemailCompanionReplication isSyncPermitted];
-[VoicemailCompanionReplication _handleVoicemailsChangedNotification:];
-[VoicemailCompanionReplication _retrySyncSession:];
-[VoicemailCompanionReplication _syncRestrictionUpdated];
-[VoicemailCompanionReplication currentMigrationVersion];
-[VoicemailCompanionReplication handleSIGTERM];
-[VoicemailCompanionReplication indexOfVoicemail:inArray:];
-[VoicemailCompanionReplication initialSyncComplete];
-[VoicemailCompanionReplication initialSyncStateObserver];
-[VoicemailCompanionReplication notSyncingCondition];
-[VoicemailCompanionReplication remoteVoicemails];
-[VoicemailCompanionReplication removeFromRemoteVoicemails:];
-[VoicemailCompanionReplication setCurrentMigrationVersion:];
-[VoicemailCompanionReplication setRemoteVoicemails:];
-[VoicemailCompanionReplication setSyncPermitted:];
-[VoicemailCompanionReplication setSyncingVoicemails:];
-[VoicemailCompanionReplication sync:force:];
-[VoicemailCompanionReplication syncServiceQueue];
-[VoicemailCompanionReplication syncSessionManager];
-[VoicemailCompanionReplication syncSessionManager:reportProgress:];
-[VoicemailCompanionReplication syncSessionManagerDidCompleteSending:];
-[VoicemailCompanionReplication syncingVoicemails];
-[VoicemailCompanionReplication voicemailsLoadedCondition];
```
