# `FigCameraViewfinderServer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`, `FigCameraViewfinderDelegate`, `FigCameraViewfinderSessionDelegate`, `FigCaptureOSStateDataProvider`
- 4 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSXPCListener" _serviceListener;
@"NSMutableArray" _connections;
@"NSObject<OS_dispatch_queue>" _callbackQueue;
@"FigCaptureOSStateHandle" _osStateHandle;
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
-[FigCameraViewfinderServer osStatePropertyList];
-[FigCameraViewfinderServer listener:shouldAcceptNewConnection:];
-[FigCameraViewfinderServer init];
-[FigCameraViewfinderServer dealloc];
-[FigCameraViewfinderServer cameraViewfinder:viewfinderSessionWillBegin:];
-[FigCameraViewfinderServer cameraViewfinderSession:didCapturePhotoWithStatus:thumbnailData:timestamp:];
-[FigCameraViewfinderServer cameraViewfinderSessionPreviewStreamDidOpen:];
-[FigCameraViewfinderServer cameraViewfinder:viewfinderSessionDidEnd:];
-[FigCameraViewfinderServer cameraViewfinder:viewfinderSessionDidBegin:];
-[FigCameraViewfinderServer cameraViewfinderSession:previewStreamDidCloseWithStatus:];
-[FigCameraViewfinderServer cameraViewfinderSessionDidFinishMovieRecording:];
-[FigCameraViewfinderServer cameraViewfinderSessionDidStartMovieRecording:];
```
