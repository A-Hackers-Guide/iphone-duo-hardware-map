# `_UISmartReplyFeedbackManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 49 instance methods, 8 class methods

## Instance variables

```
B _isLongFormCandidate;
B _isPollAction;
Q _state;
@"_UIKeyboardStateManager" _keyboardStateManagerDelegate;
@"NSString" _analyticsSessionId;
@"NSArray" _previouslyShownCandidates;
@"NSString" _selectedCandidateDescription;
@"NSDate" _reportFeedbackUIPresentedCalledTime;
d _predictionBarDebounceTimeInterval;
@"NSTimer" _predictionBarDebounceTimeIntervalTimer;
```

## Properties

```
@property (T@"NSString",&,N,V_analyticsSessionId) analyticsSessionId;
@property (T@"NSArray",&,N,V_previouslyShownCandidates) previouslyShownCandidates;
@property (T@"NSString",C,N,V_selectedCandidateDescription) selectedCandidateDescription;
@property (T@"NSDate",&,N,V_reportFeedbackUIPresentedCalledTime) reportFeedbackUIPresentedCalledTime;
@property (Td,N,V_predictionBarDebounceTimeInterval) predictionBarDebounceTimeInterval;
@property (T@"NSTimer",&,N,V_predictionBarDebounceTimeIntervalTimer) predictionBarDebounceTimeIntervalTimer;
@property (TQ,R,N,V_state) state;
@property (T@"_UIKeyboardStateManager",W,N,V_keyboardStateManagerDelegate) keyboardStateManagerDelegate;
@property (TB,R,N,V_isLongFormCandidate) isLongFormCandidate;
@property (TB,R,N,V_isPollAction) isPollAction;
```

## Class methods

```
+[_UISmartReplyFeedbackManager _sendAnalyticsForSignal:toChannel:withThreadId:payload:];
+[_UISmartReplyFeedbackManager _conversationTypePayloadValueFromConversationType:];
+[_UISmartReplyFeedbackManager candidateIsLongFormSmartReply:];
+[_UISmartReplyFeedbackManager candidateIsSmartAction:];
+[_UISmartReplyFeedbackManager candidateIsSmartReply:];
+[_UISmartReplyFeedbackManager showAIGeneratedUI];
+[_UISmartReplyFeedbackManager showReportConcernUI];
+[_UISmartReplyFeedbackManager userSelectedSmartReply:isLongForm:withMailOrMsgThreadId:withConversationType:withSmartReplyFeedbackManagerInstance:];
```

## Instance methods

```
-[_UISmartReplyFeedbackManager predictionsContainSmartReplies:];
-[_UISmartReplyFeedbackManager resetSmartReplyFeedbackUIIfAlreadyShown];
-[_UISmartReplyFeedbackManager previouslyShownCandidates];
-[_UISmartReplyFeedbackManager resetWithDebug:];
-[_UISmartReplyFeedbackManager shouldShowSmartReplyFeedbackInputDashboardViewControllerWithKeyboardIsSplit:];
-[_UISmartReplyFeedbackManager initWithKeyboardStateManagerDelegate:];
-[_UISmartReplyFeedbackManager smartReplyWasShownOrSelected];
-[_UISmartReplyFeedbackManager setKeyboardStateManagerDelegate:];
-[_UISmartReplyFeedbackManager init];
-[_UISmartReplyFeedbackManager setPredictionBarDebounceTimeInterval:];
-[_UISmartReplyFeedbackManager updateCandidates:];
-[_UISmartReplyFeedbackManager selectedCandidateDescription];
-[_UISmartReplyFeedbackManager isPollAction];
-[_UISmartReplyFeedbackManager resetOnKeyboardCandidatesCleared];
-[_UISmartReplyFeedbackManager userSelectedGenmojiSuggestionAction:withInputContextHistory:];
-[_UISmartReplyFeedbackManager smartReplyWasSelected];
-[_UISmartReplyFeedbackManager predictionBarDebounceTimeIntervalExpired];
-[_UISmartReplyFeedbackManager predictionsContainLongFormCandidates:];
-[_UISmartReplyFeedbackManager reportSmartRepliesFeedbackSignal:];
-[_UISmartReplyFeedbackManager _userSelectedSmartReply:isLongForm:withMailOrMsgThreadId:withConversationType:];
-[_UISmartReplyFeedbackManager isLongFormCandidate];
-[_UISmartReplyFeedbackManager resetStateIfNoSmartReplySelected];
-[_UISmartReplyFeedbackManager analyticsSessionId];
-[_UISmartReplyFeedbackManager willShowFeedbackUI];
-[_UISmartReplyFeedbackManager setAnalyticsSessionId:];
-[_UISmartReplyFeedbackManager setPreviouslyShownCandidates:];
-[_UISmartReplyFeedbackManager predictionsContainSmartActions:];
-[_UISmartReplyFeedbackManager setReportFeedbackUIPresentedCalledTime:];
-[_UISmartReplyFeedbackManager keyboardStateManagerDelegate];
-[_UISmartReplyFeedbackManager _sendAnalyticsForSignal:toChannel:withThreadId:payload:];
-[_UISmartReplyFeedbackManager stringListFromPredictions:];
-[_UISmartReplyFeedbackManager initWithoutBundleIdCheck];
-[_UISmartReplyFeedbackManager setSelectedCandidateDescription:];
-[_UISmartReplyFeedbackManager predictionBarDebounceTimeInterval];
-[_UISmartReplyFeedbackManager setPredictionBarDebounceTimeIntervalTimer:];
-[_UISmartReplyFeedbackManager predictionBarDebounceTimeIntervalTimer];
-[_UISmartReplyFeedbackManager reportFeedbackUIPresented];
-[_UISmartReplyFeedbackManager userSelectedPollAction:withInputContextHistory:];
-[_UISmartReplyFeedbackManager reportFeedbackUIPresentedCalledTime];
-[_UISmartReplyFeedbackManager feedbackUIWasPresented];
-[_UISmartReplyFeedbackManager userSelectedStructuredSearchAction:withInputContextHistory:];
-[_UISmartReplyFeedbackManager reportSmartRepliesThumbsUp];
-[_UISmartReplyFeedbackManager smartRepliesPresented];
-[_UISmartReplyFeedbackManager reportSmartRepliesThumbsDown];
-[_UISmartReplyFeedbackManager inputModeWillChange];
-[_UISmartReplyFeedbackManager composeFieldInFocusWithMailOrMsgThreadId:];
-[_UISmartReplyFeedbackManager reportWritingToolsPanelDismissed];
-[_UISmartReplyFeedbackManager reportSmartRepliesConcern];
-[_UISmartReplyFeedbackManager state];
```
