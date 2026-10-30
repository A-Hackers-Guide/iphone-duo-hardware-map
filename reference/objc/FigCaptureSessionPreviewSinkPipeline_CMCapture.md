# `FigCaptureSessionPreviewSinkPipeline`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCapturePreviewSinkPipeline`
- 5 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _imageQueueUpdatedNotificationSent;
B _previewSinkEnabled;
B _previewRunning;
B _providesBuffersForPreviewTap;
q _previewRunningHostTime;
```

## Properties

```
@property (TB,N,V_imageQueueUpdatedNotificationSent) imageQueueUpdatedNotificationSent;
@property (TB,N,V_previewRunning) previewRunning;
@property (Tq,R,N,V_previewRunningHostTime) previewRunningHostTime;
@property (TB,N,V_previewSinkEnabled) previewSinkEnabled;
@property (TB,N,V_providesBuffersForPreviewTap) providesBuffersForPreviewTap;
```

## Instance methods

```
-[FigCaptureSessionPreviewSinkPipeline setProvidesBuffersForPreviewTap:];
-[FigCaptureSessionPreviewSinkPipeline setPreviewSinkEnabled:];
-[FigCaptureSessionPreviewSinkPipeline imageQueueUpdatedNotificationSent];
-[FigCaptureSessionPreviewSinkPipeline setPreviewRunning:];
-[FigCaptureSessionPreviewSinkPipeline previewSinkEnabled];
-[FigCaptureSessionPreviewSinkPipeline previewRunning];
-[FigCaptureSessionPreviewSinkPipeline setImageQueueUpdatedNotificationSent:];
-[FigCaptureSessionPreviewSinkPipeline previewRunningHostTime];
-[FigCaptureSessionPreviewSinkPipeline providesBuffersForPreviewTap];
```
