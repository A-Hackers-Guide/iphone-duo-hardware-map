# `QSSFinalSpeechRecognitionResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 13 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{FinalSpeechRecognitionResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (Ti,R,N) return_code;
@property (T@"NSString",R,N) return_str;
@property (T@"QSSRecognitionResult",R,N) recognition_result;
@property (Tq,R,N) lang_profile_recreate_codes;
@property (T@"QSSAudioAnalytics",R,N) audio_analytics;
@property (Tq,R,N) watermark_detection;
@property (Td,R,N) watermark_peak_average;
@property (T@"NSString",R,N) language;
@property (T@"QSSLatnnMitigatorResult",R,N) latnn_mitigator_result;
@property (T@"NSString",R,N) request_locale;
@property (TB,R,N) has_result;
```

## Instance methods

```
-[QSSFinalSpeechRecognitionResponse language];
-[QSSFinalSpeechRecognitionResponse copyWithZone:];
-[QSSFinalSpeechRecognitionResponse addObjectToBuffer:];
-[QSSFinalSpeechRecognitionResponse flatbuffData];
-[QSSFinalSpeechRecognitionResponse initAndVerifyWithFlatbuffData:];
-[QSSFinalSpeechRecognitionResponse initWithFlatbuffData:];
-[QSSFinalSpeechRecognitionResponse initWithFlatbuffData:root:];
-[QSSFinalSpeechRecognitionResponse initWithFlatbuffData:root:verify:];
-[QSSFinalSpeechRecognitionResponse session_id];
-[QSSFinalSpeechRecognitionResponse speech_id];
-[QSSFinalSpeechRecognitionResponse audio_analytics];
-[QSSFinalSpeechRecognitionResponse has_result];
-[QSSFinalSpeechRecognitionResponse lang_profile_recreate_codes];
-[QSSFinalSpeechRecognitionResponse latnn_mitigator_result];
-[QSSFinalSpeechRecognitionResponse recognition_result];
-[QSSFinalSpeechRecognitionResponse request_locale];
-[QSSFinalSpeechRecognitionResponse return_code];
-[QSSFinalSpeechRecognitionResponse return_str];
-[QSSFinalSpeechRecognitionResponse watermark_detection];
-[QSSFinalSpeechRecognitionResponse watermark_peak_average];
```
