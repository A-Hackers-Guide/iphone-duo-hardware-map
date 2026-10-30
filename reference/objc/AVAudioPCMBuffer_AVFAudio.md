# `AVAudioPCMBuffer`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAudioBuffer`
- 0 instance variables, 8 properties, 20 instance methods, 0 class methods

## Properties

```
@property (T@"NSArray",R,N) peakPowerPerChannel;
@property (T@"NSArray",R,N) averagePowerPerChannel;
@property (TI,R,N) frameCapacity;
@property (TI,N) frameLength;
@property (TQ,R,N) stride;
@property (T^^f,R,N) floatChannelData;
@property (T^^s,R,N) int16ChannelData;
@property (T^^i,R,N) int32ChannelData;
```

## Instance methods

```
-[AVAudioPCMBuffer mutableCopyWithZone:];
-[AVAudioPCMBuffer stride];
-[AVAudioPCMBuffer copyWithZone:];
-[AVAudioPCMBuffer frameLength];
-[AVAudioPCMBuffer setFrameLength:];
-[AVAudioPCMBuffer floatChannelData];
-[AVAudioPCMBuffer frameCapacity];
-[AVAudioPCMBuffer initWithPCMFormat:bufferListNoCopy:deallocator:];
-[AVAudioPCMBuffer initWithPCMFormat:frameCapacity:];
-[AVAudioPCMBuffer int16ChannelData];
-[AVAudioPCMBuffer int32ChannelData];
-[AVAudioPCMBuffer setByteLength:];
-[AVAudioPCMBuffer calculatePower:];
-[AVAudioPCMBuffer _initChannelPtrs];
-[AVAudioPCMBuffer appendDataFromBuffer:];
-[AVAudioPCMBuffer appendDataFromBuffer:channel:];
-[AVAudioPCMBuffer averagePowerPerChannel];
-[AVAudioPCMBuffer calculatePower:forFloatData:stride:frameLength:];
-[AVAudioPCMBuffer peakPowerPerChannel];
-[AVAudioPCMBuffer splitIntoSingleChannelBuffers];
```
