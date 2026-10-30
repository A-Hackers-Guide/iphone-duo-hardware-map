# `BWIntelligentDistortionCorrectionProcessorController`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorController`
- Protocols: `BWIntelligentDistortionCorrectionProcessorInputDelegate`
- 9 instance variables, 4 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _idcMaxZoomScaleFactorByPortType;
@"<FigIntelligentDistortionCorrectionProcessor>" _processor;
^{opaqueCMFormatDescription=} _outputImageFormatDescription;
@"NSMutableDictionary" _outputFormatDescriptionByAttachedMediaKey;
@"FigStateMachine" _stateMachine;
@"NSMutableArray" _requestQueue;
@"BWIntelligentDistortionCorrectionProcessorRequest" _currentRequest;
^{__CVBuffer=} _intermediateDepthInputBuffer;
^{__CVBuffer=} _intermediateDepthOutputBuffer;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWIntelligentDistortionCorrectionProcessorController idcSupportedForCaptureType:captureFlags:];
```

## Instance methods

```
-[BWIntelligentDistortionCorrectionProcessorController dealloc];
-[BWIntelligentDistortionCorrectionProcessorController initWithConfiguration:];
-[BWIntelligentDistortionCorrectionProcessorController type];
-[BWIntelligentDistortionCorrectionProcessorController cancelProcessing];
-[BWIntelligentDistortionCorrectionProcessorController inputReceivedNewInputData:];
-[BWIntelligentDistortionCorrectionProcessorController determineWorkingBufferRequirementsWithProcessorConfig:];
-[BWIntelligentDistortionCorrectionProcessorController enqueueInputForProcessing:delegate:];
```
