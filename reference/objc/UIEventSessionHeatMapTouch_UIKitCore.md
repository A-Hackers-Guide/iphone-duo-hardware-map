# `UIEventSessionHeatMapTouch`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 10 properties, 18 instance methods, 0 class methods

## Instance variables

```
q _upDownState;
q _tapDragState;
d _dragDistance;
@"NSDate" _touchDownTime;
@"NSDate" _touchUpTime;
{CGPoint="x"d"y"d} _lastLocation;
{?="row"q"column"q"touchType"q"isValid"B} _lastVisitedCoordinate;
```

## Properties

```
@property (Tq,N,V_upDownState) upDownState;
@property (Tq,N,V_tapDragState) tapDragState;
@property (Td,N,V_dragDistance) dragDistance;
@property (Tq,R,N) dragDistanceForAnalytics;
@property (T{CGPoint=dd},N,V_lastLocation) lastLocation;
@property (T{?=qqqB},N,V_lastVisitedCoordinate) lastVisitedCoordinate;
@property (T@"NSDate",&,N,V_touchDownTime) touchDownTime;
@property (T@"NSDate",&,N,V_touchUpTime) touchUpTime;
@property (Td,R,N) touchDownDuration;
@property (Tq,R,N) touchDownDurationMS;
```

## Instance methods

```
-[UIEventSessionHeatMapTouch setLastLocation:];
-[UIEventSessionHeatMapTouch lastLocation];
-[UIEventSessionHeatMapTouch init];
-[UIEventSessionHeatMapTouch setTouchUpTime:];
-[UIEventSessionHeatMapTouch setUpDownState:];
-[UIEventSessionHeatMapTouch dragDistance];
-[UIEventSessionHeatMapTouch dragDistanceForAnalytics];
-[UIEventSessionHeatMapTouch lastVisitedCoordinate];
-[UIEventSessionHeatMapTouch setDragDistance:];
-[UIEventSessionHeatMapTouch setLastVisitedCoordinate:];
-[UIEventSessionHeatMapTouch setTapDragState:];
-[UIEventSessionHeatMapTouch setTouchDownTime:];
-[UIEventSessionHeatMapTouch tapDragState];
-[UIEventSessionHeatMapTouch touchDownDuration];
-[UIEventSessionHeatMapTouch touchDownDurationMS];
-[UIEventSessionHeatMapTouch touchDownTime];
-[UIEventSessionHeatMapTouch touchUpTime];
-[UIEventSessionHeatMapTouch upDownState];
```
