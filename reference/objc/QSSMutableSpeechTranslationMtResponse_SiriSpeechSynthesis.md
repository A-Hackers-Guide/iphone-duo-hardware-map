# `QSSMutableSpeechTranslationMtResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSSpeechTranslationMtResponse`
- 0 instance variables, 7 properties, 16 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) conversation_id;
@property (T@"NSString",C,N) request_id;
@property (Ti,N) return_code;
@property (T@"NSString",C,N) return_str;
@property (T@"QSSTranslationLocalePair",C,N) translation_locale_pair;
@property (T@"NSArray",C,N) n_best_translated_phrases;
@property (TB,N) is_final;
```

## Instance methods

```
-[QSSMutableSpeechTranslationMtResponse init];
-[QSSMutableSpeechTranslationMtResponse copyWithZone:];
-[QSSMutableSpeechTranslationMtResponse conversation_id];
-[QSSMutableSpeechTranslationMtResponse setReturn_code:];
-[QSSMutableSpeechTranslationMtResponse is_final];
-[QSSMutableSpeechTranslationMtResponse n_best_translated_phrases];
-[QSSMutableSpeechTranslationMtResponse request_id];
-[QSSMutableSpeechTranslationMtResponse return_code];
-[QSSMutableSpeechTranslationMtResponse return_str];
-[QSSMutableSpeechTranslationMtResponse setConversation_id:];
-[QSSMutableSpeechTranslationMtResponse setIs_final:];
-[QSSMutableSpeechTranslationMtResponse setN_best_translated_phrases:];
-[QSSMutableSpeechTranslationMtResponse setRequest_id:];
-[QSSMutableSpeechTranslationMtResponse setReturn_str:];
-[QSSMutableSpeechTranslationMtResponse setTranslation_locale_pair:];
-[QSSMutableSpeechTranslationMtResponse translation_locale_pair];
```
