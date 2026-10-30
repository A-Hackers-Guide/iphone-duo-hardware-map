# `FigCameraViewfinderRemoteObjectCallbacks` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance methods

```
-[FigCameraViewfinderRemoteObjectCallbacks viewfinderSessionDidFinishMovieRecording:];
-[FigCameraViewfinderRemoteObjectCallbacks viewfinderSessionDidBegin:withIdentifier:clientAuditTokenData:usesPhotoOutput:usesMovieFileOutput:];
-[FigCameraViewfinderRemoteObjectCallbacks viewfinderSession:didCapturePhotoWithStatus:thumbnailData:timestamp:];
-[FigCameraViewfinderRemoteObjectCallbacks viewfinderSessionWillBegin:withIdentifier:clientAuditTokenData:usesPhotoOutput:usesMovieFileOutput:];
-[FigCameraViewfinderRemoteObjectCallbacks viewfinderSessionDidEnd];
-[FigCameraViewfinderRemoteObjectCallbacks viewfinderSession:previewStreamDidCloseWithStatus:];
-[FigCameraViewfinderRemoteObjectCallbacks viewfinderSessionPreviewStreamDidOpen:];
-[FigCameraViewfinderRemoteObjectCallbacks viewfinderSessionDidStartMovieRecording:];
```
