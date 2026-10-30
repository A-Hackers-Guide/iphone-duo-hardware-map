# `TCProofreadingReviewRunner`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 0 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _cachedGrammarDetailsDictionary;
@"NSMutableArray" _cachedSentenceArray;
@"NSMutableArray" _cachedNegativeHashArray;
@"NSMutableDictionary" _extendedCachedGrammarDetailsDictionary;
@"NSMutableArray" _extendedCachedSentenceArray;
@"NSMutableArray" _requestedSentenceArray;
@"NSMutableArray" _requestedOptionsArray;
@"NSMutableArray" _queuedSentenceArray;
@"NSMutableDictionary" _cachedGrammarOptionsDictionary;
@"NSMutableArray" _cachedUUIDStringArray;
@"NSObject<OS_dispatch_queue>" _serialQueue;
@"NSTimer" _timer;
@"NSDate" _lastRequestTime;
q _outstandingRequestCount;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _outstandingRequestCountLock;
```

## Instance methods

```
-[TCProofreadingReviewRunner init];
-[TCProofreadingReviewRunner resetTimer];
-[TCProofreadingReviewRunner timerFired:];
-[TCProofreadingReviewRunner timerInterval];
-[TCProofreadingReviewRunner _decrementOutstandingRequestCount];
-[TCProofreadingReviewRunner _handleResults:options:forString:sentences:];
-[TCProofreadingReviewRunner _incrementOutstandingRequestCount];
-[TCProofreadingReviewRunner cachedGrammarDetailsForSentence:locale:];
-[TCProofreadingReviewRunner cachedGrammarOptionsForUUIDString:];
-[TCProofreadingReviewRunner computeGrammarDetails];
-[TCProofreadingReviewRunner computeGrammarDetailsForSentences:withOptions:];
-[TCProofreadingReviewRunner extendedCachedGrammarDetailsForSentence:locale:];
-[TCProofreadingReviewRunner grammarDetailsForSentence:locale:options:];
-[TCProofreadingReviewRunner outstandingRequestCount];
```
