# `UITextSelectionInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextInteraction`
- 12 instance variables, 0 properties, 38 instance methods, 0 class methods

## Instance variables

```
d _lastTapTimestamp;
{CGPoint="x"d"y"d} _lastTapLocation;
@"UITextGestureTuning" _gestureTuning;
B _indirectSelectionType;
B _viewConformsToTextInput;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _originalCaretRect;
B _wasOriginallyFirstResponder;
q _granularityToHandOff;
B _isCharacterGranularityOnMarkedTextPresenceEnabled;
@"UITextLoupeSession" _activeLoupeSession;
@"_UIKeyboardTextSelectionController" _activeSelectionController;
@"<_UIInvalidatable>" _grabberSuppressionAssertion;
```

## Instance methods

```
-[UITextSelectionInteraction finishSetup];
-[UITextSelectionInteraction twoFingerRangedSelectGesture:];
-[UITextSelectionInteraction shouldHandleOneFingerTapInUneditable:];
-[UITextSelectionInteraction oneFingerTapSelectsAll:];
-[UITextSelectionInteraction initWithMode:];
-[UITextSelectionInteraction _isShiftKeyBeingHeldForGesture:];
-[UITextSelectionInteraction _hasMarkedTextAtLocation:];
-[UITextSelectionInteraction _updateTapGestureHistoryWithLocation:];
-[UITextSelectionInteraction _textGranularityForNumberOfTaps:];
-[UITextSelectionInteraction _createGestureTuningIfNecessary];
-[UITextSelectionInteraction _shouldAllowEnforcedTouchTypeForTouch:forGestureRecognizer:];
-[UITextSelectionInteraction _isNowWithinRepeatedTapTime];
-[UITextSelectionInteraction tappedToSelectTextWithGesture:atPoint:granularity:completionHandler:];
-[UITextSelectionInteraction _usesPencilSelectionBehaviorForGesture:];
-[UITextSelectionInteraction willUpdateSelectionWithGesture:];
-[UITextSelectionInteraction _usesIndirectSelectionBehavior];
-[UITextSelectionInteraction confirmMarkedText:];
-[UITextSelectionInteraction tappedToPositionCursorWithGesture:atPoint:granularity:completionHandler:];
-[UITextSelectionInteraction gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[UITextSelectionInteraction handOffGranularity];
-[UITextSelectionInteraction interaction_gestureRecognizer:shouldReceiveTouch:];
-[UITextSelectionInteraction gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[UITextSelectionInteraction tappedToUpdateSelectionWithGesture:atPoint:granularity:completionHandler:];
-[UITextSelectionInteraction toggleSelectionCommands];
-[UITextSelectionInteraction initWithMode:indirect:];
-[UITextSelectionInteraction _checkForRepeatedTap:gestureLocationOut:];
-[UITextSelectionInteraction setHybridSelectionWithPoint:];
-[UITextSelectionInteraction _showSelectionCommandsIfApplicableAfterDelay:];
-[UITextSelectionInteraction _applyTransientState:];
-[UITextSelectionInteraction tapAndAHalf:];
-[UITextSelectionInteraction _isWithinRepeatedTapTimeForTouch:];
-[UITextSelectionInteraction didMoveToView:];
-[UITextSelectionInteraction _handleMultiTapGesture:];
-[UITextSelectionInteraction _transientState];
-[UITextSelectionInteraction _hasTextAlternativesAtLocation:];
-[UITextSelectionInteraction _isRepeatedTap:gestureLocationOut:];
-[UITextSelectionInteraction didUpdateSelectionWithGesture:];
-[UITextSelectionInteraction interaction_gestureRecognizerShouldBegin:];
```
