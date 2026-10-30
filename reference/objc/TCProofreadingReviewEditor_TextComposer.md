# `TCProofreadingReviewEditor`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TCPostEditing`
- 3 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _options;
@"NSDictionary" _configurations;
@"TCProofreadingReviewRunner" _runner;
```

## Instance methods

```
-[TCProofreadingReviewEditor checkString:range:tagger:offset:options:mutableResults:];
-[TCProofreadingReviewEditor initWithOptions:];
-[TCProofreadingReviewEditor _grammarResultForSentence:locale:offset:options:configuration:grammarDetails:];
-[TCProofreadingReviewEditor cachedCheckString:range:tagger:offset:options:mutableResults:];
-[TCProofreadingReviewEditor cachedGrammarOptionsForUUIDString:];
-[TCProofreadingReviewEditor checkSentence:locale:offset:options:configuration:cachedOnly:mutableResults:];
-[TCProofreadingReviewEditor extendedCachedCheckSentence:locale:offset:options:configuration:mutableResults:];
-[TCProofreadingReviewEditor loadModelsInBackground:];
-[TCProofreadingReviewEditor resetModels];
-[TCProofreadingReviewEditor shouldReportDetail:configuration:replacedString:replacementString:];
```
