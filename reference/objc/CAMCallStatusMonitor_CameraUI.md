# `CAMCallStatusMonitor`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 25 instance methods, 1 class methods

## Instance variables

```
B _callActive;
@"NSMutableSet" __disabledReasons;
@"NSObject<OS_dispatch_queue>" __avscAccessQueue;
```

## Properties

```
@property (T@"NSMutableSet",R,N,V__disabledReasons) _disabledReasons;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__avscAccessQueue) _avscAccessQueue;
@property (TB,N,GisCallActive,V_callActive) callActive;
```

## Class methods

```
+[CAMCallStatusMonitor _processNameForPid:];
```

## Instance methods

```
-[CAMCallStatusMonitor _handleApplicationWillEnterForeground:];
-[CAMCallStatusMonitor _asyncQueryCallActiveStatusForReason:];
-[CAMCallStatusMonitor _handleRecordingStateDidChangeNotification:];
-[CAMCallStatusMonitor setCallActive:];
-[CAMCallStatusMonitor init];
-[CAMCallStatusMonitor _handleApplicationDidEnterBackground:];
-[CAMCallStatusMonitor _descriptionForReasons:];
-[CAMCallStatusMonitor dealloc];
-[CAMCallStatusMonitor _accessQueue_subscribeToAVSystemControllerNotificationsWithCompletion:];
-[CAMCallStatusMonitor initDisabledForLaunch];
-[CAMCallStatusMonitor _unregisterForAVSystemControllerNotifications];
-[CAMCallStatusMonitor _accessQueue_queryCallActiveStatusForReason:];
-[CAMCallStatusMonitor isCallActive];
-[CAMCallStatusMonitor removeDisabledReason:];
-[CAMCallStatusMonitor _handleCallIsActiveDidChangeNotification:];
-[CAMCallStatusMonitor _descriptionStringForReason:];
-[CAMCallStatusMonitor _disabledReasons];
-[CAMCallStatusMonitor _registerForAVSystemControllerNotificationsAndQueryState];
-[CAMCallStatusMonitor _handleSomeClientIsActiveDidChangeNotification:];
-[CAMCallStatusMonitor _setCallActive:];
-[CAMCallStatusMonitor _processIdentifer];
-[CAMCallStatusMonitor _avscAccessQueue];
-[CAMCallStatusMonitor initWithInitialDisabledReasons:];
-[CAMCallStatusMonitor addDisabledReason:];
-[CAMCallStatusMonitor _handleServerConnectionDiedNotification:];
```
