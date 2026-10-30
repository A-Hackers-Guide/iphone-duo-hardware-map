# `SBApplicationAutoLaunchService`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `SBFMobileKeyBagObserver`
- 10 instance variables, 7 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"SBMainWorkspace" _mainWorkspace;
@"SBApplicationController" _applicationController;
@"SBRestartManager" _restartManager;
@"SBSyncController" _syncController;
@"SBFMobileKeyBag" _keybag;
@"SBMemoryPressureMonitor" _memoryPressureMonitor;
@"NSMutableArray" _queuedApplicationsThrottledForRelaunch;
@"NSTimer" _queuedApplicationsThrottledForRelaunchTimer;
B _autoLaunchSynchronously;
B _invalidated;
```

## Properties

```
@property (TB,N,G_autoLaunchSynchronously,S_setAutoLaunchSynchronously:,V_autoLaunchSynchronously) autoLaunchSynchronously;
@property (T@"NSTimer",R,N,G_queuedApplicationsThrottledForRelaunchTimer,V_queuedApplicationsThrottledForRelaunchTimer) queuedApplicationsThrottledForRelaunchTimer;
@property (T@"NSArray",R,N,G_queuedApplicationsThrottledForRelaunch,V_queuedApplicationsThrottledForRelaunch) queuedApplicationsThrottledForRelaunch;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBApplicationAutoLaunchService _installedApplicationsDidChange:];
-[SBApplicationAutoLaunchService succinctDescriptionBuilder];
-[SBApplicationAutoLaunchService dealloc];
-[SBApplicationAutoLaunchService descriptionWithMultilinePrefix:];
-[SBApplicationAutoLaunchService succinctDescription];
-[SBApplicationAutoLaunchService invalidate];
-[SBApplicationAutoLaunchService description];
-[SBApplicationAutoLaunchService keybagDidUnlockForTheFirstTime:];
-[SBApplicationAutoLaunchService descriptionBuilderWithMultilinePrefix:];
-[SBApplicationAutoLaunchService _applicationProcessStateDidChange:];
-[SBApplicationAutoLaunchService _autoLaunchAppsIfNecessaryAfterFirstUnlock];
-[SBApplicationAutoLaunchService _autoLaunchIfNecessary:forReason:];
-[SBApplicationAutoLaunchService _autoLaunchSynchronously];
-[SBApplicationAutoLaunchService _initWithWorkspace:applicationController:restartManager:syncController:keybag:memoryPressureMonitor:];
-[SBApplicationAutoLaunchService _invalidateQueuedApplicationsThrottledForRelaunchTimer];
-[SBApplicationAutoLaunchService _launchNextQueuedApplicationThrottledForRelaunch];
-[SBApplicationAutoLaunchService _memoryPressureRelieved:];
-[SBApplicationAutoLaunchService _memoryPressureWarn:];
-[SBApplicationAutoLaunchService _noteKeybagDidUnlock];
-[SBApplicationAutoLaunchService _noteTerminationAssertionRemovedForApplication:];
-[SBApplicationAutoLaunchService _queuedApplicationsThrottledForRelaunch];
-[SBApplicationAutoLaunchService _queuedApplicationsThrottledForRelaunchTimer];
-[SBApplicationAutoLaunchService _recalculateVoIPBehaviorForApplication:withExitContext:];
-[SBApplicationAutoLaunchService _scheduleAutoLaunchForApplicationExited:withExitContext:];
-[SBApplicationAutoLaunchService _scheduleThrottledApplicationRelaunchTimerIfNecessary];
-[SBApplicationAutoLaunchService _setAutoLaunchSynchronously:];
-[SBApplicationAutoLaunchService _shouldAutoLaunchApplication:forReason:];
-[SBApplicationAutoLaunchService autoLaunchApplicationsIfNecessaryForStartup];
```
