# `SBHungApplicationInteractionObserver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
Q _previousLockState;
```

## Instance methods

```
-[SBHungApplicationInteractionObserver activate];
-[SBHungApplicationInteractionObserver _lockStateDidChange:];
-[SBHungApplicationInteractionObserver _notifyInteractionWithPossiblyHungApplicationSceneEntities:withInteractionType:];
-[SBHungApplicationInteractionObserver _transitionContextRepresentsActivatingAppFromAppSwitcher:];
-[SBHungApplicationInteractionObserver _transitionContextRepresentsActivatingDynamicIslandApp:];
-[SBHungApplicationInteractionObserver _transitionContextRepresentsActivatingHomeScreen:];
-[SBHungApplicationInteractionObserver _transitionContextRepresentsArcSwipingToPreviousApp:];
-[SBHungApplicationInteractionObserver _transitionContextRepresentsTappingBreadcrumbToPreviousApp:];
-[SBHungApplicationInteractionObserver observeBackgroundingApplicationSceneEntities:withTransitionContext:];
-[SBHungApplicationInteractionObserver observeRemovedApplicationSceneEntity:];
```
