# `SBCornerFingerPanGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBScreenEdgePanGestureRecognizer`
- 5 instance variables, 1 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"SBTouchHistory" _touchHistory;
Q _corner;
q _touchInterfaceOrientationWhenGestureBegan;
{CGPoint="x"d"y"d} _firstTouchReferenceLocation;
@"SBCornerFingerGestureClassifier" _classifier;
```

## Properties

```
@property (TQ,R,N,V_corner) corner;
```

## Instance methods

```
-[SBCornerFingerPanGestureRecognizer _SBLogTouchesWithMethodName:withMethodName:];
-[SBCornerFingerPanGestureRecognizer _touchInterfaceOrientation];
-[SBCornerFingerPanGestureRecognizer _shouldBegin];
-[SBCornerFingerPanGestureRecognizer touchesEnded:withEvent:];
-[SBCornerFingerPanGestureRecognizer edges];
-[SBCornerFingerPanGestureRecognizer setState:];
-[SBCornerFingerPanGestureRecognizer _convertReferenceLocation:toOrientedLocation:orientedBounds:];
-[SBCornerFingerPanGestureRecognizer setEdges:];
-[SBCornerFingerPanGestureRecognizer initWithTarget:action:corner:classifier:];
-[SBCornerFingerPanGestureRecognizer reset];
-[SBCornerFingerPanGestureRecognizer touchesBegan:withEvent:];
-[SBCornerFingerPanGestureRecognizer touchesMoved:withEvent:];
-[SBCornerFingerPanGestureRecognizer _convertReferenceVector:toCorner:orientation:];
-[SBCornerFingerPanGestureRecognizer corner];
```
