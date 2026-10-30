# `AVAudio3DMixing` (protocol)

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 8 properties, 16 instance methods, 0 class methods

## Properties

```
@property (Tq,N) renderingAlgorithm;
@property (Tq,N) sourceMode;
@property (Tq,N) pointSourceInHeadMode;
@property (Tf,N) rate;
@property (Tf,N) reverbBlend;
@property (Tf,N) obstruction;
@property (Tf,N) occlusion;
@property (T{AVAudio3DPoint=fff},N) position;
```

## Instance methods

```
-[AVAudio3DMixing rate];
-[AVAudio3DMixing position];
-[AVAudio3DMixing setRate:];
-[AVAudio3DMixing setPosition:];
-[AVAudio3DMixing setSourceMode:];
-[AVAudio3DMixing sourceMode];
-[AVAudio3DMixing occlusion];
-[AVAudio3DMixing setObstruction:];
-[AVAudio3DMixing setReverbBlend:];
-[AVAudio3DMixing obstruction];
-[AVAudio3DMixing pointSourceInHeadMode];
-[AVAudio3DMixing renderingAlgorithm];
-[AVAudio3DMixing reverbBlend];
-[AVAudio3DMixing setOcclusion:];
-[AVAudio3DMixing setPointSourceInHeadMode:];
-[AVAudio3DMixing setRenderingAlgorithm:];
```
