# `QSSRecognitionCandidate`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 14 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{RecognitionCandidate=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (Ti,R,N) return_code;
@property (T@"NSString",R,N) return_str;
@property (T@"QSSRecognitionResult",R,N) recognition_result;
@property (T@"NSString",R,N) result_id;
@property (Td,R,N) snr;
@property (Tq,R,N) fingerprint_detection;
@property (T@"QSSAudioAnalytics",R,N) audio_analytics;
@property (Tq,R,N) watermark_detection;
@property (Td,R,N) watermark_peak_average;
@property (T@"NSString",R,N) language;
@property (T@"QSSLatnnMitigatorResult",R,N) latnn_mitigator_result;
@property (T@"NSString",R,N) request_locale;
```

## Instance methods

```
-[QSSRecognitionCandidate language];
-[QSSRecognitionCandidate snr];
-[QSSRecognitionCandidate copyWithZone:];
-[QSSRecognitionCandidate addObjectToBuffer:];
-[QSSRecognitionCandidate flatbuffData];
-[QSSRecognitionCandidate initAndVerifyWithFlatbuffData:];
-[QSSRecognitionCandidate initWithFlatbuffData:];
-[QSSRecognitionCandidate initWithFlatbuffData:root:];
-[QSSRecognitionCandidate initWithFlatbuffData:root:verify:];
-[QSSRecognitionCandidate session_id];
-[QSSRecognitionCandidate speech_id];
-[QSSRecognitionCandidate audio_analytics];
-[QSSRecognitionCandidate fingerprint_detection];
-[QSSRecognitionCandidate latnn_mitigator_result];
-[QSSRecognitionCandidate recognition_result];
-[QSSRecognitionCandidate request_locale];
-[QSSRecognitionCandidate result_id];
-[QSSRecognitionCandidate return_code];
-[QSSRecognitionCandidate return_str];
-[QSSRecognitionCandidate watermark_detection];
-[QSSRecognitionCandidate watermark_peak_average];
```
