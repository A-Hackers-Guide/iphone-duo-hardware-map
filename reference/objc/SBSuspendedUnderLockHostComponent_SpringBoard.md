# `SBSuspendedUnderLockHostComponent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `FBSceneComponent`, `SBHostedScenePolicyHostComponentObserver`, `SBLockStateObserving`, `SBDisplayContentModeTransitionObserver`
- 3 instance variables, 4 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"<SBLockStateProviding>" _observedLockStateProvider;
@"SBHostedScenePolicyHostComponent" _hostedPolicySceneComponent;
@"SBWindowScene" _hostedWindowScene;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSuspendedUnderLockHostComponent _applyPolicyIfNeeded];
-[SBSuspendedUnderLockHostComponent scene:didUpdateSettings:];
-[SBSuspendedUnderLockHostComponent displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBSuspendedUnderLockHostComponent setScene:];
-[SBSuspendedUnderLockHostComponent displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBSuspendedUnderLockHostComponent scene:willUpdateSettings:];
-[SBSuspendedUnderLockHostComponent _currentPolicy];
-[SBSuspendedUnderLockHostComponent _startObservingHostedScenePolicyComponentIfNeeded];
-[SBSuspendedUnderLockHostComponent invalidate];
-[SBSuspendedUnderLockHostComponent _policyRequiresLockObservation:];
-[SBSuspendedUnderLockHostComponent lockStateProvider:didUpdateIsUILocked:];
-[SBSuspendedUnderLockHostComponent sceneHostingPolicyHostComponentDidUpdateSuspensionUnderLockPolicy:];
-[SBSuspendedUnderLockHostComponent _shouldBeForegroundForSettings:];
-[SBSuspendedUnderLockHostComponent _setObservedLockStateProvider:];
-[SBSuspendedUnderLockHostComponent _needsUpdateForSettings:];
-[SBSuspendedUnderLockHostComponent _shouldBeUnderLock];
-[SBSuspendedUnderLockHostComponent sceneHostingPolicyHostComponentDidUpdateHostWindowScene:];
-[SBSuspendedUnderLockHostComponent _resolveObservedLockStateProvider];
```
