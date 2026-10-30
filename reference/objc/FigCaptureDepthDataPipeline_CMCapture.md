# `FigCaptureDepthDataPipeline`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureRemoteQueueSinkPipeline`
- 8 instance variables, 4 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"BWDepthConverterNode" _depthDataConverterNode;
@"BWNodeOutput" _videoAndConvertedDepthDataOutput;
@"BWPipelineStage" _pipelineStage;
@"NSString" _sourceID;
i _sourceDeviceType;
@"BWVideoDepthNode" _videoDepthNode;
@"BWInferenceNode" _opticalFlowInferenceNode;
@"BWInferenceNode" _depthScalingAndConversionInferenceNode;
```

## Properties

```
@property (T@"NSString",R,N,V_sourceID) sourceID;
@property (Ti,R,N,V_sourceDeviceType) sourceDeviceType;
@property (T@"BWPipelineStage",R,N,V_pipelineStage) pipelineStage;
@property (T@"BWNodeOutput",R,N,V_videoAndConvertedDepthDataOutput) videoAndConvertedDepthDataOutput;
```

## Class methods

```
+[FigCaptureDepthDataPipeline initialize];
```

## Instance methods

```
-[FigCaptureDepthDataPipeline dealloc];
-[FigCaptureDepthDataPipeline pipelineStage];
-[FigCaptureDepthDataPipeline sourceID];
-[FigCaptureDepthDataPipeline sourceDeviceType];
-[FigCaptureDepthDataPipeline initWithConfiguration:sourceOutput:graph:inferenceScheduler:captureDevice:name:delegate:];
-[FigCaptureDepthDataPipeline videoAndConvertedDepthDataOutput];
```
