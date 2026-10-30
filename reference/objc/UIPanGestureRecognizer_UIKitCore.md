# `UIPanGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- Protocols: `_UIScrollEventRespondable`
- 35 instance variables, 12 properties, 77 instance methods, 5 class methods

## Instance variables

```
{CAPoint3D="x"d"y"d"z"d} _firstSceneReferenceLocation;
{CAPoint3D="x"d"y"d"z"d} _lastSceneReferenceLocation;
d _lastTouchTime;
@"NSMutableArray" _touches;
Q _lastTouchCount;
Q _minimumNumberOfTouches;
Q _maximumNumberOfTouches;
d _hysteresis;
d _allowableSeparation;
{CAPoint3D="x"d"y"d"z"d} _lastUnadjustedSceneReferenceLocation;
d _allowableTouchTimeSeparation;
b1 _delegateImplementsShouldTryToBeginHorizontally;
b1 _delegateImplementsShouldTryToBeginVertically;
b1 _failsPastMaxTouches;
b1 _failsPastHysteresisWithoutMinTouches;
b1 _canPanHorizontally;
b1 _canPanVertically;
b1 _delegateAllowsPanHorizontally;
b1 _delegateAllowsPanVertically;
b1 _queriedDelegateAllowsPanHorizontally;
b1 _queriedDelegateAllowsPanVertically;
b1 _ignoresStationaryTouches;
b1 _multitouchTimerOn;
b1 _requiresImmediateMultipleTouches;
b1 _sawNonzeroStifledDeltaX;
b1 _sawNonzeroStifledDeltaY;
@"NSMutableArray" _movingTouches;
{CGPoint="x"d"y"d} _digitizerLocation;
@"UIPanGestureVelocitySample" _velocitySample;
@"UIPanGestureVelocitySample" _previousVelocitySample;
{?="canPanHorizontally"b1"canPanVertically"b1"delegateAllowsPanHorizontally"b1"delegateAllowsPanVertically"b1"queriedDelegateAllowsPanHorizontally"b1"queriedDelegateAllowsPanVertically"b1"failsPastMaxTouches"b1"multitouchTimerOn"b1"requiresImmediateMultipleTouches"b1"sawNonzeroStifledDeltaX"b1"sawNonzeroStifledDeltaY"b1"shouldConsiderAllowedScrollTypeCompatibility"b1"evaluatedAllowedScrollTypeCompatibility"b1} _panFlags;
B _iOSMacUseNonacceleratedDelta;
B _iOSMacIgnoreScrollDirectionUserPreference;
B _iOSMacScrollingEnabled;
q _allowedScrollTypesMask;
```

## Properties

```
@property (TB,N) failsPastMaxTouches;
@property (TB,N,G_ignoresStationaryTouches,S_setIgnoresStationaryTouches:) ignoresStationaryTouches;
@property (TB,N,G_iOSMacUseNonacceleratedDelta,S_setiOSMacUseNonacceleratedDelta:,V_iOSMacUseNonacceleratedDelta) iOSMacUseNonacceleratedDelta;
@property (TB,N,G_iOSMacIgnoreScrollDirectionUserPreference,S_setiOSMacIgnoreScrollDirectionUserPreference:,V_iOSMacIgnoreScrollDirectionUserPreference) iOSMacIgnoreScrollDirectionUserPreference;
@property (TB,N,G_iOSMacScrollingEnabled,S_setiOSMacScrollingEnabled:,V_iOSMacScrollingEnabled) iOSMacScrollingEnabled;
@property (TQ,N,V_minimumNumberOfTouches) minimumNumberOfTouches;
@property (TQ,N,V_maximumNumberOfTouches) maximumNumberOfTouches;
@property (Tq,N,V_allowedScrollTypesMask) allowedScrollTypesMask;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIPanGestureRecognizer supportsSecureCoding];
+[UIPanGestureRecognizer _supportsDefaultTouchTypes];
+[UIPanGestureRecognizer _supportsDefaultPressTypes];
+[UIPanGestureRecognizer _defaultHysteresis];
+[UIPanGestureRecognizer _setPanGestureRecognizersEnabled:];
```

## Instance methods

```
-[UIPanGestureRecognizer translationInView:];
-[UIPanGestureRecognizer _hysteresis];
-[UIPanGestureRecognizer touchesEnded:withEvent:];
-[UIPanGestureRecognizer velocityInView:];
-[UIPanGestureRecognizer shouldReceiveEvent:];
-[UIPanGestureRecognizer _scrollingChangedWithEvent:];
-[UIPanGestureRecognizer _resetGestureRecognizer];
-[UIPanGestureRecognizer touchesCancelled:withEvent:];
-[UIPanGestureRecognizer _convertPoint:toSceneReferenceCoordinatesFromView:];
-[UIPanGestureRecognizer _isGestureType:];
-[UIPanGestureRecognizer multitouchExpired:];
-[UIPanGestureRecognizer _willScrollX];
-[UIPanGestureRecognizer numberOfTouches];
-[UIPanGestureRecognizer _convertPoint:fromSceneReferenceCoordinatesToView:];
-[UIPanGestureRecognizer touchesBegan:withEvent:];
-[UIPanGestureRecognizer touchesMoved:withEvent:];
-[UIPanGestureRecognizer initWithTarget:action:];
-[UIPanGestureRecognizer locationInView:];
-[UIPanGestureRecognizer pressesBegan:withEvent:];
-[UIPanGestureRecognizer setDelegate:];
-[UIPanGestureRecognizer _removeHysteresisFromTranslation];
-[UIPanGestureRecognizer setMaximumNumberOfTouches:];
-[UIPanGestureRecognizer _shouldTryToBeginWithEvent:];
-[UIPanGestureRecognizer startMultitouchTimer:];
-[UIPanGestureRecognizer encodeWithCoder:];
-[UIPanGestureRecognizer clearMultitouchTimer];
-[UIPanGestureRecognizer _adjustSceneReferenceLocation:];
-[UIPanGestureRecognizer setMinimumNumberOfTouches:];
-[UIPanGestureRecognizer _willScrollY];
-[UIPanGestureRecognizer initWithCoder:];
-[UIPanGestureRecognizer maximumNumberOfTouches];
-[UIPanGestureRecognizer _centroidMovedTo:atTime:affectingTranslation:];
-[UIPanGestureRecognizer locationOfTouch:inView:];
-[UIPanGestureRecognizer _updateGestureTraits];
-[UIPanGestureRecognizer _ignoreTouchForTouchIdentifier:];
-[UIPanGestureRecognizer _setHysteresis:];
-[UIPanGestureRecognizer _allowableSeparation];
-[UIPanGestureRecognizer _allowableTouchTimeSeparation];
-[UIPanGestureRecognizer _allowedScrollTypesMask];
-[UIPanGestureRecognizer _canPanHorizontally];
-[UIPanGestureRecognizer _canPanVertically];
-[UIPanGestureRecognizer _convertVelocitySample:fromSceneReferenceCoordinatesToView:];
-[UIPanGestureRecognizer _didUpdateCentroidWithTouches:event:];
-[UIPanGestureRecognizer _failsPastHysteresisWithoutMinTouches];
-[UIPanGestureRecognizer _handleEndedTouches:withFinalStateAdjustments:];
-[UIPanGestureRecognizer _iOSMacIgnoreScrollDirectionUserPreference];
-[UIPanGestureRecognizer _iOSMacScrollingEnabled];
-[UIPanGestureRecognizer _iOSMacUseNonacceleratedDelta];
-[UIPanGestureRecognizer _ignoresStationaryTouches];
-[UIPanGestureRecognizer _initialLocationInView:];
-[UIPanGestureRecognizer _movingTouches];
-[UIPanGestureRecognizer _processScrollPhaseChanged:];
-[UIPanGestureRecognizer _requiresImmediateMultipleTouches];
-[UIPanGestureRecognizer _sceneCentroidOfTouches:excludingEnded:];
-[UIPanGestureRecognizer _setAllowableSeparation:];
-[UIPanGestureRecognizer _setAllowableTouchTimeSeparation:];
-[UIPanGestureRecognizer _setAllowedScrollTypesMask:];
-[UIPanGestureRecognizer _setCanPanHorizontally:];
-[UIPanGestureRecognizer _setCanPanVertically:];
-[UIPanGestureRecognizer _setFailsPastHysteresisWithoutMinTouches:];
-[UIPanGestureRecognizer _setIgnoresStationaryTouches:];
-[UIPanGestureRecognizer _setRequiresImmediateMultipleTouches:];
-[UIPanGestureRecognizer _setiOSMacIgnoreScrollDirectionUserPreference:];
-[UIPanGestureRecognizer _setiOSMacScrollingEnabled:];
-[UIPanGestureRecognizer _setiOSMacUseNonacceleratedDelta:];
-[UIPanGestureRecognizer _shouldBeginHorizontally:vertically:withEvent:];
-[UIPanGestureRecognizer _touchesExceedAllowableSeparation];
-[UIPanGestureRecognizer _touchesListChangedFrom:to:];
-[UIPanGestureRecognizer _updateMovingTouchesArraySavingOldArray:];
-[UIPanGestureRecognizer _willBeginAfterSatisfyingFailureRequirements];
-[UIPanGestureRecognizer allowedScrollTypesMask];
-[UIPanGestureRecognizer failsPastMaxTouches];
-[UIPanGestureRecognizer isIOSMacScrollingEnabled];
-[UIPanGestureRecognizer minimumNumberOfTouches];
-[UIPanGestureRecognizer setAllowedScrollTypesMask:];
-[UIPanGestureRecognizer setFailsPastMaxTouches:];
-[UIPanGestureRecognizer setTranslation:inView:];
```
