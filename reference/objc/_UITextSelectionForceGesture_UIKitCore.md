# `_UITextSelectionForceGesture`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UILongPressGestureRecognizer`
- 13 instance variables, 13 properties, 43 instance methods, 0 class methods

## Instance variables

```
B _shouldFailWithoutForce;
B _didLongPress;
B _touchEclipsesVelocity;
@"UIKBPanGestureVelocitySample" _velocitySample;
@"UIKBPanGestureVelocitySample" _previousVelocitySample;
@"UIKBPanGestureVelocitySample" _liftOffSample;
d _increasingForceTimestamp;
d _lastTouchTime;
q _liftOffState;
q _increasingForceState;
{CGPoint="x"d"y"d} _lastSceneReferenceLocation;
{CGPoint="x"d"y"d} _lastUnadjustedSceneReferenceLocation;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _velocityRange;
```

## Properties

```
@property (TB,N,V_didLongPress) didLongPress;
@property (T@"UIKBPanGestureVelocitySample",R,G_velocitySample,V_velocitySample) _velocitySample;
@property (T@"UIKBPanGestureVelocitySample",R,G_previousVelocitySample,V_previousVelocitySample) _previousVelocitySample;
@property (T@"UIKBPanGestureVelocitySample",R,G_liftOffSample,V_liftOffSample) _liftOffSample;
@property (Td,N,V_increasingForceTimestamp) increasingForceTimestamp;
@property (Td,N,V_lastTouchTime) lastTouchTime;
@property (T{CGPoint=dd},N,V_lastSceneReferenceLocation) lastSceneReferenceLocation;
@property (T{CGPoint=dd},N,V_lastUnadjustedSceneReferenceLocation) lastUnadjustedSceneReferenceLocation;
@property (Tq,N,V_liftOffState) liftOffState;
@property (Tq,N,V_increasingForceState) increasingForceState;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_velocityRange) velocityRange;
@property (TB,N,V_touchEclipsesVelocity) touchEclipsesVelocity;
@property (TB,N,V_shouldFailWithoutForce) shouldFailWithoutForce;
```

## Instance methods

```
-[_UITextSelectionForceGesture touchesEnded:withEvent:];
-[_UITextSelectionForceGesture velocityInView:];
-[_UITextSelectionForceGesture touchesCancelled:withEvent:];
-[_UITextSelectionForceGesture enoughTimeElapsed:];
-[_UITextSelectionForceGesture reset];
-[_UITextSelectionForceGesture touchesBegan:withEvent:];
-[_UITextSelectionForceGesture touchesMoved:withEvent:];
-[_UITextSelectionForceGesture initWithTarget:action:];
-[_UITextSelectionForceGesture didLongPress];
-[_UITextSelectionForceGesture _adjustSceneReferenceLocation:];
-[_UITextSelectionForceGesture setVelocityRange:];
-[_UITextSelectionForceGesture velocityRange];
-[_UITextSelectionForceGesture _velocitySample];
-[_UITextSelectionForceGesture _centroidInView:];
-[_UITextSelectionForceGesture _centroidMovedTo:atTime:physicalTouch:];
-[_UITextSelectionForceGesture _convertVelocitySample:fromSceneReferenceCoordinatesToView:];
-[_UITextSelectionForceGesture _liftOffSample];
-[_UITextSelectionForceGesture _locationOfTouches:];
-[_UITextSelectionForceGesture _offsetInViewFromSceneReferenceLocation:toSceneReferenceLocation:];
-[_UITextSelectionForceGesture _previousVelocitySample];
-[_UITextSelectionForceGesture _resetVelocitySamples];
-[_UITextSelectionForceGesture _shiftPanLocationToNewSceneReferenceLocation:];
-[_UITextSelectionForceGesture _shouldDelayUntilForceLevelRequirementIsMet];
-[_UITextSelectionForceGesture _updateLiftOffState];
-[_UITextSelectionForceGesture forceHasIncreasedForTimeInterval:];
-[_UITextSelectionForceGesture increasingForceState];
-[_UITextSelectionForceGesture increasingForceTimestamp];
-[_UITextSelectionForceGesture lastSceneReferenceLocation];
-[_UITextSelectionForceGesture lastTouchTime];
-[_UITextSelectionForceGesture lastUnadjustedSceneReferenceLocation];
-[_UITextSelectionForceGesture liftOffState];
-[_UITextSelectionForceGesture setDidLongPress:];
-[_UITextSelectionForceGesture setIncreasingForceState:];
-[_UITextSelectionForceGesture setIncreasingForceTimestamp:];
-[_UITextSelectionForceGesture setLastSceneReferenceLocation:];
-[_UITextSelectionForceGesture setLastTouchTime:];
-[_UITextSelectionForceGesture setLastUnadjustedSceneReferenceLocation:];
-[_UITextSelectionForceGesture setLiftOffState:];
-[_UITextSelectionForceGesture setShouldFailWithoutForce:];
-[_UITextSelectionForceGesture setTouchEclipsesVelocity:];
-[_UITextSelectionForceGesture shouldFailWithoutForce];
-[_UITextSelectionForceGesture shouldResetRangeForVelocity:previousVelocity:];
-[_UITextSelectionForceGesture touchEclipsesVelocity];
```
