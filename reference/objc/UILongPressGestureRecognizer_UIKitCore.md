# `UILongPressGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- Protocols: `UITapRecognizerDelegate`
- 33 instance variables, 24 properties, 97 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _touches;
@"NSMutableSet" _activeTouches;
Q _numberOfTouchesRequired;
d _minimumPressDuration;
d _allowableMovement;
{CGPoint="x"d"y"d} _startPointScreen;
{CGPoint="x"d"y"d} _lastCentroidScreen;
@"UIHeldAction" _enoughTimeElapsed;
@"UIDelayedAction" _tooMuchTimeElapsed;
@"UIDelayedAction" _multitouchTimer;
@"UITapRecognizer" _imp;
@"UILongPressGestureVelocitySample" _velocitySample;
@"UILongPressGestureVelocitySample" _previousVelocitySample;
@"NSObservation" _touchForceObservation;
q _impulseObservations;
d _currentImpulse;
d _lastForce;
d _lastForceTimestamp;
b1 _gotTouchEnd;
b1 _gotTooMany;
b1 _gotEnoughTaps;
b1 _cancelPastAllowableMovement;
b1 _allowsDynamicTouchesList;
B _requiresQuietImpulse;
B _requiresQuietImpulseForCurrentTouchSequence;
B __prefersToBeExclusiveWithCompetingLongPressGestureRecognizers;
B __prefersNotToBePreventedByCompetingLongPressGestureRecognizers;
B __shouldAlwaysEnableMultitouchTimerAtTouchesBegin;
q _buttonType;
d _allowableElapsedTimeForAllRequiredTouches;
d _lastTouchTime;
{CGPoint="x"d"y"d} _lastSceneReferenceLocation;
{CGPoint="x"d"y"d} _lastUnadjustedSceneReferenceLocation;
```

## Properties

```
@property (Td,N,V_minimumPressDuration) delay;
@property (T@"NSArray",&,N,V_touches) touches;
@property (T{CGPoint=dd},R,N) startPoint;
@property (T{CGPoint=dd},R,N) centroid;
@property (TB,N) cancelPastAllowableMovement;
@property (Tq,N,S_setButtonType:,V_buttonType) _buttonType;
@property (TB,N,S_setRequiresQuietImpulse:,V_requiresQuietImpulse) _requiresQuietImpulse;
@property (T{CGPoint=dd},N,V_lastSceneReferenceLocation) lastSceneReferenceLocation;
@property (T{CGPoint=dd},N,V_lastUnadjustedSceneReferenceLocation) lastUnadjustedSceneReferenceLocation;
@property (Td,N,V_lastTouchTime) lastTouchTime;
@property (T{CGPoint=dd},R,N) _centroidScreen;
@property (TB,N,V__prefersToBeExclusiveWithCompetingLongPressGestureRecognizers) _prefersToBeExclusiveWithCompetingLongPressGestureRecognizers;
@property (TB,N,V__prefersNotToBePreventedByCompetingLongPressGestureRecognizers) _prefersNotToBePreventedByCompetingLongPressGestureRecognizers;
@property (TB,N,S_setShouldAlwaysEnableMultitouchTimerAtTouchesBegin:,V__shouldAlwaysEnableMultitouchTimerAtTouchesBegin) _shouldAlwaysEnableMultitouchTimerAtTouchesBegin;
@property (Td,N,S_setAllowableElapsedTimeForAllRequiredTouches:,V_allowableElapsedTimeForAllRequiredTouches) _allowableElapsedTimeForAllRequiredTouches;
@property (TQ,N) numberOfTapsRequired;
@property (TQ,N,V_numberOfTouchesRequired) numberOfTouchesRequired;
@property (Td,N) minimumPressDuration;
@property (Td,N,V_allowableMovement) allowableMovement;
@property (T@"UIView",R,N) view;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UILongPressGestureRecognizer supportsSecureCoding];
```

## Instance methods

```
-[UILongPressGestureRecognizer numberOfTapsRequired];
-[UILongPressGestureRecognizer allowableMovement];
-[UILongPressGestureRecognizer canPreventGestureRecognizer:];
-[UILongPressGestureRecognizer _shouldReceivePress:];
-[UILongPressGestureRecognizer centroid];
-[UILongPressGestureRecognizer touchesEnded:withEvent:];
-[UILongPressGestureRecognizer velocityInView:];
-[UILongPressGestureRecognizer _resetGestureRecognizer];
-[UILongPressGestureRecognizer buttonMaskRequired];
-[UILongPressGestureRecognizer touchesCancelled:withEvent:];
-[UILongPressGestureRecognizer enoughTimeElapsed:];
-[UILongPressGestureRecognizer setAllowableMovement:];
-[UILongPressGestureRecognizer setButtonMaskRequired:];
-[UILongPressGestureRecognizer pressesCancelled:withEvent:];
-[UILongPressGestureRecognizer pressesEnded:withEvent:];
-[UILongPressGestureRecognizer touches];
-[UILongPressGestureRecognizer _isGestureType:];
-[UILongPressGestureRecognizer numberOfTouches];
-[UILongPressGestureRecognizer setView:];
-[UILongPressGestureRecognizer touchesBegan:withEvent:];
-[UILongPressGestureRecognizer touchesMoved:withEvent:];
-[UILongPressGestureRecognizer initWithTarget:action:];
-[UILongPressGestureRecognizer startPoint];
-[UILongPressGestureRecognizer locationInView:];
-[UILongPressGestureRecognizer setNumberOfTapsRequired:];
-[UILongPressGestureRecognizer pressesBegan:withEvent:];
-[UILongPressGestureRecognizer pressesChanged:withEvent:];
-[UILongPressGestureRecognizer delay];
-[UILongPressGestureRecognizer activeTouchesExceedAllowableSeparation];
-[UILongPressGestureRecognizer invalidate];
-[UILongPressGestureRecognizer setNumberOfTouchesRequired:];
-[UILongPressGestureRecognizer _shouldFailInResponseToPresses:withEvent:];
-[UILongPressGestureRecognizer tapIsPossibleForTapRecognizer:];
-[UILongPressGestureRecognizer _touchSloppinessFactor];
-[UILongPressGestureRecognizer setDelay:];
-[UILongPressGestureRecognizer _startEnoughTimeElapsedTimer];
-[UILongPressGestureRecognizer encodeWithCoder:];
-[UILongPressGestureRecognizer _adjustSceneReferenceLocation:];
-[UILongPressGestureRecognizer tapRecognizerFailedToRecognizeTap:];
-[UILongPressGestureRecognizer minimumPressDuration];
-[UILongPressGestureRecognizer initWithCoder:];
-[UILongPressGestureRecognizer numberOfTouchesRequired];
-[UILongPressGestureRecognizer _appendSubclassDescription:];
-[UILongPressGestureRecognizer setMinimumPressDuration:];
-[UILongPressGestureRecognizer locationOfTouch:inView:];
-[UILongPressGestureRecognizer tapRecognizerRecognizedTap:];
-[UILongPressGestureRecognizer _centroidScreen];
-[UILongPressGestureRecognizer setCancelPastAllowableMovement:];
-[UILongPressGestureRecognizer tooMuchElapsed:];
-[UILongPressGestureRecognizer _setButtonType:];
-[UILongPressGestureRecognizer _allowableElapsedTimeForAllRequiredTouches];
-[UILongPressGestureRecognizer _allowableSeparation];
-[UILongPressGestureRecognizer _allowableTouchTimeSeparation];
-[UILongPressGestureRecognizer _allowsDynamicTouchesList];
-[UILongPressGestureRecognizer _buttonType];
-[UILongPressGestureRecognizer _centroidInView:];
-[UILongPressGestureRecognizer _centroidMovedTo:atTime:physicalTouch:];
-[UILongPressGestureRecognizer _changeTouchesListTo:];
-[UILongPressGestureRecognizer _clearEnoughTimeElapsedTimer];
-[UILongPressGestureRecognizer _convertVelocitySample:fromSceneReferenceCoordinatesToView:];
-[UILongPressGestureRecognizer _impulseQuietEnough];
-[UILongPressGestureRecognizer _incorporateTouchForceMessageIntoImpulseQuietness:];
-[UILongPressGestureRecognizer _interactionsEndedWithValidTouches:];
-[UILongPressGestureRecognizer _locationOfTouches:];
-[UILongPressGestureRecognizer _offsetInViewFromSceneReferenceLocation:toSceneReferenceLocation:];
-[UILongPressGestureRecognizer _prefersNotToBePreventedByCompetingLongPressGestureRecognizers];
-[UILongPressGestureRecognizer _prefersToBeExclusiveWithCompetingLongPressGestureRecognizers];
-[UILongPressGestureRecognizer _requiresQuietImpulse];
-[UILongPressGestureRecognizer _resetImpulseQuietness];
-[UILongPressGestureRecognizer _resetVelocitySamples];
-[UILongPressGestureRecognizer _setAllowableElapsedTimeForAllRequiredTouches:];
-[UILongPressGestureRecognizer _setAllowableMovement:];
-[UILongPressGestureRecognizer _setAllowableSeparation:];
-[UILongPressGestureRecognizer _setAllowableTouchTimeSeparation:];
-[UILongPressGestureRecognizer _setAllowsDynamicTouchesList:];
-[UILongPressGestureRecognizer _setRequiresQuietImpulse:];
-[UILongPressGestureRecognizer _setShouldAlwaysEnableMultitouchTimerAtTouchesBegin:];
-[UILongPressGestureRecognizer _setTranslation:inView:];
-[UILongPressGestureRecognizer _shiftPanLocationToNewSceneReferenceLocation:];
-[UILongPressGestureRecognizer _shouldAlwaysEnableMultitouchTimerAtTouchesBegin];
-[UILongPressGestureRecognizer _startMultitouchTimer];
-[UILongPressGestureRecognizer _startPointInView:];
-[UILongPressGestureRecognizer _startTapFinishedTimer];
-[UILongPressGestureRecognizer _touchesMayBeRecognizedByForcePreviewingRevealGestureRecognizerWhichShouldDelayTimer:];
-[UILongPressGestureRecognizer _translationInView:];
-[UILongPressGestureRecognizer cancelPastAllowableMovement];
-[UILongPressGestureRecognizer clearAllTimers];
-[UILongPressGestureRecognizer clearAllTimersAndStartEnoughTimeElapsedTimer];
-[UILongPressGestureRecognizer lastSceneReferenceLocation];
-[UILongPressGestureRecognizer lastTouchTime];
-[UILongPressGestureRecognizer lastUnadjustedSceneReferenceLocation];
-[UILongPressGestureRecognizer setLastSceneReferenceLocation:];
-[UILongPressGestureRecognizer setLastTouchTime:];
-[UILongPressGestureRecognizer setLastUnadjustedSceneReferenceLocation:];
-[UILongPressGestureRecognizer setTouches:];
-[UILongPressGestureRecognizer set_prefersNotToBePreventedByCompetingLongPressGestureRecognizers:];
-[UILongPressGestureRecognizer set_prefersToBeExclusiveWithCompetingLongPressGestureRecognizers:];
```
