# `FigCameraViewfinderSessionLocal`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCameraViewfinderSession`
- Protocols: `FigCaptureSessionPreviewTapDelegate`, `FigCameraViewfinderStreamDelegate`
- 9 instance variables, 4 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"FigCameraViewfinderLocal" _viewfinder;
@"FigStateMachine" _stateMachine;
B _ended;
@"FigCaptureSessionProxy" _captureSessionProxy;
q _identifier;
@"FigCameraViewfinderStream" _previewStream;
@"NSObject<OS_dispatch_queue>" _previewStreamQueue;
B _previewStreamClosed;
i _previewStreamClosedErrorStatus;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FigCameraViewfinderSessionLocal viewfinder];
-[FigCameraViewfinderSessionLocal captureSessionPreviewTapDidClose:];
-[FigCameraViewfinderSessionLocal captureSession:previewTapDidOutputSampleBuffer:];
-[FigCameraViewfinderSessionLocal identifier];
-[FigCameraViewfinderSessionLocal clientAuditToken];
-[FigCameraViewfinderSessionLocal dealloc];
-[FigCameraViewfinderSessionLocal usesMovieFileOutput];
-[FigCameraViewfinderSessionLocal _captureSessionDidStartMovieRecording];
-[FigCameraViewfinderSessionLocal _initWithOwningViewfinder:captureSessionProxy:delegateStorage:];
-[FigCameraViewfinderSessionLocal cameraViewfinderStream:didCloseWithStatus:];
-[FigCameraViewfinderSessionLocal openPreviewStreamWithOptions:];
-[FigCameraViewfinderSessionLocal closePreviewStream];
-[FigCameraViewfinderSessionLocal usesPhotoOutput];
-[FigCameraViewfinderSessionLocal _captureSessionDidFinishMovieRecording];
-[FigCameraViewfinderSessionLocal cameraViewfinderStreamDidOpen:];
-[FigCameraViewfinderSessionLocal _captureSessionDidCapturePhotoWithStatus:thumbnailData:timestamp:];
-[FigCameraViewfinderSessionLocal captureSessionPreviewTapDidOpen:];
-[FigCameraViewfinderSessionLocal _captureSessionDidStop];
```
