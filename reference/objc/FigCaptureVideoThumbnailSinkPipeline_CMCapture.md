# `FigCaptureVideoThumbnailSinkPipeline`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureSinkPipeline`
- Protocols: `BWImageQueueSinkNodePreviewTapDelegate`
- 7 instance variables, 4 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"BWPixelTransferNode" _scalerNode;
@"BWImageQueueSinkNode" _imageQueueSinkNode;
@"NSObject<OS_dispatch_queue>" _notificationQueue;
B _didPropagateCurrentImageQueue;
@"<BWPipelineNotificationDelegate>" _notificationDelegate;
@"NSString" _sourceID;
i _sourceDeviceType;
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
+[FigCaptureVideoThumbnailSinkPipeline initialize];
```

## Instance methods

```
-[FigCaptureVideoThumbnailSinkPipeline imageQueueSinkNode:didAttemptToEnqueuePreviewSampleBuffer:withSuccess:];
-[FigCaptureVideoThumbnailSinkPipeline dealloc];
-[FigCaptureVideoThumbnailSinkPipeline imageQueueSinkNodeDidDisplayFirstFrame:timedOut:];
-[FigCaptureVideoThumbnailSinkPipeline imageQueueSinkNodeDidDisplayFirstFrame:atHostTime:];
-[FigCaptureVideoThumbnailSinkPipeline imageQueueSinkNodeDidDisplayFirstFrameForCurrentConfiguration:atHostTime:withPreviewStartedTime:];
-[FigCaptureVideoThumbnailSinkPipeline setDiscardsSampleData:];
```
