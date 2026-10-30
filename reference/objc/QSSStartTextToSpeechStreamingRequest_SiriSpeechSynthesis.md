# `QSSStartTextToSpeechStreamingRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 20 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{StartTextToSpeechStreamingRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (T@"NSString",R,N) stream_id;
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
-[QSSStartTextToSpeechStreamingRequest debug];
-[QSSStartTextToSpeechStreamingRequest language];
-[QSSStartTextToSpeechStreamingRequest text];
-[QSSStartTextToSpeechStreamingRequest experiment];
-[QSSStartTextToSpeechStreamingRequest profile];
-[QSSStartTextToSpeechStreamingRequest copyWithZone:];
-[QSSStartTextToSpeechStreamingRequest context];
-[QSSStartTextToSpeechStreamingRequest gender];
-[QSSStartTextToSpeechStreamingRequest addObjectToBuffer:];
-[QSSStartTextToSpeechStreamingRequest audio_type];
-[QSSStartTextToSpeechStreamingRequest context_info];
-[QSSStartTextToSpeechStreamingRequest dev_config];
-[QSSStartTextToSpeechStreamingRequest enable_word_timing_info];
-[QSSStartTextToSpeechStreamingRequest feature_flags];
-[QSSStartTextToSpeechStreamingRequest flatbuffData];
-[QSSStartTextToSpeechStreamingRequest initAndVerifyWithFlatbuffData:];
-[QSSStartTextToSpeechStreamingRequest initWithFlatbuffData:];
-[QSSStartTextToSpeechStreamingRequest initWithFlatbuffData:root:];
-[QSSStartTextToSpeechStreamingRequest initWithFlatbuffData:root:verify:];
-[QSSStartTextToSpeechStreamingRequest meta_info];
-[QSSStartTextToSpeechStreamingRequest preferred_voice_type];
-[QSSStartTextToSpeechStreamingRequest prosody_config];
-[QSSStartTextToSpeechStreamingRequest prosody_control_config];
-[QSSStartTextToSpeechStreamingRequest session_id];
-[QSSStartTextToSpeechStreamingRequest speech_id];
-[QSSStartTextToSpeechStreamingRequest stream_id];
-[QSSStartTextToSpeechStreamingRequest voice_name];
```
