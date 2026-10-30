# `UIInlineTextCompletionController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UITextCompletionAcceptanceDelegate`
- 13 instance variables, 16 properties, 74 instance methods, 1 class methods

## Instance variables

```
@"UIInlineTextCompletionPrompt" m_textCompletionPrompt;
B _currentlyAcceptingInlineCompletionByDirectTap;
B _deleting;
B _hasForwardProgress;
@"<UIInlineTextCompletionControllerDelegate>" _delegate;
@"NSString" _presentingTextCompletionAsMarkedText;
@"UIKBAnalyticsDispatcher" _analyticsDispatcher;
@"_UIInlineTextCompletion" _textCompletion;
@"UIKeyboardScheduledTask" _textCompletionPromptTask;
@"UIKeyboardScheduledTask" _inlineCompletionCoachingTask;
@"_UIInlineTextCompletion" _candidateRemovedOnWillPerformOutput;
@"_UIInlineTextCompletion" _acceptingTextCompletion;
@"_UIInlineTextCompletion" _lastAcceptedTextCompletion;
```

## Properties

```
@property (T@"_UIInlineTextCompletion",R,N,V_textCompletion) textCompletion;
@property (T@"_UIInlineTextCompletion",R,N) oneWordTextCompletion;
@property (T@"UIResponder<UITextInput>",R,N) inputDelegate;
@property (T@"UIKeyboardScheduledTask",&,N,V_textCompletionPromptTask) textCompletionPromptTask;
@property (T@"UIKeyboardScheduledTask",&,N,V_inlineCompletionCoachingTask) inlineCompletionCoachingTask;
@property (T@"NSString",C,N,V_presentingTextCompletionAsMarkedText) presentingTextCompletionAsMarkedText;
@property (T@"_UIInlineTextCompletion",&,N,V_candidateRemovedOnWillPerformOutput) candidateRemovedOnWillPerformOutput;
@property (T@"_UIInlineTextCompletion",&,N,V_acceptingTextCompletion) acceptingTextCompletion;
@property (T@"_UIInlineTextCompletion",&,N,V_lastAcceptedTextCompletion) lastAcceptedTextCompletion;
@property (TB,N,GisDeleting,V_deleting) deleting;
@property (TB,N,V_hasForwardProgress) hasForwardProgress;
@property (T@"<UIInlineTextCompletionControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N) hasPrompt;
@property (TB,N,V_currentlyAcceptingInlineCompletionByDirectTap) currentlyAcceptingInlineCompletionByDirectTap;
@property (TQ,R,N) currentInlineTextCompletionMode;
@property (T@"UIKBAnalyticsDispatcher",W,N,V_analyticsDispatcher) analyticsDispatcher;
```

## Class methods

```
+[UIInlineTextCompletionController _documentTextThroughSelection:];
```

## Instance methods

```
-[UIInlineTextCompletionController selectionDidChange];
-[UIInlineTextCompletionController setInlineCompletionCoachingTask:];
-[UIInlineTextCompletionController updateTextCompletionWithExternalSuggestion:];
-[UIInlineTextCompletionController inputDelegate];
-[UIInlineTextCompletionController inlineCompletionCoachingTask];
-[UIInlineTextCompletionController setDeleting:];
-[UIInlineTextCompletionController updateTextCompletionPromptExecutionContext:];
-[UIInlineTextCompletionController textCompletionPromptTask];
-[UIInlineTextCompletionController _oneWordTextCompletionFromTextCompletion:];
-[UIInlineTextCompletionController _removeTextCompletionPromptForReason:];
-[UIInlineTextCompletionController _updateTextCompletionPromptWithTextCompletion:parentView:inputRects:];
-[UIInlineTextCompletionController _shouldAcceptFirstWordOfCandidateForWordTerminator:];
-[UIInlineTextCompletionController _shouldAcceptUpToNextWordOfCandidateOnWordBoundaryForInteraction:];
-[UIInlineTextCompletionController _markedTextAttributes];
-[UIInlineTextCompletionController undoAcceptedTextCompletionExecutionContext:];
-[UIInlineTextCompletionController _doesFirstPredictedCharacterEndWord:];
-[UIInlineTextCompletionController _touchTextCompletionPromptTimer];
-[UIInlineTextCompletionController hasPrompt];
-[UIInlineTextCompletionController _textCompletionPromptRectsForInput:];
-[UIInlineTextCompletionController acceptTextCompletionWithInteraction:wordTerminator:];
-[UIInlineTextCompletionController setCandidateRemovedOnWillPerformOutput:];
-[UIInlineTextCompletionController _candidateToUndoAcceptedTextCompletion];
-[UIInlineTextCompletionController _inlineCompletionModeForTraitsWithCurrentPreference:];
-[UIInlineTextCompletionController _updatePromptDelay];
-[UIInlineTextCompletionController setPresentingTextCompletionAsMarkedText:];
-[UIInlineTextCompletionController updateTextCompletionDisplay];
-[UIInlineTextCompletionController setHasForwardProgress:];
-[UIInlineTextCompletionController selectionWillChange];
-[UIInlineTextCompletionController oneWordTextCompletion];
-[UIInlineTextCompletionController _isCompletion:continuingLastCompletion:];
-[UIInlineTextCompletionController _touchInlineCompletionCoachingTimer];
-[UIInlineTextCompletionController currentInlineTextCompletionMode];
-[UIInlineTextCompletionController hasForwardProgress];
-[UIInlineTextCompletionController _registerLearningForInlineCompletion:learningMode:];
-[UIInlineTextCompletionController currentlyAcceptingInlineCompletionByDirectTap];
-[UIInlineTextCompletionController setDelegate:];
-[UIInlineTextCompletionController _presentInlineTextCompletionCoachingUIWithExecutionContext:];
-[UIInlineTextCompletionController _acceptTextCompletionWithInteraction:wordTerminator:];
-[UIInlineTextCompletionController _deleteToUndoEnabled];
-[UIInlineTextCompletionController acceptTextCompletionWithInteraction:wordTerminator:outputHandledByCaller:];
-[UIInlineTextCompletionController setAcceptingTextCompletion:];
-[UIInlineTextCompletionController _inlineCompletionPreference];
-[UIInlineTextCompletionController didPerformKeyboardOutput:];
-[UIInlineTextCompletionController textCompletionPrompt];
-[UIInlineTextCompletionController _updateTextCompletionPrompt:executionContext:];
-[UIInlineTextCompletionController _acceptTypeForTypeWordTerminator:];
-[UIInlineTextCompletionController setTextCompletionPromptTask:];
-[UIInlineTextCompletionController delegate];
-[UIInlineTextCompletionController willAcceptPredictiveInput:];
-[UIInlineTextCompletionController presentingTextCompletionAsMarkedText];
-[UIInlineTextCompletionController _shouldShowInlineTextCompletionCoachingUI];
-[UIInlineTextCompletionController _clearInlineCompletionCoachingTimer];
-[UIInlineTextCompletionController acceptingTextCompletion];
-[UIInlineTextCompletionController canUndoAcceptedTextCompletion];
-[UIInlineTextCompletionController willPerformKeyboardOutput:];
-[UIInlineTextCompletionController _bestTextCompletion];
-[UIInlineTextCompletionController textCompletion];
-[UIInlineTextCompletionController setLastAcceptedTextCompletion:];
-[UIInlineTextCompletionController _upToNextWordTextCompletionFromTextCompletion:];
-[UIInlineTextCompletionController setCurrentlyAcceptingInlineCompletionByDirectTap:];
-[UIInlineTextCompletionController analyticsDispatcher];
-[UIInlineTextCompletionController _updateTextCompletionPrompt:inputRects:];
-[UIInlineTextCompletionController candidateRemovedOnWillPerformOutput];
-[UIInlineTextCompletionController _isRejectionWhenRemovingPromptForReason:];
-[UIInlineTextCompletionController _textCompletions];
-[UIInlineTextCompletionController isDeleting];
-[UIInlineTextCompletionController lastAcceptedTextCompletion];
-[UIInlineTextCompletionController setAnalyticsDispatcher:];
-[UIInlineTextCompletionController _acceptTextCompletion:learningMode:];
-[UIInlineTextCompletionController _acceptTypeForInteraction:wordTerminator:];
-[UIInlineTextCompletionController acceptTextCompletion:];
-[UIInlineTextCompletionController removeTextCompletionPrompt];
-[UIInlineTextCompletionController _clearTextCompletionPromptTimer];
-[UIInlineTextCompletionController updateTextCompletionPrompt];
```
