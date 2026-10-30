# `QSSMutableBeginTextToSpeechStreamingResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSBeginTextToSpeechStreamingResponse`
- 0 instance variables, 10 properties, 22 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) speech_id;
@property (T@"NSString",C,N) session_id;
@property (Ti,N) error_code;
@property (T@"NSString",C,N) error_str;
@property (T@"NSString",C,N) stream_id;
@property (Tq,N) audio_type;
@property (T@"QSSAudioDescription",C,N) decoder_description;
@property (T@"QSSAudioDescription",C,N) playback_description;
@property (T@"QSSTextToSpeechMeta",C,N) meta_info;
@property (Tf,N) streaming_playback_buffer_size_in_seconds;
```

## Instance methods

```
-[QSSMutableBeginTextToSpeechStreamingResponse init];
-[QSSMutableBeginTextToSpeechStreamingResponse copyWithZone:];
-[QSSMutableBeginTextToSpeechStreamingResponse audio_type];
-[QSSMutableBeginTextToSpeechStreamingResponse decoder_description];
-[QSSMutableBeginTextToSpeechStreamingResponse error_code];
-[QSSMutableBeginTextToSpeechStreamingResponse error_str];
-[QSSMutableBeginTextToSpeechStreamingResponse meta_info];
-[QSSMutableBeginTextToSpeechStreamingResponse playback_description];
-[QSSMutableBeginTextToSpeechStreamingResponse session_id];
-[QSSMutableBeginTextToSpeechStreamingResponse setAudio_type:];
-[QSSMutableBeginTextToSpeechStreamingResponse setDecoder_description:];
-[QSSMutableBeginTextToSpeechStreamingResponse setError_code:];
-[QSSMutableBeginTextToSpeechStreamingResponse setError_str:];
-[QSSMutableBeginTextToSpeechStreamingResponse setMeta_info:];
-[QSSMutableBeginTextToSpeechStreamingResponse setPlayback_description:];
-[QSSMutableBeginTextToSpeechStreamingResponse setSession_id:];
-[QSSMutableBeginTextToSpeechStreamingResponse setSpeech_id:];
-[QSSMutableBeginTextToSpeechStreamingResponse setStream_id:];
-[QSSMutableBeginTextToSpeechStreamingResponse setStreaming_playback_buffer_size_in_seconds:];
-[QSSMutableBeginTextToSpeechStreamingResponse speech_id];
-[QSSMutableBeginTextToSpeechStreamingResponse stream_id];
-[QSSMutableBeginTextToSpeechStreamingResponse streaming_playback_buffer_size_in_seconds];
```
