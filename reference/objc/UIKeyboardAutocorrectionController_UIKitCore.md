# `UIKeyboardAutocorrectionController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 9 properties, 36 instance methods, 1 class methods

## Instance variables

```
Q _signpostToken;
B _requestedAutocorrection;
B _needsAutocorrection;
B _hasPendingAutocorrection;
@"TIAutocorrectionList" _autocorrectionList;
@"TIAutocorrectionList" _textSuggestionList;
Q _maximumNumberOfCandidates;
@"_UIKeyboardCandidateGenerationContext" _candidateGenerationContext;
@"NSHashTable" _autocorrectionObservers;
@"NSMutableDictionary" _recentCandidates;
@"<UIKeyboardAutocorrectionControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<UIKeyboardAutocorrectionControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"TIKeyboardCandidate",R,N) autocorrection;
@property (T@"NSArray",R,N) textCompletions;
@property (T@"TIAutocorrectionList",&,N,V_autocorrectionList) autocorrectionList;
@property (T@"TIAutocorrectionList",&,N,V_textSuggestionList) textSuggestionList;
@property (TB,R,N) requestedAutocorrection;
@property (TQ,N,V_maximumNumberOfCandidates) maximumNumberOfCandidates;
@property (TB,R,N) hasActiveObservers;
@property (T@"_UIKeyboardCandidateGenerationContext",R,N) candidateGenerationContext;
```

## Class methods

```
+[UIKeyboardAutocorrectionController secureCandidateUIEnabled];
```

## Instance methods

```
-[UIKeyboardAutocorrectionController textSuggestionList];
-[UIKeyboardAutocorrectionController setNeedsAutocorrectionWithContext:];
-[UIKeyboardAutocorrectionController isSmartReplyCandidates];
-[UIKeyboardAutocorrectionController maximumNumberOfCandidates];
-[UIKeyboardAutocorrectionController textCompletions];
-[UIKeyboardAutocorrectionController _divertSmartPredictionsToTextChoicesAssistant];
-[UIKeyboardAutocorrectionController init];
-[UIKeyboardAutocorrectionController overrideAutocorrectionList:];
-[UIKeyboardAutocorrectionController removeAutocorrectionObserver:];
-[UIKeyboardAutocorrectionController candidatesRequireSecureHostingPresentation];
-[UIKeyboardAutocorrectionController autocorrectionList];
-[UIKeyboardAutocorrectionController setAutocorrectionList:];
-[UIKeyboardAutocorrectionController hasAutocorrection];
-[UIKeyboardAutocorrectionController hasProactiveCandidates];
-[UIKeyboardAutocorrectionController setDelegate:];
-[UIKeyboardAutocorrectionController hasTextSuggestionCandidates];
-[UIKeyboardAutocorrectionController clearAutocorrectionAndNotifyObservers:updateRemote:];
-[UIKeyboardAutocorrectionController setMaximumNumberOfCandidates:];
-[UIKeyboardAutocorrectionController setNeedsAutocorrection];
-[UIKeyboardAutocorrectionController clearAutocorrection];
-[UIKeyboardAutocorrectionController delegate];
-[UIKeyboardAutocorrectionController storedListForCandidate:];
-[UIKeyboardAutocorrectionController clearAutofillAndTextSuggestions];
-[UIKeyboardAutocorrectionController autocorrection];
-[UIKeyboardAutocorrectionController setTextSuggestionList:];
-[UIKeyboardAutocorrectionController requestAutocorrectionWithExecutionContext:];
-[UIKeyboardAutocorrectionController hasActiveObservers];
-[UIKeyboardAutocorrectionController candidateGenerationContext];
-[UIKeyboardAutocorrectionController requestedAutocorrection];
-[UIKeyboardAutocorrectionController hasAutofillCandidates];
-[UIKeyboardAutocorrectionController refreshAutocorrectionList];
-[UIKeyboardAutocorrectionController addAutocorrectionObserver:];
-[UIKeyboardAutocorrectionController updateAfterShiftStateChange];
-[UIKeyboardAutocorrectionController performBlock:withCandidateGenerationContext:];
-[UIKeyboardAutocorrectionController clearAutocorrectionAndNotifyObservers:];
-[UIKeyboardAutocorrectionController hasContinuousPathConversions];
```
