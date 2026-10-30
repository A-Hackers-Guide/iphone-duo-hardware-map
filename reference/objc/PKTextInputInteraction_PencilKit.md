# `PKTextInputInteraction`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKTextInputDebugStateReporting`, `UIEditingOverlayInteractionWithView`, `PKTextInputCanvasControllerDelegate`, `PKTextInputCanvasControllerChangeObserver`, `PKTextInputHandwritingControllerDelegate`, `PKTextInputElementsControllerDelegate`, `PKTextInputPaletteControllerDelegate`, `PKTextInputContainerViewDelegate`, `PKTextInputDrawingGestureRecognizerDelegate`, `PKTextInputFeedbackControllerDelegate`, `PKTextInputCursorControllerDelegate`, `PKTextInputReserveSpaceControllerDelegate`, `PKTextInputDebugViewControllerDelegate`, `PKTextInputTouchDetectionGestureRecognizerDelegate`, `PKTextInputLanguageSelectionControllerObserver`, `PKTextInputHoverControllerDelegate`, `PKPencilObserverInteractionDelegate`, `UIInteraction`
- 29 instance variables, 47 properties, 141 instance methods, 2 class methods

## Instance variables

```
B _shouldBeActive;
B _replayCancelled;
B __handwritingInteractionEnabled;
B __debugOverlaySettingEnabled;
@"UIView" _view;
@"PKTContainerView" __containerView;
@"PKTextInputCanvasController" __canvasController;
@"PKTextInputFeedbackController" __feedbackController;
@"PKTextInputPaletteController" __paletteController;
@"PKTextInputTouchDetectionGestureRecognizer" __touchDetectionGestureRecognizer;
@"PKTextInputElementsController" __elementsController;
@"PKTextInputHandwritingController" __handwritingController;
d __lastHandwritingEventTimestamp;
@"PKTextInputDrawingGestureRecognizer" _drawingGestureRecognizer;
@"PKTextInputSingleElementFinder" __drawingGestureElementFinder;
@"PKTextInputKeyboardSuppressionPolicyDelegate" __keyboardSuppressionPolicyDelegate;
@"PKTextInputDebugLogController" __debugLogController;
Q __debugControllerAnchorCorner;
@"PKTextInputDebugViewController" __debugViewController;
@"PKTextInputDebugStateIntrospector" __debugStateIntrospector;
@"PKTextInputCursorController" __cursorController;
@"PKTextInputReserveSpaceController" __reserveSpaceController;
d __lastDebugCornerEventTimestamp;
@"PKTextInputElement" __beginGestureElement;
@"PKTextInputElementContent" __beginGestureElementContentForLineBreak;
@"PKTextInputHoverController" __hoverController;
@"PKPencilObserverInteraction" __pencilObserverInteraction;
@"PKPencilSqueezeInteraction" __pencilSqueezeInteraction;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _editingOverlayContainerSceneBounds;
```

## Properties

```
@property (T@"PKTextInputDrawingGestureRecognizer",R,N) drawingGestureRecognizer;
@property (T@"PKTextInputCanvasController",R,N) canvasController;
@property (T@"PKTextInputElementsController",R,N) elementsController;
@property (T@"PKTextInputHandwritingController",R,N) handwritingController;
@property (T@"PKTextInputReserveSpaceController",R,N) reserveSpaceController;
@property (T@"PKTextInputDebugLogController",R,N) debugLogController;
@property (T@"PKTextInputCursorController",R,N) cursorController;
@property (T@"PKPencilObserverInteraction",R,N) pencilObserverInteraction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",W,N,V_view) view;
@property (T@"PKTContainerView",&,N,V__containerView) _containerView;
@property (T@"PKTextInputCanvasController",R,N,V__canvasController) _canvasController;
@property (T@"PKTextInputFeedbackController",&,N,V__feedbackController) _feedbackController;
@property (T@"PKTextInputPaletteController",&,N,V__paletteController) _paletteController;
@property (T@"PKTextInputTouchDetectionGestureRecognizer",&,N,V__touchDetectionGestureRecognizer) _touchDetectionGestureRecognizer;
@property (T@"PKTextInputElementsController",&,N,V__elementsController) _elementsController;
@property (T@"PKTextInputHandwritingController",&,N,V__handwritingController) _handwritingController;
@property (TB,N,S_setHandwritingInteractionEnabled:,V__handwritingInteractionEnabled) _handwritingInteractionEnabled;
@property (Td,N,S_setLastHandwritingEventTimestamp:,V__lastHandwritingEventTimestamp) _lastHandwritingEventTimestamp;
@property (T@"PKTextInputDrawingGestureRecognizer",&,N,V_drawingGestureRecognizer) drawingGestureRecognizer;
@property (T@"PKTextInputSingleElementFinder",&,N,V__drawingGestureElementFinder) _drawingGestureElementFinder;
@property (T@"PKTextInputKeyboardSuppressionPolicyDelegate",&,N,V__keyboardSuppressionPolicyDelegate) _keyboardSuppressionPolicyDelegate;
@property (T@"PKTextInputDebugLogController",&,N,V__debugLogController) _debugLogController;
@property (TQ,N,S_setDebugControllerAnchorCorner:,V__debugControllerAnchorCorner) _debugControllerAnchorCorner;
@property (T@"PKTextInputDebugViewController",&,N,V__debugViewController) _debugViewController;
@property (T@"PKTextInputDebugStateIntrospector",&,N,V__debugStateIntrospector) _debugStateIntrospector;
@property (T@"PKTextInputCursorController",&,N,V__cursorController) _cursorController;
@property (T@"PKTextInputReserveSpaceController",&,N,V__reserveSpaceController) _reserveSpaceController;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_editingOverlayContainerSceneBounds) editingOverlayContainerSceneBounds;
@property (Td,N,V__lastDebugCornerEventTimestamp) _lastDebugCornerEventTimestamp;
@property (TB,N,V__debugOverlaySettingEnabled) _debugOverlaySettingEnabled;
@property (T@"PKTextInputElement",&,N,V__beginGestureElement) _beginGestureElement;
@property (T@"PKTextInputElementContent",&,N,V__beginGestureElementContentForLineBreak) _beginGestureElementContentForLineBreak;
@property (T@"PKTextInputHoverController",&,N,V__hoverController) _hoverController;
@property (T@"PKPencilObserverInteraction",&,N,V__pencilObserverInteraction) _pencilObserverInteraction;
@property (T@"PKPencilSqueezeInteraction",&,N,V__pencilSqueezeInteraction) _pencilSqueezeInteraction;
@property (TB,R,N,GisFloatingKeyboardVisible) floatingKeyboardVisible;
@property (T@"NSArray",R,N) enabledLanguageIdentifiers;
@property (T@"NSString",R,N) currentLanguageIdentifier;
@property (TB,R,N) isCursorWeak;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKTextInputInteraction interactionForScene:];
+[PKTextInputInteraction writeCurrentPencilSharpenerLogsToURL:fullLogs:windowScene:];
```

## Instance methods

```
-[PKTextInputInteraction _feedbackController];
-[PKTextInputInteraction _updateInteractionEnabled];
-[PKTextInputInteraction presentFloatingKeyboard];
-[PKTextInputInteraction init];
-[PKTextInputInteraction dealloc];
-[PKTextInputInteraction setView:];
-[PKTextInputInteraction _updateGestureRecognizers];
-[PKTextInputInteraction editingOverlayContainerDidChangeToSceneBounds:];
-[PKTextInputInteraction view];
-[PKTextInputInteraction drawingGestureRecognizer:shouldBeginDrawingWithTouches:event:];
-[PKTextInputInteraction setDrawingGestureRecognizer:];
-[PKTextInputInteraction willMoveToView:];
-[PKTextInputInteraction _containerView];
-[PKTextInputInteraction gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[PKTextInputInteraction isFloatingKeyboardVisible];
-[PKTextInputInteraction dismissFloatingKeyboard];
-[PKTextInputInteraction drawingGestureRecognizer];
-[PKTextInputInteraction didMoveToView:];
-[PKTextInputInteraction currentLanguageIdentifier];
-[PKTextInputInteraction enabledLanguageIdentifiers];
-[PKTextInputInteraction presentProblemReportingView];
-[PKTextInputInteraction setCurrentLanguageIdentifier:];
-[PKTextInputInteraction paletteControllerContainerView:];
-[PKTextInputInteraction touchesDetected];
-[PKTextInputInteraction set_debugOverlaySettingEnabled:];
-[PKTextInputInteraction _beginGestureElement];
-[PKTextInputInteraction _beginGestureElementContentForLineBreak];
-[PKTextInputInteraction _beginGestureIfPossible:];
-[PKTextInputInteraction _canvasController];
-[PKTextInputInteraction _cursorController];
-[PKTextInputInteraction _debugControllerAnchorCorner];
-[PKTextInputInteraction _debugLogController];
-[PKTextInputInteraction _debugOverlaySettingEnabled];
-[PKTextInputInteraction _debugStateIntrospector];
-[PKTextInputInteraction _debugViewController];
-[PKTextInputInteraction _drawingGestureElementFinder];
-[PKTextInputInteraction _drawingGestureElementFinderDidFinishWithLocationInContainerView:];
-[PKTextInputInteraction _elementsController];
-[PKTextInputInteraction _findControlFromHitView:referenceView:];
-[PKTextInputInteraction _handleDrawingGestureTapInElement:gesture:touch:];
-[PKTextInputInteraction _handlePotentialDebugOverlayGestureAtPoint:];
-[PKTextInputInteraction _handwritingController];
-[PKTextInputInteraction _handwritingInteractionEnabled];
-[PKTextInputInteraction _hoverController];
-[PKTextInputInteraction _isTapAwayFromCurrentStrokesAtCanvasViewLocation:];
-[PKTextInputInteraction _keyboardSuppressionPolicyDelegate];
-[PKTextInputInteraction _lastDebugCornerEventTimestamp];
-[PKTextInputInteraction _lastHandwritingEventTimestamp];
-[PKTextInputInteraction _notifyTargetElementOfTouches:event:];
-[PKTextInputInteraction _paletteController];
-[PKTextInputInteraction _pencilObserverInteraction];
-[PKTextInputInteraction _pencilSqueezeInteraction];
-[PKTextInputInteraction _reserveSpaceController];
-[PKTextInputInteraction _setDebugControllerAnchorCorner:];
-[PKTextInputInteraction _setHandwritingInteractionEnabled:];
-[PKTextInputInteraction _setLastHandwritingEventTimestamp:];
-[PKTextInputInteraction _shouldAvoidStartingDrawingOnView:location:];
-[PKTextInputInteraction _topLevelHitViewForContainerViewPosition:event:];
-[PKTextInputInteraction _touchDetectionGestureRecognizer];
-[PKTextInputInteraction _updateCanvasController];
-[PKTextInputInteraction _updateCanvasStrokeColor];
-[PKTextInputInteraction _updateContainerView];
-[PKTextInputInteraction _updateDebugController];
-[PKTextInputInteraction _updateElementsController];
-[PKTextInputInteraction _updateHandwritingController];
-[PKTextInputInteraction _updateKeyboardSuppressionPolicy];
-[PKTextInputInteraction _updatePaletteController];
-[PKTextInputInteraction cancelReplay];
-[PKTextInputInteraction canvasController];
-[PKTextInputInteraction canvasController:drawingDidChange:];
-[PKTextInputInteraction canvasControllerCanvasDidFinishAnimatingStrokes:];
-[PKTextInputInteraction canvasControllerContainerView:];
-[PKTextInputInteraction canvasControllerDidBeginDrawing:];
-[PKTextInputInteraction canvasControllerDidCancelStroke:strokeAcceptanceState:];
-[PKTextInputInteraction canvasControllerDidEndDrawing:];
-[PKTextInputInteraction canvasControllerDrawingGestureRecognizer:];
-[PKTextInputInteraction canvasControllerEndedStroke:];
-[PKTextInputInteraction canvasControllerHasVisibleStrokesChanged:];
-[PKTextInputInteraction canvasControllerInProgressStrokeDidChange:];
-[PKTextInputInteraction canvasControllerPreferredStrokeColor:animated:];
-[PKTextInputInteraction containerView:hitTest:withEvent:];
-[PKTextInputInteraction cursorController];
-[PKTextInputInteraction cursorControllerCustomHighlightFeedbackIsVisible:];
-[PKTextInputInteraction cursorControllerWritingState:];
-[PKTextInputInteraction debugLogController];
-[PKTextInputInteraction debugViewControllerNeedsDismiss:];
-[PKTextInputInteraction drawingGestureRecognizer:shouldFinishGestureWithTouch:];
-[PKTextInputInteraction drawingGestureRecognizerDrawingTargetIsDrawingDidChange:];
-[PKTextInputInteraction drawingGestureRecognizerLongPressShouldBegin:];
-[PKTextInputInteraction drawingGestureRecognizerLongPressStateDidChange:];
-[PKTextInputInteraction drawingGestureRecognizerRequiresPastTapToBegin:];
-[PKTextInputInteraction drawingGestureRecognizerRequiresTargetElementToBegin:];
-[PKTextInputInteraction drawingGestureStrokeAcceptanceStateDidChange:];
-[PKTextInputInteraction editingOverlayContainerSceneBounds];
-[PKTextInputInteraction elementsController];
-[PKTextInputInteraction elementsControllerLastDiscoveredElementsDidChange:];
-[PKTextInputInteraction feedbackControllerContainerView:];
-[PKTextInputInteraction feedbackControllerShowingCustomFeedbackDidChange:];
-[PKTextInputInteraction handwritingController];
-[PKTextInputInteraction handwritingControllerDidFinishActiveCommands:];
-[PKTextInputInteraction handwritingControllerStrokeAlphaOverrideDidChange:];
-[PKTextInputInteraction handwritingControllerWritingStateDidChange:];
-[PKTextInputInteraction hoverController:topLevelHitViewAt:];
-[PKTextInputInteraction hoverControllerContainerView:];
-[PKTextInputInteraction hoverControllerCursorController:];
-[PKTextInputInteraction hoverControllerDidLift:];
-[PKTextInputInteraction isCursorWeak];
-[PKTextInputInteraction paletteControllerDebugSharpenerLog:];
-[PKTextInputInteraction pencilObserverInteraction];
-[PKTextInputInteraction reportDebugStateDescription:];
-[PKTextInputInteraction reserveSpaceController];
-[PKTextInputInteraction reserveSpaceController:willFocusElement:];
-[PKTextInputInteraction reserveSpaceControllerIsActiveChanged:];
-[PKTextInputInteraction reserveSpaceControllerIsPlaceholderVisibleChanged:];
-[PKTextInputInteraction saveInteractionForScene:];
-[PKTextInputInteraction setEditingOverlayContainerSceneBounds:];
-[PKTextInputInteraction set_beginGestureElement:];
-[PKTextInputInteraction set_beginGestureElementContentForLineBreak:];
-[PKTextInputInteraction set_containerView:];
-[PKTextInputInteraction set_cursorController:];
-[PKTextInputInteraction set_debugLogController:];
-[PKTextInputInteraction set_debugStateIntrospector:];
-[PKTextInputInteraction set_debugViewController:];
-[PKTextInputInteraction set_drawingGestureElementFinder:];
-[PKTextInputInteraction set_elementsController:];
-[PKTextInputInteraction set_feedbackController:];
-[PKTextInputInteraction set_handwritingController:];
-[PKTextInputInteraction set_hoverController:];
-[PKTextInputInteraction set_keyboardSuppressionPolicyDelegate:];
-[PKTextInputInteraction set_lastDebugCornerEventTimestamp:];
-[PKTextInputInteraction set_paletteController:];
-[PKTextInputInteraction set_pencilObserverInteraction:];
-[PKTextInputInteraction set_pencilSqueezeInteraction:];
-[PKTextInputInteraction set_reserveSpaceController:];
-[PKTextInputInteraction set_touchDetectionGestureRecognizer:];
-[PKTextInputInteraction simulateReserveSpaceForTextInputView:location:completion:];
-[PKTextInputInteraction supportedElementDelegateForHandwritingController:];
-[PKTextInputInteraction textInputLanguageSelectionControllerDidChangeLanguage:];
-[PKTextInputInteraction textInputPaletteControllerFloatingKeyboardWillHide:];
-[PKTextInputInteraction textInputPaletteControllerFloatingKeyboardWillShow:];
-[PKTextInputInteraction windowSceneForController:];
```
