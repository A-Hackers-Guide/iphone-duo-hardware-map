# `QSSSpeechTranslationInfo`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{SpeechTranslationInfo=[1C]} _root;
```

## Properties

```
@property (T@"QSSRecognitionSausage",R,N) raw_sausage;
@property (T@"NSArray",R,N) raw_nbest_choices;
```

## Instance methods

```
-[QSSSpeechTranslationInfo copyWithZone:];
-[QSSSpeechTranslationInfo addObjectToBuffer:];
-[QSSSpeechTranslationInfo flatbuffData];
-[QSSSpeechTranslationInfo initAndVerifyWithFlatbuffData:];
-[QSSSpeechTranslationInfo initWithFlatbuffData:];
-[QSSSpeechTranslationInfo initWithFlatbuffData:root:];
-[QSSSpeechTranslationInfo initWithFlatbuffData:root:verify:];
-[QSSSpeechTranslationInfo raw_nbest_choices];
-[QSSSpeechTranslationInfo raw_sausage];
```
