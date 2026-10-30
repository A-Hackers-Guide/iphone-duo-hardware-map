# `_UIDynamicItemObservingBehavior`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIDynamicItemBehavior`
- 5 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _enabled;
d _completionHandlerInvocationDelay;
@? _completionHandler;
q _frameCount;
{CGVector="dx"d"dy"d} _targetVelocity;
```

## Properties

```
@property (TB,N,V_enabled) enabled;
@property (Tq,N,V_frameCount) frameCount;
@property (T{CGVector=dd},N,V_targetVelocity) targetVelocity;
@property (Td,N,V_completionHandlerInvocationDelay) completionHandlerInvocationDelay;
@property (T@?,C,N,V_completionHandler) completionHandler;
```

## Instance methods

```
-[_UIDynamicItemObservingBehavior frameCount];
-[_UIDynamicItemObservingBehavior setCompletionHandler:];
-[_UIDynamicItemObservingBehavior completionHandler];
-[_UIDynamicItemObservingBehavior enabled];
-[_UIDynamicItemObservingBehavior setEnabled:];
-[_UIDynamicItemObservingBehavior setFrameCount:];
-[_UIDynamicItemObservingBehavior cancel];
-[_UIDynamicItemObservingBehavior completionHandlerInvocationDelay];
-[_UIDynamicItemObservingBehavior setCompletionHandlerInvocationDelay:];
-[_UIDynamicItemObservingBehavior setTargetVelocity:];
-[_UIDynamicItemObservingBehavior targetVelocity];
-[_UIDynamicItemObservingBehavior willMoveToAnimator:];
```
