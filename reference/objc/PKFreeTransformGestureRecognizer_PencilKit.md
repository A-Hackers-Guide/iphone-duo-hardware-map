# `PKFreeTransformGestureRecognizer`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 18 instance variables, 23 properties, 54 instance methods, 0 class methods

## Instance variables

```
B _allowSingleTouchDrag;
B _axisAligned;
B _canBegin;
B _isScaling;
B _isPanning;
d _startThreshold;
d _scaleThreshold;
d _cancelThreshold;
Q _allowedPanEdges;
d _minScale;
d _maxScale;
d _scaleDamping;
d _previousScale;
@"NSMutableOrderedSet" _touches;
d _deltaScale;
@"NSMapTable" _touchStartLocations;
@"NSMapTable" _actualTouchStartLocations;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _accumulatedTransform;
```

## Properties

```
@property (TB,N,V_canBegin) canBegin;
@property (TB,N,V_isScaling) isScaling;
@property (TB,N,V_isPanning) isPanning;
@property (Td,N,V_previousScale) previousScale;
@property (Td,N,V_deltaScale) deltaScale;
@property (T{CGAffineTransform=dddddd},N,V_accumulatedTransform) accumulatedTransform;
@property (T@"NSMapTable",&,N,V_touchStartLocations) touchStartLocations;
@property (T@"NSMapTable",&,N,V_actualTouchStartLocations) actualTouchStartLocations;
@property (Td,N,V_startThreshold) startThreshold;
@property (Td,N,V_scaleThreshold) scaleThreshold;
@property (Td,N,V_cancelThreshold) cancelThreshold;
@property (TQ,N,V_allowedPanEdges) allowedPanEdges;
@property (TB,N,V_allowSingleTouchDrag) allowSingleTouchDrag;
@property (TB,N,V_axisAligned) axisAligned;
@property (Td,N,V_minScale) minScale;
@property (Td,N,V_maxScale) maxScale;
@property (Td,N,V_scaleDamping) scaleDamping;
@property (TB,R,N) scaleIsGrowing;
@property (TB,R,N) scaleIsShrinking;
@property (Td,R,N) scale;
@property (T{CGAffineTransform=dddddd},R,N) freeTransform;
@property (T{CGAffineTransform=dddddd},R,N) unscaledFreeTransform;
@property (T@"NSMutableOrderedSet",R,N,V_touches) touches;
```

## Instance methods

```
-[PKFreeTransformGestureRecognizer touchesEnded:withEvent:];
-[PKFreeTransformGestureRecognizer touchesCancelled:withEvent:];
-[PKFreeTransformGestureRecognizer clearTouches];
-[PKFreeTransformGestureRecognizer touches];
-[PKFreeTransformGestureRecognizer minScale];
-[PKFreeTransformGestureRecognizer reset];
-[PKFreeTransformGestureRecognizer setMaxScale:];
-[PKFreeTransformGestureRecognizer touchesBegan:withEvent:];
-[PKFreeTransformGestureRecognizer touchesMoved:withEvent:];
-[PKFreeTransformGestureRecognizer initWithTarget:action:];
-[PKFreeTransformGestureRecognizer locationInView:];
-[PKFreeTransformGestureRecognizer setIsPanning:];
-[PKFreeTransformGestureRecognizer scale];
-[PKFreeTransformGestureRecognizer setMinScale:];
-[PKFreeTransformGestureRecognizer maxScale];
-[PKFreeTransformGestureRecognizer isPanning];
-[PKFreeTransformGestureRecognizer isScaling];
-[PKFreeTransformGestureRecognizer scaleThreshold];
-[PKFreeTransformGestureRecognizer setScaleThreshold:];
-[PKFreeTransformGestureRecognizer setStartThreshold:];
-[PKFreeTransformGestureRecognizer startThreshold];
-[PKFreeTransformGestureRecognizer allowedPanEdges];
-[PKFreeTransformGestureRecognizer cancelThreshold];
-[PKFreeTransformGestureRecognizer setAxisAligned:];
-[PKFreeTransformGestureRecognizer touchesMovedPastScaleThreshold:];
-[PKFreeTransformGestureRecognizer accumulatedTransform];
-[PKFreeTransformGestureRecognizer actualTouchStartLocations];
-[PKFreeTransformGestureRecognizer allowSingleTouchDrag];
-[PKFreeTransformGestureRecognizer axisAligned];
-[PKFreeTransformGestureRecognizer canBegin];
-[PKFreeTransformGestureRecognizer clampTransform:minScale:maxScale:];
-[PKFreeTransformGestureRecognizer deltaScale];
-[PKFreeTransformGestureRecognizer freeTransform];
-[PKFreeTransformGestureRecognizer previousScale];
-[PKFreeTransformGestureRecognizer resetAndAccumulateTransform];
-[PKFreeTransformGestureRecognizer resetStartingTouches];
-[PKFreeTransformGestureRecognizer scaleDamping];
-[PKFreeTransformGestureRecognizer scaleIsGrowing];
-[PKFreeTransformGestureRecognizer scaleIsShrinking];
-[PKFreeTransformGestureRecognizer setAccumulatedTransform:];
-[PKFreeTransformGestureRecognizer setActualTouchStartLocations:];
-[PKFreeTransformGestureRecognizer setAllowSingleTouchDrag:];
-[PKFreeTransformGestureRecognizer setAllowedPanEdges:];
-[PKFreeTransformGestureRecognizer setCanBegin:];
-[PKFreeTransformGestureRecognizer setCancelThreshold:];
-[PKFreeTransformGestureRecognizer setDeltaScale:];
-[PKFreeTransformGestureRecognizer setIsScaling:];
-[PKFreeTransformGestureRecognizer setPreviousScale:];
-[PKFreeTransformGestureRecognizer setScaleDamping:];
-[PKFreeTransformGestureRecognizer setTouchStartLocations:];
-[PKFreeTransformGestureRecognizer touchStartLocations];
-[PKFreeTransformGestureRecognizer touchesBegan:withEvent:rejectExcessTouches:];
-[PKFreeTransformGestureRecognizer touchesMovedPastThreshold:];
-[PKFreeTransformGestureRecognizer unscaledFreeTransform];
```
