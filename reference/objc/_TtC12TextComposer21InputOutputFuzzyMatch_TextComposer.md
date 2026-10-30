# `_TtC12TextComposer21InputOutputFuzzyMatch`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 4 instance methods, 1 class methods

## Instance variables

```
_$sSaySSG input;
_$sShySSG inputTokens;
_$sShySSG stopWords;
_$sSa -> _StringProcessing.Regex _StringProcessing.AnyRegexOutput exemptionRegexList;
```

## Class methods

```
+[_TtC12TextComposer21InputOutputFuzzyMatch tokenize:];
```

## Instance methods

```
-[_TtC12TextComposer21InputOutputFuzzyMatch init];
-[_TtC12TextComposer21InputOutputFuzzyMatch initWithInput:stopWords:exemptionRegexStringList:];
-[_TtC12TextComposer21InputOutputFuzzyMatch isExactMatchWithOutputWordTokens:threshold:alwaysAllowOneMistake:];
-[_TtC12TextComposer21InputOutputFuzzyMatch isFuzzyMatchWithOutputWordTokens:threshold:alwaysAllowOneMistake:];
```
