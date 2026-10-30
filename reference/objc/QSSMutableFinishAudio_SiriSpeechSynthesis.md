# `QSSMutableFinishAudio`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSFinishAudio`
- 0 instance variables, 4 properties, 10 instance methods, 0 class methods

## Properties

```
@property (Ti,N) packet_count;
@property (Tf,N) total_audio_recorded_seconds;
@property (T@"NSArray",C,N) features_at_endpoint;
@property (T@"NSArray",C,N) server_feature_latency_distribution;
```

## Instance methods

```
-[QSSMutableFinishAudio init];
-[QSSMutableFinishAudio copyWithZone:];
-[QSSMutableFinishAudio features_at_endpoint];
-[QSSMutableFinishAudio packet_count];
-[QSSMutableFinishAudio server_feature_latency_distribution];
-[QSSMutableFinishAudio setFeatures_at_endpoint:];
-[QSSMutableFinishAudio setPacket_count:];
-[QSSMutableFinishAudio setServer_feature_latency_distribution:];
-[QSSMutableFinishAudio setTotal_audio_recorded_seconds:];
-[QSSMutableFinishAudio total_audio_recorded_seconds];
```
