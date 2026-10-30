# `FigCaptureStillImageSinkPipeline` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 7 properties, 7 instance methods, 1 class methods

## Properties

```
@property (T@"NSArray",R,N) nodes;
@property (T@"NSString",R,N) sinkID;
@property (T@"BWStillImageCoordinatorNode",R,N) stillImageCoordinatorNode;
@property (T@"BWCompressedShotBufferNode",R,N) compressedShotBufferNode;
@property (T@"BWStillImageSampleBufferSinkNode",R,N) stillImageSinkNode;
@property (T@"BWPortraitHDRStagingNode",R,N) portraitHDRStagingNode;
@property (class, T@"NSString",R) pipelineBaseName;
```

## Class methods

```
+[FigCaptureStillImageSinkPipeline pipelineBaseName];
```

## Instance methods

```
-[FigCaptureStillImageSinkPipeline nodes];
-[FigCaptureStillImageSinkPipeline sinkID];
-[FigCaptureStillImageSinkPipeline compressedShotBufferNode];
-[FigCaptureStillImageSinkPipeline enablePrepareTimeAllocationsForDeferredPrepare];
-[FigCaptureStillImageSinkPipeline portraitHDRStagingNode];
-[FigCaptureStillImageSinkPipeline stillImageCoordinatorNode];
-[FigCaptureStillImageSinkPipeline stillImageSinkNode];
```
