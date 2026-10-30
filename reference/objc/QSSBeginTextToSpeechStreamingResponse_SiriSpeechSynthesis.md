# `QSSBeginTextToSpeechStreamingResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 10 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{BeginTextToSpeechStreamingResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (Ti,R,N) error_code;
@property (T@"NSString",R,N) error_str;
@property (T@"NSString",R,N) stream_id;
@property (Tq,R,N) audio_type;
@property (T@"QSSAudioDescription",R,N) decoder_description;
@property (T@"QSSAudioDescription",R,N) playback_description;
@property (T@"QSSTextToSpeechMeta",R,N) meta_info;
@property (Tf,R,N) streaming_playback_buffer_size_in_seconds;
```

## Instance methods

```
-[QSSBeginTextToSpeechStreamingResponse copyWithZone:];
-[QSSBeginTextToSpeechStreamingResponse addObjectToBuffer:];
-[QSSBeginTextToSpeechStreamingResponse audio_type];
-[QSSBeginTextToSpeechStreamingResponse decoder_description];
-[QSSBeginTextToSpeechStreamingResponse error_code];
-[QSSBeginTextToSpeechStreamingResponse error_str];
-[QSSBeginTextToSpeechStreamingResponse flatbuffData];
-[QSSBeginTextToSpeechStreamingResponse initAndVerifyWithFlatbuffData:];
-[QSSBeginTextToSpeechStreamingResponse initWithFlatbuffData:];
-[QSSBeginTextToSpeechStreamingResponse initWithFlatbuffData:root:];
-[QSSBeginTextToSpeechStreamingResponse initWithFlatbuffData:root:verify:];
-[QSSBeginTextToSpeechStreamingResponse meta_info];
-[QSSBeginTextToSpeechStreamingResponse playback_description];
-[QSSBeginTextToSpeechStreamingResponse session_id];
-[QSSBeginTextToSpeechStreamingResponse speech_id];
-[QSSBeginTextToSpeechStreamingResponse stream_id];
-[QSSBeginTextToSpeechStreamingResponse streaming_playback_buffer_size_in_seconds];
```
