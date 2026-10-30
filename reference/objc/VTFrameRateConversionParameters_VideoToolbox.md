# `VTFrameRateConversionParameters`

- Image: [`/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`](../userland/System__Library__Frameworks__VideoToolbox.framework__VideoToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTFrameProcessorParameters`
- 8 instance variables, 11 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"VEFrameRateConversionParameters" _veParameters;
@"NSMutableArray" _veDestinationFrames;
@"VTFrameProcessorFrame" _sourceFrame;
@"VTFrameProcessorFrame" _nextFrame;
@"VTFrameProcessorOpticalFlow" _opticalFlow;
@"NSArray" _interpolationPhase;
q _submissionMode;
@"NSArray" _destinationFrames;
```

## Properties

```
@property (T@"VTFrameProcessorFrame",R,N,V_sourceFrame) sourceFrame;
@property (T@"VTFrameProcessorFrame",R,N,V_nextFrame) nextFrame;
@property (T@"VTFrameProcessorOpticalFlow",R,N,V_opticalFlow) opticalFlow;
@property (T@"NSArray",R,N,V_interpolationPhase) interpolationPhase;
@property (Tq,R,N,V_submissionMode) submissionMode;
@property (T@"NSArray",R,N,V_destinationFrames) destinationFrames;
@property (T@"VTFrameProcessorFrame",?,R,N) destinationFrame;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[VTFrameRateConversionParameters dealloc];
-[VTFrameRateConversionParameters sourceFrame];
-[VTFrameRateConversionParameters destinationFrames];
-[VTFrameRateConversionParameters initWithSourceFrame:nextFrame:opticalFlow:interpolationPhase:submissionMode:destinationFrames:];
-[VTFrameRateConversionParameters interpolationPhase];
-[VTFrameRateConversionParameters nextFrame];
-[VTFrameRateConversionParameters opticalFlow];
-[VTFrameRateConversionParameters submissionMode];
-[VTFrameRateConversionParameters veParameters];
```
