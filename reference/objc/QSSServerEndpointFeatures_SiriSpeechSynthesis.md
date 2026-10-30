# `QSSServerEndpointFeatures`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{ServerEndpointFeatures=[1C]} _root;
```

## Properties

```
@property (Ti,R,N) processed_audio_duration_ms;
@property (Ti,R,N) num_of_words;
@property (Ti,R,N) trailing_silence_duration;
@property (Td,R,N) eos_likelihood;
@property (T@"NSArray",R,N) pause_counts;
@property (Td,R,N) silence_posterior;
@property (T@"NSString",R,N) task_name;
@property (T@"NSString",R,N) speech_id;
```

## Instance methods

```
-[QSSServerEndpointFeatures copyWithZone:];
-[QSSServerEndpointFeatures addObjectToBuffer:];
-[QSSServerEndpointFeatures flatbuffData];
-[QSSServerEndpointFeatures initAndVerifyWithFlatbuffData:];
-[QSSServerEndpointFeatures initWithFlatbuffData:];
-[QSSServerEndpointFeatures initWithFlatbuffData:root:];
-[QSSServerEndpointFeatures initWithFlatbuffData:root:verify:];
-[QSSServerEndpointFeatures speech_id];
-[QSSServerEndpointFeatures eos_likelihood];
-[QSSServerEndpointFeatures num_of_words];
-[QSSServerEndpointFeatures pause_counts];
-[QSSServerEndpointFeatures processed_audio_duration_ms];
-[QSSServerEndpointFeatures silence_posterior];
-[QSSServerEndpointFeatures task_name];
-[QSSServerEndpointFeatures trailing_silence_duration];
```
