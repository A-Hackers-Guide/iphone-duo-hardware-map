# `QSSMutableRecognitionCandidate`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSRecognitionCandidate`
- 0 instance variables, 14 properties, 30 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) speech_id;
@property (T@"NSString",C,N) session_id;
@property (Ti,N) return_code;
@property (T@"NSString",C,N) return_str;
@property (T@"QSSRecognitionResult",C,N) recognition_result;
@property (T@"NSString",C,N) result_id;
@property (Td,N) snr;
@property (Tq,N) fingerprint_detection;
@property (T@"QSSAudioAnalytics",C,N) audio_analytics;
@property (Tq,N) watermark_detection;
@property (Td,N) watermark_peak_average;
@property (T@"NSString",C,N) language;
@property (T@"QSSLatnnMitigatorResult",C,N) latnn_mitigator_result;
@property (T@"NSString",C,N) request_locale;
```

## Instance methods

```
-[QSSMutableRecognitionCandidate language];
-[QSSMutableRecognitionCandidate setSnr:];
-[QSSMutableRecognitionCandidate snr];
-[QSSMutableRecognitionCandidate init];
-[QSSMutableRecognitionCandidate copyWithZone:];
-[QSSMutableRecognitionCandidate setLanguage:];
-[QSSMutableRecognitionCandidate session_id];
-[QSSMutableRecognitionCandidate setSession_id:];
-[QSSMutableRecognitionCandidate setSpeech_id:];
-[QSSMutableRecognitionCandidate speech_id];
-[QSSMutableRecognitionCandidate audio_analytics];
-[QSSMutableRecognitionCandidate setReturn_code:];
-[QSSMutableRecognitionCandidate fingerprint_detection];
-[QSSMutableRecognitionCandidate latnn_mitigator_result];
-[QSSMutableRecognitionCandidate recognition_result];
-[QSSMutableRecognitionCandidate request_locale];
-[QSSMutableRecognitionCandidate result_id];
-[QSSMutableRecognitionCandidate return_code];
-[QSSMutableRecognitionCandidate return_str];
-[QSSMutableRecognitionCandidate setAudio_analytics:];
-[QSSMutableRecognitionCandidate setFingerprint_detection:];
-[QSSMutableRecognitionCandidate setLatnn_mitigator_result:];
-[QSSMutableRecognitionCandidate setRecognition_result:];
-[QSSMutableRecognitionCandidate setRequest_locale:];
-[QSSMutableRecognitionCandidate setResult_id:];
-[QSSMutableRecognitionCandidate setReturn_str:];
-[QSSMutableRecognitionCandidate setWatermark_detection:];
-[QSSMutableRecognitionCandidate setWatermark_peak_average:];
-[QSSMutableRecognitionCandidate watermark_detection];
-[QSSMutableRecognitionCandidate watermark_peak_average];
```
