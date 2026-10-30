# `AVVCPrepareRecordSettings`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _meteringEnabled;
I _deviceBufferFrameSize;
Q _streamID;
@"NSDictionary" _avAudioSettings;
d _recordBufferDuration;
```

## Properties

```
@property (TQ,N,V_streamID) streamID;
@property (T@"NSDictionary",&,N,V_avAudioSettings) avAudioSettings;
@property (Td,N,V_recordBufferDuration) recordBufferDuration;
@property (TB,N,V_meteringEnabled) meteringEnabled;
@property (TI,N,V_deviceBufferFrameSize) deviceBufferFrameSize;
```

## Instance methods

```
-[AVVCPrepareRecordSettings setMeteringEnabled:];
-[AVVCPrepareRecordSettings setRecordBufferDuration:];
-[AVVCPrepareRecordSettings streamID];
-[AVVCPrepareRecordSettings initWithStreamID:settings:bufferDuration:];
-[AVVCPrepareRecordSettings setStreamID:];
-[AVVCPrepareRecordSettings avAudioSettings];
-[AVVCPrepareRecordSettings meteringEnabled];
-[AVVCPrepareRecordSettings deviceBufferFrameSize];
-[AVVCPrepareRecordSettings recordBufferDuration];
-[AVVCPrepareRecordSettings setAvAudioSettings:];
-[AVVCPrepareRecordSettings setDeviceBufferFrameSize:];
```
