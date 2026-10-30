# `CSVTUIASRGrammars`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSURLSessionDelegate`
- 1 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _grammar;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CSVTUIASRGrammars sharedGrammars];
```

## Instance methods

```
-[CSVTUIASRGrammars init];
-[CSVTUIASRGrammars _getLMEWithGrammar:withLocale:];
-[CSVTUIASRGrammars _getLeadingPatternsWithGrammars:withLocale:];
-[CSVTUIASRGrammars _getRegexPatternsWithGrammars:withUtt:withLocale:];
-[CSVTUIASRGrammars _getTrailingPatternsWithGrammars:withLocale:];
-[CSVTUIASRGrammars createGrammars];
-[CSVTUIASRGrammars getLMEforLocale:];
-[CSVTUIASRGrammars getLeadingPatternsForUtt:Locale:];
-[CSVTUIASRGrammars getRegexPatternsForUtt:Locale:];
-[CSVTUIASRGrammars getTrailingPatternsForUtt:Locale:];
```
