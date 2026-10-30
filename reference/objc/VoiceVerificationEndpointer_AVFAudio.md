# `VoiceVerificationEndpointer`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `Endpointer`
- 0 instance variables, 8 properties, 14 instance methods, 0 class methods

## Properties

```
@property (Ti) endpointMode;
@property (Td) startWaitTime;
@property (Td) interspeechWaitTime;
@property (Td) endWaitTime;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[VoiceVerificationEndpointer init];
-[VoiceVerificationEndpointer dealloc];
-[VoiceVerificationEndpointer reset];
-[VoiceVerificationEndpointer setEndWaitTime:];
-[VoiceVerificationEndpointer configureWithASBD:andFrameRate:];
-[VoiceVerificationEndpointer configureWithSampleRate:andFrameRate:];
-[VoiceVerificationEndpointer endWaitTime];
-[VoiceVerificationEndpointer endpointMode];
-[VoiceVerificationEndpointer getStatus:];
-[VoiceVerificationEndpointer interspeechWaitTime];
-[VoiceVerificationEndpointer setEndpointMode:];
-[VoiceVerificationEndpointer setInterspeechWaitTime:];
-[VoiceVerificationEndpointer setStartWaitTime:];
-[VoiceVerificationEndpointer startWaitTime];
```
