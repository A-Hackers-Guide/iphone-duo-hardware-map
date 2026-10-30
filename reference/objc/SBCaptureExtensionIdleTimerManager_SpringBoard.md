# `SBCaptureExtensionIdleTimerManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`, `SBCameraViewfinderMonitorObserver`
- 3 instance variables, 5 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"<SBCameraViewfinderMonitoring>" _cameraViewfinderMonitorToken;
B _wantsAssertion;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBCaptureExtensionIdleTimerManager setWindowScene:];
-[SBCaptureExtensionIdleTimerManager initWithWindowScene:];
-[SBCaptureExtensionIdleTimerManager invalidate];
-[SBCaptureExtensionIdleTimerManager windowScene];
-[SBCaptureExtensionIdleTimerManager cameraViewfinderMonitorSessionDidBeginMovieRecording:];
-[SBCaptureExtensionIdleTimerManager cameraViewfinderMonitorSessionDidEndMovieRecording:];
```
