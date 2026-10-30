# `QSSMutablePartialTextToSpeechStreamingResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSPartialTextToSpeechStreamingResponse`
- 0 instance variables, 9 properties, 21 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) speech_id;
@property (T@"NSString",C,N) session_id;
@property (Ti,N) error_code;
@property (T@"NSString",C,N) error_str;
@property (T@"NSString",C,N) stream_id;
@property (Ti,N) current_pkt_number;
@property (T@"NSData",C,N) audio;
@property (T@"NSArray",C,N) word_timing_info;
@property (T@"QSSTextToSpeechFeature",C,N) feature;
```

## Instance methods

```
-[QSSMutablePartialTextToSpeechStreamingResponse feature];
-[QSSMutablePartialTextToSpeechStreamingResponse setAudio:];
-[QSSMutablePartialTextToSpeechStreamingResponse init];
-[QSSMutablePartialTextToSpeechStreamingResponse audio];
-[QSSMutablePartialTextToSpeechStreamingResponse copyWithZone:];
-[QSSMutablePartialTextToSpeechStreamingResponse setFeature:];
-[QSSMutablePartialTextToSpeechStreamingResponse audio:];
-[QSSMutablePartialTextToSpeechStreamingResponse current_pkt_number];
-[QSSMutablePartialTextToSpeechStreamingResponse error_code];
-[QSSMutablePartialTextToSpeechStreamingResponse error_str];
-[QSSMutablePartialTextToSpeechStreamingResponse session_id];
-[QSSMutablePartialTextToSpeechStreamingResponse setCurrent_pkt_number:];
-[QSSMutablePartialTextToSpeechStreamingResponse setError_code:];
-[QSSMutablePartialTextToSpeechStreamingResponse setError_str:];
-[QSSMutablePartialTextToSpeechStreamingResponse setSession_id:];
-[QSSMutablePartialTextToSpeechStreamingResponse setSpeech_id:];
-[QSSMutablePartialTextToSpeechStreamingResponse setStream_id:];
-[QSSMutablePartialTextToSpeechStreamingResponse setWord_timing_info:];
-[QSSMutablePartialTextToSpeechStreamingResponse speech_id];
-[QSSMutablePartialTextToSpeechStreamingResponse stream_id];
-[QSSMutablePartialTextToSpeechStreamingResponse word_timing_info];
```
