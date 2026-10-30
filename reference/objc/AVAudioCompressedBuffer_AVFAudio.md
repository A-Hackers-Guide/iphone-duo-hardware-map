# `AVAudioCompressedBuffer`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAudioBuffer`
- 0 instance variables, 8 properties, 9 instance methods, 0 class methods

## Properties

```
@property (TI,R,N) packetCapacity;
@property (TI,N) packetCount;
@property (Tq,R,N) maximumPacketSize;
@property (T^v,R,N) data;
@property (TI,R,D,N) byteCapacity;
@property (TI,D,N) byteLength;
@property (T^{AudioStreamPacketDescription=qII},R,N) packetDescriptions;
@property (T^{AudioStreamPacketDependencyDescription=IIII},R,N) packetDependencies;
```

## Instance methods

```
-[AVAudioCompressedBuffer data];
-[AVAudioCompressedBuffer packetDescriptions];
-[AVAudioCompressedBuffer setPacketCount:];
-[AVAudioCompressedBuffer initWithFormat:packetCapacity:maximumPacketSize:];
-[AVAudioCompressedBuffer maximumPacketSize];
-[AVAudioCompressedBuffer packetCapacity];
-[AVAudioCompressedBuffer packetCount];
-[AVAudioCompressedBuffer initWithFormat:packetCapacity:];
-[AVAudioCompressedBuffer packetDependencies];
```
