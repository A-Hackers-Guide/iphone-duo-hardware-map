# `CMWakeGestureManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 27 instance variables, 1 properties, 26 instance methods, 13 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" fDispatchQ;
B gestureUpdatesStarted;
^{Dispatcher=^^?@} fWakeDispatcher;
^{Dispatcher=^^?@} fPowerStateDispatcher;
{unique_ptr<CMWakeGestureVisitor, std::default_delete<CMWakeGestureVisitor>>=""{?="__ptr_"^{CMWakeGestureVisitor}}} fWakeGestureVisitor;
q fCurrentState;
i fMeasureLatencyState;
d fWakePacketTimestamp;
^{IONotificationPort=} fIoNotifyPort;
I fIoNotification;
I backlightService;
d fLastNotificationTime;
i fLockScreenToken;
d fLastDisplayOnTime;
@"NSString" fProcessName;
B fIsRunningInPrimaryProcess;
B fEnableLatencyAlert;
B fEnableAudioAlert;
i fLatencyAlertThreshold;
B fIsDisplayActive;
i fNightStandThreshold;
B fNightStandModeEnabled;
^v fGestureService;
q fConfigType;
i fSelector;
@"<CMWakeGestureDelegate>" fUpdatedDelegate;
@"<CMWakeGestureDelegate>" fDelegate;
```

## Properties

```
@property (T@"<CMWakeGestureDelegate>",N) delegate;
```

## Class methods

```
+[CMWakeGestureManager sharedManager];
+[CMWakeGestureManager hasSlowBootArgs];
+[CMWakeGestureManager isWakeGestureAvailable];
+[CMWakeGestureManager isWakeGestureOverrideEnabled];
+[CMWakeGestureManager stringForGestureState:];
+[CMWakeGestureManager stringForMode:];
+[CMWakeGestureManager stringForNotification:];
+[CMWakeGestureManager stringForStartPose:];
+[CMWakeGestureManager stringForViewPose:];
+[CMWakeGestureManager toConfig:];
+[CMWakeGestureManager toPropertyC:];
+[CMWakeGestureManager toRaw:];
+[CMWakeGestureManager toState:];
```

## Instance methods

```
-[CMWakeGestureManager setBacklightState:];
-[CMWakeGestureManager initWithQueue:];
-[CMWakeGestureManager dealloc];
-[CMWakeGestureManager setDelegate:];
-[CMWakeGestureManager delegate];
-[CMWakeGestureManager _stopWakeGestureUpdates_onQueue];
-[CMWakeGestureManager loadPreferences];
-[CMWakeGestureManager _destroyIONotificationsOnQueue];
-[CMWakeGestureManager forceDetected];
-[CMWakeGestureManager initWithQueue:configType:];
-[CMWakeGestureManager invokeDelegateWithState:];
-[CMWakeGestureManager logWakeLatency];
-[CMWakeGestureManager onBacklightServiceUpdated:];
-[CMWakeGestureManager onNotificationControl:];
-[CMWakeGestureManager onPowerStateUpdated:];
-[CMWakeGestureManager onWakeUpdated:];
-[CMWakeGestureManager playAlert];
-[CMWakeGestureManager reenableDetectedStateRecognition];
-[CMWakeGestureManager sendWakeTriggerAnalytics:withDisplay:isSuppressionActive:];
-[CMWakeGestureManager setNightStandWakeEnabled:withConfiguration:];
-[CMWakeGestureManager simulateGesture:after:];
-[CMWakeGestureManager simulateGestureWithDelay:Duration:];
-[CMWakeGestureManager startWakeGestureService];
-[CMWakeGestureManager startWakeGestureUpdates];
-[CMWakeGestureManager stopWakeGestureService];
-[CMWakeGestureManager stopWakeGestureUpdates];
```
