# `PKTextInputDrawingGestureRecognizer`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- Protocols: `PKDrawingReplaySupport`, `PKDrawingGestureRecognizerProtocol`, `PKTextInputDebugStateReporting`
- 21 instance variables, 15 properties, 72 instance methods, 1 class methods

## Instance variables

```
B _waitingForTargetElementSearch;
B _requiresTargetElementToBegin;
B _requiresPastTapToBegin;
d _drawStartTime;
d _touchesBeganTimestamp;
{CGPoint="x"d"y"d} _drawTouchStartPoint;
@? _timeoutBlock;
@? _longPressTentativeBlock;
@? _longPressSuccessBlock;
@? _notMovingCancelBlock;
@? _gestureEnvironmentResetTimeoutBlock;
B _drawingTargetIsDrawing;
B _isReplaying;
Q _activeInputProperties;
@"<PKDrawingGestureTarget>" drawingTarget;
q _strokeAcceptanceState;
q _longPressState;
@"PKTextInputElement" _targetElement;
@"UITouch" _drawingTouch;
q _panState;
q _panDirection;
```

## Properties

```
@property (T@"UITouch",&,N,V_drawingTouch) drawingTouch;
@property (TB,N,S_setDrawingTargetIsDrawing:,V_drawingTargetIsDrawing) drawingTargetIsDrawing;
@property (Tq,N,S_setStrokeAcceptanceState:,V_strokeAcceptanceState) strokeAcceptanceState;
@property (Tq,N,S_setLongPressState:,V_longPressState) longPressState;
@property (Tq,N,S_setPanState:,V_panState) panState;
@property (Tq,N,S_setPanDirection:,V_panDirection) panDirection;
@property (T@"PKTextInputElement",&,N,V_targetElement) targetElement;
@property (T@"<PKTextInputDrawingGestureRecognizerDelegate>",W,D,N) delegate;
@property (TB,N,V_isReplaying) isReplaying;
@property (T@"<PKDrawingGestureTarget>",W,N,VdrawingTarget) drawingTarget;
@property (TQ,R,N,V_activeInputProperties) activeInputProperties;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKTextInputDrawingGestureRecognizer _systemGestureClassesToAvoid];
```

## Instance methods

```
-[PKTextInputDrawingGestureRecognizer touchesEnded:withEvent:];
-[PKTextInputDrawingGestureRecognizer _replayDrawingBegan:];
-[PKTextInputDrawingGestureRecognizer setState:];
-[PKTextInputDrawingGestureRecognizer touchesCancelled:withEvent:];
-[PKTextInputDrawingGestureRecognizer _replayDrawingMoved:];
-[PKTextInputDrawingGestureRecognizer setDrawingTarget:];
-[PKTextInputDrawingGestureRecognizer isReplaying];
-[PKTextInputDrawingGestureRecognizer reset];
-[PKTextInputDrawingGestureRecognizer _replayDrawingBegan:coordinateSpace:activeInputProperties:inputType:];
-[PKTextInputDrawingGestureRecognizer end];
-[PKTextInputDrawingGestureRecognizer touchesBegan:withEvent:];
-[PKTextInputDrawingGestureRecognizer touchesMoved:withEvent:];
-[PKTextInputDrawingGestureRecognizer initWithTarget:action:];
-[PKTextInputDrawingGestureRecognizer setDrawingTouch:];
-[PKTextInputDrawingGestureRecognizer locationInView:];
-[PKTextInputDrawingGestureRecognizer shouldBeRequiredToFailByGestureRecognizer:];
-[PKTextInputDrawingGestureRecognizer drawingTarget];
-[PKTextInputDrawingGestureRecognizer _drawingEnded];
-[PKTextInputDrawingGestureRecognizer activeInputProperties];
-[PKTextInputDrawingGestureRecognizer _replayDrawingEnded];
-[PKTextInputDrawingGestureRecognizer description];
-[PKTextInputDrawingGestureRecognizer _replayDrawingMoved:coordinateSpace:];
-[PKTextInputDrawingGestureRecognizer cancel];
-[PKTextInputDrawingGestureRecognizer _endDrawing];
-[PKTextInputDrawingGestureRecognizer drawingTouch];
-[PKTextInputDrawingGestureRecognizer _drawingBegan];
-[PKTextInputDrawingGestureRecognizer _drawingMoved:];
-[PKTextInputDrawingGestureRecognizer _replayDrawingCancelled];
-[PKTextInputDrawingGestureRecognizer touchesEstimatedPropertiesUpdated:];
-[PKTextInputDrawingGestureRecognizer setTargetElement:];
-[PKTextInputDrawingGestureRecognizer targetElement];
-[PKTextInputDrawingGestureRecognizer _updatePanGestureStateForTouch:];
-[PKTextInputDrawingGestureRecognizer setIsReplaying:];
-[PKTextInputDrawingGestureRecognizer timeIntervalSinceStartOfGesture];
-[PKTextInputDrawingGestureRecognizer _acceptStrokeTimeoutTriggered];
-[PKTextInputDrawingGestureRecognizer _beginDrawingIfNeeded];
-[PKTextInputDrawingGestureRecognizer _cancelLongPressTimerBlocks];
-[PKTextInputDrawingGestureRecognizer _cancelNotMovingCancellationBlock];
-[PKTextInputDrawingGestureRecognizer _cancelOrFailGesture];
-[PKTextInputDrawingGestureRecognizer _cancelScheduledStrokeAcceptanceBlock];
-[PKTextInputDrawingGestureRecognizer _distanceFromStartPositionForTouch:];
-[PKTextInputDrawingGestureRecognizer _enumerateTouchesForUpdateWithEvent:block:];
-[PKTextInputDrawingGestureRecognizer _evaluateCancelIfNotMoving];
-[PKTextInputDrawingGestureRecognizer _evaluateMovingToBeganStateUseTimestampFromTouch:];
-[PKTextInputDrawingGestureRecognizer _gestureStartedInsideTargetElement];
-[PKTextInputDrawingGestureRecognizer _hasMovedPastMinimumPanThresholdForTouch:];
-[PKTextInputDrawingGestureRecognizer _hasMovedPastScrollThresholdForTouch:];
-[PKTextInputDrawingGestureRecognizer _isValidLongPress];
-[PKTextInputDrawingGestureRecognizer _isValidLongPressOverDuration:];
-[PKTextInputDrawingGestureRecognizer _isWithinLongPressDistanceForTouch:];
-[PKTextInputDrawingGestureRecognizer _longPressSuccessTimerFired];
-[PKTextInputDrawingGestureRecognizer _longPressTentativeTimerFired];
-[PKTextInputDrawingGestureRecognizer _panDirectionForTouch:];
-[PKTextInputDrawingGestureRecognizer _scheduleLongPressTimerBlocks];
-[PKTextInputDrawingGestureRecognizer _setDrawingTargetIsDrawing:];
-[PKTextInputDrawingGestureRecognizer _setLongPressState:];
-[PKTextInputDrawingGestureRecognizer _setPanDirection:];
-[PKTextInputDrawingGestureRecognizer _setPanState:];
-[PKTextInputDrawingGestureRecognizer _setStrokeAcceptanceState:];
-[PKTextInputDrawingGestureRecognizer _updateLongPressValidityForTouch:];
-[PKTextInputDrawingGestureRecognizer _updatePanStateForCandidateElements:];
-[PKTextInputDrawingGestureRecognizer _updateStrokeAcceptanceStateUseTimestampFromTouch:];
-[PKTextInputDrawingGestureRecognizer cancelDrawing];
-[PKTextInputDrawingGestureRecognizer drawingTargetIsDrawing];
-[PKTextInputDrawingGestureRecognizer finishedElementFindingWithElement:candidateElements:];
-[PKTextInputDrawingGestureRecognizer hasMovedPastTapUseTimestampFromTouch:];
-[PKTextInputDrawingGestureRecognizer longPressState];
-[PKTextInputDrawingGestureRecognizer panDirection];
-[PKTextInputDrawingGestureRecognizer panState];
-[PKTextInputDrawingGestureRecognizer reportDebugStateDescription:];
-[PKTextInputDrawingGestureRecognizer strokeAcceptanceState];
-[PKTextInputDrawingGestureRecognizer timeIntervalSinceTouchesBeganForTouch:];
```
