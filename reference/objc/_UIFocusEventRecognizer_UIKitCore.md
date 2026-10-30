# `_UIFocusEventRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `_UIFocusEnginePanGestureRecognizerDelegate`, `_UIRotaryGestureRecognizerDelegate`
- 41 instance variables, 12 properties, 129 instance methods, 1 class methods

## Instance variables

```
@"NSMapTable" _gestureRecognizers;
@"_UIFocusRotaryIndicatorView" _rotaryIndicatorView;
@"NSTimer" _showRotaryIndicatorAfterDelayTimer;
d _panDeadBand;
{CGPoint="x"d"y"d} _touchBeganPoint;
{CGPoint="x"d"y"d} _lastKnownTouchPoint;
[5{CGPoint="x"d"y"d}] _previousPoints;
i _numFrames;
{CGVector="dx"d"dy"d} _progressAccumulator;
{CGVector="dx"d"dy"d} _unlockedAccumulator;
d _lastButtonPressTime;
Q _failedContinuousMovementHeading;
d _failedContinuousMovementTime;
{CGPoint="x"d"y"d} _firstMomentumTouchPoint;
{CGPoint="x"d"y"d} _lastMomentumTouchPoint;
{CGPoint="x"d"y"d} _momentumVelocity;
d _momentumFriction;
Q _focusUpdateCountSinceLastContinuousMovementBegan;
@"CADisplayLink" _momentumDisplayLink;
@"NSTimer" _joystickModeExitTimer;
@"NSTimer" _joystickModeRepeatTimer;
d _previousJoystickFocusMovementTime;
d _previousJoystickRegionEntryTime;
Q _joystickRepeatingHeading;
@"CADisplayLink" _joystickFocusDirectionDisplayLink;
@"_UIFocusMovementInfo" _previousJoystickFocusMovementInfo;
q _joystickRepeatCount;
@"UIScrollView" _lastScrolledScroll;
d _lastEdgeScrollEdgeValue;
Q _inputType;
@"_UIFocusItemUIKitMetadata" _cachedFocusItemMetadata;
@"CARInputDeviceTouchpad" _currentCarKitTouchpad;
@"_UISceneCarPlaySessionTouchpad" _currentCarTouchpad;
{?="isEligibleToCrossSpeedBump"b1"isContinuingTouchWithMomentum"b1"isPerformingJoystickRollback"b1"isJoystickInRepeatMode"b1"isPendingJoystickRepeat"b1"isFastScrolling"b1"shouldApplyAcceleration"b1"shouldSupressActiveIndirectMotionUpdates"b1"startDeferingFocusOnTapHoldEnded"b1} _flags;
B _enabled;
@"UIView" _owningView;
@"NSArray" _keyCommands;
@"<_UIFocusEventRecognizerDelegate>" _delegate;
@"UIMoveEvent" _moveEvent;
@"_UIFocusEffectsController" _motionEffectsController;
@"_UIFocusFastScrollingRecognizer" _fastScrollingRecognizer;
```

## Properties

```
@property (T@"UIMoveEvent",&,N,G_moveEvent,S_setMoveEvent:,V_moveEvent) moveEvent;
@property (T@"_UIFocusEffectsController",R,N,G_motionEffectsController,V_motionEffectsController) motionEffectsController;
@property (T@"_UIFocusFastScrollingRecognizer",R,N,G_fastScrollingRecognizer,V_fastScrollingRecognizer) fastScrollingRecognizer;
@property (T@"UIView",R,W,N,V_owningView) owningView;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (T@"NSArray",R,N,V_keyCommands) keyCommands;
@property (T@"<_UIFocusEventRecognizerDelegate>",W,N,V_delegate) delegate;
@property (T@"NSSet",R,N) gesturesForFailureRequirements;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIFocusEventRecognizer _canSupportFastScrolling];
```

## Instance methods

```
-[_UIFocusEventRecognizer _moveWithEvent:];
-[_UIFocusEventRecognizer _setMoveEvent:];
-[_UIFocusEventRecognizer _gestureRecognizerFailed:];
-[_UIFocusEventRecognizer _sendGestureBeginNotification];
-[_UIFocusEventRecognizer gesturesForFailureRequirements];
-[_UIFocusEventRecognizer _continueTouchWithMomentum];
-[_UIFocusEventRecognizer _motionEffectsController];
-[_UIFocusEventRecognizer _applyButtonMaskTimeToValue:remoteTouchSurfaceType:];
-[_UIFocusEventRecognizer gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[_UIFocusEventRecognizer _exitJoystickModeForReal:];
-[_UIFocusEventRecognizer _handleJoystickTiltMode:];
-[_UIFocusEventRecognizer _recordMomentumForPoint:reportedVelocity:];
-[_UIFocusEventRecognizer _updateRotaryDistance:delta:reportedVelocity:remoteTouchSurfaceType:focusMovementAxis:];
-[_UIFocusEventRecognizer _panGestureCancelled:];
-[_UIFocusEventRecognizer _handleRotaryGesture:];
-[_UIFocusEventRecognizer _resetMomentum];
-[_UIFocusEventRecognizer init];
-[_UIFocusEventRecognizer _uiktest_panGestureRecognizer];
-[_UIFocusEventRecognizer _moveInDirection:groupFilter:withSearchInfo:];
-[_UIFocusEventRecognizer _cancelShowRotaryIndicatorTimer];
-[_UIFocusEventRecognizer _shouldPerformFocusUpdateWithCurrentMomentumStatus];
-[_UIFocusEventRecognizer _updateFailedContinuousMovementHeading:];
-[_UIFocusEventRecognizer _updateGestureRecognizersForcingRemoval:studyLogData:];
-[_UIFocusEventRecognizer _canMoveFocusWithRotaryInputInFocusContext:];
-[_UIFocusEventRecognizer _focusMovementSystem];
-[_UIFocusEventRecognizer dealloc];
-[_UIFocusEventRecognizer _handlePageButtonGesture:];
-[_UIFocusEventRecognizer _updateGestureRecognizersForcingRemoval:];
-[_UIFocusEventRecognizer _cancelAllGestureRecognizers];
-[_UIFocusEventRecognizer _touchSensitivityForFocusItemMetadata:remoteTouchSurfaceType:];
-[_UIFocusEventRecognizer _momentumHeartbeat:];
-[_UIFocusEventRecognizer _showRotaryIndicatorAfterDelay];
-[_UIFocusEventRecognizer reset];
-[_UIFocusEventRecognizer _touchRegionForDigitizerLocation:];
-[_UIFocusEventRecognizer _panGestureEnd:];
-[_UIFocusEventRecognizer keyCommands];
-[_UIFocusEventRecognizer _pointForLinearValue:axis:];
-[_UIFocusEventRecognizer _handleJoystickGesture:];
-[_UIFocusEventRecognizer _momentumFocusHeadingForAccumulator:];
-[_UIFocusEventRecognizer _handleSelectObserverGesture:];
-[_UIFocusEventRecognizer _moveInDirection:groupFilter:];
-[_UIFocusEventRecognizer _createRotaryMovementRequestWithFocusSystem:];
-[_UIFocusEventRecognizer isEnabled];
-[_UIFocusEventRecognizer _hasFailedMovementHeadingExpired];
-[_UIFocusEventRecognizer _panGestureStart:];
-[_UIFocusEventRecognizer _joystickGestureBegan:];
-[_UIFocusEventRecognizer _attemptPanFocusMovementWithHeading:acceleratedVelocity:focusSystem:studyLogData:];
-[_UIFocusEventRecognizer rotaryGestureRecognizerFailedClassifyingMovement:];
-[_UIFocusEventRecognizer _joystickVelocityForHeading:];
-[_UIFocusEventRecognizer _joystickRepeatDurationForTimeInMovementZone:];
-[_UIFocusEventRecognizer _attemptRotaryFocusMovementWithLinearHeading:directionalHeading:focusMovementAxis:focusSystem:acceleratedVelocity:studyLogData:];
-[_UIFocusEventRecognizer gestureForName:];
-[_UIFocusEventRecognizer _handleRotaryBegin:];
-[_UIFocusEventRecognizer _handleArrowButtonGesture:];
-[_UIFocusEventRecognizer _globalCoordinateSpace];
-[_UIFocusEventRecognizer setDelegate:];
-[_UIFocusEventRecognizer _applyPanDeadbandToValue:startPoint:currentPoint:remoteTouchSurfaceType:];
-[_UIFocusEventRecognizer owningView];
-[_UIFocusEventRecognizer _resetProgressAccumulator];
-[_UIFocusEventRecognizer gestureRecognizerShouldBegin:];
-[_UIFocusEventRecognizer _cleanupPanMomentumWithAccumulator:movementSuccess:];
-[_UIFocusEventRecognizer _uiktest_handlePanGesture:];
-[_UIFocusEventRecognizer focusEnginePanGestureRecognizerShouldRecognizeImmediately:];
-[_UIFocusEventRecognizer _updateMotionEffectsControllerWithProgressAccumulator:unlockedAccumulator:];
-[_UIFocusEventRecognizer _focusSystemSceneComponent];
-[_UIFocusEventRecognizer _didRecognizeFocusMovementRequest:];
-[_UIFocusEventRecognizer _handleTapGesture:];
-[_UIFocusEventRecognizer _resetContinuousMovementState];
-[_UIFocusEventRecognizer setEnabled:];
-[_UIFocusEventRecognizer initWithOwningView:];
-[_UIFocusEventRecognizer _handleTabulatorGesture:];
-[_UIFocusEventRecognizer _focusBehaviorDidChange:];
-[_UIFocusEventRecognizer _resetCachedFocusItemMetadata];
-[_UIFocusEventRecognizer _handleShoulderButtonGesture:];
-[_UIFocusEventRecognizer _resetProgressAccumulatorWithHeading:];
-[_UIFocusEventRecognizer _updateAccumulatorsWithScaledDelta:unlockedDelta:studyLogData:];
-[_UIFocusEventRecognizer _joystickAttemptFocusMovementWithRequest:];
-[_UIFocusEventRecognizer _moveEvent];
-[_UIFocusEventRecognizer _moveInDirection:groupFilter:withEvaluator:];
-[_UIFocusEventRecognizer _createPanMovementRequestWithFocusSystem:];
-[_UIFocusEventRecognizer _momentumReferenceSize];
-[_UIFocusEventRecognizer _uiktest_setPanGestureRecognizer:];
-[_UIFocusEventRecognizer _hideRotaryIndicator];
-[_UIFocusEventRecognizer gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UIFocusEventRecognizer _joystickGestureEnded:];
-[_UIFocusEventRecognizer delegate];
-[_UIFocusEventRecognizer _updateRotaryIndicatorView];
-[_UIFocusEventRecognizer _handleRotaryEnd:];
-[_UIFocusEventRecognizer _resetMotionEffects];
-[_UIFocusEventRecognizer _calculateDirectionalHeadingForAccumulator:studyLogData:];
-[_UIFocusEventRecognizer _createStudyLogDataForRotaryDistance:delta:reportedVelocity:];
-[_UIFocusEventRecognizer _calculateLinearHeadingForAccumulator:studyLogData:];
-[_UIFocusEventRecognizer _handlePanGesture:];
-[_UIFocusEventRecognizer _retrieveFocusItemMetadata];
-[_UIFocusEventRecognizer _joystickFocusMovement:shouldBeConsideredEqualToFocusMovement:];
-[_UIFocusEventRecognizer _accelerationFactorForCurrentVelocity:alpha:isRotaryGesture:isFocusInKeyboard:remoteTouchSurfaceType:];
-[_UIFocusEventRecognizer _attemptToRecognizeContinuousMovementRequest:];
-[_UIFocusEventRecognizer _continuousMovementFailedWithPrimaryHeading:];
-[_UIFocusEventRecognizer _handleJoystickRepeatMode:];
-[_UIFocusEventRecognizer _showRotaryIndicator];
-[_UIFocusEventRecognizer _createMovementInfoForHeading:groupFilter:acceleratedVelocity:];
-[_UIFocusEventRecognizer _joystickDisplayLinkHeartbeat:];
-[_UIFocusEventRecognizer _continuousMovementSucceededWithDirectionalHeading:];
-[_UIFocusEventRecognizer _handleSelectGesture:];
-[_UIFocusEventRecognizer _calculateDeltaForNormalizedPoint:studyLogData:];
-[_UIFocusEventRecognizer _focusSystemEnabledStateDidChange:];
-[_UIFocusEventRecognizer _buttonMaskTimeHasExpired];
-[_UIFocusEventRecognizer _updatePanLocation:reportedVelocity:remoteTouchSurfaceType:];
-[_UIFocusEventRecognizer _applyHorizontalFlipForFocusItemMetadata:toDelta:];
-[_UIFocusEventRecognizer _resetPanDeadband];
-[_UIFocusEventRecognizer _applyAxisLockingForNormalizedPoint:toDelta:];
-[_UIFocusEventRecognizer _sendMomentumEndNotificationsAndAnimateRollback:];
-[_UIFocusEventRecognizer _focusMovementForJoystickPosition:usingMinimumRadius:focusMovementStyle:];
-[_UIFocusEventRecognizer _beginMomentumImmediatelyWithVelocity:friction:];
-[_UIFocusEventRecognizer rotaryGestureRecognizerBeganClassifyingMovement:];
-[_UIFocusEventRecognizer _createStudyLogDataForPanNormalizedPoint:reportedVelocity:];
-[_UIFocusEventRecognizer _fastScrollingRecognizer];
-[_UIFocusEventRecognizer _focusDidUpdate:];
-[_UIFocusEventRecognizer _shouldAcceptInputType:];
-[_UIFocusEventRecognizer _resetFailedMovementHeading];
-[_UIFocusEventRecognizer _headingForJoystickPosition:usingMinimumRadius:];
-[_UIFocusEventRecognizer _timerFiredForShowRotaryIndicator:];
-[_UIFocusEventRecognizer _joystickPerformRepeat:];
-[_UIFocusEventRecognizer setGesture:forName:];
-[_UIFocusEventRecognizer _joystickGestureUpdated:];
-[_UIFocusEventRecognizer _stopMomentumAndPerformRollback];
-[_UIFocusEventRecognizer currentFocusBehavior];
-[_UIFocusEventRecognizer _resetJoystick];
-[_UIFocusEventRecognizer _handleRotaryCancelled:];
```
