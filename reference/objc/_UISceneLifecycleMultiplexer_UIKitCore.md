# `_UISceneLifecycleMultiplexer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 7 properties, 19 instance methods, 8 class methods

## Instance variables

```
@"UIScene" _uiSceneOfRecord;
@"UIApplicationSceneSettings" _transitionalLifecycleState;
{?="completedLaunch"b1"activatedOnce"b1} _multiplexerFlags;
```

## Properties

```
@property (TB,R,N) activatedOnce;
@property (TB,R,N) lifecycleWantsUnnecessaryDelayForSceneDelivery;
@property (Tq,R,N) applicationState;
@property (TB,R,N,GisActive) active;
@property (TB,R,N) suspendedEventsOnly;
@property (TB,R,N) suspendedUnderLock;
@property (TB,R,N) runningInTaskSwitcher;
```

## Class methods

```
+[_UISceneLifecycleMultiplexer sharedInstance];
+[_UISceneLifecycleMultiplexer mostActiveWindowSceneOnScreen:];
+[_UISceneLifecycleMultiplexer _compareLifecycleStateOfScene:toScene:];
+[_UISceneLifecycleMultiplexer mostActiveSceneIncludingInternal:withTest:];
+[_UISceneLifecycleMultiplexer mostActiveScene];
+[_UISceneLifecycleMultiplexer _mostActiveSceneForApplicationState];
+[_UISceneLifecycleMultiplexer configureInitialDeactivationReasons:];
+[_UISceneLifecycleMultiplexer mostActiveSceneWithTest:];
```

## Instance methods

```
-[_UISceneLifecycleMultiplexer activatedOnce];
-[_UISceneLifecycleMultiplexer _performBlock:withApplicationOfDeactivationReasons:fromReasons:];
-[_UISceneLifecycleMultiplexer applicationState];
-[_UISceneLifecycleMultiplexer _evalTransitionToSettings:fromSettings:forceExit:withTransitionStore:];
-[_UISceneLifecycleMultiplexer isTrackingScene:];
-[_UISceneLifecycleMultiplexer completeApplicationLaunchWithFBSScene:transitionContext:];
-[_UISceneLifecycleMultiplexer _prepareForClientSuspensionWithScene:];
-[_UISceneLifecycleMultiplexer uiScene:transitionedFromState:withTransitionContext:];
-[_UISceneLifecycleMultiplexer forceExitWithTransitionContext:scene:];
-[_UISceneLifecycleMultiplexer _scheduleFirstCommit];
-[_UISceneLifecycleMultiplexer suspendedUnderLock];
-[_UISceneLifecycleMultiplexer _globalTestRelatedActivationActionsForFirstActivation:foreground:interfaceStyle:transitionContext:];
-[_UISceneLifecycleMultiplexer initForAppSingleton:];
-[_UISceneLifecycleMultiplexer runningInTaskSwitcher];
-[_UISceneLifecycleMultiplexer lifecycleWantsUnnecessaryDelayForSceneDelivery];
-[_UISceneLifecycleMultiplexer isActive];
-[_UISceneLifecycleMultiplexer suspendedEventsOnly];
-[_UISceneLifecycleMultiplexer noteApplicationLaunchCompleted];
-[_UISceneLifecycleMultiplexer collectBackingStores];
```
