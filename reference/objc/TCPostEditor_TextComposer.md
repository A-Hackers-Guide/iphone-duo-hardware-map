# `TCPostEditor`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 0 properties, 63 instance methods, 10 class methods

## Instance variables

```
@"NSDictionary" _options;
@"NSMutableDictionary" _editors;
@"TCTagger" _tagger;
@"TCSentenceCache" _sentenceCache;
@"TCSentenceCache" _extendedSentenceCache;
@"TCXPCClient" _xpcClient;
@"NSTimer" _idleTimer;
d _timeoutInterval;
d _minTimeoutInterval;
d _maxTimeoutInterval;
```

## Class methods

```
+[TCPostEditor sharedEditor];
+[TCPostEditor logIgnoredSentence:taggerFlags:];
+[TCPostEditor allowAllLanguages];
+[TCPostEditor allowMultilingual];
+[TCPostEditor checkingEnabledForLanguage:];
+[TCPostEditor deviceHasSuitableANE];
+[TCPostEditor enabledLanguages];
+[TCPostEditor enabledLanguagesForProofreadingReview];
+[TCPostEditor suppressTelemetryWithOptions:];
+[TCPostEditor uuidForSentence:detailRange:corrections:];
```

## Instance methods

```
-[TCPostEditor xpcClient];
-[TCPostEditor resetCache];
-[TCPostEditor warmEditorsInBackground:];
-[TCPostEditor useCacheWithOptions:];
-[TCPostEditor performProofreadingReview];
-[TCPostEditor taggerWithString:language:];
-[TCPostEditor extendedGrammarDetailForString:containingRange:language:actualRange:];
-[TCPostEditor clearTagger];
-[TCPostEditor editorOfType:];
-[TCPostEditor dealloc];
-[TCPostEditor enabledLanguageForProofreadingReviewForLanguage:string:];
-[TCPostEditor increaseIdleTimeoutInterval:];
-[TCPostEditor checkString:range:tagger:offset:options:mutableResults:];
-[TCPostEditor combinedResultsForResults:useAutocorrection:];
-[TCPostEditor storeCachedResults:forString:range:language:offset:];
-[TCPostEditor resultByCombiningCorrectionResultsInRange:fromResults:alreadyAddedResults:];
-[TCPostEditor requireANE];
-[TCPostEditor requestCheckingOfString:language:offset:options:completionHandler:];
-[TCPostEditor recordResponse:toResult:language:];
-[TCPostEditor allEditorTypes];
-[TCPostEditor recordResponse:toGrammarDetail:language:];
-[TCPostEditor defaultRemoteEditorTypes];
-[TCPostEditor enabledLanguageForLanguage:string:];
-[TCPostEditor initWithOptions:];
-[TCPostEditor requestLocalResultsFromProofreadingReviewOfString:range:language:offset:options:completionHandler:];
-[TCPostEditor requestCheckingOfString:range:language:options:completionHandler:];
-[TCPostEditor requiredANENotPresent];
-[TCPostEditor _requestProofreadingReviewOfString:range:language:offset:options:testOnly:completionHandler:];
-[TCPostEditor initWithChecker:];
-[TCPostEditor localResultsFromCheckingString:range:language:offset:options:];
-[TCPostEditor requestCheckingOfString:range:language:offset:options:completionHandler:];
-[TCPostEditor requestResultOptionsForUUIDString:completionHandler:];
-[TCPostEditor controlRepeatedAutocorrectionResultsForString:range:language:offset:mutableResults:];
-[TCPostEditor performPhraseAnalysis];
-[TCPostEditor defaultEditorTypesForAppKit];
-[TCPostEditor idleTimerFired:];
-[TCPostEditor remoteCheckString:range:tagger:offset:options:mutableResults:completionHandler:];
-[TCPostEditor grammarDetailForString:range:language:];
-[TCPostEditor requestProofreadingReviewOfString:range:language:offset:options:completionHandler:];
-[TCPostEditor localResultOptionsForUUIDString:];
-[TCPostEditor localAndCachedResultsFromCheckingString:range:language:offset:options:performProofreadingReview:];
-[TCPostEditor resetIdleTimer];
-[TCPostEditor resultByCombiningGrammarResultsInRange:fromResults:];
-[TCPostEditor retrieveCachedResultsForString:range:language:offset:mutableResults:remainingRange:];
-[TCPostEditor conditionalFinalResultsFromCheckingString:range:language:options:];
-[TCPostEditor defaultLocalEditorTypes];
-[TCPostEditor grammarDetailForRange:inString:sentenceRange:tagger:];
-[TCPostEditor useServer];
-[TCPostEditor useAutocorrectionWithOptions:];
-[TCPostEditor finalResultsFromCheckingString:range:language:options:];
-[TCPostEditor _cachedResultsFromProofreadingReviewOfString:range:language:offset:options:];
-[TCPostEditor performProofreadingReviewWithOptions:];
-[TCPostEditor resetRepeatedAutocorrectionCache];
-[TCPostEditor requestCheckingOfString:language:offset:optionsData:completionHandler:];
-[TCPostEditor localRecordResponse:toGrammarDetail:language:appIdentifier:];
-[TCPostEditor defaultEditorTypesForProofreadingReview];
-[TCPostEditor reversionForString:range:language:];
-[TCPostEditor extendedGrammarDetailContainingRange:inString:sentenceRange:tagger:actualRange:];
-[TCPostEditor resetEditors];
-[TCPostEditor resultsFromCheckingString:range:language:options:];
-[TCPostEditor finalResultsFromCheckingString:range:language:conditionalOnTerminationEstimation:options:];
-[TCPostEditor controlRepeatedAutocorrectionsWithOptions:];
-[TCPostEditor _setTimeoutValuesWithOptions:];
```
