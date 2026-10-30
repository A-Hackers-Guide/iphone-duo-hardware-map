# `Endpointer` (protocol)

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 12 instance methods, 0 class methods

## Properties

```
@property (Ti) endpointMode;
@property (Td) startWaitTime;
@property (Td) interspeechWaitTime;
@property (Td) endWaitTime;
```

## Instance methods

```
-[Endpointer reset];
-[Endpointer setEndWaitTime:];
-[Endpointer endWaitTime];
-[Endpointer endpointMode];
-[Endpointer getStatus:];
-[Endpointer interspeechWaitTime];
-[Endpointer setEndpointMode:];
-[Endpointer setInterspeechWaitTime:];
-[Endpointer setStartWaitTime:];
-[Endpointer startWaitTime];
-[Endpointer configureWithASBD:andFrameRate:];
-[Endpointer configureWithSampleRate:andFrameRate:];
```
