# `UITextInteraction_AssistantDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `UITextAutoscrolling`, `NSObject`
- 0 instance variables, 22 properties, 90 instance methods, 0 class methods

## Properties

```
@property (TB,N) autoscrolled;
@property (T{CGPoint=dd},N) loupeGestureEndPoint;
@property (TB,N) needsGestureUpdate;
@property (TB,R,N) willHandoffLoupeMagnifier;
@property (TB,N) expectingCommit;
@property (T@"_UIKeyboardTextSelectionController",R,N) activeSelectionController;
@property (T@"UITextCursorAssertionController",R,N) _assertionController;
@property (T@"_UITextInteractionEditMenuAssistant",R,N) _editMenuAssistant;
@property (T@"_UITextChoiceAccelerationAssistant",R,N) _textChoicesAssistant;
@property (T@,&,N) grabberSuppressionAssertion;
@property (T@,&,N) keyboardSuppressionAssertion;
@property (T@"UIView<_UITextSelectionWidgetAnimating>",R,N) _caretView;
@property (Ti,N) selectionHighlightMode;
@property (T@"UITextSelection",R,N) activeSelection;
@property (T@"UITextRangeAdjustmentInteraction",R,N) rangeAdjustmentInteraction;
@property (TB,N,GisSelectionDisplayVisible) selectionDisplayVisible;
@property (TB,N,GisCursorBlinkAnimationEnabled) cursorBlinkAnimationEnabled;
@property (TB,R,N,GisDisplayingVerticalSelection) displayingVerticalSelection;
@property (Ti,N) glowViewMode;
@property (T@"UIView",R,N) dynamicCaretView;
@property (T@"UIContextMenuInteraction",R,N) contextMenuInteraction;
@property (T@"<UIContextMenuInteractionDelegate>",W,N) externalContextMenuInteractionDelegate;
```

## Instance methods

```
-[UITextInteraction_AssistantDelegate _textChoicesAssistant];
-[UITextInteraction_AssistantDelegate _editMenuAssistant];
-[UITextInteraction_AssistantDelegate dismissMenuForInputUI];
-[UITextInteraction_AssistantDelegate hideSelectionCommands];
-[UITextInteraction_AssistantDelegate _assertionController];
-[UITextInteraction_AssistantDelegate convertPointToRenderSpace:textRange:];
-[UITextInteraction_AssistantDelegate selectionChanged];
-[UITextInteraction_AssistantDelegate setExternalContextMenuInteractionDelegate:];
-[UITextInteraction_AssistantDelegate canBeginDragCursor:];
-[UITextInteraction_AssistantDelegate keyboardSuppressionAssertion];
-[UITextInteraction_AssistantDelegate view];
-[UITextInteraction_AssistantDelegate presentMenuForInputUI:preferredArrowDirection:];
-[UITextInteraction_AssistantDelegate isDisplayingMenuForInputUI];
-[UITextInteraction_AssistantDelegate contextMenuInteraction];
-[UITextInteraction_AssistantDelegate setSelectionWithPoint:];
-[UITextInteraction_AssistantDelegate willHandoffLoupeMagnifier];
-[UITextInteraction_AssistantDelegate willBeginFloatingCursor:];
-[UITextInteraction_AssistantDelegate setKeyboardSuppressionAssertion:];
-[UITextInteraction_AssistantDelegate showSelectionCommands];
-[UITextInteraction_AssistantDelegate grabberSuppressionAssertion];
-[UITextInteraction_AssistantDelegate endFloatingCursor];
-[UITextInteraction_AssistantDelegate setGrabberSuppressionAssertion:];
-[UITextInteraction_AssistantDelegate beginFloatingCursorAtPoint:];
-[UITextInteraction_AssistantDelegate isDisplayingMenu];
-[UITextInteraction_AssistantDelegate setGestureRecognizers];
-[UITextInteraction_AssistantDelegate scrollSelectionToVisible];
-[UITextInteraction_AssistantDelegate extendSelectionToPoint:];
-[UITextInteraction_AssistantDelegate activeSelection];
-[UITextInteraction_AssistantDelegate expectingCommit];
-[UITextInteraction_AssistantDelegate didPerformLoupeSelectionHandoff];
-[UITextInteraction_AssistantDelegate setCursorBlinkAnimationEnabled:];
-[UITextInteraction_AssistantDelegate _caretView];
-[UITextInteraction_AssistantDelegate _legacySelectionView];
-[UITextInteraction_AssistantDelegate activeSelectionController];
-[UITextInteraction_AssistantDelegate autoscrolled];
-[UITextInteraction_AssistantDelegate checkEditabilityAndSetFirstResponderIfNecessary];
-[UITextInteraction_AssistantDelegate clearStashedSelection];
-[UITextInteraction_AssistantDelegate containerAllowsSelectionTintOnly];
-[UITextInteraction_AssistantDelegate containerIsTextField];
-[UITextInteraction_AssistantDelegate convertPointToRenderSpace:textPosition:];
-[UITextInteraction_AssistantDelegate didEndSelectionInteraction];
-[UITextInteraction_AssistantDelegate didUseStashedSelection];
-[UITextInteraction_AssistantDelegate dynamicCaretView];
-[UITextInteraction_AssistantDelegate extendSelectionToLoupeOrSetToPoint:];
-[UITextInteraction_AssistantDelegate externalContextMenuInteractionDelegate];
-[UITextInteraction_AssistantDelegate glowViewMode];
-[UITextInteraction_AssistantDelegate hasActiveSelectionInteraction];
-[UITextInteraction_AssistantDelegate isCursorBlinkAnimationEnabled];
-[UITextInteraction_AssistantDelegate isDisplayingVerticalSelection];
-[UITextInteraction_AssistantDelegate isSelectionDisplayVisible];
-[UITextInteraction_AssistantDelegate lollipopGestureWithState:location:locationOfFirstTouch:forTouchType:];
-[UITextInteraction_AssistantDelegate loupeGestureEndPoint];
-[UITextInteraction_AssistantDelegate loupeOrientation];
-[UITextInteraction_AssistantDelegate needsGestureUpdate];
-[UITextInteraction_AssistantDelegate notifyKeyboardSelectionChanged];
-[UITextInteraction_AssistantDelegate obtainSelectionGrabberSuppressionAssertion];
-[UITextInteraction_AssistantDelegate rangeAdjustmentInteraction];
-[UITextInteraction_AssistantDelegate rangeForTextReplacement:];
-[UITextInteraction_AssistantDelegate resetWillHandoffLoupeMagnifier];
-[UITextInteraction_AssistantDelegate scheduleDictationReplacementsForAlternatives:range:];
-[UITextInteraction_AssistantDelegate scheduleReplacementsForRange:withOptions:];
-[UITextInteraction_AssistantDelegate selectWordWithoutShowingCommands];
-[UITextInteraction_AssistantDelegate selectionHighlightMode];
-[UITextInteraction_AssistantDelegate setAutomaticSelectionCommandsSuppressedForPointerTouchType:];
-[UITextInteraction_AssistantDelegate setAutoscrolled:];
-[UITextInteraction_AssistantDelegate setExpectingCommit:];
-[UITextInteraction_AssistantDelegate setFirstResponderIfNecessary];
-[UITextInteraction_AssistantDelegate setFirstResponderIfNecessaryActivatingSelection:];
-[UITextInteraction_AssistantDelegate setGlowViewMode:];
-[UITextInteraction_AssistantDelegate setLoupeGestureEndPoint:];
-[UITextInteraction_AssistantDelegate setNeedsGestureUpdate:];
-[UITextInteraction_AssistantDelegate setNeedsSelectionDisplayUpdate];
-[UITextInteraction_AssistantDelegate setSelectionDisplayVisible:];
-[UITextInteraction_AssistantDelegate setSelectionHighlightMode:];
-[UITextInteraction_AssistantDelegate setSuppressSystemUI:];
-[UITextInteraction_AssistantDelegate shouldDisplayLoupeSessionForTouchType:];
-[UITextInteraction_AssistantDelegate showProofreadingSuggestionList:selectedIndex:range:];
-[UITextInteraction_AssistantDelegate stashCurrentSelection];
-[UITextInteraction_AssistantDelegate supportsIndirectInteractions];
-[UITextInteraction_AssistantDelegate updateDisplayedSelection];
-[UITextInteraction_AssistantDelegate updateFloatingCursorAtPoint:animated:];
-[UITextInteraction_AssistantDelegate updateWithMagnifierTerminalPoint:];
-[UITextInteraction_AssistantDelegate updatedTextReplacementsMenuWithMenuElements:];
-[UITextInteraction_AssistantDelegate useGesturesForEditableContent];
-[UITextInteraction_AssistantDelegate usesAsynchronousSelectionController];
-[UITextInteraction_AssistantDelegate viewConformsToAsynchronousInteractionProtocol];
-[UITextInteraction_AssistantDelegate viewCouldBecomeEditable:];
-[UITextInteraction_AssistantDelegate willBeginSelectionInteraction];
-[UITextInteraction_AssistantDelegate overrideGestureRecognizer:shouldReceiveTouch:];
-[UITextInteraction_AssistantDelegate overrideGestureRecognizerShouldBegin:];
```
