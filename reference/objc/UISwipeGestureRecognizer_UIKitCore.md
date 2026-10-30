# `UISwipeGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- Protocols: `_UIScrollEventRespondable`
- 19 instance variables, 7 properties, 22 instance methods, 3 class methods

## Instance variables

```
d _maximumDuration;
d _minimumPrimaryMovement;
d _maximumPrimaryMovement;
d _minimumSecondaryMovement;
d _maximumSecondaryMovement;
d _maximumOppositeMovement;
d _minimumPrimaryMovementRate;
d _rateOfMinimumMovementDecay;
d _rateOfMaximumMovementDecay;
Q _numberOfTouchesRequired;
@"NSMutableArray" _touches;
Q _direction;
{CGPoint="x"d"y"d} _startLocation;
{CGPoint="x"d"y"d} _previousLocation;
^{CGPoint=dd} _startLocations;
d _startTime;
^{CGPoint=dd} _previousLocations;
d _previousTime;
@"NSString" _pendingFailureReason;
```

## Properties

```
@property (Td,N,V_maximumDuration) maximumDuration;
@property (TQ,N,V_numberOfTouchesRequired) numberOfTouchesRequired;
@property (TQ,N,V_direction) direction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISwipeGestureRecognizer supportsSecureCoding];
+[UISwipeGestureRecognizer _supportsDefaultTouchTypes];
+[UISwipeGestureRecognizer _supportsDefaultPressTypes];
```

## Instance methods

```
-[UISwipeGestureRecognizer touchesEnded:withEvent:];
-[UISwipeGestureRecognizer shouldReceiveEvent:];
-[UISwipeGestureRecognizer _scrollingChangedWithEvent:];
-[UISwipeGestureRecognizer _resetGestureRecognizer];
-[UISwipeGestureRecognizer touchesCancelled:withEvent:];
-[UISwipeGestureRecognizer _isGestureType:];
-[UISwipeGestureRecognizer dealloc];
-[UISwipeGestureRecognizer maximumDuration];
-[UISwipeGestureRecognizer numberOfTouches];
-[UISwipeGestureRecognizer setDirection:];
-[UISwipeGestureRecognizer touchesBegan:withEvent:];
-[UISwipeGestureRecognizer touchesMoved:withEvent:];
-[UISwipeGestureRecognizer initWithTarget:action:];
-[UISwipeGestureRecognizer locationInView:];
-[UISwipeGestureRecognizer direction];
-[UISwipeGestureRecognizer setNumberOfTouchesRequired:];
-[UISwipeGestureRecognizer encodeWithCoder:];
-[UISwipeGestureRecognizer setMaximumDuration:];
-[UISwipeGestureRecognizer initWithCoder:];
-[UISwipeGestureRecognizer numberOfTouchesRequired];
-[UISwipeGestureRecognizer _appendSubclassDescription:];
-[UISwipeGestureRecognizer locationOfTouch:inView:];
```
