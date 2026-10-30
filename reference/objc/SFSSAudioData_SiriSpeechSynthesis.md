# `SFSSAudioData`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSData" _audioData;
q _packetCount;
@"NSData" _packetDescriptions;
{AudioStreamBasicDescription="mSampleRate"d"mFormatID"I"mFormatFlags"I"mBytesPerPacket"I"mFramesPerPacket"I"mBytesPerFrame"I"mChannelsPerFrame"I"mBitsPerChannel"I"mReserved"I} _asbd;
```

## Properties

```
@property (T@"NSData",&,N,V_audioData) audioData;
@property (T{AudioStreamBasicDescription=dIIIIIIII},N,V_asbd) asbd;
@property (Tq,N,V_packetCount) packetCount;
@property (T@"NSData",&,N,V_packetDescriptions) packetDescriptions;
```

## Instance methods

```
-[SFSSAudioData duration];
-[SFSSAudioData packetDescriptions];
-[SFSSAudioData setPacketCount:];
-[SFSSAudioData packetCount];
-[SFSSAudioData setPacketDescriptions:];
-[SFSSAudioData asbd];
-[SFSSAudioData audioData];
-[SFSSAudioData setAsbd:];
-[SFSSAudioData setAudioData:];
-[SFSSAudioData initWithASBD:rawData:];
-[SFSSAudioData populateWithOpusData:];
-[SFSSAudioData populateWithPCMData:];
```
