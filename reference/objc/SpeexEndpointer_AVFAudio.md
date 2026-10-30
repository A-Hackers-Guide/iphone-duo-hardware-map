# `SpeexEndpointer`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `Endpointer`
- 7 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
d mStartWaitTime;
d mInterspeechWaitTime;
d mEndWaitTime;
i mEndpointMode;
I mFrameRate;
i mLastStatus;
^{Impl=^v^{Averager}} _impl;
```

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
-[SpeexEndpointer init];
-[SpeexEndpointer dealloc];
-[SpeexEndpointer reset];
-[SpeexEndpointer setEndWaitTime:];
-[SpeexEndpointer configureWithASBD:andFrameRate:];
-[SpeexEndpointer configureWithSampleRate:andFrameRate:];
-[SpeexEndpointer endWaitTime];
-[SpeexEndpointer endpointMode];
-[SpeexEndpointer getStatus:];
-[SpeexEndpointer getStatus:count:];
-[SpeexEndpointer interspeechWaitTime];
-[SpeexEndpointer setEndpointMode:];
-[SpeexEndpointer setInterspeechWaitTime:];
-[SpeexEndpointer setStartWaitTime:];
-[SpeexEndpointer startWaitTime];
```
