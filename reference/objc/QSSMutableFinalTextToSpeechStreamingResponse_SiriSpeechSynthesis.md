# `QSSMutableFinalTextToSpeechStreamingResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSFinalTextToSpeechStreamingResponse`
- 0 instance variables, 7 properties, 16 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) speech_id;
@property (T@"NSString",C,N) session_id;
@property (Ti,N) error_code;
@property (T@"NSString",C,N) error_str;
@property (T@"NSString",C,N) stream_id;
@property (Ti,N) total_pkt_number;
@property (T@"QSSTextToSpeechResponseDevData",C,N) dev_data;
```

## Instance methods

```
-[QSSMutableFinalTextToSpeechStreamingResponse init];
-[QSSMutableFinalTextToSpeechStreamingResponse copyWithZone:];
-[QSSMutableFinalTextToSpeechStreamingResponse error_code];
-[QSSMutableFinalTextToSpeechStreamingResponse error_str];
-[QSSMutableFinalTextToSpeechStreamingResponse session_id];
-[QSSMutableFinalTextToSpeechStreamingResponse setError_code:];
-[QSSMutableFinalTextToSpeechStreamingResponse setError_str:];
-[QSSMutableFinalTextToSpeechStreamingResponse setSession_id:];
-[QSSMutableFinalTextToSpeechStreamingResponse setSpeech_id:];
-[QSSMutableFinalTextToSpeechStreamingResponse setStream_id:];
-[QSSMutableFinalTextToSpeechStreamingResponse setTotal_pkt_number:];
-[QSSMutableFinalTextToSpeechStreamingResponse speech_id];
-[QSSMutableFinalTextToSpeechStreamingResponse stream_id];
-[QSSMutableFinalTextToSpeechStreamingResponse total_pkt_number];
-[QSSMutableFinalTextToSpeechStreamingResponse dev_data];
-[QSSMutableFinalTextToSpeechStreamingResponse setDev_data:];
```
