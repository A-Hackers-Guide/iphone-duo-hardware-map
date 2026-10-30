# `TCGECEditor`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TCPostEditing`
- 7 instance variables, 0 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _options;
@"NSObject<TCGECModel>" _model;
@"NSMutableDictionary" _cachedGrammarDetailsDictionary;
@"NSMutableArray" _cachedSentenceArray;
@"NSObject<OS_dispatch_queue>" _serialQueue;
Q _modelLoadingState;
B _proofreadingReviewActive;
```

## Instance methods

```
-[TCGECEditor dealloc];
-[TCGECEditor checkString:range:tagger:offset:options:mutableResults:];
-[TCGECEditor initWithOptions:];
-[TCGECEditor backgroundLoadingQueue];
-[TCGECEditor _loadModel];
-[TCGECEditor OTABundlePath];
-[TCGECEditor _proofreadingReviewFinished:];
-[TCGECEditor categoryForIssueType:];
-[TCGECEditor checkSentence:locale:offset:options:requireResult:mutableResults:];
-[TCGECEditor computedGrammarDetailsForSentence:locale:options:];
-[TCGECEditor grammarDetailsForSentence:locale:options:];
-[TCGECEditor loadModelsInBackground:];
-[TCGECEditor modelTypeWithOptions:];
-[TCGECEditor modelUsingBackgroundLoading:];
-[TCGECEditor resetModels];
```
