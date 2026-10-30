# `UITextCheckingController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 2 properties, 42 instance methods, 0 class methods

## Instance variables

```
@"<UITextCheckingClient>" _client;
@"UITextChecker" _textChecker;
@"NSTimer" _pauseTimer;
d _lastPauseTimer;
{_NSRange="location"Q"length"Q} _selectedRangeFromPreviousUnchecked;
{_NSRange="location"Q"length"Q} _previousCheckedSentenceRange;
{_NSRange="location"Q"length"Q} _previousCheckedSelectedRange;
q _prechangeCheckingSequenceNumber;
@"NSMutableArray" _proofreadingReviewTimers;
@"NSMutableOrderedSet" _recentlyShimmeredGrammarUUIDs;
{__tccClientFlags="respondsToAutocorrectionType"b1"respondsToSpellCheckingType"b1"respondsToSmartQuotesType"b1"respondsToSmartDashesType"b1"respondsToSmartInsertDeleteType"b1"respondsToContinuousSpellCheckingEnabled"b1"respondsToGrammarCheckingType"b1} _tccClientFlags;
B _isGrammarCheckingEnabled;
```

## Properties

```
@property (T@"<UITextCheckingClient>",R) client;
@property (TB,N,SsetGrammarCheckingEnabled:,V_isGrammarCheckingEnabled) isGrammarCheckingEnabled;
```

## Instance methods

```
-[UITextCheckingController selectedRange];
-[UITextCheckingController textChecker];
-[UITextCheckingController terminatedSentenceRangeInTextRange:];
-[UITextCheckingController invalidateTimers];
-[UITextCheckingController annotatedSubstringForRange:];
-[UITextCheckingController didChangeTextInRange:];
-[UITextCheckingController considerTextCheckingForRange:];
-[UITextCheckingController initWithClient:];
-[UITextCheckingController _addCorrectionUnderlinesForCandidates:ranges:inSentenceRange:];
-[UITextCheckingController didChangeSelectionFromRange:];
-[UITextCheckingController dealloc];
-[UITextCheckingController preheatTextChecker];
-[UITextCheckingController checkSpellingForWordInRange:];
-[UITextCheckingController applyGrammarCheckingIndication];
-[UITextCheckingController performFinalGrammarCheckingWithAutocorrection:];
-[UITextCheckingController nsRangeForTextRange:];
-[UITextCheckingController _pauseTimer:];
-[UITextCheckingController isGrammarCheckingEnabled];
-[UITextCheckingController _handleGrammarCheckingResults:sequenceNumber:forSentenceRange:isFinal:autocorrectionCount:];
-[UITextCheckingController _performProofreadingReviewForSentence:language:range:];
-[UITextCheckingController invalidate];
-[UITextCheckingController removeSpellingMarkersFromWordInRange:];
-[UITextCheckingController checkGrammarForSentenceInRange:onPause:proofreadingReviewFollowUp:];
-[UITextCheckingController _addProofreadingReviewTimer:];
-[UITextCheckingController foundApostropheAfterRange:];
-[UITextCheckingController _removeProofreadingReviewTimer:];
-[UITextCheckingController willReplaceTextInRange:withText:];
-[UITextCheckingController _invalidateProofreadingReviewTimers];
-[UITextCheckingController removeGrammarMarkersFromWordsInRange:];
-[UITextCheckingController setGrammarCheckingEnabled:];
-[UITextCheckingController insertedTextInRange:];
-[UITextCheckingController performFinalGrammarChecking];
-[UITextCheckingController checkSpellingForSelectionChangeFromRange:];
-[UITextCheckingController continuousSpellCheckingEnabled];
-[UITextCheckingController feedbackForGrammarMarkersFromWordsInRange:replacementText:];
-[UITextCheckingController _addGrammarAttributesForRange:details:inAnnotatedString:];
-[UITextCheckingController removeGrammarAnnotationFromWordAtPosition:];
-[UITextCheckingController didUnmarkText];
-[UITextCheckingController client];
-[UITextCheckingController rangeIsSuitableForGrammarAutocorrections:];
-[UITextCheckingController validAnnotations];
-[UITextCheckingController annotatedStringWithValidAnnotationsForAnnotatedString:];
```
