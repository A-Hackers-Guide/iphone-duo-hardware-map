# `UIApplicationSceneTransitionContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneTransitionContext`
- 0 instance variables, 13 properties, 29 instance methods, 0 class methods

## Properties

```
@property (T@"NSDictionary",&,N) payload;
@property (TB,N) forTesting;
@property (TB,N) safeMode;
@property (Td,N) userLaunchEventTime;
@property (Td,N) execTime;
@property (TQ,N) signpostID;
@property (T@"NSObject<OS_xpc_object>",&,N) launchMetricsPayload;
@property (TB,N) shouldTakeKeyboardFocus;
@property (TB,N) waitForBackgroundTaskCompletion;
@property (T@"UISClickAttribution",&,N) clickAttribution;
@property (T@"UISPasteSharingToken",&,N) pasteSharingToken;
@property (Tq,N) statusBarAnimation;
@property (TB,N) disableTouchCancellationOnRotation;
```

## Instance methods

```
-[UIApplicationSceneTransitionContext pasteSharingToken];
-[UIApplicationSceneTransitionContext payload];
-[UIApplicationSceneTransitionContext valueDescriptionForFlag:object:ofSetting:];
-[UIApplicationSceneTransitionContext keyDescriptionForSetting:];
-[UIApplicationSceneTransitionContext setPayload:];
-[UIApplicationSceneTransitionContext setSignpostID:];
-[UIApplicationSceneTransitionContext signpostID];
-[UIApplicationSceneTransitionContext waitForBackgroundTaskCompletion];
-[UIApplicationSceneTransitionContext clickAttribution];
-[UIApplicationSceneTransitionContext disableTouchCancellationOnRotation];
-[UIApplicationSceneTransitionContext execTime];
-[UIApplicationSceneTransitionContext forTesting];
-[UIApplicationSceneTransitionContext isUISubclass];
-[UIApplicationSceneTransitionContext launchMetricsPayload];
-[UIApplicationSceneTransitionContext safeMode];
-[UIApplicationSceneTransitionContext setClickAttribution:];
-[UIApplicationSceneTransitionContext setDisableTouchCancellationOnRotation:];
-[UIApplicationSceneTransitionContext setExecTime:];
-[UIApplicationSceneTransitionContext setForTesting:];
-[UIApplicationSceneTransitionContext setLaunchMetricsPayload:];
-[UIApplicationSceneTransitionContext setPasteSharingToken:];
-[UIApplicationSceneTransitionContext setSafeMode:];
-[UIApplicationSceneTransitionContext setShouldTakeKeyboardFocus:];
-[UIApplicationSceneTransitionContext setStatusBarAnimation:];
-[UIApplicationSceneTransitionContext setUserLaunchEventTime:];
-[UIApplicationSceneTransitionContext setWaitForBackgroundTaskCompletion:];
-[UIApplicationSceneTransitionContext shouldTakeKeyboardFocus];
-[UIApplicationSceneTransitionContext statusBarAnimation];
-[UIApplicationSceneTransitionContext userLaunchEventTime];
```
