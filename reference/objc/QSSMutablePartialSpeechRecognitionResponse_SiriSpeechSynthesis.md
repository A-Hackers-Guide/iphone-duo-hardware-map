# `QSSMutablePartialSpeechRecognitionResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSPartialSpeechRecognitionResponse`
- 0 instance variables, 10 properties, 22 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) speech_id;
@property (T@"NSString",C,N) session_id;
@property (Ti,N) return_code;
@property (T@"NSString",C,N) return_str;
@property (T@"NSString",C,N) recognition_text;
@property (TB,N) is_stable_result;
@property (Ti,N) audio_duration_ms;
@property (Ti,N) confidence;
@property (T@"NSString",C,N) language;
@property (T@"NSString",C,N) request_locale;
```

## Instance methods

```
-[QSSMutablePartialSpeechRecognitionResponse language];
-[QSSMutablePartialSpeechRecognitionResponse init];
-[QSSMutablePartialSpeechRecognitionResponse setConfidence:];
-[QSSMutablePartialSpeechRecognitionResponse copyWithZone:];
-[QSSMutablePartialSpeechRecognitionResponse confidence];
-[QSSMutablePartialSpeechRecognitionResponse setLanguage:];
-[QSSMutablePartialSpeechRecognitionResponse session_id];
-[QSSMutablePartialSpeechRecognitionResponse setSession_id:];
-[QSSMutablePartialSpeechRecognitionResponse setSpeech_id:];
-[QSSMutablePartialSpeechRecognitionResponse speech_id];
-[QSSMutablePartialSpeechRecognitionResponse setReturn_code:];
-[QSSMutablePartialSpeechRecognitionResponse audio_duration_ms];
-[QSSMutablePartialSpeechRecognitionResponse is_stable_result];
-[QSSMutablePartialSpeechRecognitionResponse recognition_text];
-[QSSMutablePartialSpeechRecognitionResponse request_locale];
-[QSSMutablePartialSpeechRecognitionResponse return_code];
-[QSSMutablePartialSpeechRecognitionResponse return_str];
-[QSSMutablePartialSpeechRecognitionResponse setAudio_duration_ms:];
-[QSSMutablePartialSpeechRecognitionResponse setIs_stable_result:];
-[QSSMutablePartialSpeechRecognitionResponse setRecognition_text:];
-[QSSMutablePartialSpeechRecognitionResponse setRequest_locale:];
-[QSSMutablePartialSpeechRecognitionResponse setReturn_str:];
```
