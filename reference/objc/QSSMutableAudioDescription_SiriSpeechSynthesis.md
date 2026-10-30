# `QSSMutableAudioDescription`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSAudioDescription`
- 0 instance variables, 9 properties, 20 instance methods, 0 class methods

## Properties

```
@property (Td,N) sample_rate;
@property (TI,N) format_id;
@property (TI,N) format_flags;
@property (TI,N) bytes_per_packet;
@property (TI,N) frames_per_packet;
@property (TI,N) bytes_per_frame;
@property (TI,N) channels_per_frame;
@property (TI,N) bits_per_channel;
@property (TI,N) reserved;
```

## Instance methods

```
-[QSSMutableAudioDescription init];
-[QSSMutableAudioDescription reserved];
-[QSSMutableAudioDescription copyWithZone:];
-[QSSMutableAudioDescription setReserved:];
-[QSSMutableAudioDescription bytes_per_frame];
-[QSSMutableAudioDescription setSample_rate:];
-[QSSMutableAudioDescription bits_per_channel];
-[QSSMutableAudioDescription bytes_per_packet];
-[QSSMutableAudioDescription channels_per_frame];
-[QSSMutableAudioDescription format_flags];
-[QSSMutableAudioDescription format_id];
-[QSSMutableAudioDescription frames_per_packet];
-[QSSMutableAudioDescription sample_rate];
-[QSSMutableAudioDescription setBits_per_channel:];
-[QSSMutableAudioDescription setBytes_per_frame:];
-[QSSMutableAudioDescription setBytes_per_packet:];
-[QSSMutableAudioDescription setChannels_per_frame:];
-[QSSMutableAudioDescription setFormat_flags:];
-[QSSMutableAudioDescription setFormat_id:];
-[QSSMutableAudioDescription setFrames_per_packet:];
```
