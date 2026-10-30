# `QSSTextToSpeechRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 19 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (T@"NSString",R,N) language;
@property (T@"NSString",R,N) gender;
@property (T@"NSString",R,N) text;
@property (Tq,R,N) audio_type;
@property (TB,R,N) enable_word_timing_info;
@property (T@"NSString",R,N) voice_name;
@property (T@"NSArray",R,N) context_info;
@property (Tq,R,N) preferred_voice_type;
@property (T@"QSSTextToSpeechRequestMeta",R,N) meta_info;
@property (T@"QSSTextToSpeechRequestContext",R,N) context;
@property (T@"QSSTextToSpeechRequestExperiment",R,N) experiment;
@property (T@"QSSTTSRequestFeatureFlags",R,N) feature_flags;
@property (T@"QSSTextToSpeechRequestDebug",R,N) debug;
@property (T@"QSSTextToSpeechUserProfile",R,N) profile;
@property (T@"QSSTextToSpeechRequestDevConfig",R,N) dev_config;
@property (T@"QSSTextToSpeechRequestProsodyTransferConfig",R,N) prosody_config;
@property (T@"QSSTextToSpeechRequestProsodyControlConfig",R,N) prosody_control_config;
```

## Instance methods

```
-[QSSTextToSpeechRequest debug];
-[QSSTextToSpeechRequest language];
-[QSSTextToSpeechRequest text];
-[QSSTextToSpeechRequest experiment];
-[QSSTextToSpeechRequest profile];
-[QSSTextToSpeechRequest copyWithZone:];
-[QSSTextToSpeechRequest context];
-[QSSTextToSpeechRequest gender];
-[QSSTextToSpeechRequest addObjectToBuffer:];
-[QSSTextToSpeechRequest audio_type];
-[QSSTextToSpeechRequest context_info];
-[QSSTextToSpeechRequest dev_config];
-[QSSTextToSpeechRequest enable_word_timing_info];
-[QSSTextToSpeechRequest feature_flags];
-[QSSTextToSpeechRequest flatbuffData];
-[QSSTextToSpeechRequest initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechRequest initWithFlatbuffData:];
-[QSSTextToSpeechRequest initWithFlatbuffData:root:];
-[QSSTextToSpeechRequest initWithFlatbuffData:root:verify:];
-[QSSTextToSpeechRequest meta_info];
-[QSSTextToSpeechRequest preferred_voice_type];
-[QSSTextToSpeechRequest prosody_config];
-[QSSTextToSpeechRequest prosody_control_config];
-[QSSTextToSpeechRequest session_id];
-[QSSTextToSpeechRequest speech_id];
-[QSSTextToSpeechRequest voice_name];
```
