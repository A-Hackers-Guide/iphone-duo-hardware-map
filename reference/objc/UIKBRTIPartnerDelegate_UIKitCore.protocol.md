# `UIKBRTIPartnerDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `UIKeyboardImplStateProtocol`, `UITextInputSuggestionDelegate`
- 0 instance variables, 4 properties, 119 instance methods, 0 class methods

## Properties

```
@property (T@"UIKeyboardTaskQueue",R,N) taskQueue;
@property (TB,N) performingRemoteTextOperations;
@property (TB,R,N) needAutofillLogin;
@property (TB,N) canSuggestSupplementalItemsForCurrentSelection;
```

## Instance methods

```
-[UIKBRTIPartnerDelegate handleAutoFillCreditCardDetected];
-[UIKBRTIPartnerDelegate startSmartReplyWritingToolWithParams:];
-[UIKBRTIPartnerDelegate asyncWebKitInteractionDelegate];
-[UIKBRTIPartnerDelegate remoteTextEditingMetadata];
-[UIKBRTIPartnerDelegate correctionRect];
-[UIKBRTIPartnerDelegate textDidScroll];
-[UIKBRTIPartnerDelegate showTextChoicesPrompt];
-[UIKBRTIPartnerDelegate canInsertStickerAsTextInputPayload];
-[UIKBRTIPartnerDelegate acceptAutocorrection];
-[UIKBRTIPartnerDelegate handleGrammarCorrectionEntries:];
-[UIKBRTIPartnerDelegate delegateAsResponder];
-[UIKBRTIPartnerDelegate handleAutoFillCreditCardPopoverCommand];
-[UIKBRTIPartnerDelegate inputModeSwitcherVisible];
-[UIKBRTIPartnerDelegate selectionScrolling];
-[UIKBRTIPartnerDelegate updateInputDelegateForRemoteDocumentStateChange:selectedTextRange:hasText:forceSync:];
-[UIKBRTIPartnerDelegate insertSticker:deleteCount:];
-[UIKBRTIPartnerDelegate clearShiftState];
-[UIKBRTIPartnerDelegate removeInlineTextCompletionPrompt];
-[UIKBRTIPartnerDelegate delegateSupportsImagePaste];
-[UIKBRTIPartnerDelegate taskQueue];
-[UIKBRTIPartnerDelegate handleEmojiPopoverKeyCommand];
-[UIKBRTIPartnerDelegate endAcceptingInlineCompletionByDirectTap];
-[UIKBRTIPartnerDelegate handleRemoteIndirectGestureWithState:];
-[UIKBRTIPartnerDelegate setKeyboardInputMode:userInitiated:];
-[UIKBRTIPartnerDelegate setAttributedMarkedText:selectedRange:inputString:searchString:];
-[UIKBRTIPartnerDelegate handleRemoteDictationEvent_setEditMenuFrame:];
-[UIKBRTIPartnerDelegate inputDelegateManager];
-[UIKBRTIPartnerDelegate updateAssistantViewInfo:];
-[UIKBRTIPartnerDelegate handleRemoteDictationEvent_handleTip:];
-[UIKBRTIPartnerDelegate handleRemoteKeyboardCameraEvent_startCameraInput:];
-[UIKBRTIPartnerDelegate setCaretVisible:];
-[UIKBRTIPartnerDelegate handleAutoFillPasswordPopoverCommand];
-[UIKBRTIPartnerDelegate updateDocumentViewsAfterKeyboardOutput:];
-[UIKBRTIPartnerDelegate canInsertEmojiImageTextAttachment];
-[UIKBRTIPartnerDelegate applyAssistantItem:];
-[UIKBRTIPartnerDelegate setPerformingRemoteTextOperations:];
-[UIKBRTIPartnerDelegate setInputModeSwitcherVisibleInRemote:];
-[UIKBRTIPartnerDelegate provideAutoFillTypingUpdatesIfNecessary];
-[UIKBRTIPartnerDelegate textInputTraits];
-[UIKBRTIPartnerDelegate canInsertAdaptiveImageGlyph];
-[UIKBRTIPartnerDelegate replaceRange:oldText:withText:];
-[UIKBRTIPartnerDelegate resetInputDelegate];
-[UIKBRTIPartnerDelegate insertAdaptiveImageGlyph:];
-[UIKBRTIPartnerDelegate asyncInputDelegate];
-[UIKBRTIPartnerDelegate handleRemoteDictationEvent_switchToDictationLanguage:];
-[UIKBRTIPartnerDelegate acceptInlineCompletionWithCompletionHandler:];
-[UIKBRTIPartnerDelegate writingToolsDidEnd];
-[UIKBRTIPartnerDelegate modifyTextInputTraits:forceSync:];
-[UIKBRTIPartnerDelegate insertCustomTextSuggestion:];
-[UIKBRTIPartnerDelegate inputSystemSourceSession];
-[UIKBRTIPartnerDelegate setCanSuggestSupplementalItemsForCurrentSelection:];
-[UIKBRTIPartnerDelegate canSuggestSupplementalItemsForCurrentSelection];
-[UIKBRTIPartnerDelegate delegateConformanceType];
-[UIKBRTIPartnerDelegate performKeyboardOutput:checkingDelegate:forwardToRemoteInputSource:];
-[UIKBRTIPartnerDelegate insertAttributedText:];
-[UIKBRTIPartnerDelegate setRestoresToEmojiInputMode];
-[UIKBRTIPartnerDelegate resumeDictationForResponderChange];
-[UIKBRTIPartnerDelegate inputDelegate];
-[UIKBRTIPartnerDelegate setRemoteDelegateSupportsAdaptiveImageGlyph:];
-[UIKBRTIPartnerDelegate handleRemoteDictationEvent_startDictation];
-[UIKBRTIPartnerDelegate textWillScroll];
-[UIKBRTIPartnerDelegate _updateCanSuggestSupplementalItemsForCurrentSelection];
-[UIKBRTIPartnerDelegate textContentTypeForCurrentInputDelegate];
-[UIKBRTIPartnerDelegate setInputMode:userInitiated:];
-[UIKBRTIPartnerDelegate setCandidateDisplayIsExtended:];
-[UIKBRTIPartnerDelegate setRemoteDelegateSupportsImagePaste:];
-[UIKBRTIPartnerDelegate acceptAutocorrectionWithCompletionHandler:];
-[UIKBRTIPartnerDelegate acceptAutocorrectionWithCompletionHandler:requestedByRemoteInputDestination:];
-[UIKBRTIPartnerDelegate beginAcceptingInlineCompletionByDirectTap];
-[UIKBRTIPartnerDelegate performKeyboardOutput:userInfo:];
-[UIKBRTIPartnerDelegate performingRemoteTextOperations];
-[UIKBRTIPartnerDelegate textDidChange:];
-[UIKBRTIPartnerDelegate updateDelegatePasteSupportIfNeeded];
-[UIKBRTIPartnerDelegate updateInputDelegateForRemoteTraitChange:forceSync:];
-[UIKBRTIPartnerDelegate handleRemoteDictationEvent_movePopoverView:];
-[UIKBRTIPartnerDelegate performOperations:withTextInputSource:];
-[UIKBRTIPartnerDelegate updateForExpectedRemoteDocumentStateChange:selectedTextRange:forceSync:];
-[UIKBRTIPartnerDelegate presentKeyboardFeedbackAssistantViewControllerForLogURL:];
-[UIKBRTIPartnerDelegate handleEventFromRemoteSource_autoFillIsMenuPresented:];
-[UIKBRTIPartnerDelegate performStopAutoDeleteAtDocumentStart];
-[UIKBRTIPartnerDelegate _handleWebKeyEvent:withEventType:withInputString:withInputStringIgnoringModifiers:];
-[UIKBRTIPartnerDelegate handleAutoFillContactPopoverCommand];
-[UIKBRTIPartnerDelegate returnKeyEnabled];
-[UIKBRTIPartnerDelegate assertTextForRemoteDocument:withSelectionDelta:updatingSelection:];
-[UIKBRTIPartnerDelegate insertEmojiImageTextAttachment:];
-[UIKBRTIPartnerDelegate changingContextWithTrigger:];
-[UIKBRTIPartnerDelegate handleEventFromRemoteSource_insertionPointExitedTextWithSupplementalItems];
-[UIKBRTIPartnerDelegate ejectKeyDown];
-[UIKBRTIPartnerDelegate handleRemoteDictationEvent_updateIdleDetection:];
-[UIKBRTIPartnerDelegate setShiftStatesNeededInDestination:autoShifted:shiftLocked:];
-[UIKBRTIPartnerDelegate presentEmojiGenerationWithInputString:];
-[UIKBRTIPartnerDelegate handleRemoteDictationEvent_stopDictation:];
-[UIKBRTIPartnerDelegate handleRemoteDictationEvent_resumeDictation];
-[UIKBRTIPartnerDelegate handleRemoteDictationEvent_stopDictationIgnoreFinalizePhrases];
-[UIKBRTIPartnerDelegate handleAutoFillPasswordDetected];
-[UIKBRTIPartnerDelegate handleEventFromRemoteSource_insertionPointEnteredText:withSupplementalCandidate:];
-[UIKBRTIPartnerDelegate handleAutoFillContactDetected];
-[UIKBRTIPartnerDelegate textWillChange:];
-[UIKBRTIPartnerDelegate undoWithKeyboardInput:];
-[UIKBRTIPartnerDelegate delegate];
-[UIKBRTIPartnerDelegate handleEventFromRemoteSource_chooseSupplementalItem:toReplaceText:];
-[UIKBRTIPartnerDelegate performKeyboardEvent:];
-[UIKBRTIPartnerDelegate handleEventFromRemoteSource_insertAutofillContent:];
-[UIKBRTIPartnerDelegate handleEventFromRemoteDestination_canSuggestSupplementalItemsForCurrentSelection:];
-[UIKBRTIPartnerDelegate setInlineCompletionAsMarkedText:selectedRange:inputString:searchString:];
-[UIKBRTIPartnerDelegate assertIntermediateText:];
-[UIKBRTIPartnerDelegate needAutofillLogin];
-[UIKBRTIPartnerDelegate performTextOperationActionSelector:];
-[UIKBRTIPartnerDelegate handleRemoteDictationEvent_setDisambiguationActive:maxOptions:];
-[UIKBRTIPartnerDelegate handleRemoteDictationEvent_switchToDictationInputModeWithOptions:];
-[UIKBRTIPartnerDelegate handleAutoDeleteContinuationOnDestinationWithDeletionCount:];
-[UIKBRTIPartnerDelegate insertSticker:];
-[UIKBRTIPartnerDelegate handleEventFromRemoteSource_cancelChooseSupplementalItemToInsert];
-[UIKBRTIPartnerDelegate handleEventCallbackFromRemoteDestination_didChooseSupplementalItem:toReplaceText:];
-[UIKBRTIPartnerDelegate dismissTextChoicePrompt];
-[UIKBRTIPartnerDelegate acceptingCandidateWithTrigger:];
-[UIKBRTIPartnerDelegate handleRemoteDictationEvent_cancelDictation];
-[UIKBRTIPartnerDelegate handleEventFromRemoteSource_insertSupplementalCandidate:textToCommit:];
-[UIKBRTIPartnerDelegate presentTextChoicePromptForRange:];
```
