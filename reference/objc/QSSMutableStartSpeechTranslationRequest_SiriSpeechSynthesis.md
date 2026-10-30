# `QSSMutableStartSpeechTranslationRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSStartSpeechTranslationRequest`
- 0 instance variables, 10 properties, 22 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) conversation_id;
@property (T@"NSString",C,N) request_id;
@property (T@"NSArray",C,N) translation_locale_pairs;
@property (T@"QSSStartSpeechRequest",C,N) start_speech_request;
@property (T@"QSSTranslationRequest",C,N) translation_request;
@property (T@"NSArray",C,N) text_to_speech_requests;
@property (TB,N) restricted_mode;
@property (T@"NSString",C,N) app_id;
@property (Tq,N) opt_in_status;
@property (TB,N) streaming_mode;
```

## Instance methods

```
-[QSSMutableStartSpeechTranslationRequest init];
-[QSSMutableStartSpeechTranslationRequest copyWithZone:];
-[QSSMutableStartSpeechTranslationRequest app_id];
-[QSSMutableStartSpeechTranslationRequest setApp_id:];
-[QSSMutableStartSpeechTranslationRequest conversation_id];
-[QSSMutableStartSpeechTranslationRequest restricted_mode];
-[QSSMutableStartSpeechTranslationRequest opt_in_status];
-[QSSMutableStartSpeechTranslationRequest request_id];
-[QSSMutableStartSpeechTranslationRequest setConversation_id:];
-[QSSMutableStartSpeechTranslationRequest setOpt_in_status:];
-[QSSMutableStartSpeechTranslationRequest setRequest_id:];
-[QSSMutableStartSpeechTranslationRequest setRestricted_mode:];
-[QSSMutableStartSpeechTranslationRequest setStart_speech_request:];
-[QSSMutableStartSpeechTranslationRequest setStreaming_mode:];
-[QSSMutableStartSpeechTranslationRequest setText_to_speech_requests:];
-[QSSMutableStartSpeechTranslationRequest setTranslation_locale_pairs:];
-[QSSMutableStartSpeechTranslationRequest setTranslation_request:];
-[QSSMutableStartSpeechTranslationRequest start_speech_request];
-[QSSMutableStartSpeechTranslationRequest streaming_mode];
-[QSSMutableStartSpeechTranslationRequest text_to_speech_requests];
-[QSSMutableStartSpeechTranslationRequest translation_locale_pairs];
-[QSSMutableStartSpeechTranslationRequest translation_request];
```
