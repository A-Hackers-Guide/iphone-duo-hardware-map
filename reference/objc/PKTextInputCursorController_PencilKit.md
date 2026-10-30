# `PKTextInputCursorController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKTextInputDebugStateReporting`
- 20 instance variables, 18 properties, 63 instance methods, 0 class methods

## Instance variables

```
@"<UITextCursorAssertion>" _nonBlinkingAssertion;
@"<UITextCursorAssertion>" _nonVisibleAssertion;
@"<UITextCursorAssertion>" _ghostAssertion;
B _cursorShouldFlash;
@? _restoreAfterFlashCursorBlock;
B _lastKnownTextInputResponderWasKey;
@"PKTextInputSettings" _settings;
B _isCursorTemporarilyStrong;
B _forceStrong;
B _forceVisible;
B _forceHidden;
B __trackedLastKnownTextInputResponderWindowIsKey;
@"<PKTextInputCursorControllerDelegate>" _delegate;
d _lastElementTapToFocusTimestamp;
q _cursorStyle;
q _mode;
@"UIResponder<UITextInput>" __lastKnownTextInputResponder;
@"UITextCursorAssertionController" _implicitAssertionController;
d __lastSwitchToIdleWritingStateTime;
@"PKTextInputSettings" __textInputSettings;
```

## Properties

```
@property (Tq,N,S_setCursorStyle:,V_cursorStyle) cursorStyle;
@property (Tq,N,S_setMode:,V_mode) mode;
@property (T@"UIResponder<UITextInput>",W,N,S_setLastKnownTextInputResponder:,V__lastKnownTextInputResponder) _lastKnownTextInputResponder;
@property (TB,N,S_setTrackedLastKnownTextInputResponderWindowIsKey:,V__trackedLastKnownTextInputResponderWindowIsKey) _trackedLastKnownTextInputResponderWindowIsKey;
@property (T@"UITextCursorAssertionController",&,N,V_implicitAssertionController) implicitAssertionController;
@property (Td,N,V__lastSwitchToIdleWritingStateTime) _lastSwitchToIdleWritingStateTime;
@property (T@"PKTextInputSettings",&,N,V__textInputSettings) _textInputSettings;
@property (T@"<PKTextInputCursorControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N) isCursorWeak;
@property (TB,R,N,V_isCursorTemporarilyStrong) isCursorTemporarilyStrong;
@property (TB,N,V_forceStrong) forceStrong;
@property (TB,N,V_forceVisible) forceVisible;
@property (TB,N,V_forceHidden) forceHidden;
@property (Td,N,V_lastElementTapToFocusTimestamp) lastElementTapToFocusTimestamp;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKTextInputCursorController resetState];
-[PKTextInputCursorController _setMode:];
-[PKTextInputCursorController init];
-[PKTextInputCursorController setForceHidden:];
-[PKTextInputCursorController setDelegate:];
-[PKTextInputCursorController firstResponderDidChange:];
-[PKTextInputCursorController forceHidden];
-[PKTextInputCursorController scrollViewWillBeginDragging:];
-[PKTextInputCursorController mode];
-[PKTextInputCursorController delegate];
-[PKTextInputCursorController keyboardWillShow:];
-[PKTextInputCursorController keyboardWillChangeFrame:];
-[PKTextInputCursorController initWithSettings:];
-[PKTextInputCursorController setImplicitAssertionController:];
-[PKTextInputCursorController scribbleEnabled];
-[PKTextInputCursorController setForceStrong:];
-[PKTextInputCursorController _currentAssertionController];
-[PKTextInputCursorController _delayedRevokeTemporaryStrongMode];
-[PKTextInputCursorController _handleDidPerformReturn:];
-[PKTextInputCursorController _handleUndoRedo:];
-[PKTextInputCursorController _implicitAssertionControllerIfPossible];
-[PKTextInputCursorController _lastKnownTextInputResponder];
-[PKTextInputCursorController _lastSwitchToIdleWritingStateTime];
-[PKTextInputCursorController _setCursorStyle:];
-[PKTextInputCursorController _setLastKnownTextInputResponder:];
-[PKTextInputCursorController _setTrackedLastKnownTextInputResponderWindowIsKey:];
-[PKTextInputCursorController _textInputSettings];
-[PKTextInputCursorController _textInputSourceDidChange:];
-[PKTextInputCursorController _trackedLastKnownTextInputResponderWindowIsKey];
-[PKTextInputCursorController _updateAssertionsForCurrentState];
-[PKTextInputCursorController _updateCursorStyle];
-[PKTextInputCursorController _windowForResponder:];
-[PKTextInputCursorController _writingStateEvaluationTimerExpired];
-[PKTextInputCursorController canMakeCursorWeakForResponder:];
-[PKTextInputCursorController cursorStyle];
-[PKTextInputCursorController customHighlightFeedbackVisibilityDidChange];
-[PKTextInputCursorController flashCursor];
-[PKTextInputCursorController forceStrong];
-[PKTextInputCursorController forceVisible];
-[PKTextInputCursorController implicitAssertionController];
-[PKTextInputCursorController invalidateGhostAssertion];
-[PKTextInputCursorController invalidateNonBlinkingAssertion];
-[PKTextInputCursorController invalidateNonVisibleAssertion];
-[PKTextInputCursorController isCursorTemporarilyStrong];
-[PKTextInputCursorController isCursorWeak];
-[PKTextInputCursorController keyWindowDidChange:];
-[PKTextInputCursorController lastElementTapToFocusTimestamp];
-[PKTextInputCursorController lastKnownTextInputResponderWindowIsKey];
-[PKTextInputCursorController makeCursorStrong];
-[PKTextInputCursorController makeCursorTemporarilyStrongWhileWriting];
-[PKTextInputCursorController makeCursorTemporarilyStrongWithTimeout:];
-[PKTextInputCursorController makeCursorWeak];
-[PKTextInputCursorController removeAllAssertions];
-[PKTextInputCursorController reportDebugStateDescription:];
-[PKTextInputCursorController resetCursorTemporarilyStrongState];
-[PKTextInputCursorController setForceVisible:];
-[PKTextInputCursorController setLastElementTapToFocusTimestamp:];
-[PKTextInputCursorController set_lastSwitchToIdleWritingStateTime:];
-[PKTextInputCursorController set_textInputSettings:];
-[PKTextInputCursorController simulateFirstResponderChangeForTesting:];
-[PKTextInputCursorController simulateResetCursorTimeout];
-[PKTextInputCursorController textInputSourceDidChange:];
-[PKTextInputCursorController writingStateDidChange];
```
