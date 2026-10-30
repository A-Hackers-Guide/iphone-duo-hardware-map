# `SBOutwardSwipeGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 5 instance variables, 1 properties, 8 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _startLocation;
{CGVector="dx"d"dy"d} _outwardDirection;
d _startTime;
B _tracking;
Q _numberOfTouchesRequired;
```

## Properties

```
@property (TQ,N,V_numberOfTouchesRequired) numberOfTouchesRequired;
```

## Instance methods

```
-[SBOutwardSwipeGestureRecognizer touchesEnded:withEvent:];
-[SBOutwardSwipeGestureRecognizer touchesCancelled:withEvent:];
-[SBOutwardSwipeGestureRecognizer reset];
-[SBOutwardSwipeGestureRecognizer touchesBegan:withEvent:];
-[SBOutwardSwipeGestureRecognizer touchesMoved:withEvent:];
-[SBOutwardSwipeGestureRecognizer initWithTarget:action:];
-[SBOutwardSwipeGestureRecognizer setNumberOfTouchesRequired:];
-[SBOutwardSwipeGestureRecognizer numberOfTouchesRequired];
```
