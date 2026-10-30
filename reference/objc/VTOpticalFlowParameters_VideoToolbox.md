# `VTOpticalFlowParameters`

- Image: [`/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`](../userland/System__Library__Frameworks__VideoToolbox.framework__VideoToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTFrameProcessorParameters`
- 5 instance variables, 10 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"VEOpticalFlowParameters" _veParameters;
@"VTFrameProcessorFrame" _sourceFrame;
@"VTFrameProcessorFrame" _nextFrame;
q _submissionMode;
@"VTFrameProcessorOpticalFlow" _destinationOpticalFlow;
```

## Properties

```
@property (T@"VTFrameProcessorFrame",R,N,V_sourceFrame) sourceFrame;
@property (T@"VTFrameProcessorFrame",R,N,V_nextFrame) nextFrame;
@property (Tq,R,N,V_submissionMode) submissionMode;
@property (T@"VTFrameProcessorOpticalFlow",R,N,V_destinationOpticalFlow) destinationOpticalFlow;
@property (T@"VTFrameProcessorFrame",?,R,N) destinationFrame;
@property (T@"NSArray",?,R,N) destinationFrames;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[VTOpticalFlowParameters dealloc];
-[VTOpticalFlowParameters sourceFrame];
-[VTOpticalFlowParameters destinationOpticalFlow];
-[VTOpticalFlowParameters initWithSourceFrame:nextFrame:submissionMode:destinationOpticalFlow:];
-[VTOpticalFlowParameters nextFrame];
-[VTOpticalFlowParameters submissionMode];
-[VTOpticalFlowParameters veParameters];
```
