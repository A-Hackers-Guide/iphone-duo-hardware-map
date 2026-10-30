# `SBPIPStashTabSuppressionPolicyProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBBannerManagerTransitionObserver`, `SBLayoutStateTransitionObserver`, `SBDeviceApplicationSceneHandleObserver`, `UIGestureRecognizerDelegate`, `SBUIActiveOrientationObserver`
- 11 instance variables, 12 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _requestIdentifiersForPresentedExpanseBanners;
B _invalidated;
@"UIApplicationSceneClientSettingsDiffInspector" _clientSettingsInspector;
B _stashTabCanBeHidden;
@"<SBPIPStashTabSuppressionPolicyProviderObserver>" _observer;
@"SBBannerManager" _bannerManager;
@"SBWindowScene" _sbWindowScene;
@"SBSwitcherController" _switcherController;
@"SBWindowScenePIPManager" _pipManager;
@"SBDeviceApplicationSceneHandle" _sceneHandleToObserve;
@"NSTimer" _reevaluatePolicyTimer;
```

## Properties

```
@property (T@"SBBannerManager",R,W,N,V_bannerManager) bannerManager;
@property (T@"SBWindowScene",R,W,N,V_sbWindowScene) sbWindowScene;
@property (T@"SBSwitcherController",R,W,N,V_switcherController) switcherController;
@property (T@"SBWindowScenePIPManager",R,W,N,V_pipManager) pipManager;
@property (TB,N,V_stashTabCanBeHidden) stashTabCanBeHidden;
@property (T@"SBDeviceApplicationSceneHandle",W,N,V_sceneHandleToObserve) sceneHandleToObserve;
@property (T@"NSTimer",&,N,V_reevaluatePolicyTimer) reevaluatePolicyTimer;
@property (T@"<SBPIPStashTabSuppressionPolicyProviderObserver>",W,N,V_observer) observer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBPIPStashTabSuppressionPolicyProvider sceneHandle:didUpdateClientSettings:];
-[SBPIPStashTabSuppressionPolicyProvider activeInterfaceOrientationDidChangeToOrientation:willAnimateWithDuration:fromOrientation:];
-[SBPIPStashTabSuppressionPolicyProvider switcherController];
-[SBPIPStashTabSuppressionPolicyProvider observer];
-[SBPIPStashTabSuppressionPolicyProvider bannerManager];
-[SBPIPStashTabSuppressionPolicyProvider dealloc];
-[SBPIPStashTabSuppressionPolicyProvider activeInterfaceOrientationWillChangeToOrientation:];
-[SBPIPStashTabSuppressionPolicyProvider invalidate];
-[SBPIPStashTabSuppressionPolicyProvider layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:];
-[SBPIPStashTabSuppressionPolicyProvider setObserver:];
-[SBPIPStashTabSuppressionPolicyProvider bannerManager:willDismissPresentable:withTransitionCoordinator:userInfo:];
-[SBPIPStashTabSuppressionPolicyProvider bannerManager:willPresentPresentable:withTransitionCoordinator:userInfo:];
-[SBPIPStashTabSuppressionPolicyProvider _tapRecognized:];
-[SBPIPStashTabSuppressionPolicyProvider _reevaluatePolicy];
-[SBPIPStashTabSuppressionPolicyProvider _resetReevaluatePolicyTimer];
-[SBPIPStashTabSuppressionPolicyProvider _startTrackingPresentable:];
-[SBPIPStashTabSuppressionPolicyProvider _stopTrackingPresentable:];
-[SBPIPStashTabSuppressionPolicyProvider _updateSceneHandleToObserveForLayoutState:];
-[SBPIPStashTabSuppressionPolicyProvider initWithObserver:bannerManager:windowScene:pipManager:];
-[SBPIPStashTabSuppressionPolicyProvider pipManager];
-[SBPIPStashTabSuppressionPolicyProvider reevaluatePolicyTimer];
-[SBPIPStashTabSuppressionPolicyProvider sbWindowScene];
-[SBPIPStashTabSuppressionPolicyProvider sceneHandleToObserve];
-[SBPIPStashTabSuppressionPolicyProvider setReevaluatePolicyTimer:];
-[SBPIPStashTabSuppressionPolicyProvider setSceneHandleToObserve:];
-[SBPIPStashTabSuppressionPolicyProvider setStashTabCanBeHidden:];
-[SBPIPStashTabSuppressionPolicyProvider stashTabCanBeHidden];
```
