# `UIDragRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 11 instance variables, 10 properties, 30 instance methods, 2 class methods

## Instance variables

```
d _maximumDeviation;
d _minimumDistance;
{CGPoint="x"d"y"d} _startPosition;
B _restrictsToAngle;
d _angle;
@"UITouch" _touch;
@"UIDelayedAction" _tooSlow;
d _startAngle;
d _quietPeriod;
B _canBeginDrag;
@"UIDelayedAction" ignoreTouch;
```

## Properties

```
@property (T{CGPoint=dd},N,V_startPosition) startPosition;
@property (Td,N,V_startAngle) startAngle;
@property (T@"UITouch",&,N,V_touch) touch;
@property (T@"UIDelayedAction",&,N,VignoreTouch) ignoreTouch;
@property (TB,N,V_restrictsToAngle) restrictsToAngle;
@property (Td,N,V_angle) angle;
@property (Td,N,V_maximumDeviation) maximumDeviation;
@property (Td,N,V_minimumDistance) minimumDistance;
@property (Td,N,V_quietPeriod) quietPeriod;
@property (TB,N,V_canBeginDrag) canBeginDrag;
```

## Class methods

```
+[UIDragRecognizer _supportsDefaultTouchTypes];
+[UIDragRecognizer _supportsDefaultPressTypes];
```

## Instance methods

```
-[UIDragRecognizer setAngle:];
-[UIDragRecognizer angle];
-[UIDragRecognizer tooSlow:];
-[UIDragRecognizer touchesEnded:withEvent:];
-[UIDragRecognizer touch];
-[UIDragRecognizer _resetGestureRecognizer];
-[UIDragRecognizer clearTimer];
-[UIDragRecognizer touchesCancelled:withEvent:];
-[UIDragRecognizer dealloc];
-[UIDragRecognizer setTouch:];
-[UIDragRecognizer touchesBegan:withEvent:];
-[UIDragRecognizer touchesMoved:withEvent:];
-[UIDragRecognizer initWithTarget:action:];
-[UIDragRecognizer setStartAngle:];
-[UIDragRecognizer startAngle];
-[UIDragRecognizer minimumDistance];
-[UIDragRecognizer setIgnoreTouch:];
-[UIDragRecognizer setQuietPeriod:];
-[UIDragRecognizer canBeginDrag];
-[UIDragRecognizer clearIgnoreTouch];
-[UIDragRecognizer ignoreTouch];
-[UIDragRecognizer maximumDeviation];
-[UIDragRecognizer quietPeriod];
-[UIDragRecognizer restrictsToAngle];
-[UIDragRecognizer setCanBeginDrag:];
-[UIDragRecognizer setMaximumDeviation:];
-[UIDragRecognizer setMinimumDistance:];
-[UIDragRecognizer setRestrictsToAngle:];
-[UIDragRecognizer setStartPosition:];
-[UIDragRecognizer startPosition];
```
