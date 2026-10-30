# `SBCornerPencilPanGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBScreenEdgePanGestureRecognizer`
- Protocols: `PTSettingsKeyObserver`
- 5 instance variables, 5 properties, 16 instance methods, 3 class methods

## Instance variables

```
@"SBTouchHistory" _touchHistory;
Q _corner;
d _cornerHorizontalEdgeLength;
d _cornerVerticalEdgeLength;
q _touchInterfaceOrientationWhenGestureBegan;
```

## Properties

```
@property (TQ,R,N,V_corner) corner;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBCornerPencilPanGestureRecognizer _edgesForCorner:];
+[SBCornerPencilPanGestureRecognizer _shouldSupportStylusTouches];
+[SBCornerPencilPanGestureRecognizer interactiveCornerPanGestureRecognizerWithSettings:corner:target:action:];
```

## Instance methods

```
-[SBCornerPencilPanGestureRecognizer _SBLogTouchesWithMethodName:withMethodName:];
-[SBCornerPencilPanGestureRecognizer _touchInterfaceOrientation];
-[SBCornerPencilPanGestureRecognizer touchesEnded:withEvent:];
-[SBCornerPencilPanGestureRecognizer _updateSettingsDerivedValues:];
-[SBCornerPencilPanGestureRecognizer setState:];
-[SBCornerPencilPanGestureRecognizer _convertReferenceLocation:toOrientedLocation:orientedBounds:];
-[SBCornerPencilPanGestureRecognizer setEdges:];
-[SBCornerPencilPanGestureRecognizer _edgeOffsets];
-[SBCornerPencilPanGestureRecognizer reset];
-[SBCornerPencilPanGestureRecognizer shouldReceiveTouch:];
-[SBCornerPencilPanGestureRecognizer _initWithSettings:corner:target:action:type:options:];
-[SBCornerPencilPanGestureRecognizer touchesBegan:withEvent:];
-[SBCornerPencilPanGestureRecognizer touchesMoved:withEvent:];
-[SBCornerPencilPanGestureRecognizer settings:changedValueForKey:];
-[SBCornerPencilPanGestureRecognizer _isOrientedLocation:inCorner:forOrientedBounds:withEdgeOffsets:];
-[SBCornerPencilPanGestureRecognizer corner];
```
