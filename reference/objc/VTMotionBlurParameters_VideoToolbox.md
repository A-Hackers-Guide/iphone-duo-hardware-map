# `VTMotionBlurParameters`

- Image: [`/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`](../userland/System__Library__Frameworks__VideoToolbox.framework__VideoToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTFrameProcessorParameters`
- 9 instance variables, 13 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"VEMotionBlurParameters" _veParameters;
@"VTFrameProcessorFrame" _sourceFrame;
@"VTFrameProcessorFrame" _nextFrame;
@"VTFrameProcessorFrame" _previousFrame;
@"VTFrameProcessorOpticalFlow" _nextOpticalFlow;
@"VTFrameProcessorOpticalFlow" _previousOpticalFlow;
q _motionBlurStrength;
q _submissionMode;
@"VTFrameProcessorFrame" _destinationFrame;
```

## Properties

```
@property (T@"VTFrameProcessorFrame",R,N,V_sourceFrame) sourceFrame;
@property (T@"VTFrameProcessorFrame",R,N,V_nextFrame) nextFrame;
@property (T@"VTFrameProcessorFrame",R,N,V_previousFrame) previousFrame;
@property (T@"VTFrameProcessorOpticalFlow",R,N,V_nextOpticalFlow) nextOpticalFlow;
@property (T@"VTFrameProcessorOpticalFlow",R,N,V_previousOpticalFlow) previousOpticalFlow;
@property (Tq,R,N,V_motionBlurStrength) motionBlurStrength;
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
-[VTMotionBlurParameters dealloc];
-[VTMotionBlurParameters sourceFrame];
-[VTMotionBlurParameters nextOpticalFlow];
-[VTMotionBlurParameters destinationFrame];
-[VTMotionBlurParameters initWithSourceFrame:nextFrame:previousFrame:nextOpticalFlow:previousOpticalFlow:motionBlurStrength:submissionMode:destinationFrame:];
-[VTMotionBlurParameters motionBlurStrength];
-[VTMotionBlurParameters nextFrame];
-[VTMotionBlurParameters previousFrame];
-[VTMotionBlurParameters previousOpticalFlow];
-[VTMotionBlurParameters submissionMode];
-[VTMotionBlurParameters veParameters];
```
