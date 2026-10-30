# `_UIKBProductivityPinchGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 16 instance variables, 10 properties, 35 instance methods, 1 class methods

## Instance variables

```
B _recognized;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _transform;
@ _transformAnalyzer;
B _hasFailedOnOtherDominantMotion;
Q _numberOfTouchesRequired;
B _multitouchTimerEnabled;
B _tooMuchSingleMovement;
d _avgTouchesToCentroidDistance;
q _pinchDirection;
d _beginPinchTimestamp;
d _beforeReductionTimeInterval;
d _beginPerimeter;
@"NSMutableArray" _activeTouches;
d _allowableElapsedTimeForAllRequiredTouches;
@"NSMutableDictionary" _beginTouchLocations;
{CGPoint="x"d"y"d} _beginCentroid;
```

## Properties

```
@property (Td,N,V_beginPinchTimestamp) beginPinchTimestamp;
@property (Td,N,V_beforeReductionTimeInterval) beforeReductionTimeInterval;
@property (Td,N,V_beginPerimeter) beginPerimeter;
@property (T{CGPoint=dd},N,V_beginCentroid) beginCentroid;
@property (T@"NSMutableArray",&,N,V_activeTouches) activeTouches;
@property (Td,N,V_allowableElapsedTimeForAllRequiredTouches) allowableElapsedTimeForAllRequiredTouches;
@property (T@"NSMutableDictionary",&,N,V_beginTouchLocations) beginTouchLocations;
@property (TB,N,V_tooMuchSingleMovement) tooMuchSingleMovement;
@property (Td,R,N,V_avgTouchesToCentroidDistance) avgTouchesToCentroidDistance;
@property (Tq,R,N,V_pinchDirection) pinchDirection;
```

## Class methods

```
+[_UIKBProductivityPinchGestureRecognizer productivityPinchGestureRecognizerWithTarget:action:delegate:];
```

## Instance methods

```
-[_UIKBProductivityPinchGestureRecognizer touchesEnded:withEvent:];
-[_UIKBProductivityPinchGestureRecognizer setActiveTouches:];
-[_UIKBProductivityPinchGestureRecognizer touchesCancelled:withEvent:];
-[_UIKBProductivityPinchGestureRecognizer tooMuchSingleMovement];
-[_UIKBProductivityPinchGestureRecognizer setBeginPerimeter:];
-[_UIKBProductivityPinchGestureRecognizer beginCentroid];
-[_UIKBProductivityPinchGestureRecognizer sufficientMotionInDirection:withLocation:withScale:withAngle:];
-[_UIKBProductivityPinchGestureRecognizer multitouchExpired:];
-[_UIKBProductivityPinchGestureRecognizer beginPerimeter];
-[_UIKBProductivityPinchGestureRecognizer pinchDirection];
-[_UIKBProductivityPinchGestureRecognizer reset];
-[_UIKBProductivityPinchGestureRecognizer setBeforeReductionTimeInterval:];
-[_UIKBProductivityPinchGestureRecognizer touchesBegan:withEvent:];
-[_UIKBProductivityPinchGestureRecognizer touchesMoved:withEvent:];
-[_UIKBProductivityPinchGestureRecognizer beginPinchTimestamp];
-[_UIKBProductivityPinchGestureRecognizer initWithTarget:action:];
-[_UIKBProductivityPinchGestureRecognizer setBeginCentroid:];
-[_UIKBProductivityPinchGestureRecognizer setTooMuchSingleMovement:];
-[_UIKBProductivityPinchGestureRecognizer scale];
-[_UIKBProductivityPinchGestureRecognizer startMultitouchTimer:];
-[_UIKBProductivityPinchGestureRecognizer beforeReductionTimeInterval];
-[_UIKBProductivityPinchGestureRecognizer clearMultitouchTimer];
-[_UIKBProductivityPinchGestureRecognizer setBeginPinchTimestamp:];
-[_UIKBProductivityPinchGestureRecognizer beginTouchLocations];
-[_UIKBProductivityPinchGestureRecognizer perimeterOfTouches:];
-[_UIKBProductivityPinchGestureRecognizer allowableElapsedTimeForAllRequiredTouches];
-[_UIKBProductivityPinchGestureRecognizer centroidOfTouches:];
-[_UIKBProductivityPinchGestureRecognizer activeTouches];
-[_UIKBProductivityPinchGestureRecognizer pinchDirectionWithCurrentTime:perimeter:];
-[_UIKBProductivityPinchGestureRecognizer avgDistanceToCentroid:];
-[_UIKBProductivityPinchGestureRecognizer initWithCoder:];
-[_UIKBProductivityPinchGestureRecognizer _updateTransformAnalyzerWeights];
-[_UIKBProductivityPinchGestureRecognizer avgTouchesToCentroidDistance];
-[_UIKBProductivityPinchGestureRecognizer setBeginTouchLocations:];
-[_UIKBProductivityPinchGestureRecognizer setAllowableElapsedTimeForAllRequiredTouches:];
```
