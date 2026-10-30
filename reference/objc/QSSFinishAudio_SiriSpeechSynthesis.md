# `QSSFinishAudio`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{FinishAudio=[1C]} _root;
```

## Properties

```
@property (Ti,R,N) packet_count;
@property (Tf,R,N) total_audio_recorded_seconds;
@property (T@"NSArray",R,N) features_at_endpoint;
@property (T@"NSArray",R,N) server_feature_latency_distribution;
```

## Instance methods

```
-[QSSFinishAudio copyWithZone:];
-[QSSFinishAudio addObjectToBuffer:];
-[QSSFinishAudio flatbuffData];
-[QSSFinishAudio initAndVerifyWithFlatbuffData:];
-[QSSFinishAudio initWithFlatbuffData:];
-[QSSFinishAudio initWithFlatbuffData:root:];
-[QSSFinishAudio initWithFlatbuffData:root:verify:];
-[QSSFinishAudio features_at_endpoint];
-[QSSFinishAudio packet_count];
-[QSSFinishAudio server_feature_latency_distribution];
-[QSSFinishAudio total_audio_recorded_seconds];
```
