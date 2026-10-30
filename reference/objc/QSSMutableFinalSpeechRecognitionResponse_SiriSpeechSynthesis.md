# `QSSMutableFinalSpeechRecognitionResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSFinalSpeechRecognitionResponse`
- 0 instance variables, 13 properties, 28 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) speech_id;
@property (T@"NSString",C,N) session_id;
@property (Ti,N) return_code;
@property (T@"NSString",C,N) return_str;
@property (T@"QSSRecognitionResult",C,N) recognition_result;
@property (Tq,N) lang_profile_recreate_codes;
@property (T@"QSSAudioAnalytics",C,N) audio_analytics;
@property (Tq,N) watermark_detection;
@property (Td,N) watermark_peak_average;
@property (T@"NSString",C,N) language;
@property (T@"QSSLatnnMitigatorResult",C,N) latnn_mitigator_result;
@property (T@"NSString",C,N) request_locale;
@property (TB,N) has_result;
```

## Instance methods

```
-[QSSMutableFinalSpeechRecognitionResponse language];
-[QSSMutableFinalSpeechRecognitionResponse init];
-[QSSMutableFinalSpeechRecognitionResponse copyWithZone:];
-[QSSMutableFinalSpeechRecognitionResponse setLanguage:];
-[QSSMutableFinalSpeechRecognitionResponse session_id];
-[QSSMutableFinalSpeechRecognitionResponse setSession_id:];
-[QSSMutableFinalSpeechRecognitionResponse setSpeech_id:];
-[QSSMutableFinalSpeechRecognitionResponse speech_id];
-[QSSMutableFinalSpeechRecognitionResponse audio_analytics];
-[QSSMutableFinalSpeechRecognitionResponse setLang_profile_recreate_codes:];
-[QSSMutableFinalSpeechRecognitionResponse setReturn_code:];
-[QSSMutableFinalSpeechRecognitionResponse has_result];
-[QSSMutableFinalSpeechRecognitionResponse lang_profile_recreate_codes];
-[QSSMutableFinalSpeechRecognitionResponse latnn_mitigator_result];
-[QSSMutableFinalSpeechRecognitionResponse recognition_result];
-[QSSMutableFinalSpeechRecognitionResponse request_locale];
-[QSSMutableFinalSpeechRecognitionResponse return_code];
-[QSSMutableFinalSpeechRecognitionResponse return_str];
-[QSSMutableFinalSpeechRecognitionResponse setAudio_analytics:];
-[QSSMutableFinalSpeechRecognitionResponse setHas_result:];
-[QSSMutableFinalSpeechRecognitionResponse setLatnn_mitigator_result:];
-[QSSMutableFinalSpeechRecognitionResponse setRecognition_result:];
-[QSSMutableFinalSpeechRecognitionResponse setRequest_locale:];
-[QSSMutableFinalSpeechRecognitionResponse setReturn_str:];
-[QSSMutableFinalSpeechRecognitionResponse setWatermark_detection:];
-[QSSMutableFinalSpeechRecognitionResponse setWatermark_peak_average:];
-[QSSMutableFinalSpeechRecognitionResponse watermark_detection];
-[QSSMutableFinalSpeechRecognitionResponse watermark_peak_average];
```
