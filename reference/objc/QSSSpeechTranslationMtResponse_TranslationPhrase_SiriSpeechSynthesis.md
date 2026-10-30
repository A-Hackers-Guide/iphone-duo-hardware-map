# `QSSSpeechTranslationMtResponse_TranslationPhrase`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TranslationPhrase=[1C]} _root;
```

## Properties

```
@property (Tf,R,N) confidence;
@property (T@"NSString",R,N) translation_phrase;
@property (T@"NSString",R,N) meta_info;
@property (TB,R,N) low_confidence;
```

## Instance methods

```
-[QSSSpeechTranslationMtResponse_TranslationPhrase copyWithZone:];
-[QSSSpeechTranslationMtResponse_TranslationPhrase confidence];
-[QSSSpeechTranslationMtResponse_TranslationPhrase addObjectToBuffer:];
-[QSSSpeechTranslationMtResponse_TranslationPhrase flatbuffData];
-[QSSSpeechTranslationMtResponse_TranslationPhrase initAndVerifyWithFlatbuffData:];
-[QSSSpeechTranslationMtResponse_TranslationPhrase initWithFlatbuffData:];
-[QSSSpeechTranslationMtResponse_TranslationPhrase initWithFlatbuffData:root:];
-[QSSSpeechTranslationMtResponse_TranslationPhrase initWithFlatbuffData:root:verify:];
-[QSSSpeechTranslationMtResponse_TranslationPhrase meta_info];
-[QSSSpeechTranslationMtResponse_TranslationPhrase low_confidence];
-[QSSSpeechTranslationMtResponse_TranslationPhrase translation_phrase];
```
