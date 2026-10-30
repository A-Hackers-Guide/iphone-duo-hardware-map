# `QSSSpeechTranslationMtResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{SpeechTranslationMtResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) conversation_id;
@property (T@"NSString",R,N) request_id;
@property (Ti,R,N) return_code;
@property (T@"NSString",R,N) return_str;
@property (T@"QSSTranslationLocalePair",R,N) translation_locale_pair;
@property (T@"NSArray",R,N) n_best_translated_phrases;
@property (TB,R,N) is_final;
```

## Instance methods

```
-[QSSSpeechTranslationMtResponse copyWithZone:];
-[QSSSpeechTranslationMtResponse addObjectToBuffer:];
-[QSSSpeechTranslationMtResponse flatbuffData];
-[QSSSpeechTranslationMtResponse initAndVerifyWithFlatbuffData:];
-[QSSSpeechTranslationMtResponse initWithFlatbuffData:];
-[QSSSpeechTranslationMtResponse initWithFlatbuffData:root:];
-[QSSSpeechTranslationMtResponse initWithFlatbuffData:root:verify:];
-[QSSSpeechTranslationMtResponse conversation_id];
-[QSSSpeechTranslationMtResponse is_final];
-[QSSSpeechTranslationMtResponse n_best_translated_phrases];
-[QSSSpeechTranslationMtResponse request_id];
-[QSSSpeechTranslationMtResponse return_code];
-[QSSSpeechTranslationMtResponse return_str];
-[QSSSpeechTranslationMtResponse translation_locale_pair];
```
