# `CAMViewfinderViewControllerIntentsDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 9 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisCapturingFromTimer) capturingFromTimer;
@property (Tq,R,N) currentCaptureDevice;
@property (Tq,R,N) currentCaptureMode;
@property (TB,R,N,GisRecording) recording;
```

## Instance methods

```
-[CAMViewfinderViewControllerIntentsDelegate isCapturingFromTimer];
-[CAMViewfinderViewControllerIntentsDelegate currentCaptureMode];
-[CAMViewfinderViewControllerIntentsDelegate setSingleUseTimerWithDuration:];
-[CAMViewfinderViewControllerIntentsDelegate navigateToViewfinderView];
-[CAMViewfinderViewControllerIntentsDelegate isRecording];
-[CAMViewfinderViewControllerIntentsDelegate pressShutterForRemoteShutter];
-[CAMViewfinderViewControllerIntentsDelegate changeToMode:device:animated:];
-[CAMViewfinderViewControllerIntentsDelegate isInCameraRollView];
-[CAMViewfinderViewControllerIntentsDelegate currentCaptureDevice];
```
