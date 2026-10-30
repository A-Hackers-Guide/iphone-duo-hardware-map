# `PKAutoRefineLogEntry`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKHandwritingSynthesisLogEntry`
- 7 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _unrefinedStrokes;
@"NSArray" _refinedStrokes;
@"NSArray" _unchangedStrokes;
B _isAutoRefined;
q _refinedWordCount;
d _tokenDeviation;
d _tokenTranslation;
```

## Properties

```
@property (T@"NSArray",R,V_refinedStrokes) refinedStrokes;
@property (T@"NSArray",R) originalStrokes;
@property (T@"NSArray",R,V_unchangedStrokes) unchangedStrokes;
@property (Tq,R,V_refinedWordCount) refinedWordCount;
@property (Td,R,V_tokenDeviation) tokenDeviation;
@property (Td,R,V_tokenTranslation) tokenTranslation;
@property (TB,R,V_isAutoRefined) isAutoRefined;
```

## Instance methods

```
-[PKAutoRefineLogEntry contextStrokes];
-[PKAutoRefineLogEntry originalStrokes];
-[PKAutoRefineLogEntry estimateMetricsWithTokenDeviation:tokenHeight:];
-[PKAutoRefineLogEntry initWithRefinedStrokes:originalStrokes:unchangedStrokes:locale:refinedWordCount:duration:isAutoRefined:debugInfo:];
-[PKAutoRefineLogEntry isAutoRefined];
-[PKAutoRefineLogEntry refinedStrokes];
-[PKAutoRefineLogEntry refinedWordCount];
-[PKAutoRefineLogEntry synthesizedStrokes];
-[PKAutoRefineLogEntry tokenDeviation];
-[PKAutoRefineLogEntry tokenTranslation];
-[PKAutoRefineLogEntry unchangedStrokes];
```
