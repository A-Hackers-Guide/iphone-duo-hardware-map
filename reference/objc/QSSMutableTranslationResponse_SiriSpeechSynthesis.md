# `QSSMutableTranslationResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSTranslationResponse`
- 0 instance variables, 9 properties, 20 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) speech_id;
@property (T@"NSString",C,N) request_id;
@property (Ti,N) return_code;
@property (T@"NSString",C,N) return_string;
@property (T@"NSArray",C,N) n_best_translated_phrases;
@property (T@"NSString",C,N) engine_input;
@property (T@"NSArray",C,N) engine_output;
@property (T@"NSString",C,N) sequence_id;
@property (TB,N) final_message;
```

## Instance methods

```
-[QSSMutableTranslationResponse init];
-[QSSMutableTranslationResponse copyWithZone:];
-[QSSMutableTranslationResponse setSpeech_id:];
-[QSSMutableTranslationResponse speech_id];
-[QSSMutableTranslationResponse setSequence_id:];
-[QSSMutableTranslationResponse setReturn_code:];
-[QSSMutableTranslationResponse engine_input];
-[QSSMutableTranslationResponse engine_output];
-[QSSMutableTranslationResponse final_message];
-[QSSMutableTranslationResponse n_best_translated_phrases];
-[QSSMutableTranslationResponse request_id];
-[QSSMutableTranslationResponse return_code];
-[QSSMutableTranslationResponse return_string];
-[QSSMutableTranslationResponse sequence_id];
-[QSSMutableTranslationResponse setEngine_input:];
-[QSSMutableTranslationResponse setEngine_output:];
-[QSSMutableTranslationResponse setFinal_message:];
-[QSSMutableTranslationResponse setN_best_translated_phrases:];
-[QSSMutableTranslationResponse setRequest_id:];
-[QSSMutableTranslationResponse setReturn_string:];
```
