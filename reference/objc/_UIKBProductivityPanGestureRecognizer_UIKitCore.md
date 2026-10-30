# `_UIKBProductivityPanGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPanGestureRecognizer`
- 7 instance variables, 7 properties, 23 instance methods, 1 class methods

## Instance variables

```
B _tooMuchSingleMovement;
d _beginPanTimestamp;
@"NSMutableSet" _activeTouches;
@"NSMutableSet" _shiftTouches;
@"_UIGestureRecognizerTransformAnalyzer" _transformAnalyzer;
@"NSMutableDictionary" _beginTouchLocations;
{CGPoint="x"d"y"d} _beginPanCentroid;
```

## Properties

```
@property (Td,N,V_beginPanTimestamp) beginPanTimestamp;
@property (T{CGPoint=dd},N,V_beginPanCentroid) beginPanCentroid;
@property (T@"NSMutableSet",&,N,V_activeTouches) activeTouches;
@property (T@"NSMutableSet",&,N,V_shiftTouches) shiftTouches;
@property (T@"_UIGestureRecognizerTransformAnalyzer",&,N,V_transformAnalyzer) transformAnalyzer;
@property (T@"NSMutableDictionary",&,N,V_beginTouchLocations) beginTouchLocations;
@property (TB,N,V_tooMuchSingleMovement) tooMuchSingleMovement;
```

## Class methods

```
+[_UIKBProductivityPanGestureRecognizer productivityPanGestureRecognizerWithTarget:action:delegate:];
```

## Instance methods

```
-[_UIKBProductivityPanGestureRecognizer touchesEnded:withEvent:];
-[_UIKBProductivityPanGestureRecognizer setActiveTouches:];
-[_UIKBProductivityPanGestureRecognizer beginPanTimestamp];
-[_UIKBProductivityPanGestureRecognizer touchesCancelled:withEvent:];
-[_UIKBProductivityPanGestureRecognizer tooMuchSingleMovement];
-[_UIKBProductivityPanGestureRecognizer shiftTouches];
-[_UIKBProductivityPanGestureRecognizer isShiftOrMoreKeyForTouch:];
-[_UIKBProductivityPanGestureRecognizer reset];
-[_UIKBProductivityPanGestureRecognizer transformAnalyzer];
-[_UIKBProductivityPanGestureRecognizer touchesBegan:withEvent:];
-[_UIKBProductivityPanGestureRecognizer touchesMoved:withEvent:];
-[_UIKBProductivityPanGestureRecognizer initWithTarget:action:];
-[_UIKBProductivityPanGestureRecognizer setTransformAnalyzer:];
-[_UIKBProductivityPanGestureRecognizer setTooMuchSingleMovement:];
-[_UIKBProductivityPanGestureRecognizer setShiftTouches:];
-[_UIKBProductivityPanGestureRecognizer beginTouchLocations];
-[_UIKBProductivityPanGestureRecognizer centroidOfTouches:];
-[_UIKBProductivityPanGestureRecognizer activeTouches];
-[_UIKBProductivityPanGestureRecognizer initWithCoder:];
-[_UIKBProductivityPanGestureRecognizer beginPanCentroid];
-[_UIKBProductivityPanGestureRecognizer setBeginPanCentroid:];
-[_UIKBProductivityPanGestureRecognizer setBeginTouchLocations:];
-[_UIKBProductivityPanGestureRecognizer setBeginPanTimestamp:];
```
