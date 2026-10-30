# `SBSyncController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `DDRResetObserver`, `SBIdleTimerProviding`
- 13 instance variables, 6 properties, 34 instance methods, 1 class methods

## Instance variables

```
i _restoreState;
i _resetState;
i _restoreTimerState;
@"NSTimer" _restoreTimer;
@"NSTimer" _progressTimer;
B _appsChangedDuringSync;
i _restoreStartedNotifyToken;
i _restoreEndedNotifyToken;
@"SBFAuthenticationAssertion" _disableDeviceLockAssertion;
@"SBWindowSceneStatusBarSettingsAssertion" _hideStatusBarAssertion;
B _isAppSyncing;
B _inExtendedAppSyncCoalescePeriod;
@"<SBIdleTimerCoordinating>" _idleTimerCoordinator;
```

## Properties

```
@property (T@"<SBIdleTimerCoordinating>",W,N,G_idleTimerCoordinator,S_setIdleTimerCoordinator:,V_idleTimerCoordinator) idleTimerCoordinator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) hasIdleTimerBehaviors;
```

## Class methods

```
+[SBSyncController sharedInstance];
```

## Instance methods

```
-[SBSyncController resetState];
-[SBSyncController isRestoring];
-[SBSyncController stopObserving];
-[SBSyncController restoreState];
-[SBSyncController isResetting];
-[SBSyncController _idleTimerCoordinator];
-[SBSyncController startObserving];
-[SBSyncController dealloc];
-[SBSyncController _idleTimerBehavior];
-[SBSyncController isInUse];
-[SBSyncController hasIdleTimerBehaviors];
-[SBSyncController _setIdleTimerCoordinator:];
-[SBSyncController coordinatorRequestedIdleTimerBehavior:];
-[SBSyncController _setRestoreState:];
-[SBSyncController resetService:willBeginDataResetWithMode:];
-[SBSyncController finishedTerminatingApplications];
-[SBSyncController cancelRestoring];
-[SBSyncController _appInstallationNotification];
-[SBSyncController _delayedQuitApplications];
-[SBSyncController _didEndRestoring:];
-[SBSyncController _invalidateRestoreTimer];
-[SBSyncController _isBackupAgentRunning];
-[SBSyncController _killApplicationsIfNecessary];
-[SBSyncController _notifyRestoreCanProceed];
-[SBSyncController _rebootNow];
-[SBSyncController _restoreTimerFired:];
-[SBSyncController _setupRestoreTimer];
-[SBSyncController _syncSessionDidBegin];
-[SBSyncController _syncSessionDidEnd];
-[SBSyncController _wirelessSyncBegan:];
-[SBSyncController _wirelessSyncEnded:];
-[SBSyncController beginRestoring];
-[SBSyncController resetService:didBeginDataResetWithMode:];
-[SBSyncController resetService:didCompleteDataResetMode:withError:completion:];
```
