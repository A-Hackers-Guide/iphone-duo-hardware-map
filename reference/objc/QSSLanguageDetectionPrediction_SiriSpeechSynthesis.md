# `QSSLanguageDetectionPrediction`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{LanguageDetectionPrediction=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) locale;
@property (Tf,R,N) confidence;
@property (Tf,R,N) threshold;
@property (TB,R,N) is_low_confidence;
```

## Instance methods

```
-[QSSLanguageDetectionPrediction threshold];
-[QSSLanguageDetectionPrediction locale];
-[QSSLanguageDetectionPrediction copyWithZone:];
-[QSSLanguageDetectionPrediction confidence];
-[QSSLanguageDetectionPrediction addObjectToBuffer:];
-[QSSLanguageDetectionPrediction flatbuffData];
-[QSSLanguageDetectionPrediction initAndVerifyWithFlatbuffData:];
-[QSSLanguageDetectionPrediction initWithFlatbuffData:];
-[QSSLanguageDetectionPrediction initWithFlatbuffData:root:];
-[QSSLanguageDetectionPrediction initWithFlatbuffData:root:verify:];
-[QSSLanguageDetectionPrediction is_low_confidence];
```
