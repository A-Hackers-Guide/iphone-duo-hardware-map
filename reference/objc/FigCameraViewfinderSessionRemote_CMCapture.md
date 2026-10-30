# `FigCameraViewfinderSessionRemote`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCameraViewfinderSession`
- 8 instance variables, 0 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"<FigCameraViewfinderSessionRemoteObject>" _remoteViewfinderSession;
{?="val"[8I]} _clientAuditToken;
B _usesPhotoOutput;
B _usesMovieFileOutput;
I _state;
@"FigStateMachine" _stateMachine;
B _recordingMovie;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _recordingMovieLock;
```

## Instance methods

```
-[FigCameraViewfinderSessionRemote _serverDied];
-[FigCameraViewfinderSessionRemote _previewStreamDidOpen];
-[FigCameraViewfinderSessionRemote clientAuditToken];
-[FigCameraViewfinderSessionRemote dealloc];
-[FigCameraViewfinderSessionRemote usesMovieFileOutput];
-[FigCameraViewfinderSessionRemote _movieRecordingDidStart];
-[FigCameraViewfinderSessionRemote openPreviewStreamWithOptions:];
-[FigCameraViewfinderSessionRemote closePreviewStream];
-[FigCameraViewfinderSessionRemote usesPhotoOutput];
-[FigCameraViewfinderSessionRemote _previewStreamDidCloseWithStatus:];
-[FigCameraViewfinderSessionRemote _movieRecordingDidFinish];
-[FigCameraViewfinderSessionRemote _clientDisconnectedFromServer];
-[FigCameraViewfinderSessionRemote _initWithRemoteViewfinderSession:clientAuditToken:usesPhotoOutput:usesMovieFileOutput:delegateStorage:];
```
