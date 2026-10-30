# `AVVCAudioBuffer`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 13 properties, 19 instance methods, 0 class methods

## Instance variables

```
^v _impl;
```

## Properties

```
@property (Ti,R) channels;
@property (Ti,R) bytesCapacity;
@property (Ti) bytesDataSize;
@property (T^v,R) data;
@property (Ti,R) packetDescriptionCapacity;
@property (Ti,R) packetDescriptionCount;
@property (T^{AudioStreamPacketDescription=qII},R) packetDescriptions;
@property (TQ,N) timeStamp;
@property (T^{AudioStreamBasicDescription=dIIIIIIII},R) streamDescription;
@property (TB,R) upsamplingSourceAudio;
@property (TB,R) remoteVoiceActivityAvailable;
@property (TC,R) remoteVoiceActivityRMS;
@property (TC,R) remoteVoiceActivityVAD;
```

## Instance methods

```
-[AVVCAudioBuffer finalize];
-[AVVCAudioBuffer channels];
-[AVVCAudioBuffer data];
-[AVVCAudioBuffer dealloc];
-[AVVCAudioBuffer streamDescription];
-[AVVCAudioBuffer setTimeStamp:];
-[AVVCAudioBuffer timeStamp];
-[AVVCAudioBuffer bytesDataSize];
-[AVVCAudioBuffer packetDescriptionCount];
-[AVVCAudioBuffer packetDescriptions];
-[AVVCAudioBuffer bytesCapacity];
-[AVVCAudioBuffer initWithAudioQueueBuffer:channels:timeStamp:];
-[AVVCAudioBuffer packetDescriptionCapacity];
-[AVVCAudioBuffer remoteVoiceActivityAvailable];
-[AVVCAudioBuffer remoteVoiceActivityRMS];
-[AVVCAudioBuffer remoteVoiceActivityVAD];
-[AVVCAudioBuffer setBytesDataSize:];
-[AVVCAudioBuffer setPacketDescriptions:count:];
-[AVVCAudioBuffer upsamplingSourceAudio];
```
