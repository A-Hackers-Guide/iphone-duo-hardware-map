# `_UIInterruptScrollDecelerationGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- Protocols: `_UIScrollEventRespondable`, `_UIHoverEventRespondable`
- 3 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"UIHoverEvent" _currentHoverEvent;
q _previousTrackpadFingerDownCount;
q _trackpadFingerDownCount;
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
-[_UIInterruptScrollDecelerationGestureRecognizer canPreventGestureRecognizer:];
-[_UIInterruptScrollDecelerationGestureRecognizer _hoverMoved:withEvent:];
-[_UIInterruptScrollDecelerationGestureRecognizer _shouldReceivePress:];
-[_UIInterruptScrollDecelerationGestureRecognizer _hoverEntered:withEvent:];
-[_UIInterruptScrollDecelerationGestureRecognizer _hoverCancelled:withEvent:];
-[_UIInterruptScrollDecelerationGestureRecognizer _acceptsBeingFailureRequirementForGestureRecognizer:];
-[_UIInterruptScrollDecelerationGestureRecognizer _scrollingChangedWithEvent:];
-[_UIInterruptScrollDecelerationGestureRecognizer canBePreventedByGestureRecognizer:];
-[_UIInterruptScrollDecelerationGestureRecognizer _acceptsBeingFailureDependentOnGestureRecognizer:];
-[_UIInterruptScrollDecelerationGestureRecognizer _canCancelGestureRecognizer:];
-[_UIInterruptScrollDecelerationGestureRecognizer reset];
-[_UIInterruptScrollDecelerationGestureRecognizer _hoverExited:withEvent:];
-[_UIInterruptScrollDecelerationGestureRecognizer _shouldReceiveTouch:forEvent:recognizerView:];
```
