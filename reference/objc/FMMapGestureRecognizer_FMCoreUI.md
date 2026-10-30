# `FMMapGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/FMCoreUI.framework/FMCoreUI`](../userland/System__Library__PrivateFrameworks__FMCoreUI.framework__FMCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 14 instance variables, 14 properties, 41 instance methods, 0 class methods

## Instance variables

```
B _isSwipeEnabled;
B _isTrackingTouches;
B _isSwipingFromTheEdge;
B _isSwipingGestureEnded;
B _isRTLOrientation;
i _touchRadius;
@"<FMMapGestureRecognizerDelegate>" _touchDelegate;
@"UITouch" _previousTouch;
d _swipeThreshold;
d _velocity;
@"NSMutableArray" _otherGestures;
@"NSTimer" _doubleTapTimer;
{CGPoint="x"d"y"d} _initialTouchLocation;
{CGPoint="x"d"y"d} _lastTouchPoint;
```

## Properties

```
@property (T{CGPoint=dd},N,V_initialTouchLocation) initialTouchLocation;
@property (T@"UITouch",&,N,V_previousTouch) previousTouch;
@property (T{CGPoint=dd},N,V_lastTouchPoint) lastTouchPoint;
@property (Td,N,V_swipeThreshold) swipeThreshold;
@property (Td,N,V_velocity) velocity;
@property (TB,N,V_isTrackingTouches) isTrackingTouches;
@property (TB,N,V_isSwipingFromTheEdge) isSwipingFromTheEdge;
@property (TB,N,V_isSwipingGestureEnded) isSwipingGestureEnded;
@property (TB,N,V_isRTLOrientation) isRTLOrientation;
@property (T@"NSMutableArray",&,N,V_otherGestures) otherGestures;
@property (T@"NSTimer",&,N,V_doubleTapTimer) doubleTapTimer;
@property (T@"<FMMapGestureRecognizerDelegate>",W,N,V_touchDelegate) touchDelegate;
@property (Ti,N,V_touchRadius) touchRadius;
@property (TB,N,V_isSwipeEnabled) isSwipeEnabled;
```

## Instance methods

```
-[FMMapGestureRecognizer canPreventGestureRecognizer:];
-[FMMapGestureRecognizer touchesEnded:withEvent:];
-[FMMapGestureRecognizer initialTouchLocation];
-[FMMapGestureRecognizer canBePreventedByGestureRecognizer:];
-[FMMapGestureRecognizer touchesCancelled:withEvent:];
-[FMMapGestureRecognizer setInitialTouchLocation:];
-[FMMapGestureRecognizer init];
-[FMMapGestureRecognizer dealloc];
-[FMMapGestureRecognizer reset];
-[FMMapGestureRecognizer velocity];
-[FMMapGestureRecognizer touchesBegan:withEvent:];
-[FMMapGestureRecognizer touchesMoved:withEvent:];
-[FMMapGestureRecognizer touchDelegate];
-[FMMapGestureRecognizer setTouchDelegate:];
-[FMMapGestureRecognizer setVelocity:];
-[FMMapGestureRecognizer previousTouch];
-[FMMapGestureRecognizer isTrackingTouches];
-[FMMapGestureRecognizer lastTouchPoint];
-[FMMapGestureRecognizer setLastTouchPoint:];
-[FMMapGestureRecognizer setTouchRadius:];
-[FMMapGestureRecognizer distanceBetweenPointA:andPointB:];
-[FMMapGestureRecognizer doubleTapTimer];
-[FMMapGestureRecognizer finishSwipeGesture:];
-[FMMapGestureRecognizer invalidateGesture];
-[FMMapGestureRecognizer isRTLOrientation];
-[FMMapGestureRecognizer isSwipeEnabled];
-[FMMapGestureRecognizer isSwipingFromTheEdge];
-[FMMapGestureRecognizer isSwipingGestureEnded];
-[FMMapGestureRecognizer mapTappedTimer];
-[FMMapGestureRecognizer otherGestures];
-[FMMapGestureRecognizer setDoubleTapTimer:];
-[FMMapGestureRecognizer setIsRTLOrientation:];
-[FMMapGestureRecognizer setIsSwipeEnabled:];
-[FMMapGestureRecognizer setIsSwipingFromTheEdge:];
-[FMMapGestureRecognizer setIsSwipingGestureEnded:];
-[FMMapGestureRecognizer setIsTrackingTouches:];
-[FMMapGestureRecognizer setOtherGestures:];
-[FMMapGestureRecognizer setPreviousTouch:];
-[FMMapGestureRecognizer setSwipeThreshold:];
-[FMMapGestureRecognizer swipeThreshold];
-[FMMapGestureRecognizer touchRadius];
```
