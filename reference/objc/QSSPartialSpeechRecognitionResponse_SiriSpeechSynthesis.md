# `QSSPartialSpeechRecognitionResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 10 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{PartialSpeechRecognitionResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (Ti,R,N) return_code;
@property (T@"NSString",R,N) return_str;
@property (T@"NSString",R,N) recognition_text;
@property (TB,R,N) is_stable_result;
@property (Ti,R,N) audio_duration_ms;
@property (Ti,R,N) confidence;
@property (T@"NSString",R,N) language;
@property (T@"NSString",R,N) request_locale;
```

## Instance methods

```
-[QSSPartialSpeechRecognitionResponse language];
-[QSSPartialSpeechRecognitionResponse copyWithZone:];
-[QSSPartialSpeechRecognitionResponse confidence];
-[QSSPartialSpeechRecognitionResponse addObjectToBuffer:];
-[QSSPartialSpeechRecognitionResponse flatbuffData];
-[QSSPartialSpeechRecognitionResponse initAndVerifyWithFlatbuffData:];
-[QSSPartialSpeechRecognitionResponse initWithFlatbuffData:];
-[QSSPartialSpeechRecognitionResponse initWithFlatbuffData:root:];
-[QSSPartialSpeechRecognitionResponse initWithFlatbuffData:root:verify:];
-[QSSPartialSpeechRecognitionResponse session_id];
-[QSSPartialSpeechRecognitionResponse speech_id];
-[QSSPartialSpeechRecognitionResponse audio_duration_ms];
-[QSSPartialSpeechRecognitionResponse is_stable_result];
-[QSSPartialSpeechRecognitionResponse recognition_text];
-[QSSPartialSpeechRecognitionResponse request_locale];
-[QSSPartialSpeechRecognitionResponse return_code];
-[QSSPartialSpeechRecognitionResponse return_str];
```
