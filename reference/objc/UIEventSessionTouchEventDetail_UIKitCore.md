# `UIEventSessionTouchEventDetail`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
q _upDownState;
q _tapDragState;
q _windowSection;
d _dragDistanceSquared;
{CGPoint="x"d"y"d} _lastLocation;
```

## Properties

```
@property (Tq,N,V_upDownState) upDownState;
@property (Tq,N,V_tapDragState) tapDragState;
@property (Tq,N,V_windowSection) windowSection;
@property (Td,N,V_dragDistanceSquared) dragDistanceSquared;
@property (T{CGPoint=dd},N,V_lastLocation) lastLocation;
```

## Instance methods

```
-[UIEventSessionTouchEventDetail setLastLocation:];
-[UIEventSessionTouchEventDetail lastLocation];
-[UIEventSessionTouchEventDetail init];
-[UIEventSessionTouchEventDetail setUpDownState:];
-[UIEventSessionTouchEventDetail dragDistanceSquared];
-[UIEventSessionTouchEventDetail setDragDistanceSquared:];
-[UIEventSessionTouchEventDetail setTapDragState:];
-[UIEventSessionTouchEventDetail setWindowSection:];
-[UIEventSessionTouchEventDetail tapDragState];
-[UIEventSessionTouchEventDetail upDownState];
-[UIEventSessionTouchEventDetail windowSection];
```
