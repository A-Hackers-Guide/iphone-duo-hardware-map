# `CBDisplayTransitionPolicy`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBExternalDisplayKeyPolicy`
- 11 instance variables, 0 properties, 32 instance methods, 3 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"NSObject<OS_dispatch_queue>" _queue;
@"<CBDisplayPropertyPolicyDelegate>" _delegate;
q _state;
d _gracePeriodDuration;
@"NSObject<OS_dispatch_source>" _gracePeriodTimer;
@"NSSet" _syncedKeys;
@"NSMutableSet" _goingOffline;
f _currentAngleDegrees;
B _hasAngleSample;
d _lastAngleBelowCriticalThresholdTime;
```

## Class methods

```
+[CBDisplayTransitionPolicy stringFromState:];
+[CBDisplayTransitionPolicy isBrightnessCommit:];
+[CBDisplayTransitionPolicy stringFromPropertyKey:];
```

## Instance methods

```
-[CBDisplayTransitionPolicy copyPropertyForKey:];
-[CBDisplayTransitionPolicy copyStatusInfo];
-[CBDisplayTransitionPolicy setProperty:forKey:];
-[CBDisplayTransitionPolicy initWithDelegate:queue:];
-[CBDisplayTransitionPolicy dealloc];
-[CBDisplayTransitionPolicy cancel];
-[CBDisplayTransitionPolicy reevaluateState];
-[CBDisplayTransitionPolicy activeSyncLeader];
-[CBDisplayTransitionPolicy activeSyncedCount];
-[CBDisplayTransitionPolicy beginGracePeriod];
-[CBDisplayTransitionPolicy cancelGracePeriod];
-[CBDisplayTransitionPolicy cancelGracePeriodInternal];
-[CBDisplayTransitionPolicy commitBrightnessToLeaderAndSync:];
-[CBDisplayTransitionPolicy containerDidAdd:];
-[CBDisplayTransitionPolicy containerWillRemove:];
-[CBDisplayTransitionPolicy gracePeriodDidExpire];
-[CBDisplayTransitionPolicy handleBrightnessCommit:forKey:];
-[CBDisplayTransitionPolicy handleDisplayActivation:forContainer:];
-[CBDisplayTransitionPolicy handleDisplayDeactivation:forContainer:];
-[CBDisplayTransitionPolicy handleDisplayModeChange:forContainer:];
-[CBDisplayTransitionPolicy isDeviceStableOpen];
-[CBDisplayTransitionPolicy isSourceSettled:target:];
-[CBDisplayTransitionPolicy isSyncedContainer:];
-[CBDisplayTransitionPolicy isTopToBottomHandoffFromSource:toTarget:];
-[CBDisplayTransitionPolicy panelPlacementForContainer:];
-[CBDisplayTransitionPolicy performHandoffFromContainer:toContainer:];
-[CBDisplayTransitionPolicy prepareHandoffFromSource:toNewDisplay:];
-[CBDisplayTransitionPolicy processNotificationForKey:value:container:handle:];
-[CBDisplayTransitionPolicy setProperty:forKey:forContainer:];
-[CBDisplayTransitionPolicy syncCurveFromContainer:];
-[CBDisplayTransitionPolicy syncedContainers];
-[CBDisplayTransitionPolicy updateAngle:];
```
