# `QSSMutableServerEndpointFeatures`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSServerEndpointFeatures`
- 0 instance variables, 8 properties, 18 instance methods, 0 class methods

## Properties

```
@property (Ti,N) processed_audio_duration_ms;
@property (Ti,N) num_of_words;
@property (Ti,N) trailing_silence_duration;
@property (Td,N) eos_likelihood;
@property (T@"NSArray",C,N) pause_counts;
@property (Td,N) silence_posterior;
@property (T@"NSString",C,N) task_name;
@property (T@"NSString",C,N) speech_id;
```

## Instance methods

```
-[QSSMutableServerEndpointFeatures init];
-[QSSMutableServerEndpointFeatures copyWithZone:];
-[QSSMutableServerEndpointFeatures setSpeech_id:];
-[QSSMutableServerEndpointFeatures speech_id];
-[QSSMutableServerEndpointFeatures setProcessed_audio_duration_ms:];
-[QSSMutableServerEndpointFeatures eos_likelihood];
-[QSSMutableServerEndpointFeatures num_of_words];
-[QSSMutableServerEndpointFeatures pause_counts];
-[QSSMutableServerEndpointFeatures processed_audio_duration_ms];
-[QSSMutableServerEndpointFeatures setEos_likelihood:];
-[QSSMutableServerEndpointFeatures setNum_of_words:];
-[QSSMutableServerEndpointFeatures setPause_counts:];
-[QSSMutableServerEndpointFeatures setSilence_posterior:];
-[QSSMutableServerEndpointFeatures setTask_name:];
-[QSSMutableServerEndpointFeatures setTrailing_silence_duration:];
-[QSSMutableServerEndpointFeatures silence_posterior];
-[QSSMutableServerEndpointFeatures task_name];
-[QSSMutableServerEndpointFeatures trailing_silence_duration];
```
