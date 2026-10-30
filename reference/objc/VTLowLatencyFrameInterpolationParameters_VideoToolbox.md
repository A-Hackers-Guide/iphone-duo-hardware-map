# `VTLowLatencyFrameInterpolationParameters`

- Image: [`/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`](../userland/System__Library__Frameworks__VideoToolbox.framework__VideoToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTFrameProcessorParameters`
- 5 instance variables, 9 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_group>" _parameterDispatchGroup;
@"VTFrameProcessorFrame" _sourceFrame;
@"VTFrameProcessorFrame" _previousFrame;
@"NSArray" _interpolationPhase;
@"NSArray" _destinationFrames;
```

## Properties

```
@property (T@"VTFrameProcessorFrame",R,N,V_sourceFrame) sourceFrame;
@property (T@"VTFrameProcessorFrame",R,N,V_previousFrame) previousFrame;
@property (T@"NSArray",R,N,V_interpolationPhase) interpolationPhase;
@property (T@"NSArray",R,N,V_destinationFrames) destinationFrames;
@property (T@"VTFrameProcessorFrame",?,R,N) destinationFrame;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[VTLowLatencyFrameInterpolationParameters dealloc];
-[VTLowLatencyFrameInterpolationParameters sourceFrame];
-[VTLowLatencyFrameInterpolationParameters destinationFrames];
-[VTLowLatencyFrameInterpolationParameters initWithSourceFrame:previousFrame:interpolationPhase:destinationFrames:];
-[VTLowLatencyFrameInterpolationParameters interpolationPhase];
-[VTLowLatencyFrameInterpolationParameters parameterDispatchGroup];
-[VTLowLatencyFrameInterpolationParameters previousFrame];
```
