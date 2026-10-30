# `QSSTextToSpeechRequestProsodyControlConfig`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechRequestProsodyControlConfig=[1C]} _root;
```

## Properties

```
@property (Tf,R,N) global_rate;
@property (Tf,R,N) global_pitch;
@property (Tf,R,N) global_energy;
@property (Tf,R,N) global_sent_pitch;
@property (Tf,R,N) global_sent_pitchrange;
@property (Tf,R,N) global_sent_duration;
@property (Tf,R,N) global_sent_energy;
@property (Tf,R,N) global_sent_tilt;
```

## Instance methods

```
-[QSSTextToSpeechRequestProsodyControlConfig copyWithZone:];
-[QSSTextToSpeechRequestProsodyControlConfig addObjectToBuffer:];
-[QSSTextToSpeechRequestProsodyControlConfig flatbuffData];
-[QSSTextToSpeechRequestProsodyControlConfig global_energy];
-[QSSTextToSpeechRequestProsodyControlConfig global_pitch];
-[QSSTextToSpeechRequestProsodyControlConfig global_rate];
-[QSSTextToSpeechRequestProsodyControlConfig global_sent_duration];
-[QSSTextToSpeechRequestProsodyControlConfig global_sent_energy];
-[QSSTextToSpeechRequestProsodyControlConfig global_sent_pitch];
-[QSSTextToSpeechRequestProsodyControlConfig global_sent_pitchrange];
-[QSSTextToSpeechRequestProsodyControlConfig global_sent_tilt];
-[QSSTextToSpeechRequestProsodyControlConfig initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechRequestProsodyControlConfig initWithFlatbuffData:];
-[QSSTextToSpeechRequestProsodyControlConfig initWithFlatbuffData:root:];
-[QSSTextToSpeechRequestProsodyControlConfig initWithFlatbuffData:root:verify:];
```
