# `UIGestureEnvironment`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
^{__CFRunLoopObserver=} _gestureEnvironmentUpdateObserver;
@"NSMutableSet" _gestureRecognizersNeedingUpdate;
@"NSMutableSet" _gestureRecognizersNeedingReset;
@"NSMutableSet" _gestureRecognizersNeedingRemoval;
@"NSMutableArray" _dirtyGestureRecognizers;
@"NSMutableSet" _gestureRecognizersBlockedFromReset;
Q _lastBlockedResetEvaluationMachTime;
@"<BSInvalidatable>" _blockedResetStateCaptureToken;
@"NSMapTable" _touchContinuationDeliveryActions;
B _dirtyGestureRecognizersUnsorted;
B _updateExclusivity;
B _isUpdatingGestureEnvironment;
@"UIGestureGraph" _dependencyGraph;
@"NSMapTable" _nodesByGestureRecognizer;
@"<GFGestureNodeCoordinator>" _nodeCoordinator;
```

## Instance methods

```
-[UIGestureEnvironment addGestureRecognizer:];
-[UIGestureEnvironment init];
-[UIGestureEnvironment dealloc];
-[UIGestureEnvironment removeGestureRecognizer:];
```
