# `QSSMutableTextToSpeechResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSTextToSpeechResponse`
- 0 instance variables, 13 properties, 29 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) speech_id;
@property (T@"NSString",C,N) session_id;
@property (Ti,N) error_code;
@property (T@"NSString",C,N) error_str;
@property (Tq,N) audio_type;
@property (Ti,N) sample_rate;
@property (T@"NSData",C,N) audio;
@property (T@"QSSAudioDescription",C,N) decoder_description;
@property (T@"QSSAudioDescription",C,N) playback_description;
@property (T@"NSArray",C,N) word_timing_info;
@property (T@"QSSTextToSpeechMeta",C,N) meta_info;
@property (T@"QSSTextToSpeechFeature",C,N) feature;
@property (T@"QSSTextToSpeechResponseDevData",C,N) dev_data;
```

## Instance methods

```
-[QSSMutableTextToSpeechResponse feature];
-[QSSMutableTextToSpeechResponse setAudio:];
-[QSSMutableTextToSpeechResponse init];
-[QSSMutableTextToSpeechResponse audio];
-[QSSMutableTextToSpeechResponse copyWithZone:];
-[QSSMutableTextToSpeechResponse setFeature:];
-[QSSMutableTextToSpeechResponse setSample_rate:];
-[QSSMutableTextToSpeechResponse audio:];
-[QSSMutableTextToSpeechResponse audio_type];
-[QSSMutableTextToSpeechResponse decoder_description];
-[QSSMutableTextToSpeechResponse error_code];
-[QSSMutableTextToSpeechResponse error_str];
-[QSSMutableTextToSpeechResponse meta_info];
-[QSSMutableTextToSpeechResponse playback_description];
-[QSSMutableTextToSpeechResponse sample_rate];
-[QSSMutableTextToSpeechResponse session_id];
-[QSSMutableTextToSpeechResponse setAudio_type:];
-[QSSMutableTextToSpeechResponse setDecoder_description:];
-[QSSMutableTextToSpeechResponse setError_code:];
-[QSSMutableTextToSpeechResponse setError_str:];
-[QSSMutableTextToSpeechResponse setMeta_info:];
-[QSSMutableTextToSpeechResponse setPlayback_description:];
-[QSSMutableTextToSpeechResponse setSession_id:];
-[QSSMutableTextToSpeechResponse setSpeech_id:];
-[QSSMutableTextToSpeechResponse setWord_timing_info:];
-[QSSMutableTextToSpeechResponse speech_id];
-[QSSMutableTextToSpeechResponse word_timing_info];
-[QSSMutableTextToSpeechResponse dev_data];
-[QSSMutableTextToSpeechResponse setDev_data:];
```
