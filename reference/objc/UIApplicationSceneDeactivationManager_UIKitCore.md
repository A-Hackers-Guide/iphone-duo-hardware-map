# `UIApplicationSceneDeactivationManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 3 instance variables, 4 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _assertions;
@"NSMutableSet" _eligibleScenes;
@"FBScene" _updatingScene;
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
-[UIApplicationSceneDeactivationManager succinctDescriptionBuilder];
-[UIApplicationSceneDeactivationManager init];
-[UIApplicationSceneDeactivationManager descriptionWithMultilinePrefix:];
-[UIApplicationSceneDeactivationManager succinctDescription];
-[UIApplicationSceneDeactivationManager assertions];
-[UIApplicationSceneDeactivationManager removeAssertion:];
-[UIApplicationSceneDeactivationManager description];
-[UIApplicationSceneDeactivationManager descriptionBuilderWithMultilinePrefix:];
-[UIApplicationSceneDeactivationManager _areEligibleSettings:];
-[UIApplicationSceneDeactivationManager _deactivationReasonsForScene:withSettings:];
-[UIApplicationSceneDeactivationManager _isEligibleScene:];
-[UIApplicationSceneDeactivationManager _isEligibleScene:withSettings:];
-[UIApplicationSceneDeactivationManager _setDeactivationReasons:onScene:withSettings:reason:];
-[UIApplicationSceneDeactivationManager _trackScene:];
-[UIApplicationSceneDeactivationManager _untrackScene:];
-[UIApplicationSceneDeactivationManager _updateScenesWithTransitionContext:reason:];
-[UIApplicationSceneDeactivationManager addAssertion:withTransitionContext:];
-[UIApplicationSceneDeactivationManager amendSceneSettings:forScene:];
-[UIApplicationSceneDeactivationManager beginTrackingScene:];
-[UIApplicationSceneDeactivationManager eligibleScenes];
-[UIApplicationSceneDeactivationManager endTrackingScene:];
-[UIApplicationSceneDeactivationManager newAssertionWithReason:];
```
