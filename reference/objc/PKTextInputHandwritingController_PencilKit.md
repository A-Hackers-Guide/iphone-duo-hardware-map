# `PKTextInputHandwritingController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKTextInputHandwritingShotDelegate`, `PKTextInputResultCommandDelegate`, `PKTextInputWritingSessionDelegate`, `PKTextInputCanvasControllerChangeObserver`, `PKTextInputDebugStateReporting`
- 19 instance variables, 27 properties, 83 instance methods, 1 class methods

## Instance variables

```
@"<PKTextInputHandwritingControllerDelegate>" _delegate;
@"PKTextInputCanvasController" _canvasController;
@"PKTextInputElementsController" _elementsController;
@"PKTextInputFeedbackController" _feedbackController;
@"PKTextInputReserveSpaceController" _reserveSpaceController;
@"PKTextInputDebugLogController" _debugLogController;
@"PKTextInputCursorController" _cursorController;
d _strokeAlphaOverride;
@"PKTextInputRecognitionManager" __recognitionManager;
@"PKTextInputWritingSession" __writingSession;
@"PKTextInputHandwritingShot" __activeHandwritingShot;
@"PKTextInputHandwritingShot" __possibleHandwritingShot;
@"PKTextInputResultCommand" __activeResultCommand;
@"NSMutableArray" __resultCommandsQueue;
d __lastInProgressStrokeUpdateTime;
@"NSUUID" __lastInProgressStrokeUUID;
@"PKDrawing" __lastKnownDrawing;
@"PKTextInputTargetState" __activeInputTargetState;
d __floatingBackgroundLastUpdateTime;
```

## Properties

```
@property (T@"PKTextInputRecognitionManager",R,N) debugRecognitionManager;
@property (T@"PKTextInputTargetState",R,N) debugActiveInputTargetState;
@property (T@"PKTextInputResultCommand",&,N,S_setActiveResultCommand:) _activeResultCommand;
@property (T@"PKTextInputRecognitionManager",&,N,V__recognitionManager) _recognitionManager;
@property (T@"PKTextInputWritingSession",&,N,S_setWritingSession:,V__writingSession) _writingSession;
@property (T@"PKTextInputHandwritingShot",&,N,S_setActiveHandwritingShot:,V__activeHandwritingShot) _activeHandwritingShot;
@property (T@"PKTextInputHandwritingShot",&,N,S_setPossibleHandwritingShot:,V__possibleHandwritingShot) _possibleHandwritingShot;
@property (T@"PKTextInputResultCommand",&,N,S_setActiveResultCommand:,V__activeResultCommand) _activeResultCommand;
@property (T@"NSMutableArray",R,N,V__resultCommandsQueue) _resultCommandsQueue;
@property (Td,N,V__lastInProgressStrokeUpdateTime) _lastInProgressStrokeUpdateTime;
@property (T@"NSUUID",C,N,V__lastInProgressStrokeUUID) _lastInProgressStrokeUUID;
@property (T@"PKDrawing",C,N,S_setLastKnownDrawing:,V__lastKnownDrawing) _lastKnownDrawing;
@property (T@"PKTextInputTargetState",&,N,S_setActiveInputTargetState:,V__activeInputTargetState) _activeInputTargetState;
@property (Td,N,V__floatingBackgroundLastUpdateTime) _floatingBackgroundLastUpdateTime;
@property (T@"<PKTextInputHandwritingControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"PKTextInputCanvasController",R,N,V_canvasController) canvasController;
@property (T@"PKTextInputElementsController",R,N,V_elementsController) elementsController;
@property (T@"PKTextInputFeedbackController",R,N,V_feedbackController) feedbackController;
@property (T@"PKTextInputReserveSpaceController",R,N,V_reserveSpaceController) reserveSpaceController;
@property (T@"PKTextInputDebugLogController",R,N,V_debugLogController) debugLogController;
@property (T@"PKTextInputCursorController",R,N,V_cursorController) cursorController;
@property (Tq,R,N) writingState;
@property (Td,R,N,V_strokeAlphaOverride) strokeAlphaOverride;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKTextInputHandwritingController _isCorrectionResultGesture:];
```

## Instance methods

```
-[PKTextInputHandwritingController setDelegate:];
-[PKTextInputHandwritingController delegate];
-[PKTextInputHandwritingController feedbackController];
-[PKTextInputHandwritingController _writingSession];
-[PKTextInputHandwritingController _lastInProgressStrokeUpdateTime];
-[PKTextInputHandwritingController _activeHandwritingShot];
-[PKTextInputHandwritingController _activeInputTargetState];
-[PKTextInputHandwritingController _activeResultCommand];
-[PKTextInputHandwritingController _cancelInProgressStrokeFromHandwritingShots];
-[PKTextInputHandwritingController _cancelPendingResultCommand];
-[PKTextInputHandwritingController _continuousRecognitionInterval];
-[PKTextInputHandwritingController _createPossibleHandwritingShotIfNeeded];
-[PKTextInputHandwritingController _evaluateAndProcessResultCommandsQueue];
-[PKTextInputHandwritingController _evaluateAndProcessResultCommandsQueueImmediateCommit:];
-[PKTextInputHandwritingController _floatingBackgroundLastUpdateTime];
-[PKTextInputHandwritingController _handleActiveHandwritingShotRecognitionFinished];
-[PKTextInputHandwritingController _handleResultCommandFinished:];
-[PKTextInputHandwritingController _immediateCommitTypeForQueryItem:handwritingShot:];
-[PKTextInputHandwritingController _lastInProgressStrokeUUID];
-[PKTextInputHandwritingController _lastKnownDrawing];
-[PKTextInputHandwritingController _notifyDelegateOfResultCommandState];
-[PKTextInputHandwritingController _pendingResultCommand];
-[PKTextInputHandwritingController _possibleHandwritingShot];
-[PKTextInputHandwritingController _processPossibleShotIfReady];
-[PKTextInputHandwritingController _recognitionManager];
-[PKTextInputHandwritingController _resultCommandToProcessQueryItem:handwritingShot:];
-[PKTextInputHandwritingController _resultCommandsQueue];
-[PKTextInputHandwritingController _scheduleCommitForResultCommandIfNeeded:];
-[PKTextInputHandwritingController _setActiveHandwritingShot:];
-[PKTextInputHandwritingController _setActiveInputTargetState:];
-[PKTextInputHandwritingController _setActiveResultCommand:];
-[PKTextInputHandwritingController _setLastKnownDrawing:];
-[PKTextInputHandwritingController _setPossibleHandwritingShot:];
-[PKTextInputHandwritingController _setWritingSession:];
-[PKTextInputHandwritingController _updateFloatingBackground];
-[PKTextInputHandwritingController _updateRecognitionManager];
-[PKTextInputHandwritingController _updateStrokeAlphaOverride];
-[PKTextInputHandwritingController _updateWritingSession];
-[PKTextInputHandwritingController _wantsFloatingBackground];
-[PKTextInputHandwritingController canvasController];
-[PKTextInputHandwritingController canvasController:drawingDidChange:];
-[PKTextInputHandwritingController canvasControllerDidBeginDrawing:];
-[PKTextInputHandwritingController canvasControllerDidCancelStroke:strokeAcceptanceState:];
-[PKTextInputHandwritingController canvasControllerDidEndDrawing:];
-[PKTextInputHandwritingController canvasControllerEndedStroke:];
-[PKTextInputHandwritingController canvasControllerInProgressStrokeDidChange:];
-[PKTextInputHandwritingController cleanUpFromCancelledReplay];
-[PKTextInputHandwritingController cursorController];
-[PKTextInputHandwritingController debugActiveInputTargetState];
-[PKTextInputHandwritingController debugLogController];
-[PKTextInputHandwritingController debugRecognitionManager];
-[PKTextInputHandwritingController elementsController];
-[PKTextInputHandwritingController handwritingShot:activePreviewRangeForElementRecognitionIdentifier:queryItemStableIdentifier:];
-[PKTextInputHandwritingController handwritingShot:hasCommittedResultsInSessionToElementRecognitionIdentifier:];
-[PKTextInputHandwritingController handwritingShot:inProgressGestureInitialSelectedRangeForElementRecognitionIdentifier:];
-[PKTextInputHandwritingController handwritingShot:lastCharacterLevelPositionForElementRecognitionIdentifier:];
-[PKTextInputHandwritingController handwritingShot:preferredTargetElementForQueryItemStableIdentifier:simultaneousItemStableIdentifiers:proposedTargetElement:];
-[PKTextInputHandwritingController handwritingShot:shouldSuppressGesturesForStrokesBounds:coordinateSpace:];
-[PKTextInputHandwritingController handwritingShot:willFocusAndLoadDataForTargetElement:];
-[PKTextInputHandwritingController handwritingShotDidChangeState:];
-[PKTextInputHandwritingController handwritingShotDidOverrideStrongCursor:];
-[PKTextInputHandwritingController handwritingShotStrokeIdentifiersToExcludeFromRecognition:];
-[PKTextInputHandwritingController initWithCanvasController:elementsController:feedbackController:reserveSpaceController:debugLogController:cursorController:];
-[PKTextInputHandwritingController quickCommitIfPossible];
-[PKTextInputHandwritingController reportDebugStateDescription:];
-[PKTextInputHandwritingController reserveSpaceController];
-[PKTextInputHandwritingController reserveSpaceControllerIsActiveChanged];
-[PKTextInputHandwritingController reserveSpaceControllerWillFocusElement:];
-[PKTextInputHandwritingController resultCommandCanvasController:];
-[PKTextInputHandwritingController resultCommandCursorController:];
-[PKTextInputHandwritingController resultCommandFeedbackController:];
-[PKTextInputHandwritingController resultCommandStateDidChange:];
-[PKTextInputHandwritingController resultCommandSupportedElementDelegate:];
-[PKTextInputHandwritingController set_floatingBackgroundLastUpdateTime:];
-[PKTextInputHandwritingController set_lastInProgressStrokeUUID:];
-[PKTextInputHandwritingController set_lastInProgressStrokeUpdateTime:];
-[PKTextInputHandwritingController set_recognitionManager:];
-[PKTextInputHandwritingController strokeAlphaOverride];
-[PKTextInputHandwritingController writingSession:didEndWritingInElement:];
-[PKTextInputHandwritingController writingSession:didInsertTextInElement:];
-[PKTextInputHandwritingController writingSession:elementHasPendingOperations:];
-[PKTextInputHandwritingController writingSession:willBeginWritingInElement:];
-[PKTextInputHandwritingController writingState];
```
