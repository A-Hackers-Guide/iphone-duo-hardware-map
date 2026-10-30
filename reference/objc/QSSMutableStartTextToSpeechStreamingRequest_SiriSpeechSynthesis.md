# `QSSMutableStartTextToSpeechStreamingRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSStartTextToSpeechStreamingRequest`
- 0 instance variables, 20 properties, 42 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) speech_id;
@property (T@"NSString",C,N) session_id;
@property (T@"NSString",C,N) stream_id;
@property (T@"NSString",C,N) language;
@property (T@"NSString",C,N) gender;
@property (T@"NSString",C,N) text;
@property (Tq,N) audio_type;
@property (TB,N) enable_word_timing_info;
@property (T@"NSString",C,N) voice_name;
@property (T@"NSArray",C,N) context_info;
@property (Tq,N) preferred_voice_type;
@property (T@"QSSTextToSpeechRequestMeta",C,N) meta_info;
@property (T@"QSSTextToSpeechRequestContext",C,N) context;
@property (T@"QSSTextToSpeechRequestExperiment",C,N) experiment;
@property (T@"QSSTTSRequestFeatureFlags",C,N) feature_flags;
@property (T@"QSSTextToSpeechRequestDebug",C,N) debug;
@property (T@"QSSTextToSpeechUserProfile",C,N) profile;
@property (T@"QSSTextToSpeechRequestDevConfig",C,N) dev_config;
@property (T@"QSSTextToSpeechRequestProsodyTransferConfig",C,N) prosody_config;
@property (T@"QSSTextToSpeechRequestProsodyControlConfig",C,N) prosody_control_config;
```

## Instance methods

```
-[QSSMutableStartTextToSpeechStreamingRequest debug];
-[QSSMutableStartTextToSpeechStreamingRequest language];
-[QSSMutableStartTextToSpeechStreamingRequest text];
-[QSSMutableStartTextToSpeechStreamingRequest setDebug:];
-[QSSMutableStartTextToSpeechStreamingRequest init];
-[QSSMutableStartTextToSpeechStreamingRequest setProfile:];
-[QSSMutableStartTextToSpeechStreamingRequest experiment];
-[QSSMutableStartTextToSpeechStreamingRequest profile];
-[QSSMutableStartTextToSpeechStreamingRequest setContext:];
-[QSSMutableStartTextToSpeechStreamingRequest setExperiment:];
-[QSSMutableStartTextToSpeechStreamingRequest setGender:];
-[QSSMutableStartTextToSpeechStreamingRequest setText:];
-[QSSMutableStartTextToSpeechStreamingRequest copyWithZone:];
-[QSSMutableStartTextToSpeechStreamingRequest context];
-[QSSMutableStartTextToSpeechStreamingRequest gender];
-[QSSMutableStartTextToSpeechStreamingRequest setLanguage:];
-[QSSMutableStartTextToSpeechStreamingRequest audio_type];
-[QSSMutableStartTextToSpeechStreamingRequest context_info];
-[QSSMutableStartTextToSpeechStreamingRequest dev_config];
-[QSSMutableStartTextToSpeechStreamingRequest enable_word_timing_info];
-[QSSMutableStartTextToSpeechStreamingRequest feature_flags];
-[QSSMutableStartTextToSpeechStreamingRequest meta_info];
-[QSSMutableStartTextToSpeechStreamingRequest preferred_voice_type];
-[QSSMutableStartTextToSpeechStreamingRequest prosody_config];
-[QSSMutableStartTextToSpeechStreamingRequest prosody_control_config];
-[QSSMutableStartTextToSpeechStreamingRequest session_id];
-[QSSMutableStartTextToSpeechStreamingRequest setAudio_type:];
-[QSSMutableStartTextToSpeechStreamingRequest setContext_info:];
-[QSSMutableStartTextToSpeechStreamingRequest setDev_config:];
-[QSSMutableStartTextToSpeechStreamingRequest setEnable_word_timing_info:];
-[QSSMutableStartTextToSpeechStreamingRequest setFeature_flags:];
-[QSSMutableStartTextToSpeechStreamingRequest setMeta_info:];
-[QSSMutableStartTextToSpeechStreamingRequest setPreferred_voice_type:];
-[QSSMutableStartTextToSpeechStreamingRequest setProsody_config:];
-[QSSMutableStartTextToSpeechStreamingRequest setProsody_control_config:];
-[QSSMutableStartTextToSpeechStreamingRequest setSession_id:];
-[QSSMutableStartTextToSpeechStreamingRequest setSpeech_id:];
-[QSSMutableStartTextToSpeechStreamingRequest setStream_id:];
-[QSSMutableStartTextToSpeechStreamingRequest setVoice_name:];
-[QSSMutableStartTextToSpeechStreamingRequest speech_id];
-[QSSMutableStartTextToSpeechStreamingRequest stream_id];
-[QSSMutableStartTextToSpeechStreamingRequest voice_name];
```
