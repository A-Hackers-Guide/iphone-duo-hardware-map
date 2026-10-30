# `QSSBatchTranslationResponse_TranslationPhrase`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 5 properties, 12 instance methods, 0 class methods

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
@property (T@"NSArray",R,N) repeated_spans;
```

## Instance methods

```
-[QSSBatchTranslationResponse_TranslationPhrase copyWithZone:];
-[QSSBatchTranslationResponse_TranslationPhrase confidence];
-[QSSBatchTranslationResponse_TranslationPhrase addObjectToBuffer:];
-[QSSBatchTranslationResponse_TranslationPhrase flatbuffData];
-[QSSBatchTranslationResponse_TranslationPhrase initAndVerifyWithFlatbuffData:];
-[QSSBatchTranslationResponse_TranslationPhrase initWithFlatbuffData:];
-[QSSBatchTranslationResponse_TranslationPhrase initWithFlatbuffData:root:];
-[QSSBatchTranslationResponse_TranslationPhrase initWithFlatbuffData:root:verify:];
-[QSSBatchTranslationResponse_TranslationPhrase meta_info];
-[QSSBatchTranslationResponse_TranslationPhrase low_confidence];
-[QSSBatchTranslationResponse_TranslationPhrase repeated_spans];
-[QSSBatchTranslationResponse_TranslationPhrase translation_phrase];
```
