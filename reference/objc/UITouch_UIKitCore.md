# `UITouch`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIResponderForwardableEventComponent`
- 55 instance variables, 40 properties, 95 instance methods, 1 class methods

## Instance variables

```
d _movementMagnitudeSquared;
q _phase;
Q _tapCount;
q _edgeType;
Q _edgeAim;
Q _precision;
I _touchIdentifier;
@"UIWindow" _window;
@"UIResponder<_UIGestureRecognizerContainer>" _responder;
@"UIView" _cachedResponderView;
@"UIView" _warpedIntoView;
@"NSMutableArray" _gestureRecognizers;
@"NSMutableArray" _forwardingRecord;
{CGPoint="x"d"y"d} _locationInWindow;
{CGPoint="x"d"y"d} _previousLocationInWindow;
{CGPoint="x"d"y"d} _preciseLocationInWindow;
{CGPoint="x"d"y"d} _precisePreviousLocationInWindow;
d _previousPressure;
q _pathIndex;
C _pathIdentity;
d _pathMajorRadius;
d _majorRadiusTolerance;
d _pressure;
d _maxObservedPressure;
f _zGradient;
{?="_firstTouchForView"b1"_isTap"b1"_isDelayed"b1"_sentTouchesEnded"b1"_abandonForwardingRecord"b1"_deliversUpdatesInTouchesMovedIsValid"b1"_deliversUpdatesInTouchesMoved"b1"_isPredictedTouch"b1"_didDispatchAsEnded"b1"_isPointerTouch"b1"_isRestingTouch"b1"_isTapToClick"b1"_isGESTouch"b1"_isTransitioningFromGESTouch"b1} _touchFlags;
@"_UITouchPredictor" _touchPredictor;
d _rollAngle;
d _previousRollAngle;
B _eaten;
B _needsForceUpdate;
B _hasForceUpdate;
C _forceStage;
B _needsRollUpdate;
B _hasRollUpdate;
B __expectedToBecomeDrag;
d _timestamp;
q _updateCorrelationToken;
d _maximumPossiblePressure;
Q _senderID;
^{__IOHIDEvent=} _hidEvent;
@"<BKSHIDEventProvenance>" _provenance;
d _altitudeAngle;
Q _pointerSenderID;
Q _pointerSource;
@"_UISTouchAuthenticationRecord" _touchAuthenticationRecord;
q _type;
@"<_UITouchPhaseChangeDelegate>" __phaseChangeDelegate;
@"UIWindow" __windowServerHitTestWindow;
d _azimuthAngleInCADisplay;
d _azimuthAngleInWindow;
@"BKSHIDEventAuthenticationMessage" __authenticationMessage;
@"BKSWindowServerHitTestSecurityAnalysis" __hitTestSecurityAnalysis;
d _initialTouchTimestamp;
{CGSize="width"d"height"d} _displacement;
```

## Properties

```
@property (Tq,N,S_setPathIndex:,V_pathIndex) _pathIndex;
@property (TC,N,S_setPathIdentity:,V_pathIdentity) _pathIdentity;
@property (Td,R,N,V_pressure) _pressure;
@property (Tf,N,S_setZGradient:,V_zGradient) _zGradient;
@property (Tq,N,S_setEdgeType:,V_edgeType) _edgeType;
@property (TQ,N,S_setEdgeAim:,V_edgeAim) _edgeAim;
@property (Tq,N,S_setType:,V_type) type;
@property (TQ,N,S_setSenderID:,V_senderID) _senderID;
@property (TQ,N,S_setPointerSenderID:,V_pointerSenderID) _pointerSenderID;
@property (T^{__IOHIDEvent=},N,S_setHidEvent:,V_hidEvent) _hidEvent;
@property (T@"_UISTouchAuthenticationRecord",&,N,S_setTouchAuthenticationRecord:,V_touchAuthenticationRecord) _touchAuthenticationRecord;
@property (Td,N,V_initialTouchTimestamp) initialTouchTimestamp;
@property (Td,N,V_timestamp) timestamp;
@property (Tq,N) phase;
@property (TQ,N) tapCount;
@property (T@"UIWindow",&,N) window;
@property (T@"UIView",&,N) view;
@property (TB,R,N) _supportsForce;
@property (TC,N,S_setForceStage:,V_forceStage) _forceStage;
@property (TB,N,S_setIsPointerTouch:) _isPointerTouch;
@property (TB,R,N) _originatesFromPointerEvent;
@property (TB,N,S_setIsRestingTouch:) _isRestingTouch;
@property (TB,N,S_setIsTapToClick:) _isTapToClick;
@property (Td,R,N) majorRadius;
@property (Td,R,N) majorRadiusTolerance;
@property (T@"NSArray",R,C,N) gestureRecognizers;
@property (Td,R,N) force;
@property (Td,R,N) maximumPossibleForce;
@property (Td,R,N) altitudeAngle;
@property (T@"NSNumber",R,N) estimationUpdateIndex;
@property (Tq,R,N) estimatedProperties;
@property (Tq,R,N) estimatedPropertiesExpectingUpdates;
@property (Td,R,N) rollAngle;
@property (T@"UIResponder<_UIGestureRecognizerContainer>",&,N,S_setResponder:) _responder;
@property (TQ,R,N) _eventComponentType;
@property (T@"_UIEventComponentPhaseValue",&,N,S_setEventComponentPhase:) _eventComponentPhase;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UITouch _createTouchesWithGSEvent:phase:view:];
```

## Instance methods

```
-[UITouch setTimestamp:];
-[UITouch gestureRecognizers];
-[UITouch _isAbandoningForwardingRecord];
-[UITouch phase];
-[UITouch info];
-[UITouch _locationInSceneReferenceSpace];
-[UITouch isDelayed];
-[UITouch dealloc];
-[UITouch timestamp];
-[UITouch _responder];
-[UITouch _abandonForwardingRecord];
-[UITouch setView:];
-[UITouch window];
-[UITouch _mutableForwardingRecord];
-[UITouch _setResponder:];
-[UITouch locationInView:];
-[UITouch _forwardingRecord];
-[UITouch view];
-[UITouch initialTouchTimestamp];
-[UITouch type];
-[UITouch _eventComponentPhaseForValue:];
-[UITouch rollAngle];
-[UITouch setInitialTouchTimestamp:];
-[UITouch description];
-[UITouch _eventComponentPhase];
-[UITouch setPhase:];
-[UITouch _eventComponentType];
-[UITouch force];
-[UITouch _phaseDescription];
-[UITouch _setEventComponentPhase:];
-[UITouch _clone];
-[UITouch setWindow:];
-[UITouch _responderSelectorForPhase:];
-[UITouch _wantsForwardingFromResponder:toNextResponder:withEvent:];
-[UITouch _setType:];
-[UITouch tapCount];
-[UITouch setIsDelayed:];
-[UITouch _setForceStage:];
-[UITouch _isPointerTouch];
-[UITouch _isRestingTouch];
-[UITouch _clearForReenteringHoverInWindow:];
-[UITouch _clearGestureRecognizers];
-[UITouch _clonePropertiesToTouch:];
-[UITouch _compareIndex:];
-[UITouch _edgeAim];
-[UITouch _edgeForceActive];
-[UITouch _edgeForcePending];
-[UITouch _edgeType];
-[UITouch _forceStage];
-[UITouch _gestureRecognizers];
-[UITouch _hidEvent];
-[UITouch _isFirstTouchForView];
-[UITouch _isTapToClick];
-[UITouch _loadStateFromTouch:];
-[UITouch _originatesFromPointerEvent];
-[UITouch _pathIdentity];
-[UITouch _pathIndex];
-[UITouch _pathMajorRadius];
-[UITouch _pointerSenderID];
-[UITouch _pressure];
-[UITouch _previousLocationInSceneReferenceSpace];
-[UITouch _rollAngle];
-[UITouch _senderID];
-[UITouch _setEdgeAim:];
-[UITouch _setEdgeType:];
-[UITouch _setHidEvent:];
-[UITouch _setIsFirstTouchForView:];
-[UITouch _setIsPointerTouch:];
-[UITouch _setIsRestingTouch:];
-[UITouch _setIsTapToClick:];
-[UITouch _setLocationInWindow:resetPrevious:];
-[UITouch _setPathIdentity:];
-[UITouch _setPathIndex:];
-[UITouch _setPointerSenderID:];
-[UITouch _setPreviousTouch:];
-[UITouch _setSenderID:];
-[UITouch _setTouchAuthenticationRecord:];
-[UITouch _setZGradient:];
-[UITouch _supportsForce];
-[UITouch _touchAuthenticationRecord];
-[UITouch _touchIdentifier];
-[UITouch _zGradient];
-[UITouch altitudeAngle];
-[UITouch azimuthAngleInView:];
-[UITouch azimuthUnitVectorInView:];
-[UITouch estimatedProperties];
-[UITouch estimatedPropertiesExpectingUpdates];
-[UITouch estimationUpdateIndex];
-[UITouch majorRadius];
-[UITouch majorRadiusTolerance];
-[UITouch maximumPossibleForce];
-[UITouch preciseLocationInView:];
-[UITouch precisePreviousLocationInView:];
-[UITouch previousLocationInView:];
-[UITouch setTapCount:];
```
