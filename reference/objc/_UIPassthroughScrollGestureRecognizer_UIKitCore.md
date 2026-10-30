# `_UIPassthroughScrollGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- Protocols: `_UIScrollEventRespondable`
- 8 instance variables, 9 properties, 25 instance methods, 2 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _startPoint;
d _startTime;
{CGVector="dx"d"dy"d} _accumulatedScrollEventDelta;
{?="commandHeldThroughAllTouchPhases"b1"acceptsFailureRequirements"b1} _flags;
B _endForPrimaryButtonDown;
B _endForSecondaryButtonDown;
B _acceptsFailureRequirements;
Q _endReason;
```

## Properties

```
@property (TQ,R,N,V_endReason) endReason;
@property (TB,N,V_endForPrimaryButtonDown) endForPrimaryButtonDown;
@property (TB,N,V_endForSecondaryButtonDown) endForSecondaryButtonDown;
@property (TB,N,G_acceptsFailureRequirements,S_setAcceptsFailureRequirements:,V_acceptsFailureRequirements) acceptsFailureRequirements;
@property (T@"<_UIPassthroughGestureDelegate>",W,D,N) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIPassthroughScrollGestureRecognizer _supportsTouchContinuation];
+[_UIPassthroughScrollGestureRecognizer canHandleEventForPassthrough:];
```

## Instance methods

```
-[_UIPassthroughScrollGestureRecognizer _window];
-[_UIPassthroughScrollGestureRecognizer touchesEnded:withEvent:];
-[_UIPassthroughScrollGestureRecognizer shouldReceiveEvent:];
-[_UIPassthroughScrollGestureRecognizer _acceptsBeingFailureRequirementForGestureRecognizer:];
-[_UIPassthroughScrollGestureRecognizer _scrollingChangedWithEvent:];
-[_UIPassthroughScrollGestureRecognizer canBePreventedByGestureRecognizer:];
-[_UIPassthroughScrollGestureRecognizer _acceptsBeingFailureDependentOnGestureRecognizer:];
-[_UIPassthroughScrollGestureRecognizer _shouldReceiveTouch:withEvent:];
-[_UIPassthroughScrollGestureRecognizer touchesCancelled:withEvent:];
-[_UIPassthroughScrollGestureRecognizer setEndForSecondaryButtonDown:];
-[_UIPassthroughScrollGestureRecognizer _transformChangedWithEvent:];
-[_UIPassthroughScrollGestureRecognizer _endWithReason:];
-[_UIPassthroughScrollGestureRecognizer endForPrimaryButtonDown];
-[_UIPassthroughScrollGestureRecognizer endReason];
-[_UIPassthroughScrollGestureRecognizer reset];
-[_UIPassthroughScrollGestureRecognizer setView:];
-[_UIPassthroughScrollGestureRecognizer setEndForPrimaryButtonDown:];
-[_UIPassthroughScrollGestureRecognizer touchesBegan:withEvent:];
-[_UIPassthroughScrollGestureRecognizer acceptsFailureRequirements];
-[_UIPassthroughScrollGestureRecognizer touchesMoved:withEvent:];
-[_UIPassthroughScrollGestureRecognizer initWithTarget:action:];
-[_UIPassthroughScrollGestureRecognizer _acceptsFailureRequirements];
-[_UIPassthroughScrollGestureRecognizer _beginAtLocation:];
-[_UIPassthroughScrollGestureRecognizer endForSecondaryButtonDown];
-[_UIPassthroughScrollGestureRecognizer _setAcceptsFailureRequirements:];
```
