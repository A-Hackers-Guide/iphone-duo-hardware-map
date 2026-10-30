# `AVAudioIOController` (protocol)

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__AudioSession.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 8 instance methods, 0 class methods

## Properties

```
@property (T{AVAudioIOPeriod=ddQf},R,N) IOPeriod;
@property (TB,R,N,GisRunning) running;
@property (TB,R,N) supportsDynamicLatency;
@property (T{AVAudioTimeInterval=ddQ},R,N) dynamicLatency;
```

## Instance methods

```
-[AVAudioIOController isRunning];
-[AVAudioIOController currentTime];
-[AVAudioIOController presentationTime];
-[AVAudioIOController IOPeriod];
-[AVAudioIOController createIOEventBlock:];
-[AVAudioIOController destroyIOEventBlock:];
-[AVAudioIOController dynamicLatency];
-[AVAudioIOController supportsDynamicLatency];
```
