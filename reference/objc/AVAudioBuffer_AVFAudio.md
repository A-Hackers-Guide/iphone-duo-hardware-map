# `AVAudioBuffer`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`
- 2 instance variables, 3 properties, 12 instance methods, 0 class methods

## Instance variables

```
^v _impl;
@? _deallocator;
```

## Properties

```
@property (T@"AVAudioFormat",R,N) format;
@property (Tr^{AudioBufferList=I[1{AudioBuffer=II^v}]},R,N) audioBufferList;
@property (T^{AudioBufferList=I[1{AudioBuffer=II^v}]},R,N) mutableAudioBufferList;
```

## Instance methods

```
-[AVAudioBuffer mutableCopyWithZone:];
-[AVAudioBuffer dealloc];
-[AVAudioBuffer description];
-[AVAudioBuffer copyWithZone:];
-[AVAudioBuffer format];
-[AVAudioBuffer byteLength];
-[AVAudioBuffer mutableAudioBufferList];
-[AVAudioBuffer audioBufferList];
-[AVAudioBuffer byteCapacity];
-[AVAudioBuffer setByteLength:];
-[AVAudioBuffer initWithFormat:byteCapacity:];
-[AVAudioBuffer initWithPCMFormat:byteCapacity:bufferListNoCopy:deallocator:];
```
