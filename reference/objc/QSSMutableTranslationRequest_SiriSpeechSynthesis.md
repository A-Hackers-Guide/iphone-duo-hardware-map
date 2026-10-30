# `QSSMutableTranslationRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSTranslationRequest`
- 0 instance variables, 15 properties, 32 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) speech_id;
@property (T@"NSString",C,N) request_id;
@property (T@"NSString",C,N) task;
@property (T@"NSString",C,N) source_language;
@property (T@"NSString",C,N) target_language;
@property (T@"NSArray",C,N) translation_phrase;
@property (T@"QSSSiriTranslationInfo",C,N) siri_translation_info;
@property (T@"QSSSpeechTranslationInfo",C,N) speech_translation_info;
@property (T@"QSSSiriPayloadTranslationInfo",C,N) siri_payload_translation_info;
@property (T@"NSString",C,N) sequence_id;
@property (T@"QSSWebTranslationInfo",C,N) web_translation_info;
@property (TB,N) disable_log;
@property (Tq,N) opt_in_status;
@property (T@"NSString",C,N) app_id;
@property (T@"NSString",C,N) use_case;
```

## Instance methods

```
-[QSSMutableTranslationRequest init];
-[QSSMutableTranslationRequest setTask:];
-[QSSMutableTranslationRequest task];
-[QSSMutableTranslationRequest copyWithZone:];
-[QSSMutableTranslationRequest app_id];
-[QSSMutableTranslationRequest setApp_id:];
-[QSSMutableTranslationRequest setSpeech_id:];
-[QSSMutableTranslationRequest speech_id];
-[QSSMutableTranslationRequest setSequence_id:];
-[QSSMutableTranslationRequest setDisable_log:];
-[QSSMutableTranslationRequest source_language];
-[QSSMutableTranslationRequest target_language];
-[QSSMutableTranslationRequest disable_log];
-[QSSMutableTranslationRequest opt_in_status];
-[QSSMutableTranslationRequest request_id];
-[QSSMutableTranslationRequest sequence_id];
-[QSSMutableTranslationRequest setOpt_in_status:];
-[QSSMutableTranslationRequest setRequest_id:];
-[QSSMutableTranslationRequest setSiri_payload_translation_info:];
-[QSSMutableTranslationRequest setSiri_translation_info:];
-[QSSMutableTranslationRequest setSource_language:];
-[QSSMutableTranslationRequest setSpeech_translation_info:];
-[QSSMutableTranslationRequest setTarget_language:];
-[QSSMutableTranslationRequest setTranslation_phrase:];
-[QSSMutableTranslationRequest setUse_case:];
-[QSSMutableTranslationRequest setWeb_translation_info:];
-[QSSMutableTranslationRequest siri_payload_translation_info];
-[QSSMutableTranslationRequest siri_translation_info];
-[QSSMutableTranslationRequest speech_translation_info];
-[QSSMutableTranslationRequest translation_phrase];
-[QSSMutableTranslationRequest use_case];
-[QSSMutableTranslationRequest web_translation_info];
```
