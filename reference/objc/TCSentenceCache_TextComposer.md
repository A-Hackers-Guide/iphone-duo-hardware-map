# `TCSentenceCache`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 1 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _cachedResultsDictionary;
@"NSMutableArray" _cachedSentenceArray;
@"NSMutableSet" _cachedAutocorrectedSentences;
@"NSMutableDictionary" _cachedReversionsDictionary;
@"NSMutableArray" _cachedCorrectionArray;
@"NSObject<OS_dispatch_queue>" _serialQueue;
Q _capacity;
```

## Properties

```
@property (TQ,R) capacity;
```

## Instance methods

```
-[TCSentenceCache capacity];
-[TCSentenceCache reset];
-[TCSentenceCache initWithCapacity:];
-[TCSentenceCache resetRepeatedAutocorrectionCache];
-[TCSentenceCache _controlRepeatedAutocorrectionResultsForSentence:offset:mutableResults:];
-[TCSentenceCache _detailRange:inSentence:matchesRange:inString:sentenceRange:];
-[TCSentenceCache _inSerialQueueAddCachedReversion:forCorrections:];
-[TCSentenceCache _inSerialQueueAddCachedReversionsForResults:sentence:];
-[TCSentenceCache _retrieveCachedGrammarDetailForRange:inString:sentenceRange:matchingSentence:];
-[TCSentenceCache _retrieveCachedResultsForSentence:offset:mutableResults:];
-[TCSentenceCache _storeCachedResults:forSentence:];
-[TCSentenceCache _storeExtendedCachedResultsForGrammarDetails:startingIndex:sentence:];
-[TCSentenceCache addGrammarDetailsForSentenceRange:result:mutableDetails:];
-[TCSentenceCache controlRepeatedAutocorrectionResultsForString:range:tagger:offset:mutableResults:];
-[TCSentenceCache retrieveCachedGrammarDetailContainingRange:inString:sentenceRange:tagger:actualRange:];
-[TCSentenceCache retrieveCachedGrammarDetailForRange:inString:sentenceRange:tagger:];
-[TCSentenceCache retrieveCachedResultsForString:range:tagger:offset:ignoreTermination:mutableResults:remainingRange:];
-[TCSentenceCache retrieveCachedResultsForString:range:tagger:offset:mutableResults:remainingRange:];
-[TCSentenceCache retrieveCachedReversionsForString:];
-[TCSentenceCache storeCachedResults:forString:range:tagger:offset:];
-[TCSentenceCache storeExtendedCachedResults:forString:range:tagger:offset:];
```
