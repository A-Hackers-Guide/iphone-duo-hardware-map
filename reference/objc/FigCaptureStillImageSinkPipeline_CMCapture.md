# `FigCaptureStillImageSinkPipeline`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureSinkPipeline`
- Protocols: `FigCaptureStillImageSinkPipeline`
- 7 instance variables, 10 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"BWFigVideoCaptureDevice" _captureDevice;
@"BWStillImageCoordinatorNode" _stillImageCoordinatorNode;
@"BWStillImageSampleBufferSinkNode" _stillImageSinkNode;
@"BWStillImageBravoDisparityNode" _stillImageDisparityNode;
@"BWDepthConverterNode" _stillImageDepthConverterNode;
@"BWPortraitHDRStagingNode" _portraitHDRStagingNode;
@"BWSISNode" _legacySISNode;
```

## Properties

```
@property (T@"NSArray",R,N) nodes;
@property (T@"NSString",R,N) sinkID;
@property (T@"BWStillImageCoordinatorNode",R,N) stillImageCoordinatorNode;
@property (T@"BWCompressedShotBufferNode",R,N) compressedShotBufferNode;
@property (T@"BWStillImageSampleBufferSinkNode",R,N) stillImageSinkNode;
@property (T@"BWPortraitHDRStagingNode",R,N) portraitHDRStagingNode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FigCaptureStillImageSinkPipeline initialize];
+[FigCaptureStillImageSinkPipeline pipelineBaseName];
```

## Instance methods

```
-[FigCaptureStillImageSinkPipeline dealloc];
-[FigCaptureStillImageSinkPipeline compressedShotBufferNode];
-[FigCaptureStillImageSinkPipeline enablePrepareTimeAllocationsForDeferredPrepare];
-[FigCaptureStillImageSinkPipeline initWithConfiguration:captureDevice:sourceOutputsByPortType:captureStatusDelegate:inferenceScheduler:graph:name:];
-[FigCaptureStillImageSinkPipeline portraitHDRStagingNode];
-[FigCaptureStillImageSinkPipeline stillImageCoordinatorNode];
-[FigCaptureStillImageSinkPipeline stillImageSinkNode];
```
