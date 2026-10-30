# `_UITouchDownGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 4 instance variables, 1 properties, 14 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _locationInView;
{CGPoint="x"d"y"d} _initialLocationInScreenSpace;
@"UIDelayedAction" _activationDelay;
d _allowableMovement;
```

## Properties

```
@property (Td,N,V_allowableMovement) allowableMovement;
```

## Instance methods

```
-[_UITouchDownGestureRecognizer allowableMovement];
-[_UITouchDownGestureRecognizer touchesEnded:withEvent:];
-[_UITouchDownGestureRecognizer touchesCancelled:withEvent:];
-[_UITouchDownGestureRecognizer setAllowableMovement:];
-[_UITouchDownGestureRecognizer recognizeOrFailForCurrentLocation];
-[_UITouchDownGestureRecognizer reset];
-[_UITouchDownGestureRecognizer locationIsMostlyInsideView:];
-[_UITouchDownGestureRecognizer cancelActivationDelay];
-[_UITouchDownGestureRecognizer touchesBegan:withEvent:];
-[_UITouchDownGestureRecognizer touchesMoved:withEvent:];
-[_UITouchDownGestureRecognizer initWithTarget:action:];
-[_UITouchDownGestureRecognizer locationInView:];
-[_UITouchDownGestureRecognizer activationDelayHandler];
-[_UITouchDownGestureRecognizer gestureIsStillValid];
```
