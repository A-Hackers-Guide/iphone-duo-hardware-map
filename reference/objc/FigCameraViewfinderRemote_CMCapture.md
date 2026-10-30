# `FigCameraViewfinderRemote`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCameraViewfinder`
- Protocols: `FigCameraViewfinderRemoteObjectCallbacks`
- 5 instance variables, 4 properties, 12 instance methods, 3 class methods

## Instance variables

```
@"NSMapTable" _weakSessionTable;
@"FigStateMachine" _stateMachine;
@"FigNSXPCConnection" _connection;
@"NSObject<OS_dispatch_queue>" _connectionManagementQueue;
@"<FigCameraViewfinderRemoteObject>" _remoteViewfinder;
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
+[FigCameraViewfinderRemote initialize];
+[FigCameraViewfinderRemote cameraViewfinder];
+[FigCameraViewfinderRemote remoteObjectCallbacksInterface];
```

## Instance methods

```
-[FigCameraViewfinderRemote viewfinderSessionDidFinishMovieRecording:];
-[FigCameraViewfinderRemote viewfinderSessionDidBegin:withIdentifier:clientAuditTokenData:usesPhotoOutput:usesMovieFileOutput:];
-[FigCameraViewfinderRemote init];
-[FigCameraViewfinderRemote stop];
-[FigCameraViewfinderRemote startWithOptions:];
-[FigCameraViewfinderRemote dealloc];
-[FigCameraViewfinderRemote viewfinderSession:didCapturePhotoWithStatus:thumbnailData:timestamp:];
-[FigCameraViewfinderRemote viewfinderSessionWillBegin:withIdentifier:clientAuditTokenData:usesPhotoOutput:usesMovieFileOutput:];
-[FigCameraViewfinderRemote viewfinderSessionDidEnd];
-[FigCameraViewfinderRemote viewfinderSession:previewStreamDidCloseWithStatus:];
-[FigCameraViewfinderRemote viewfinderSessionPreviewStreamDidOpen:];
-[FigCameraViewfinderRemote viewfinderSessionDidStartMovieRecording:];
```
