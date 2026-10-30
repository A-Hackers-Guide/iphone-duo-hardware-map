# `PHASEPlatform` (protocol)

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 16 instance methods, 0 class methods

## Properties

```
@property (Td,R,N) sampleRate;
@property (TB,R,N) running;
@property (TI,R,N) bufferFrameSize;
@property (T@"<PHASESessionInterface>",?,R,N) sessionInterface;
@property (T@"<PHASERoomCongruenceInterface>",?,R,N) roomCongruenceInterface;
@property (T@"OS_os_workgroup",?,R,N) workgroup;
```

## Instance methods

```
-[PHASEPlatform sampleRate];
-[PHASEPlatform stop];
-[PHASEPlatform start];
-[PHASEPlatform running];
-[PHASEPlatform bufferFrameSize];
-[PHASEPlatform deviceLatencyInFramesForDirection:];
-[PHASEPlatform numberOfStreamsForDirection:];
-[PHASEPlatform registerIOBlock:];
-[PHASEPlatform registerOverloadNotification:];
-[PHASEPlatform registerRouteChangeNotification:];
-[PHASEPlatform streamInfoForIndex:direction:];
-[PHASEPlatform workgroup];
-[PHASEPlatform enableIO:direction:];
-[PHASEPlatform registerTapInterface:];
-[PHASEPlatform roomCongruenceInterface];
-[PHASEPlatform sessionInterface];
```
