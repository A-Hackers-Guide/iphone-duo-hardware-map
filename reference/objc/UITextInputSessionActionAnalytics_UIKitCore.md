# `UITextInputSessionActionAnalytics`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 22 instance variables, 5 properties, 103 instance methods, 14 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableOrderedSet" _recentActions;
@"NSMutableSet" _accumulators;
@"NSMutableSet" _efficacyAccumulators;
@"NSMutableSet" _dynamicAccumulators;
@"NSSet" _separateCycleAccumulatorNames;
Q _maxDepth;
B _trackingDuration;
Q _beginTimestamp;
q _overrideSource;
q _useOverrideSourceCounter;
@"NSString" _overrideInputModeString;
@"NSString" _overrideKeyboardTypeString;
@"NSMutableDictionary" _keystrokeLatenciesMsByInputType;
Q _keystrokeLatencySampleCount;
@"NSString" _keystrokeInputModeString;
@"NSString" _keystrokeKeyboardTypeString;
@"<UITextInputSessionActionAnalyticsDelegateSource>" _delegateSource;
@"NSUUID" _sessionIdentifier;
@"NSDictionary" _keyboardTrialParameters;
@"IATextInputActionsInputMode" _inputMode;
Q _allowCursorMovementCounter;
```

## Properties

```
@property (T@"<UITextInputSessionActionAnalyticsDelegateSource>",W,N,V_delegateSource) delegateSource;
@property (T@"NSUUID",&,N,V_sessionIdentifier) sessionIdentifier;
@property (T@"NSDictionary",C,N,V_keyboardTrialParameters) keyboardTrialParameters;
@property (T@"IATextInputActionsInputMode",&,N,V_inputMode) inputMode;
@property (TQ,R,N,V_allowCursorMovementCounter) allowCursorMovementCounter;
```

## Class methods

```
+[UITextInputSessionActionAnalytics addEndingObserver:];
+[UITextInputSessionActionAnalytics allowedValuesForTextInputSource];
+[UITextInputSessionActionAnalytics stringForKeyboardDockItemButtonPressResult:];
+[UITextInputSessionActionAnalytics removeObserver:];
+[UITextInputSessionActionAnalytics q_notifyEndingObserversWithSessionAnalytics:];
+[UITextInputSessionActionAnalytics stringForReplaceWithCandidateType:];
+[UITextInputSessionActionAnalytics sharedPunctuationCharacterSet];
+[UITextInputSessionActionAnalytics populateActionInputMode:withLanguage:];
+[UITextInputSessionActionAnalytics addObserver:];
+[UITextInputSessionActionAnalytics populateActionInputMode:];
+[UITextInputSessionActionAnalytics removeEndingObserver:];
+[UITextInputSessionActionAnalytics stringForKeyboardDockItemButtonType:];
+[UITextInputSessionActionAnalytics stringValueForSource:];
+[UITextInputSessionActionAnalytics q_notifyStartingObservers];
```

## Instance methods

```
-[UITextInputSessionActionAnalytics didUndo];
-[UITextInputSessionActionAnalytics appBundleId];
-[UITextInputSessionActionAnalytics setInputMode:];
-[UITextInputSessionActionAnalytics sessionIdentifier];
-[UITextInputSessionActionAnalytics didKBMenuDismiss:];
-[UITextInputSessionActionAnalytics didKBMenuAppear:originalInputMode:];
-[UITextInputSessionActionAnalytics didInlineCompletionTapOnCompletionReplacementForText:withText:];
-[UITextInputSessionActionAnalytics didAutocorrectTapOnCompletionReplacementForText:withText:];
-[UITextInputSessionActionAnalytics didRedo];
-[UITextInputSessionActionAnalytics setKeyboardTrialParameters:];
-[UITextInputSessionActionAnalytics didCalloutBarReplacementForText:withText:];
-[UITextInputSessionActionAnalytics _didDeleteBackwardAction:];
-[UITextInputSessionActionAnalytics inputMode];
-[UITextInputSessionActionAnalytics inputMode];
-[UITextInputSessionActionAnalytics init];
-[UITextInputSessionActionAnalytics didInsertText:relativeRangeBefore:selectedTextBefore:withLanguage:];
-[UITextInputSessionActionAnalytics didDictationEnd];
-[UITextInputSessionActionAnalytics didAutocorrectReplacementForText:withText:];
-[UITextInputSessionActionAnalytics keyboardTrialParameters];
-[UITextInputSessionActionAnalytics keyboardTrialParameters];
-[UITextInputSessionActionAnalytics didInlineCompletionReplacementForText:withText:];
-[UITextInputSessionActionAnalytics didReplaceWithCandidate:];
-[UITextInputSessionActionAnalytics setSessionIdentifier:];
-[UITextInputSessionActionAnalytics didCompositionReplacementForText:withText:];
-[UITextInputSessionActionAnalytics didSessionEnd];
-[UITextInputSessionActionAnalytics incrementAllowCursorMovementCount];
-[UITextInputSessionActionAnalytics didDictationBegin:usesMultiModalDictation:];
-[UITextInputSessionActionAnalytics enumerateAnalytics:];
-[UITextInputSessionActionAnalytics didDecompositionReplacementForText:withText:];
-[UITextInputSessionActionAnalytics didRevisionBubbleReplacementForText:withText:];
-[UITextInputSessionActionAnalytics didGlomojiTap:originalInputMode:newInputMode:];
-[UITextInputSessionActionAnalytics didOther];
-[UITextInputSessionActionAnalytics decrementAllowCursorMovementCount];
-[UITextInputSessionActionAnalytics didCandidateBarReplacementForText:withText:];
-[UITextInputSessionActionAnalytics didRevisionBubbleTap];
-[UITextInputSessionActionAnalytics didCandidateBarAction];
-[UITextInputSessionActionAnalytics _instanceOfActionClass:];
-[UITextInputSessionActionAnalytics didChangeToSelection:relativeRangeBefore:];
-[UITextInputSessionActionAnalytics didKBMenuInteraction:selectedAction:newInputMode:];
-[UITextInputSessionActionAnalytics didDeleteBackwardText:];
-[UITextInputSessionActionAnalytics source];
-[UITextInputSessionActionAnalytics didBegin];
-[UITextInputSessionActionAnalytics didCopy];
-[UITextInputSessionActionAnalytics getEfficacyAccumulatorWithName:];
-[UITextInputSessionActionAnalytics processBundleId];
-[UITextInputSessionActionAnalytics addAccumulator:];
-[UITextInputSessionActionAnalytics didCommitTextFromUnknownSource:];
-[UITextInputSessionActionAnalytics _didCommitText:withSource:];
-[UITextInputSessionActionAnalytics _didDeleteBackwardCount:shouldOverrideInputActionCountToZero:withLanguage:];
-[UITextInputSessionActionAnalytics _didDeleteBackwardText:shouldOverrideInputActionCountToZero:withLanguage:];
-[UITextInputSessionActionAnalytics _didInsertTextAction:numCharsDeleted:withLanguage:];
-[UITextInputSessionActionAnalytics _emojiCountForText:];
-[UITextInputSessionActionAnalytics _getActiveTextInputSource];
-[UITextInputSessionActionAnalytics _normalizedTextLength:];
-[UITextInputSessionActionAnalytics _optionsForText:];
-[UITextInputSessionActionAnalytics _performWithInputModeOverride:block:];
-[UITextInputSessionActionAnalytics _performWithInputModeOverride:keyboardType:block:];
-[UITextInputSessionActionAnalytics _performWithTextInputActionsSource:block:];
-[UITextInputSessionActionAnalytics _punctuationCountForText:];
-[UITextInputSessionActionAnalytics _reportKeyboardLatencyIfKeyboardChanged];
-[UITextInputSessionActionAnalytics _textInputActionsAnalyticsForTesting];
-[UITextInputSessionActionAnalytics _textInsertionActionForText:relativeRangeBefore:withLanguage:];
-[UITextInputSessionActionAnalytics addDynamicAccumulator:];
-[UITextInputSessionActionAnalytics addEfficacyAccumulator:];
-[UITextInputSessionActionAnalytics allAccumulatorNames];
-[UITextInputSessionActionAnalytics allEfficacyAccumulatorNames];
-[UITextInputSessionActionAnalytics allowCursorMovementCounter];
-[UITextInputSessionActionAnalytics beginTrackingSessionDurationIfNecessary];
-[UITextInputSessionActionAnalytics delegateSource];
-[UITextInputSessionActionAnalytics didCommitTextFromCandidateBar:];
-[UITextInputSessionActionAnalytics didCommitTextFromImplicitAction:];
-[UITextInputSessionActionAnalytics didCommitTextFromKeyboard:];
-[UITextInputSessionActionAnalytics didCut];
-[UITextInputSessionActionAnalytics didDeleteBackwardCount:];
-[UITextInputSessionActionAnalytics didDeleteKeyPressWithInputSource:];
-[UITextInputSessionActionAnalytics didInsertKeyPressWithInputSource:];
-[UITextInputSessionActionAnalytics didInsertText:relativeRangeBefore:];
-[UITextInputSessionActionAnalytics didInsertText:relativeRangeBefore:withLanguage:];
-[UITextInputSessionActionAnalytics didInsertText:relativeRangeBefore:withNumAlternatives:];
-[UITextInputSessionActionAnalytics didKeyPress:inputSource:];
-[UITextInputSessionActionAnalytics didKeyboardDockItemButtonPress:buttonType:buttonSize:touchDown:touchUp:touchDuration:inputSource:];
-[UITextInputSessionActionAnalytics didMeasureKeystrokeLatency:ofInputType:];
-[UITextInputSessionActionAnalytics didOnWebSearchKeyboardPressKey:withMetadata:];
-[UITextInputSessionActionAnalytics didPaste];
-[UITextInputSessionActionAnalytics didReplacementForText:withText:withSource:withType:withInputActionCount:];
-[UITextInputSessionActionAnalytics enumerateSeparateCycleAnalytics:];
-[UITextInputSessionActionAnalytics enumerateTextInputActionAnalytics:];
-[UITextInputSessionActionAnalytics flagOptions];
-[UITextInputSessionActionAnalytics getAppBundleId];
-[UITextInputSessionActionAnalytics getDynamicAccumulatorWithName:];
-[UITextInputSessionActionAnalytics initWithEventHandler:];
-[UITextInputSessionActionAnalytics q_addAccumulator:];
-[UITextInputSessionActionAnalytics q_addActionAndUpdate:];
-[UITextInputSessionActionAnalytics q_addDynamicAccumulator:];
-[UITextInputSessionActionAnalytics q_addEfficacyAccumulator:];
-[UITextInputSessionActionAnalytics q_copyAccumulatorWithName:];
-[UITextInputSessionActionAnalytics q_flushRecentActions];
-[UITextInputSessionActionAnalytics q_setSeparateCycleAccumulatorNames:];
-[UITextInputSessionActionAnalytics q_setupDefaultAnalytics];
-[UITextInputSessionActionAnalytics q_updateAnalyticsFromAccumulators];
-[UITextInputSessionActionAnalytics reportKeyboardLatencyAndClearSamples];
-[UITextInputSessionActionAnalytics setDelegateSource:];
-[UITextInputSessionActionAnalytics writeAnalytics];
```
