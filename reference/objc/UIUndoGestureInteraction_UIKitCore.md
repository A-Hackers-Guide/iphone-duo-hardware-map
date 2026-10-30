# `UIUndoGestureInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInteractiveUndoHUDActionDelegate`, `UIGestureRecognizerDelegate`, `UIEditingOverlayInteractionWithView`, `UIInteraction`
- 34 instance variables, 38 properties, 161 instance methods, 5 class methods

## Instance variables

```
B _interactiveHUDIsVisible;
B _undoStateHUDIsAnimating;
B _multiPinchTimerOn;
@"UIView" _view;
@"_UIKBUndoGestureObserver" _observerGesture;
@"_UIKBProductivitySingleTapGesture" _threeFingerSingleTap;
@"_UIKBProductivityDoubleTapGesture" _threeFingerDoubleTap;
@"_UIKBProductivityPanGestureRecognizer" _threeFingerSlide;
@"_UIKBProductivityLongPressGestureRecognizer" _threeFingerLongPress;
@"_UIKBProductivityPinchGestureRecognizer" _threeFingerPinch;
@"UIKBUndoInteractionHUD" _undoInteractiveHUD;
q _interactiveHUDMode;
@? _pasteConfirmationAction;
@"UIKBUndoStateHUD" _undoStateHUD;
@"NSLayoutConstraint" _undoStateHUDTopConstraint;
@"NSLayoutConstraint" _undoStateHUDCenterConstraint;
@"NSLayoutConstraint" _undoHUDContainerWidthConstraint;
@"NSLayoutConstraint" _undoHUDContainerHeightConstraint;
@"UIDelayedAction" _undoStateHUDDismissTimer;
q _currentAppearance;
@"UILayoutGuide" _layoutGuide;
q _previousRecognizedPanDirection;
@"UIDelayedAction" _multiPansTimer;
d _remainingDistanceToTravel;
q _beginPanDirection;
Q _panDownStateChangedCounter;
d _lastTapTimestamp;
d _initPinchableDistance;
d _previousPinchPerimeter;
q _potentialPinchDirection;
@"UIKBTextEditingTraits" _editingTraits;
{CGPoint="x"d"y"d} _previousPanLocation;
{CGPoint="x"d"y"d} _beginPanLocation;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _currentActuallSceneBounds;
```

## Properties

```
@property (T@"UIView",W,N,V_view) view;
@property (T@"_UIKBUndoGestureObserver",&,N,V_observerGesture) observerGesture;
@property (T@"_UIKBProductivitySingleTapGesture",&,N,V_threeFingerSingleTap) threeFingerSingleTap;
@property (T@"_UIKBProductivityDoubleTapGesture",&,N,V_threeFingerDoubleTap) threeFingerDoubleTap;
@property (T@"_UIKBProductivityPanGestureRecognizer",&,N,V_threeFingerSlide) threeFingerSlide;
@property (T@"_UIKBProductivityLongPressGestureRecognizer",&,N,V_threeFingerLongPress) threeFingerLongPress;
@property (T@"_UIKBProductivityPinchGestureRecognizer",&,N,V_threeFingerPinch) threeFingerPinch;
@property (T@"UIKBUndoInteractionHUD",&,N,V_undoInteractiveHUD) undoInteractiveHUD;
@property (Tq,N,V_interactiveHUDMode) interactiveHUDMode;
@property (T@?,C,N,V_pasteConfirmationAction) pasteConfirmationAction;
@property (T@"UIKBUndoStateHUD",&,N,V_undoStateHUD) undoStateHUD;
@property (T@"NSLayoutConstraint",&,N,V_undoStateHUDTopConstraint) undoStateHUDTopConstraint;
@property (T@"NSLayoutConstraint",&,N,V_undoStateHUDCenterConstraint) undoStateHUDCenterConstraint;
@property (T@"NSLayoutConstraint",&,N,V_undoHUDContainerWidthConstraint) undoHUDContainerWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_undoHUDContainerHeightConstraint) undoHUDContainerHeightConstraint;
@property (T@"UIDelayedAction",&,N,V_undoStateHUDDismissTimer) undoStateHUDDismissTimer;
@property (Tq,N,V_currentAppearance) currentAppearance;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_currentActuallSceneBounds) currentActuallSceneBounds;
@property (T@"UILayoutGuide",&,N,V_layoutGuide) layoutGuide;
@property (TB,N,V_interactiveHUDIsVisible) interactiveHUDIsVisible;
@property (Tq,N,V_previousRecognizedPanDirection) previousRecognizedPanDirection;
@property (T@"UIDelayedAction",&,N,V_multiPansTimer) multiPansTimer;
@property (Td,N,V_remainingDistanceToTravel) remainingDistanceToTravel;
@property (T{CGPoint=dd},N,V_previousPanLocation) previousPanLocation;
@property (T{CGPoint=dd},N,V_beginPanLocation) beginPanLocation;
@property (Tq,N,V_beginPanDirection) beginPanDirection;
@property (TQ,N,V_panDownStateChangedCounter) panDownStateChangedCounter;
@property (TB,N,V_undoStateHUDIsAnimating) undoStateHUDIsAnimating;
@property (Td,N,V_lastTapTimestamp) lastTapTimestamp;
@property (TB,N,V_multiPinchTimerOn) multiPinchTimerOn;
@property (Td,N,V_initPinchableDistance) initPinchableDistance;
@property (Td,N,V_previousPinchPerimeter) previousPinchPerimeter;
@property (Tq,N,V_potentialPinchDirection) potentialPinchDirection;
@property (T@"UIKBTextEditingTraits",&,N,V_editingTraits) editingTraits;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIUndoGestureInteraction _isKeyWindowSceneSessionRoleValidForTutorial];
+[UIUndoGestureInteraction iWorkFamily];
+[UIUndoGestureInteraction presentProductivityGestureTutorialIfNeededWithCompletion:];
+[UIUndoGestureInteraction presentProductivityGestureTutorialInlineWithCompletion:];
+[UIUndoGestureInteraction showSecurePasteConfirmationWithCompletionHandler:];
```

## Instance methods

```
-[UIUndoGestureInteraction undo:];
-[UIUndoGestureInteraction cutOperation];
-[UIUndoGestureInteraction pasteOperation];
-[UIUndoGestureInteraction _endPan:];
-[UIUndoGestureInteraction canRedo];
-[UIUndoGestureInteraction canUndo];
-[UIUndoGestureInteraction copyOperation];
-[UIUndoGestureInteraction currentResponder];
-[UIUndoGestureInteraction tooSlow:];
-[UIUndoGestureInteraction setRemainingDistanceToTravel:];
-[UIUndoGestureInteraction setLayoutGuide:];
-[UIUndoGestureInteraction setUndoHUDContainerWidthConstraint:];
-[UIUndoGestureInteraction threeFingerDoubleTapUndoAction];
-[UIUndoGestureInteraction _undoManager];
-[UIUndoGestureInteraction pasteConfirmationAction];
-[UIUndoGestureInteraction setCurrentAppearance:];
-[UIUndoGestureInteraction setThreeFingerSingleTap:];
-[UIUndoGestureInteraction threeFingerDoubleTap];
-[UIUndoGestureInteraction _updatePinch:];
-[UIUndoGestureInteraction threeFingerLongPress:];
-[UIUndoGestureInteraction performActionWithDirection:];
-[UIUndoGestureInteraction setPreviousRecognizedPanDirection:];
-[UIUndoGestureInteraction _cancelPinch:];
-[UIUndoGestureInteraction setPotentialPinchDirection:];
-[UIUndoGestureInteraction gestureRecognizer:shouldReceiveTouch:];
-[UIUndoGestureInteraction panDownStateChangedCounter];
-[UIUndoGestureInteraction currentActuallSceneBounds];
-[UIUndoGestureInteraction clearUndoStateHUDDismissTimer];
-[UIUndoGestureInteraction layoutGuide];
-[UIUndoGestureInteraction needUpdateHUDForContainerChange];
-[UIUndoGestureInteraction _endPinchWithDirection:];
-[UIUndoGestureInteraction applicationWillSuspend];
-[UIUndoGestureInteraction undoStateHUDTopConstraint];
-[UIUndoGestureInteraction previousPanLocation];
-[UIUndoGestureInteraction isRTLMode];
-[UIUndoGestureInteraction editingTraits];
-[UIUndoGestureInteraction setBeginPanLocation:];
-[UIUndoGestureInteraction deactiveActiveKeysIfNeeded:];
-[UIUndoGestureInteraction setUndoStateHUD:];
-[UIUndoGestureInteraction undoControlTypeWithDirection:];
-[UIUndoGestureInteraction _endPanWithDirection:];
-[UIUndoGestureInteraction textEditingOperationsAvailableWithGestureRecognizer:];
-[UIUndoGestureInteraction threeFingerLongPress];
-[UIUndoGestureInteraction _installUndoManagerObservers];
-[UIUndoGestureInteraction interactiveHUDMode];
-[UIUndoGestureInteraction _removeGestureRecognizers];
-[UIUndoGestureInteraction setUndoStateHUDIsAnimating:];
-[UIUndoGestureInteraction setUndoStateHUDTopConstraint:];
-[UIUndoGestureInteraction _updateHUDControlState];
-[UIUndoGestureInteraction currentTime];
-[UIUndoGestureInteraction currentAppearance];
-[UIUndoGestureInteraction setUndoStateHUDVisibility:withType:available:];
-[UIUndoGestureInteraction threeFingerPinch:];
-[UIUndoGestureInteraction threeFingerSlide];
-[UIUndoGestureInteraction setPasteConfirmationAction:];
-[UIUndoGestureInteraction setView:];
-[UIUndoGestureInteraction undoStateHUDCenterConstraint];
-[UIUndoGestureInteraction setThreeFingerSlide:];
-[UIUndoGestureInteraction clearMultiPinchTimer];
-[UIUndoGestureInteraction animateSpringCoverWithSuccess:direction:remainingDistanceToTravel:];
-[UIUndoGestureInteraction undoStateHUDDismissTimerElaspsed:];
-[UIUndoGestureInteraction _createAndUpdateUndoInteractiveHUDIfNecessary];
-[UIUndoGestureInteraction beginPanLocation];
-[UIUndoGestureInteraction editingInteractionOptionsAllowGestureRecognizerToBegin:];
-[UIUndoGestureInteraction editingOverlayContainerDidChangeToSceneBounds:];
-[UIUndoGestureInteraction setUndoInteractiveHUDVisibility:];
-[UIUndoGestureInteraction _addGestureRecognizers];
-[UIUndoGestureInteraction undoManagerOperationsUndoRedoAvailable];
-[UIUndoGestureInteraction animateDisplayingStateHUD];
-[UIUndoGestureInteraction undoStateHUDIsAnimating];
-[UIUndoGestureInteraction setInitPinchableDistance:];
-[UIUndoGestureInteraction view];
-[UIUndoGestureInteraction setPreviousPanLocation:];
-[UIUndoGestureInteraction observerGesture];
-[UIUndoGestureInteraction gestureRecognizerShouldBegin:];
-[UIUndoGestureInteraction animateInStateHUD];
-[UIUndoGestureInteraction scrollViewForInputDelegate];
-[UIUndoGestureInteraction setUndoInteractiveHUD:];
-[UIUndoGestureInteraction undoGestureIsMoving:];
-[UIUndoGestureInteraction undoStateHUDDismissTimer];
-[UIUndoGestureInteraction observerGestureHandler:];
-[UIUndoGestureInteraction setMultiPansTimer:];
-[UIUndoGestureInteraction undoStateHUD];
-[UIUndoGestureInteraction setThreeFingerLongPress:];
-[UIUndoGestureInteraction setBeginPanDirection:];
-[UIUndoGestureInteraction setMultiPinchTimerOn:];
-[UIUndoGestureInteraction initPinchableDistance];
-[UIUndoGestureInteraction _createAndUpdateUndoStateHUDIfNecessary];
-[UIUndoGestureInteraction threeFingerPinch];
-[UIUndoGestureInteraction interactiveHUDButtonForDirection:];
-[UIUndoGestureInteraction canCopy];
-[UIUndoGestureInteraction previousRecognizedPanDirection];
-[UIUndoGestureInteraction removeAllHUDOnContainerChange];
-[UIUndoGestureInteraction fullyCloseCoverWithComplete:];
-[UIUndoGestureInteraction interactiveHUDIsVisible];
-[UIUndoGestureInteraction willMoveToView:];
-[UIUndoGestureInteraction keyboardAppearance];
-[UIUndoGestureInteraction _threeFingerSingleTapAction];
-[UIUndoGestureInteraction gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[UIUndoGestureInteraction canPaste];
-[UIUndoGestureInteraction setObserverGesture:];
-[UIUndoGestureInteraction setPasteConfirmationHUDVisibility:];
-[UIUndoGestureInteraction _updateUndoPan:];
-[UIUndoGestureInteraction threeFingerSlide:];
-[UIUndoGestureInteraction currentInteractiveHUDVisible];
-[UIUndoGestureInteraction beginPanDirection];
-[UIUndoGestureInteraction _undoManagerFlattenedGroupingInfo];
-[UIUndoGestureInteraction canCut];
-[UIUndoGestureInteraction _startPinch:];
-[UIUndoGestureInteraction setInteractiveHUDMode:];
-[UIUndoGestureInteraction gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[UIUndoGestureInteraction currentStateHUDVisible];
-[UIUndoGestureInteraction _createGestureRecognizersIfNecessary];
-[UIUndoGestureInteraction setLastTapTimestamp:];
-[UIUndoGestureInteraction redo:];
-[UIUndoGestureInteraction setEditingTraits:];
-[UIUndoGestureInteraction responderForOperation:withSender:];
-[UIUndoGestureInteraction remainingDistanceToTravel];
-[UIUndoGestureInteraction setPreviousPinchPerimeter:];
-[UIUndoGestureInteraction setPanDownStateChangedCounter:];
-[UIUndoGestureInteraction setUndoStateHUDDismissTimer:];
-[UIUndoGestureInteraction threeFingerDoubleTap:];
-[UIUndoGestureInteraction actualSceneBounds];
-[UIUndoGestureInteraction setCurrentActuallSceneBounds:];
-[UIUndoGestureInteraction performGestureWithDirection:];
-[UIUndoGestureInteraction touchUndoStateHUDDismissTimer];
-[UIUndoGestureInteraction performGestureWithDirection:authenticationMessage:];
-[UIUndoGestureInteraction setInteractiveHUDIsVisible:];
-[UIUndoGestureInteraction layoutUndoInteractiveHUD];
-[UIUndoGestureInteraction setUndoStateHUDCenterConstraint:];
-[UIUndoGestureInteraction multiPinchTimerOn];
-[UIUndoGestureInteraction bundleIniWorkFamily:];
-[UIUndoGestureInteraction setUndoHUDType:visibility:];
-[UIUndoGestureInteraction threeFingerSingleTap];
-[UIUndoGestureInteraction multiPansTimer];
-[UIUndoGestureInteraction undoInteractiveHUD];
-[UIUndoGestureInteraction multiPansTimerElaspsed:];
-[UIUndoGestureInteraction _endPinch:];
-[UIUndoGestureInteraction setThreeFingerDoubleTap:];
-[UIUndoGestureInteraction startMultiPinchTimer:];
-[UIUndoGestureInteraction currentInteractionHUD];
-[UIUndoGestureInteraction fullyOpenAndCloseCoverWithBeginDirection:];
-[UIUndoGestureInteraction _startUndoPan:];
-[UIUndoGestureInteraction previousPinchPerimeter];
-[UIUndoGestureInteraction setUndoHUDContainerHeightConstraint:];
-[UIUndoGestureInteraction didMoveToView:];
-[UIUndoGestureInteraction undoManagerOperationsCutCopyPasteAvailable];
-[UIUndoGestureInteraction clearMultiPansTimer];
-[UIUndoGestureInteraction layoutUndoStateHUD];
-[UIUndoGestureInteraction _uninstallUndoManagerObservers];
-[UIUndoGestureInteraction lastTapTimestamp];
-[UIUndoGestureInteraction potentialPinchDirection];
-[UIUndoGestureInteraction slideDirectionWithGesture:];
-[UIUndoGestureInteraction clearHUDViews];
-[UIUndoGestureInteraction undoHUDContainerHeightConstraint];
-[UIUndoGestureInteraction undoHUDContainerWidthConstraint];
-[UIUndoGestureInteraction disableEnclosingScrollViewScrolling];
-[UIUndoGestureInteraction threeFingerSingleTap:];
-[UIUndoGestureInteraction setThreeFingerPinch:];
-[UIUndoGestureInteraction touchMultiPansTimer];
-[UIUndoGestureInteraction privateEditingInteractionOptions];
```
