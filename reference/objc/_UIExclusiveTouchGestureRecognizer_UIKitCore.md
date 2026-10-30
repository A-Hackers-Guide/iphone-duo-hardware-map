# `_UIExclusiveTouchGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _achievedMaximumAbsoluteAccumulatedMovement;
{CGPoint="x"d"y"d} _maximumAbsoluteAccumulatedMovement;
{CGPoint="x"d"y"d} _accumulatedMovement;
```

## Properties

```
@property (T@"<_UIExclusiveTouchGestureRecognizerDelegate>",W,D,N) delegate;
@property (T{CGPoint=dd},N,V_maximumAbsoluteAccumulatedMovement) maximumAbsoluteAccumulatedMovement;
@property (TB,R,N,V_achievedMaximumAbsoluteAccumulatedMovement) achievedMaximumAbsoluteAccumulatedMovement;
@property (T{CGPoint=dd},R,N,V_accumulatedMovement) accumulatedMovement;
```

## Instance methods

```
-[_UIExclusiveTouchGestureRecognizer touchesEnded:withEvent:];
-[_UIExclusiveTouchGestureRecognizer _shouldReceiveTouch:withEvent:];
-[_UIExclusiveTouchGestureRecognizer touchesCancelled:withEvent:];
-[_UIExclusiveTouchGestureRecognizer reset];
-[_UIExclusiveTouchGestureRecognizer touchesBegan:withEvent:];
-[_UIExclusiveTouchGestureRecognizer touchesMoved:withEvent:];
-[_UIExclusiveTouchGestureRecognizer setMaximumAbsoluteAccumulatedMovement:];
-[_UIExclusiveTouchGestureRecognizer maximumAbsoluteAccumulatedMovement];
-[_UIExclusiveTouchGestureRecognizer description];
-[_UIExclusiveTouchGestureRecognizer accumulatedMovement];
-[_UIExclusiveTouchGestureRecognizer achievedMaximumAbsoluteAccumulatedMovement];
```
