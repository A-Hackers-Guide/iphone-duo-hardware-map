# `AVAudioSharedPCMBuffer`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAudioPCMBuffer`
- 0 instance variables, 2 properties, 4 instance methods, 0 class methods

## Properties

```
@property (T@"AVAudioSharedBufferToken",R,N) sharedBufferToken;
@property (TB,R,N) backedBySharedMemory;
```

## Instance methods

```
-[AVAudioSharedPCMBuffer initWithPCMFormat:frameCapacity:];
-[AVAudioSharedPCMBuffer backedBySharedMemory];
-[AVAudioSharedPCMBuffer initWithPCMFormat:sharedBufferToken:];
-[AVAudioSharedPCMBuffer sharedBufferToken];
```
