# `FigVirtualCaptureCardCaptureSessionMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigCameraViewfinderDelegate`, `FigCameraViewfinderSessionDelegate`
- 4 instance variables, 5 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"FigCameraViewfinderLocal" _viewfinder;
@"NSObject<OS_dispatch_queue>" _delegateQueue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _isRecording;
```

## Properties

```
@property (TB,R) hasActiveCaptureSession;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FigVirtualCaptureCardCaptureSessionMonitor sharedMonitor];
```

## Instance methods

```
-[FigVirtualCaptureCardCaptureSessionMonitor init];
-[FigVirtualCaptureCardCaptureSessionMonitor stop];
-[FigVirtualCaptureCardCaptureSessionMonitor dealloc];
-[FigVirtualCaptureCardCaptureSessionMonitor start];
-[FigVirtualCaptureCardCaptureSessionMonitor cameraViewfinder:viewfinderSessionWillBegin:];
-[FigVirtualCaptureCardCaptureSessionMonitor cameraViewfinder:viewfinderSessionDidEnd:];
-[FigVirtualCaptureCardCaptureSessionMonitor cameraViewfinder:viewfinderSessionDidBegin:];
-[FigVirtualCaptureCardCaptureSessionMonitor cameraViewfinderSessionDidFinishMovieRecording:];
-[FigVirtualCaptureCardCaptureSessionMonitor cameraViewfinderSessionDidStartMovieRecording:];
-[FigVirtualCaptureCardCaptureSessionMonitor hasActiveCaptureSession];
```
