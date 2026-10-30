# `SBSafeAreaResolverHostComponent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `SBFStatusBarManagerObserver`
- 3 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"SBSafeAreaResolverUtility" _safeAreaResolverUtility;
@"SBWindowScene" _registeredWindowScene;
@"<SBSafeAreaResolverExtensionDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBSafeAreaResolverExtensionDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSafeAreaResolverHostComponent statusBarManager:didUpdateAvoidanceFrameForStatusBar:withAnimationSettings:];
-[SBSafeAreaResolverHostComponent statusBarManager:didUpdateOcclusionFrameForStatusBar:];
-[SBSafeAreaResolverHostComponent scene:didUpdateSettings:];
-[SBSafeAreaResolverHostComponent setScene:];
-[SBSafeAreaResolverHostComponent _stopObservingStatusBar];
-[SBSafeAreaResolverHostComponent _preferredWindowControlsPlacementForScene:application:];
-[SBSafeAreaResolverHostComponent invalidate];
-[SBSafeAreaResolverHostComponent _reevaluateSafeAreaForScene:];
-[SBSafeAreaResolverHostComponent setDelegate:];
-[SBSafeAreaResolverHostComponent _updateStatusBarObservationForScene:];
-[SBSafeAreaResolverHostComponent delegate];
-[SBSafeAreaResolverHostComponent _isEligibleHostedScene:];
```
