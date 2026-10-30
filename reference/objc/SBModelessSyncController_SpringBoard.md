# `SBModelessSyncController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 5 properties, 19 instance methods, 1 class methods

## Instance variables

```
B _isAppSyncing;
B _isSyncing;
i _syncRegistrationToken;
i _iCloudRestoreToken;
B _restoringFromICloud;
B _isAutoSyncing;
B _isWirelessSyncing;
@"ATConnection" _airTrafficConnection;
```

## Properties

```
@property (TB,R,N,V_isAppSyncing) isAppSyncing;
@property (TB,R,N,V_isSyncing) isSyncing;
@property (TB,R,N) isRestoringFromICloud;
@property (TB,R,N,V_isAutoSyncing) isAutoSyncing;
@property (TB,R,N,V_isWirelessSyncing) isWirelessSyncing;
```

## Class methods

```
+[SBModelessSyncController sharedInstance];
```

## Instance methods

```
-[SBModelessSyncController beginMonitoring];
-[SBModelessSyncController init];
-[SBModelessSyncController dealloc];
-[SBModelessSyncController endMonitoring];
-[SBModelessSyncController connectionWasInterrupted:];
-[SBModelessSyncController isSyncing];
-[SBModelessSyncController setIsSyncing:];
-[SBModelessSyncController _appSyncStateChanged];
-[SBModelessSyncController _beginObservingICloudRestoreStatus];
-[SBModelessSyncController _endObservingICloudRestoreStatus];
-[SBModelessSyncController _iCloudStatusChanged];
-[SBModelessSyncController _setAppSyncState:];
-[SBModelessSyncController _updateIconsForStateChange];
-[SBModelessSyncController connection:updatedProgress:];
-[SBModelessSyncController gotLowBatteryWarning];
-[SBModelessSyncController isAppSyncing];
-[SBModelessSyncController isAutoSyncing];
-[SBModelessSyncController isRestoringFromICloud];
-[SBModelessSyncController isWirelessSyncing];
```
