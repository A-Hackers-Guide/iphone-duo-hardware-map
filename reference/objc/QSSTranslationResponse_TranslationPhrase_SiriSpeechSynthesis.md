# `QSSTranslationResponse_TranslationPhrase`

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
@property (T@"NSArray",R,N) translated_tokens;
@property (T@"NSString",R,N) meta_info;
@property (T@"NSArray",R,N) spans;
@property (TB,R,N) low_confidence;
```

## Instance methods

```
-[QSSTranslationResponse_TranslationPhrase copyWithZone:];
-[QSSTranslationResponse_TranslationPhrase spans];
-[QSSTranslationResponse_TranslationPhrase confidence];
-[QSSTranslationResponse_TranslationPhrase addObjectToBuffer:];
-[QSSTranslationResponse_TranslationPhrase flatbuffData];
-[QSSTranslationResponse_TranslationPhrase initAndVerifyWithFlatbuffData:];
-[QSSTranslationResponse_TranslationPhrase initWithFlatbuffData:];
-[QSSTranslationResponse_TranslationPhrase initWithFlatbuffData:root:];
-[QSSTranslationResponse_TranslationPhrase initWithFlatbuffData:root:verify:];
-[QSSTranslationResponse_TranslationPhrase meta_info];
-[QSSTranslationResponse_TranslationPhrase low_confidence];
-[QSSTranslationResponse_TranslationPhrase translated_tokens];
```
