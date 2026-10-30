# `_UIRotaryGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 18 instance variables, 8 properties, 54 instance methods, 0 class methods

## Instance variables

```
{?="delegateRotaryGestureRecognizerCanBeginFromRest"b1"delegateRotaryGestureRecognizerMustBeginFromRest"b1"delegateRotaryGestureRecognizerStartedRestTimer"b1"delegateRotaryGestureRecognizerCancelledRestTimer"b1"delegateRotaryGestureRecognizerBeganClassifyingMovement"b1"delegateRotaryGestureRecognizerUpdatedClassifyingMovement"b1"delegateRotaryGestureRecognizerFailedClassifyingMovement"b1"delegateWasNonNil"b1} _rotaryGestureRecognizerFlags;
B _hasNotifiedDelegateBeganClassifyingMovement;
d _startWheelPosition;
d _currentWheelPosition;
d _rotaryDeadBand;
q _movementClassification;
{CGPoint="x"d"y"d} _touchBeganPoint;
{CGPoint="x"d"y"d} _digitizerLocation;
@"NSMutableArray" _recentRotaryEvents;
@"NSNumber" _delegateMustBeginFromRestValue;
@"NSTimer" _restingTouchBeginTimer;
@"NSTimer" _restingTouchRecoveryTimer;
B _isActivelyTouching;
d _accumulatedDistance;
d _delta;
d _velocity;
q _startRegion;
q _beganMode;
```

## Properties

```
@property (Td,N,V_accumulatedDistance) accumulatedDistance;
@property (Td,N,V_delta) delta;
@property (Td,N,V_velocity) velocity;
@property (TB,N,V_isActivelyTouching) isActivelyTouching;
@property (Tq,N,V_startRegion) startRegion;
@property (Tq,N,V_beganMode) beganMode;
@property (T@"<_UIRotaryGestureRecognizerDelegate>",W,D,N) delegate;
@property (Td,R,N) position;
```

## Instance methods

```
-[_UIRotaryGestureRecognizer touchesEnded:withEvent:];
-[_UIRotaryGestureRecognizer position];
-[_UIRotaryGestureRecognizer touchesCancelled:withEvent:];
-[_UIRotaryGestureRecognizer reset];
-[_UIRotaryGestureRecognizer velocity];
-[_UIRotaryGestureRecognizer touchesBegan:withEvent:];
-[_UIRotaryGestureRecognizer touchesMoved:withEvent:];
-[_UIRotaryGestureRecognizer initWithTarget:action:];
-[_UIRotaryGestureRecognizer setDelegate:];
-[_UIRotaryGestureRecognizer initWithCoder:];
-[_UIRotaryGestureRecognizer setVelocity:];
-[_UIRotaryGestureRecognizer setStartRegion:];
-[_UIRotaryGestureRecognizer _activateRestingTouchRecoveryTimer];
-[_UIRotaryGestureRecognizer _applyDeadbandToValue:];
-[_UIRotaryGestureRecognizer _applyDistanceWeightToValue:];
-[_UIRotaryGestureRecognizer _applyScaleFactor:toValue:fromAngle:toAngle:];
-[_UIRotaryGestureRecognizer _attemptToClassifyWithPreviousLocation:newLocation:];
-[_UIRotaryGestureRecognizer _attemptToStartFromRestingTouch:];
-[_UIRotaryGestureRecognizer _calculateAngleForTouchLocation:];
-[_UIRotaryGestureRecognizer _calculateCurrentWheelPosition];
-[_UIRotaryGestureRecognizer _calculateRadialDistance:];
-[_UIRotaryGestureRecognizer _calculateWheelPositionForTouchLocation:];
-[_UIRotaryGestureRecognizer _deadzoneRangeForCurrentTouchLocation];
-[_UIRotaryGestureRecognizer _deltaForEventInfos:];
-[_UIRotaryGestureRecognizer _directionalMovementClassificationDistanceThreshold];
-[_UIRotaryGestureRecognizer _effectiveCanBeginFromRest];
-[_UIRotaryGestureRecognizer _effectiveMustBeginFromRest];
-[_UIRotaryGestureRecognizer _endGestureFromRestingTouchRecovery:];
-[_UIRotaryGestureRecognizer _enterRecoveryWindowOrEndGestureWithState:];
-[_UIRotaryGestureRecognizer _invalidateRestingTouchBeginTimerIfNecessary];
-[_UIRotaryGestureRecognizer _invalidateRestingTouchRecoveryTimerIfNecessary];
-[_UIRotaryGestureRecognizer _isPoint:inRangeOfCenter:];
-[_UIRotaryGestureRecognizer _isTouchFarEnoughFromCenterToActivateRestingTouch:];
-[_UIRotaryGestureRecognizer _isTouchInRangeOfInitialTouchForRestingTouchActivation:];
-[_UIRotaryGestureRecognizer _movementClassificationAngleThresholdNumerator];
-[_UIRotaryGestureRecognizer _notifyDelegateBeganClassifyingMovementIfNecessary];
-[_UIRotaryGestureRecognizer _notifyDelegateFailedClassifyingMovement];
-[_UIRotaryGestureRecognizer _notifyDelegateRestTimerCancelledIfNecessary:];
-[_UIRotaryGestureRecognizer _notifyDelegateUpdatedClassifyingMovement];
-[_UIRotaryGestureRecognizer _processEvent:];
-[_UIRotaryGestureRecognizer _regionForTouchLocation:];
-[_UIRotaryGestureRecognizer _regionForWheelPosition:];
-[_UIRotaryGestureRecognizer _resetDeadband];
-[_UIRotaryGestureRecognizer _restingTouchRangeForCurrentTouchLocation];
-[_UIRotaryGestureRecognizer _velocityForEventInfos:];
-[_UIRotaryGestureRecognizer accumulatedDistance];
-[_UIRotaryGestureRecognizer beganMode];
-[_UIRotaryGestureRecognizer delta];
-[_UIRotaryGestureRecognizer isActivelyTouching];
-[_UIRotaryGestureRecognizer setAccumulatedDistance:];
-[_UIRotaryGestureRecognizer setBeganMode:];
-[_UIRotaryGestureRecognizer setDelta:];
-[_UIRotaryGestureRecognizer setIsActivelyTouching:];
-[_UIRotaryGestureRecognizer startRegion];
```
