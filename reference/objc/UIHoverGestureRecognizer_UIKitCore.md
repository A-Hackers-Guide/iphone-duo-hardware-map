# `UIHoverGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 5 instance variables, 12 properties, 40 instance methods, 0 class methods

## Instance variables

```
@"UIHoverEvent" _currentHoverEvent;
@"UITouch" _currentTouch;
B _pausesWhilePanning;
q _previousTrackpadFingerDownCount;
q _trackpadFingerDownCount;
```

## Properties

```
@property (TB,N,G_pausesWhilePanning,S_setPausesWhilePanning:,V_pausesWhilePanning) pausesWhilePanning;
@property (Td,R,N) _hoverHeight;
@property (Td,R,N) _maximumHoverHeight;
@property (Td,R,N) _hoverTouchTimestamp;
@property (Tq,R,N,G_previousTrackpadFingerDownCount,V_previousTrackpadFingerDownCount) previousTrackpadFingerDownCount;
@property (Tq,R,N,G_trackpadFingerDownCount,V_trackpadFingerDownCount) trackpadFingerDownCount;
@property (Td,R,N) _zOffset;
@property (Td,R,N) _altitudeAngle;
@property (Td,R,N) _rollAngle;
@property (Td,R,N) zOffset;
@property (Td,R,N) altitudeAngle;
@property (Td,R,N) rollAngle;
```

## Instance methods

```
-[UIHoverGestureRecognizer canPreventGestureRecognizer:];
-[UIHoverGestureRecognizer _hoverMoved:withEvent:];
-[UIHoverGestureRecognizer _shouldReceivePress:];
-[UIHoverGestureRecognizer _hoverEntered:withEvent:];
-[UIHoverGestureRecognizer _hoverCancelled:withEvent:];
-[UIHoverGestureRecognizer _acceptsBeingFailureRequirementForGestureRecognizer:];
-[UIHoverGestureRecognizer setAllowedTouchTypes:];
-[UIHoverGestureRecognizer canBePreventedByGestureRecognizer:];
-[UIHoverGestureRecognizer _acceptsBeingFailureDependentOnGestureRecognizer:];
-[UIHoverGestureRecognizer _shouldReceiveTouch:withEvent:];
-[UIHoverGestureRecognizer _canCancelGestureRecognizer:];
-[UIHoverGestureRecognizer reset];
-[UIHoverGestureRecognizer _hoverExited:withEvent:];
-[UIHoverGestureRecognizer initWithTarget:action:];
-[UIHoverGestureRecognizer locationInView:];
-[UIHoverGestureRecognizer _trackpadFingerDownCount];
-[UIHoverGestureRecognizer rollAngle];
-[UIHoverGestureRecognizer _shouldReceiveEvent:];
-[UIHoverGestureRecognizer _canBeCancelledByGestureRecognizer:];
-[UIHoverGestureRecognizer _resetInternalState];
-[UIHoverGestureRecognizer zOffset];
-[UIHoverGestureRecognizer _altitudeAngle];
-[UIHoverGestureRecognizer _azimuthAngleInView:];
-[UIHoverGestureRecognizer _azimuthUnitVectorInView:];
-[UIHoverGestureRecognizer _hoverHeight];
-[UIHoverGestureRecognizer _hoverTouchTimestamp];
-[UIHoverGestureRecognizer _isPaused];
-[UIHoverGestureRecognizer _location3DInView:];
-[UIHoverGestureRecognizer _maximumHoverHeight];
-[UIHoverGestureRecognizer _pausesWhilePanning];
-[UIHoverGestureRecognizer _preciseLocationInView:];
-[UIHoverGestureRecognizer _previousTrackpadFingerDownCount];
-[UIHoverGestureRecognizer _rollAngle];
-[UIHoverGestureRecognizer _setPausesWhilePanning:];
-[UIHoverGestureRecognizer _wantsHoverEventsWhilePointerIsLocked];
-[UIHoverGestureRecognizer _zOffset];
-[UIHoverGestureRecognizer altitudeAngle];
-[UIHoverGestureRecognizer azimuthAngleInView:];
-[UIHoverGestureRecognizer azimuthUnitVectorInView:];
-[UIHoverGestureRecognizer setRequiresExclusiveTouchType:];
```
