# `QSSMutableTextToSpeechRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSTextToSpeechRequest`
- 0 instance variables, 19 properties, 40 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) speech_id;
@property (T@"NSString",C,N) session_id;
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
-[QSSMutableTextToSpeechRequest debug];
-[QSSMutableTextToSpeechRequest language];
-[QSSMutableTextToSpeechRequest text];
-[QSSMutableTextToSpeechRequest setDebug:];
-[QSSMutableTextToSpeechRequest init];
-[QSSMutableTextToSpeechRequest setProfile:];
-[QSSMutableTextToSpeechRequest experiment];
-[QSSMutableTextToSpeechRequest profile];
-[QSSMutableTextToSpeechRequest setContext:];
-[QSSMutableTextToSpeechRequest setExperiment:];
-[QSSMutableTextToSpeechRequest setGender:];
-[QSSMutableTextToSpeechRequest setText:];
-[QSSMutableTextToSpeechRequest copyWithZone:];
-[QSSMutableTextToSpeechRequest context];
-[QSSMutableTextToSpeechRequest gender];
-[QSSMutableTextToSpeechRequest setLanguage:];
-[QSSMutableTextToSpeechRequest audio_type];
-[QSSMutableTextToSpeechRequest context_info];
-[QSSMutableTextToSpeechRequest dev_config];
-[QSSMutableTextToSpeechRequest enable_word_timing_info];
-[QSSMutableTextToSpeechRequest feature_flags];
-[QSSMutableTextToSpeechRequest meta_info];
-[QSSMutableTextToSpeechRequest preferred_voice_type];
-[QSSMutableTextToSpeechRequest prosody_config];
-[QSSMutableTextToSpeechRequest prosody_control_config];
-[QSSMutableTextToSpeechRequest session_id];
-[QSSMutableTextToSpeechRequest setAudio_type:];
-[QSSMutableTextToSpeechRequest setContext_info:];
-[QSSMutableTextToSpeechRequest setDev_config:];
-[QSSMutableTextToSpeechRequest setEnable_word_timing_info:];
-[QSSMutableTextToSpeechRequest setFeature_flags:];
-[QSSMutableTextToSpeechRequest setMeta_info:];
-[QSSMutableTextToSpeechRequest setPreferred_voice_type:];
-[QSSMutableTextToSpeechRequest setProsody_config:];
-[QSSMutableTextToSpeechRequest setProsody_control_config:];
-[QSSMutableTextToSpeechRequest setSession_id:];
-[QSSMutableTextToSpeechRequest setSpeech_id:];
-[QSSMutableTextToSpeechRequest setVoice_name:];
-[QSSMutableTextToSpeechRequest speech_id];
-[QSSMutableTextToSpeechRequest voice_name];
```
