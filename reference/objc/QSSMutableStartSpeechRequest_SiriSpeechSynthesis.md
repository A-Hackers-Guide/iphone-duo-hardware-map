# `QSSMutableStartSpeechRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSStartSpeechRequest`
- 0 instance variables, 35 properties, 72 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) speech_id;
@property (T@"NSString",C,N) session_id;
@property (T@"NSString",C,N) language;
@property (T@"NSString",C,N) task_name;
@property (Tq,N) codec;
@property (TB,N) stream_results;
@property (TB,N) enable_server_side_endpoint;
@property (T@"NSString",C,N) device_type;
@property (T@"NSString",C,N) device_os;
@property (T@"NSString",C,N) mic_type;
@property (T@"NSString",C,N) udm_host;
@property (Ti,N) udm_port;
@property (TB,N) tandem_mode;
@property (TB,N) store_audio;
@property (TB,N) stream_unstable_results;
@property (T@"NSString",C,N) request_locale;
@property (Tq,N) end_point_mode;
@property (Ti,N) start_audio_bookmark;
@property (TB,N) is_far_field;
@property (TB,N) enable_utterance_detection;
@property (TB,N) enable_endpoint_candidate;
@property (TQ,N) start_recognition_at;
@property (TQ,N) start_endpointing_at;
@property (TB,N) enable_hybrid_endpoint;
@property (T@"NSString",C,N) client_endpointer_model_version;
@property (T@"NSString",C,N) keyboard_identifier;
@property (T@"NSString",C,N) input_origin;
@property (TI,N) initial_recognition_candidate_id;
@property (TB,N) disable_auto_punctuation;
@property (TB,N) keyboard_dictation;
@property (T@"NSString",C,N) experiment_id;
@property (Tq,N) speech_request_source;
@property (T@"NSString",C,N) fork_id;
@property (T@"NSString",C,N) application_name;
@property (T@"NSString",C,N) metadata;
```

## Instance methods

```
-[QSSMutableStartSpeechRequest language];
-[QSSMutableStartSpeechRequest codec];
-[QSSMutableStartSpeechRequest init];
-[QSSMutableStartSpeechRequest setDevice_type:];
-[QSSMutableStartSpeechRequest metadata];
-[QSSMutableStartSpeechRequest device_type];
-[QSSMutableStartSpeechRequest setMetadata:];
-[QSSMutableStartSpeechRequest setCodec:];
-[QSSMutableStartSpeechRequest copyWithZone:];
-[QSSMutableStartSpeechRequest setLanguage:];
-[QSSMutableStartSpeechRequest experiment_id];
-[QSSMutableStartSpeechRequest session_id];
-[QSSMutableStartSpeechRequest setSession_id:];
-[QSSMutableStartSpeechRequest setSpeech_id:];
-[QSSMutableStartSpeechRequest speech_id];
-[QSSMutableStartSpeechRequest client_endpointer_model_version];
-[QSSMutableStartSpeechRequest fork_id];
-[QSSMutableStartSpeechRequest setEnable_server_side_endpoint:];
-[QSSMutableStartSpeechRequest setStore_audio:];
-[QSSMutableStartSpeechRequest setTandem_mode:];
-[QSSMutableStartSpeechRequest application_name];
-[QSSMutableStartSpeechRequest device_os];
-[QSSMutableStartSpeechRequest disable_auto_punctuation];
-[QSSMutableStartSpeechRequest enable_endpoint_candidate];
-[QSSMutableStartSpeechRequest enable_hybrid_endpoint];
-[QSSMutableStartSpeechRequest enable_server_side_endpoint];
-[QSSMutableStartSpeechRequest enable_utterance_detection];
-[QSSMutableStartSpeechRequest end_point_mode];
-[QSSMutableStartSpeechRequest initial_recognition_candidate_id];
-[QSSMutableStartSpeechRequest input_origin];
-[QSSMutableStartSpeechRequest is_far_field];
-[QSSMutableStartSpeechRequest keyboard_dictation];
-[QSSMutableStartSpeechRequest keyboard_identifier];
-[QSSMutableStartSpeechRequest mic_type];
-[QSSMutableStartSpeechRequest request_locale];
-[QSSMutableStartSpeechRequest setApplication_name:];
-[QSSMutableStartSpeechRequest setClient_endpointer_model_version:];
-[QSSMutableStartSpeechRequest setDevice_os:];
-[QSSMutableStartSpeechRequest setDisable_auto_punctuation:];
-[QSSMutableStartSpeechRequest setEnable_endpoint_candidate:];
-[QSSMutableStartSpeechRequest setEnable_hybrid_endpoint:];
-[QSSMutableStartSpeechRequest setEnable_utterance_detection:];
-[QSSMutableStartSpeechRequest setEnd_point_mode:];
-[QSSMutableStartSpeechRequest setExperiment_id:];
-[QSSMutableStartSpeechRequest setFork_id:];
-[QSSMutableStartSpeechRequest setInitial_recognition_candidate_id:];
-[QSSMutableStartSpeechRequest setInput_origin:];
-[QSSMutableStartSpeechRequest setIs_far_field:];
-[QSSMutableStartSpeechRequest setKeyboard_dictation:];
-[QSSMutableStartSpeechRequest setKeyboard_identifier:];
-[QSSMutableStartSpeechRequest setMic_type:];
-[QSSMutableStartSpeechRequest setRequest_locale:];
-[QSSMutableStartSpeechRequest setSpeech_request_source:];
-[QSSMutableStartSpeechRequest setStart_audio_bookmark:];
-[QSSMutableStartSpeechRequest setStart_endpointing_at:];
-[QSSMutableStartSpeechRequest setStart_recognition_at:];
-[QSSMutableStartSpeechRequest setStream_results:];
-[QSSMutableStartSpeechRequest setStream_unstable_results:];
-[QSSMutableStartSpeechRequest setTask_name:];
-[QSSMutableStartSpeechRequest setUdm_host:];
-[QSSMutableStartSpeechRequest setUdm_port:];
-[QSSMutableStartSpeechRequest speech_request_source];
-[QSSMutableStartSpeechRequest start_audio_bookmark];
-[QSSMutableStartSpeechRequest start_endpointing_at];
-[QSSMutableStartSpeechRequest start_recognition_at];
-[QSSMutableStartSpeechRequest store_audio];
-[QSSMutableStartSpeechRequest stream_results];
-[QSSMutableStartSpeechRequest stream_unstable_results];
-[QSSMutableStartSpeechRequest tandem_mode];
-[QSSMutableStartSpeechRequest task_name];
-[QSSMutableStartSpeechRequest udm_host];
-[QSSMutableStartSpeechRequest udm_port];
```
