# `VTSuperResolutionScalerParameters`

- Image: [`/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`](../userland/System__Library__Frameworks__VideoToolbox.framework__VideoToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTFrameProcessorParameters`
- 7 instance variables, 11 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"VESuperResolutionParameters" _veParameters;
@"VTFrameProcessorFrame" _sourceFrame;
@"VTFrameProcessorFrame" _previousFrame;
@"VTFrameProcessorFrame" _previousOutputFrame;
@"VTFrameProcessorOpticalFlow" _opticalFlow;
q _submissionMode;
@"VTFrameProcessorFrame" _destinationFrame;
```

## Properties

```
@property (T@"VTFrameProcessorFrame",R,N,V_sourceFrame) sourceFrame;
@property (T@"VTFrameProcessorFrame",R,N,V_previousFrame) previousFrame;
@property (T@"VTFrameProcessorFrame",R,N,V_previousOutputFrame) previousOutputFrame;
@property (T@"VTFrameProcessorOpticalFlow",R,N,V_opticalFlow) opticalFlow;
@property (Tq,R,N,V_submissionMode) submissionMode;
@property (T@"VTFrameProcessorFrame",R,N,V_destinationFrame) destinationFrame;
@property (T@"NSArray",?,R,N) destinationFrames;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[VTSuperResolutionScalerParameters dealloc];
-[VTSuperResolutionScalerParameters sourceFrame];
-[VTSuperResolutionScalerParameters destinationFrame];
-[VTSuperResolutionScalerParameters initWithSourceFrame:previousFrame:previousOutputFrame:opticalFlow:submissionMode:destinationFrame:];
-[VTSuperResolutionScalerParameters opticalFlow];
-[VTSuperResolutionScalerParameters previousFrame];
-[VTSuperResolutionScalerParameters previousOutputFrame];
-[VTSuperResolutionScalerParameters submissionMode];
-[VTSuperResolutionScalerParameters veParameters];
```
