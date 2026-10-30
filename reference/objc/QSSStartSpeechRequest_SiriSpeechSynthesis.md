# `QSSStartSpeechRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 35 properties, 42 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{StartSpeechRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (T@"NSString",R,N) language;
@property (T@"NSString",R,N) task_name;
@property (Tq,R,N) codec;
@property (TB,R,N) stream_results;
@property (TB,R,N) enable_server_side_endpoint;
@property (T@"NSString",R,N) device_type;
@property (T@"NSString",R,N) device_os;
@property (T@"NSString",R,N) mic_type;
@property (T@"NSString",R,N) udm_host;
@property (Ti,R,N) udm_port;
@property (TB,R,N) tandem_mode;
@property (TB,R,N) store_audio;
@property (TB,R,N) stream_unstable_results;
@property (T@"NSString",R,N) request_locale;
@property (Tq,R,N) end_point_mode;
@property (Ti,R,N) start_audio_bookmark;
@property (TB,R,N) is_far_field;
@property (TB,R,N) enable_utterance_detection;
@property (TB,R,N) enable_endpoint_candidate;
@property (TQ,R,N) start_recognition_at;
@property (TQ,R,N) start_endpointing_at;
@property (TB,R,N) enable_hybrid_endpoint;
@property (T@"NSString",R,N) client_endpointer_model_version;
@property (T@"NSString",R,N) keyboard_identifier;
@property (T@"NSString",R,N) input_origin;
@property (TI,R,N) initial_recognition_candidate_id;
@property (TB,R,N) disable_auto_punctuation;
@property (TB,R,N) keyboard_dictation;
@property (T@"NSString",R,N) experiment_id;
@property (Tq,R,N) speech_request_source;
@property (T@"NSString",R,N) fork_id;
@property (T@"NSString",R,N) application_name;
@property (T@"NSString",R,N) metadata;
```

## Instance methods

```
-[QSSStartSpeechRequest language];
-[QSSStartSpeechRequest codec];
-[QSSStartSpeechRequest metadata];
-[QSSStartSpeechRequest device_type];
-[QSSStartSpeechRequest copyWithZone:];
-[QSSStartSpeechRequest experiment_id];
-[QSSStartSpeechRequest addObjectToBuffer:];
-[QSSStartSpeechRequest flatbuffData];
-[QSSStartSpeechRequest initAndVerifyWithFlatbuffData:];
-[QSSStartSpeechRequest initWithFlatbuffData:];
-[QSSStartSpeechRequest initWithFlatbuffData:root:];
-[QSSStartSpeechRequest initWithFlatbuffData:root:verify:];
-[QSSStartSpeechRequest session_id];
-[QSSStartSpeechRequest speech_id];
-[QSSStartSpeechRequest client_endpointer_model_version];
-[QSSStartSpeechRequest fork_id];
-[QSSStartSpeechRequest application_name];
-[QSSStartSpeechRequest device_os];
-[QSSStartSpeechRequest disable_auto_punctuation];
-[QSSStartSpeechRequest enable_endpoint_candidate];
-[QSSStartSpeechRequest enable_hybrid_endpoint];
-[QSSStartSpeechRequest enable_server_side_endpoint];
-[QSSStartSpeechRequest enable_utterance_detection];
-[QSSStartSpeechRequest end_point_mode];
-[QSSStartSpeechRequest initial_recognition_candidate_id];
-[QSSStartSpeechRequest input_origin];
-[QSSStartSpeechRequest is_far_field];
-[QSSStartSpeechRequest keyboard_dictation];
-[QSSStartSpeechRequest keyboard_identifier];
-[QSSStartSpeechRequest mic_type];
-[QSSStartSpeechRequest request_locale];
-[QSSStartSpeechRequest speech_request_source];
-[QSSStartSpeechRequest start_audio_bookmark];
-[QSSStartSpeechRequest start_endpointing_at];
-[QSSStartSpeechRequest start_recognition_at];
-[QSSStartSpeechRequest store_audio];
-[QSSStartSpeechRequest stream_results];
-[QSSStartSpeechRequest stream_unstable_results];
-[QSSStartSpeechRequest tandem_mode];
-[QSSStartSpeechRequest task_name];
-[QSSStartSpeechRequest udm_host];
-[QSSStartSpeechRequest udm_port];
```
