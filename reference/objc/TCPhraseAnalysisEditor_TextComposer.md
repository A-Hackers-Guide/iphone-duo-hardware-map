# `TCPhraseAnalysisEditor`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TCPostEditing`
- 4 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _options;
^v _parser;
@"NSMutableDictionary" _cachedGrammarDetailsDictionary;
@"NSMutableArray" _cachedSentenceArray;
```

## Instance methods

```
-[TCPhraseAnalysisEditor dealloc];
-[TCPhraseAnalysisEditor checkString:range:tagger:offset:options:mutableResults:];
-[TCPhraseAnalysisEditor initWithOptions:];
-[TCPhraseAnalysisEditor checkSentence:locale:offset:options:mutableResults:];
-[TCPhraseAnalysisEditor computedGrammarDetailsForSentence:locale:options:];
-[TCPhraseAnalysisEditor grammarDetailsForSentence:locale:options:];
-[TCPhraseAnalysisEditor loadModelsInBackground:];
-[TCPhraseAnalysisEditor resetModels];
```
