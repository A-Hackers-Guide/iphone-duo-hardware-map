# `QSSAudioDescription`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 9 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{AudioDescription=[1C]} _root;
```

## Properties

```
@property (Td,R,N) sample_rate;
@property (TI,R,N) format_id;
@property (TI,R,N) format_flags;
@property (TI,R,N) bytes_per_packet;
@property (TI,R,N) frames_per_packet;
@property (TI,R,N) bytes_per_frame;
@property (TI,R,N) channels_per_frame;
@property (TI,R,N) bits_per_channel;
@property (TI,R,N) reserved;
```

## Instance methods

```
-[QSSAudioDescription reserved];
-[QSSAudioDescription copyWithZone:];
-[QSSAudioDescription bytes_per_frame];
-[QSSAudioDescription addObjectToBuffer:];
-[QSSAudioDescription bits_per_channel];
-[QSSAudioDescription bytes_per_packet];
-[QSSAudioDescription channels_per_frame];
-[QSSAudioDescription flatbuffData];
-[QSSAudioDescription format_flags];
-[QSSAudioDescription format_id];
-[QSSAudioDescription frames_per_packet];
-[QSSAudioDescription initAndVerifyWithFlatbuffData:];
-[QSSAudioDescription initWithFlatbuffData:];
-[QSSAudioDescription initWithFlatbuffData:root:];
-[QSSAudioDescription initWithFlatbuffData:root:verify:];
-[QSSAudioDescription sample_rate];
```
