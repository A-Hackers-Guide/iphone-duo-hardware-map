# `CAMIdleController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMStillImageCaptureRequestDelegate`, `CAMVideoCaptureRequestDelegate`, `CAMPanoramaCaptureRequestDelegate`, `CAMStillImageCapturingVideoDelegate`
- 3 instance variables, 8 properties, 29 instance methods, 0 class methods

## Instance variables

```
B _updatingIdleTimer;
B _intelligenceMode;
@"NSTimer" _enableIdleTimer;
```

## Properties

```
@property (TB,N,GisUpdatingIdleTimer,S_setUpdatingIdleTimer:,V_updatingIdleTimer) updatingIdleTimer;
@property (TB,R,N,G_isIdleTimerIndefinitelyDisabled) idleTimerIndefinitelyDisabled;
@property (T@"NSTimer",&,N,G_enableIdleTimer,S_setEnableIdleTimer:,V_enableIdleTimer) enableIdleTimer;
@property (TB,N,GisIntelligenceMode,V_intelligenceMode) intelligenceMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMIdleController videoRequestDidStopCapturing:];
-[CAMIdleController panoramaRequestDidStopCapturing:interrupted:];
-[CAMIdleController panoramaRequestDidStartCapturing:];
-[CAMIdleController videoRequestDidStartCapturing:];
-[CAMIdleController stillImageRequestsDidStopCapturingCTMVideo];
-[CAMIdleController init];
-[CAMIdleController stillImageRequestWillStartCapturingCTMVideoWithCaptureInFlight:];
-[CAMIdleController dealloc];
-[CAMIdleController stillImageRequestDidStopCapturingStillImage:];
-[CAMIdleController _activeIdleTimerDelay];
-[CAMIdleController _delayIdleTimerByTimeInterval:];
-[CAMIdleController _delayIdleTimerByTimeIntervalUnlessIndefinitelyDisabled:];
-[CAMIdleController _enableIdleTimer];
-[CAMIdleController _immediatelyEnableApplicationIdleTimer];
-[CAMIdleController _indefinitelyDisableApplicationIdleTimer];
-[CAMIdleController _isIdleTimerIndefinitelyDisabled];
-[CAMIdleController _setEnableIdleTimer:];
-[CAMIdleController _setUpdatingIdleTimer:];
-[CAMIdleController _teardownEnableIdleTimer];
-[CAMIdleController isIntelligenceMode];
-[CAMIdleController isUpdatingIdleTimer];
-[CAMIdleController setIntelligenceMode:];
-[CAMIdleController startUpdatingIdleTimer];
-[CAMIdleController stopUpdatingIdleTimer];
-[CAMIdleController timelapseRequestDidResumeCapturing];
-[CAMIdleController timelapseRequestDidStartCapturing];
-[CAMIdleController timelapseRequestDidStopCapturing];
-[CAMIdleController updateForVideoPaused];
-[CAMIdleController updateForVideoResumed];
```
