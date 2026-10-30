# `UIKBRTIPartner`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `RTIInputSystemClientDelegate`, `RTIInputSystemSessionDelegate`, `_UIGeometryChangeObserver`
- 30 instance variables, 24 properties, 167 instance methods, 1 class methods

## Instance variables

```
@"RTIDocumentTraits" _remoteDocumentTraits;
@"NSNumber" _cachedHasPreviousKeyResponder;
@"NSNumber" _cachedHasNextKeyResponder;
^{__CFStringTokenizer=} _wkRectTokenizer;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"UIKeyboardTaskExecutionContext" _waitingRTIOutputOperationResponseContext;
@"UIKeyboardTaskSubqueue" _keyboardTaskSubqueue;
@"NSDictionary" _pendingDisableBecomeFirstResponderParameters;
B _dontTakeKeyboardSnapshot;
B _applicationDeactivationReasonAssistant;
q _id;
B _inputSystemClientEnabled;
B _isNotifyingDelegateOfRemoteOutputOperation;
B _applicationStateIsActiveForRTI;
B _viewServiceStateIsActiveForRTI;
B _isObservingGeometry;
@"<UIKBRTIPartnerDelegate>" _partnerDelegate;
@"RTIInputSystemClient" _rtiClient;
@"RTIDocumentTraits" _rtiDocumentTraits;
@"RTIDocumentState" _rtiDocumentState;
@"UITextRange" _extentRangeForDocumentState;
@"RTIInputSourceState" _rtiInputSourceState;
@"TIKeyboardOutput" _pendingOutputOperation;
@"NSUUID" _currentSessionIdentifier;
@"NSMutableDictionary" _rtiSessionMarkers;
@"NSMutableDictionary" _supplementalLexicons;
@"NSMutableDictionary" _textSuggestions;
@"NSMutableArray" _queuedSupplementalLexiconOperations;
@"NSUUID" _authenticatingSessionIdentifier;
@? _textOperationsFilter;
```

## Properties

```
@property (T@"NSUUID",C,N,V_currentSessionIdentifier) currentSessionIdentifier;
@property (TB,N,V_isObservingGeometry) isObservingGeometry;
@property (T@"NSMutableDictionary",&,N,V_rtiSessionMarkers) rtiSessionMarkers;
@property (T@"NSMutableDictionary",&,N,V_supplementalLexicons) supplementalLexicons;
@property (T@"NSMutableDictionary",&,N,V_textSuggestions) textSuggestions;
@property (T@"NSMutableArray",&,N,V_queuedSupplementalLexiconOperations) queuedSupplementalLexiconOperations;
@property (T@"UIKeyboardTaskSubqueue",&,N) keyboardTaskSubqueue;
@property (T@"NSUUID",C,N,V_authenticatingSessionIdentifier) authenticatingSessionIdentifier;
@property (T@?,C,N,V_textOperationsFilter) textOperationsFilter;
@property (T@"<UIKBRTIPartnerDelegate>",W,N,V_partnerDelegate) partnerDelegate;
@property (TB,N,V_inputSystemClientEnabled) inputSystemClientEnabled;
@property (TB,R,N,V_isNotifyingDelegateOfRemoteOutputOperation) isNotifyingDelegateOfRemoteOutputOperation;
@property (T@"RTIInputSystemClient",&,N,V_rtiClient) rtiClient;
@property (T@"RTIDocumentTraits",&,N,V_rtiDocumentTraits) rtiDocumentTraits;
@property (T@"RTIDocumentState",&,N,V_rtiDocumentState) rtiDocumentState;
@property (T@"UITextRange",&,N,V_extentRangeForDocumentState) extentRangeForDocumentState;
@property (T@"RTIInputSourceState",R,N,V_rtiInputSourceState) rtiInputSourceState;
@property (TB,N,V_applicationStateIsActiveForRTI) applicationStateIsActiveForRTI;
@property (TB,N,V_viewServiceStateIsActiveForRTI) viewServiceStateIsActiveForRTI;
@property (T@"TIKeyboardOutput",&,N,V_pendingOutputOperation) pendingOutputOperation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKBRTIPartner registerTextOperationCustomInfo];
```

## Instance methods

```
-[UIKBRTIPartner applyAssistantItem:];
-[UIKBRTIPartner forwardKeyboardCameraEvent_startCameraInput:];
-[UIKBRTIPartner textSuggestions];
-[UIKBRTIPartner _screenModeDidChange:];
-[UIKBRTIPartner extentRangeForDocumentState];
-[UIKBRTIPartner _createRTIClientIfNecessary];
-[UIKBRTIPartner _remoteInputSystemRequiresTextSuggestionUpdates];
-[UIKBRTIPartner _newInputSystemAutoFillUIClient];
-[UIKBRTIPartner _queueSupplementalLexiconOperation:lexicon:];
-[UIKBRTIPartner synchronousForwardKeyInputMethodCommandEventToUIHost:canHandleAppKeyCommand:];
-[UIKBRTIPartner inputSession:textSuggestionsChanged:];
-[UIKBRTIPartner connectionInterrupted:];
-[UIKBRTIPartner _updateRTIAllowedAndNotify:withReason:];
-[UIKBRTIPartner insertionPointColor];
-[UIKBRTIPartner convertRect:from:];
-[UIKBRTIPartner remoteTextInputClientHasActiveSession];
-[UIKBRTIPartner forwardKeyboardEventToUIHost:];
-[UIKBRTIPartner _createRTIClient];
-[UIKBRTIPartner inputDelegate];
-[UIKBRTIPartner _didRemoveSupplementalLexiconWithIdentifier:];
-[UIKBRTIPartner queuedSupplementalLexiconOperations];
-[UIKBRTIPartner _updateGeometryObserverIfNecessary];
-[UIKBRTIPartner _remoteInputSystemRequiresDocumentStateForAutofill];
-[UIKBRTIPartner _uiTextGranularityForRTITextGranularity:];
-[UIKBRTIPartner rtiDocumentState];
-[UIKBRTIPartner textSuggestionsChanged:];
-[UIKBRTIPartner forwardGrammarCorrectionEntries:];
-[UIKBRTIPartner finishCompletionHandlersIfNeeded];
-[UIKBRTIPartner rtiClient];
-[UIKBRTIPartner setPartnerDelegate:];
-[UIKBRTIPartner forwardKeyboardOperation:object:];
-[UIKBRTIPartner forwardEventCallbackToRemoteSource_didChooseSupplementalItem:toReplaceText:];
-[UIKBRTIPartner documentTextInRange:forInputDelegate:];
-[UIKBRTIPartner setIsObservingGeometry:];
-[UIKBRTIPartner inputSession:didAddRTISupplementalLexicon:];
-[UIKBRTIPartner textOperation_insertSupplementalCandidate:textToCommit:];
-[UIKBRTIPartner init];
-[UIKBRTIPartner exchangeWaitingRTIOutputOperationResponseContext:];
-[UIKBRTIPartner applyRemoteDocumentTraitsIfNecessary:force:];
-[UIKBRTIPartner forwardInputDestinationEventToUIHost:];
-[UIKBRTIPartner setExtentRangeForDocumentState:];
-[UIKBRTIPartner endInputSessionWithIdentifier:shouldResign:];
-[UIKBRTIPartner connectionInvalidated:];
-[UIKBRTIPartner pendingOutputOperation];
-[UIKBRTIPartner setKeyboardTaskSubqueue:];
-[UIKBRTIPartner setRtiDocumentTraits:];
-[UIKBRTIPartner forwardKeyboardSuppression:suppressAssistantBar:];
-[UIKBRTIPartner synchronousForwardKeyCommandsToUIHost:];
-[UIKBRTIPartner endInputSessionWithIdentifier:shouldResign:waitForReply:];
-[UIKBRTIPartner dealloc];
-[UIKBRTIPartner _tryKeyCommand:];
-[UIKBRTIPartner _defaultRTIMachNames];
-[UIKBRTIPartner _canHandleResponderCommand:sender:target:];
-[UIKBRTIPartner performInputOperation:];
-[UIKBRTIPartner _relativeReplacementRangeForAnnotationOperation:];
-[UIKBRTIPartner isObservingGeometry];
-[UIKBRTIPartner textOperation_cancelChooseSupplementalItemToInsert];
-[UIKBRTIPartner _ignoredReasonsForKeyboard];
-[UIKBRTIPartner setViewServiceStateIsActiveForRTI:];
-[UIKBRTIPartner _viewServiceHostWillResignActive:];
-[UIKBRTIPartner inputSession:didRemoveRTISupplementalLexicon:];
-[UIKBRTIPartner setAuthenticatingSessionIdentifier:];
-[UIKBRTIPartner inputDelegateView];
-[UIKBRTIPartner _addTextCheckingAnnotatedStringToDocumentState:];
-[UIKBRTIPartner defaultDocumentRequestDidChange:];
-[UIKBRTIPartner setRtiSessionMarkers:];
-[UIKBRTIPartner forwardApplicationOperation:object:];
-[UIKBRTIPartner _geometryChanged:forAncestor:];
-[UIKBRTIPartner setRtiDocumentState:];
-[UIKBRTIPartner documentTraitsChanged];
-[UIKBRTIPartner _queryUIKitDocumentRequest:completion:];
-[UIKBRTIPartner _newInputSystemUIClient];
-[UIKBRTIPartner _queryWKDocumentRequest:completion:];
-[UIKBRTIPartner _addAutocorrectStylingToDocumentState:];
-[UIKBRTIPartner ensureRTIConnection];
-[UIKBRTIPartner forwardSelectorToUIHost:completionHandler:];
-[UIKBRTIPartner forwardTypologyLogURL:];
-[UIKBRTIPartner _getWKDocumentContextSynchronously:];
-[UIKBRTIPartner _queued_performTextOperations:resultHandler:];
-[UIKBRTIPartner invalidate];
-[UIKBRTIPartner _performKeyboardOutputOperations:];
-[UIKBRTIPartner endInputSessionWithIdentifier:];
-[UIKBRTIPartner didRemoveSupplementalLexicon:];
-[UIKBRTIPartner setInputSystemClientEnabled:];
-[UIKBRTIPartner forwardEventToRemoteSource_canSuggestSupplementalItemsForCurrentSelection:];
-[UIKBRTIPartner _ignoredReasonsForAutoFill];
-[UIKBRTIPartner _applicationWillAddDeactivationReason:];
-[UIKBRTIPartner inputSession:documentStateDidChange:withMergeResult:];
-[UIKBRTIPartner setCurrentSessionIdentifier:];
-[UIKBRTIPartner _performQueuedSupplementalLexiconOperations];
-[UIKBRTIPartner keyboardTaskSubqueue];
-[UIKBRTIPartner _didAddSupplementalLexicon:];
-[UIKBRTIPartner forwardInputDestinationEventToUIHost:params:];
-[UIKBRTIPartner inputSession:documentStateDidChange:];
-[UIKBRTIPartner textOperation_chooseSupplementalItem:toReplaceText:];
-[UIKBRTIPartner forwardClearForwardingInputDelegateAndResign:];
-[UIKBRTIPartner setTextOperationsFilter:];
-[UIKBRTIPartner viewServiceStateIsActiveForRTI];
-[UIKBRTIPartner hasActiveRTIOnenessSession];
-[UIKBRTIPartner _remoteInputSystemRequiresDocumentStateUpdates];
-[UIKBRTIPartner textOperationsFilter];
-[UIKBRTIPartner setSupplementalLexicons:];
-[UIKBRTIPartner setRtiClient:];
-[UIKBRTIPartner _applicationWillSuspend:];
-[UIKBRTIPartner performTextOperations:resultHandler:];
-[UIKBRTIPartner beginAllowingRemoteTextInput:];
-[UIKBRTIPartner performTextOperations:];
-[UIKBRTIPartner setPendingOutputOperation:];
-[UIKBRTIPartner forwardScrollEventToUIHost:contentTransform:environmentTransform:];
-[UIKBRTIPartner delegate];
-[UIKBRTIPartner inputSession:performInputOperation:withResponse:];
-[UIKBRTIPartner restartCurrentSession];
-[UIKBRTIPartner setQueuedSupplementalLexiconOperations:];
-[UIKBRTIPartner _applicationDidRemoveDeactivationReason:];
-[UIKBRTIPartner documentStateChanged:];
-[UIKBRTIPartner compareWaitingRTIOutputOperationResponseContext:andExchange:];
-[UIKBRTIPartner documentStateChanged];
-[UIKBRTIPartner inputSystemClientEnabled];
-[UIKBRTIPartner autofillPayloadDelegate];
-[UIKBRTIPartner inputSession:documentTraitsDidChange:];
-[UIKBRTIPartner removeTextSuggestionsForSessionWithID:];
-[UIKBRTIPartner supplementalLexicons];
-[UIKBRTIPartner payloadDelegate];
-[UIKBRTIPartner _performTextCheckingAnnotationOperations:];
-[UIKBRTIPartner currentSessionIdentifier];
-[UIKBRTIPartner sendAutoFillDidInsertCallbacksWithTextOperations:];
-[UIKBRTIPartner didAddSupplementalLexicon:];
-[UIKBRTIPartner inputSession:performInputOperation:];
-[UIKBRTIPartner updateTextSuggestionsIfNecessary:];
-[UIKBRTIPartner setTextSuggestions:];
-[UIKBRTIPartner _didCreateRTIClient:];
-[UIKBRTIPartner _selectionClipRect];
-[UIKBRTIPartner endAllowingRemoteTextInput:];
-[UIKBRTIPartner _queryDocumentRequest:completion:];
-[UIKBRTIPartner _addFirstSelectionRectToDocumentState:];
-[UIKBRTIPartner endAllowingRemoteTextInput:waitForReply:];
-[UIKBRTIPartner _tryKeyCommandWithSelector:];
-[UIKBRTIPartner _addCharacterRectsToDocumentState:textRange:offset:];
-[UIKBRTIPartner applicationStateIsActiveForRTI];
-[UIKBRTIPartner forwardAutofillPayload:toPayloadDelegate:];
-[UIKBRTIPartner beginInputSessionWithIdentifier:];
-[UIKBRTIPartner updateAnimationForOptions:];
-[UIKBRTIPartner rtiDocumentTraits];
-[UIKBRTIPartner _newRTIConnection];
-[UIKBRTIPartner documentTraitsDisableAutomaticKeyboardUI];
-[UIKBRTIPartner endInputSessionOnSwitchingApps];
-[UIKBRTIPartner textOperation_insertionPointEnteredText:withSupplementalCandidate:];
-[UIKBRTIPartner _updateRTITraitsIfNecessary];
-[UIKBRTIPartner textOperation_insertAutofillContent:];
-[UIKBRTIPartner _viewServiceHostDidBecomeActive:];
-[UIKBRTIPartner _addMergedTextRectsToDocumentState:forWKContext:textInputView:granularity:];
-[UIKBRTIPartner authenticatingSessionIdentifier];
-[UIKBRTIPartner forwardKeyboardInputMode:];
-[UIKBRTIPartner synchronousForwardKeyCommandsBeforePublicToUIHost:];
-[UIKBRTIPartner forwardDictationEventToUIHost:withOptionalObject:];
-[UIKBRTIPartner applyRemoteDocumentStateIfNecessary:force:];
-[UIKBRTIPartner rtiInputSourceState];
-[UIKBRTIPartner _updateRTIStateWithCompletion:];
-[UIKBRTIPartner _performDocumentRequest:completion:];
-[UIKBRTIPartner textOperation_insertionPointExitedTextWithSupplementalItems];
-[UIKBRTIPartner updateStateWithCompletion:updateTraits:];
-[UIKBRTIPartner addTextSuggestions:];
-[UIKBRTIPartner rtiSessionMarkers];
-[UIKBRTIPartner performDocumentRequest:completion:];
-[UIKBRTIPartner isNotifyingDelegateOfRemoteOutputOperation];
-[UIKBRTIPartner partnerDelegate];
-[UIKBRTIPartner setApplicationStateIsActiveForRTI:];
```
