# `BWCinematographyLowLightMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 1 properties, 3 instance methods, 0 class methods

## Instance variables

```
[30B] _pastFramesWereBrightEnough;
i _pastFramesWereBrightEnoughPointer;
B _currentStateIsBrightEnough;
f _alphaLowLight;
i _luxLevelThreshold;
i _alphaRampFrameCount;
```

## Properties

```
@property (Tf,R,N) alphaLowLight;
```

## Instance methods

```
-[BWCinematographyLowLightMonitor alphaLowLight];
-[BWCinematographyLowLightMonitor initWithTuningParameters:];
-[BWCinematographyLowLightMonitor updateAlphaLowLightWithMetadata:imageSampleBuffer:];
```
