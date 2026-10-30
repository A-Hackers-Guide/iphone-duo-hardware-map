# `CCCameraConnection`

- Image: [`/System/Library/PrivateFrameworks/CompanionCamera.framework/CompanionCamera`](../userland/System__Library__PrivateFrameworks__CompanionCamera.framework__CompanionCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CCCameraConnectionProtocol`, `FigCameraViewfinderDelegate`, `FigCameraViewfinderSessionDelegate`
- 24 instance variables, 5 properties, 105 instance methods, 0 class methods

## Instance variables

```
@"CCCameraConnectionInternal" _internal;
@"NSXPCConnection" _xpc;
@ _orientationChangeObserver;
@"NSString" _previewEndpoint;
@"FigCameraViewfinder" _remoteViewfinder;
@"FigCameraViewfinderSession" _remoteViewfinderSession;
Q _remoteViewfinderSessionState;
Q _desiredPreviewState;
Q _currentPreviewState;
Q _interruptionCount;
@"NSObject<OS_dispatch_source>" _zoomTimer;
f _pendingZoomAmount;
f _lastSentZoomAmount;
i _deviceConnectedNotificationToken;
i _deviceDisconnectedNotificationToken;
B _burstInProgress;
B _capturingVideo;
@"NSDate" _captureStartDate;
B _capturingPaused;
@"NSDate" _capturePauseDate;
B _capturingPersonalPhotographer;
q _shallowDepthOfFieldStatus;
q _stereoCaptureStatus;
@"<CCCameraConnectionDelegate>" _delegate;
```

## Properties

```
@property (T@"<CCCameraConnectionDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CCCameraConnection _connect];
-[CCCameraConnection open];
-[CCCameraConnection _irisMode];
-[CCCameraConnection xpc_startCaptureWithMode:reply:];
-[CCCameraConnection xpc_ensureSwitchedToOneOfSupportedCaptureModes:reply:];
-[CCCameraConnection isPreviewConnected];
-[CCCameraConnection didPauseCaptureTimerWithPauseTime:];
-[CCCameraConnection _openPreview];
-[CCCameraConnection _disconnect];
-[CCCameraConnection _sharedLibraryMode];
-[CCCameraConnection close];
-[CCCameraConnection captureDeviceDidChange:];
-[CCCameraConnection xpc_endBurstCaptureWithReply:];
-[CCCameraConnection _currentZoomMagnification];
-[CCCameraConnection personalPhotographerSupportDidChange:];
-[CCCameraConnection xpc_setHDRMode:];
-[CCCameraConnection xpc_setSharedLibraryMode:];
-[CCCameraConnection _personalPhotographerSessionTimerState];
-[CCCameraConnection xpc_setIrisMode:];
-[CCCameraConnection init];
-[CCCameraConnection xpc_stopPersonalPhotographerSessionWithReply:];
-[CCCameraConnection burstCaptureNumberOfPhotosDidChange:];
-[CCCameraConnection _flashMode];
-[CCCameraConnection _supportedCaptureDevices];
-[CCCameraConnection xpc_toggleCameraDevice];
-[CCCameraConnection _shouldReportEvent];
-[CCCameraConnection _captureDevice];
-[CCCameraConnection xpc_cancelCountdown];
-[CCCameraConnection sharedLibraryModeDidChange];
-[CCCameraConnection showingLivePreviewDidChange];
-[CCCameraConnection didUpdateShallowDepthOfFieldStatus:];
-[CCCameraConnection dealloc];
-[CCCameraConnection didResumeCaptureTimerWithNewStartTime:];
-[CCCameraConnection switchedOrientation:];
-[CCCameraConnection _handleInvalidation];
-[CCCameraConnection didStopCapture];
-[CCCameraConnection xpc_setZoom:reply:];
-[CCCameraConnection _personalPhotographerMode];
-[CCCameraConnection zoomDidChange:];
-[CCCameraConnection xpc_pauseCaptureWithReply:];
-[CCCameraConnection modeSelected:];
-[CCCameraConnection _handleInterruption];
-[CCCameraConnection cameraViewfinderSession:didCapturePhotoWithStatus:thumbnailData:timestamp:];
-[CCCameraConnection xpc_stopCaptureWithReply:];
-[CCCameraConnection xpc_setFocusPoint:];
-[CCCameraConnection _supportsMomentCapture];
-[CCCameraConnection _maximumZoomMagnification];
-[CCCameraConnection setDelegate:];
-[CCCameraConnection xpc_setPreviewEndpoint:];
-[CCCameraConnection personalPhotographerModeDidChange:];
-[CCCameraConnection didStartCaptureTimer];
-[CCCameraConnection xpc_setCaptureMode:reply:];
-[CCCameraConnection cameraViewfinderSessionPreviewStreamDidOpen:];
-[CCCameraConnection _flashSupport];
-[CCCameraConnection _closePreview];
-[CCCameraConnection panoramaDirectionDidChange:];
-[CCCameraConnection _captureMode];
-[CCCameraConnection xpc_startPersonalPhotographerSessionWithReply:];
-[CCCameraConnection _zoomAmount];
-[CCCameraConnection countdownCanceled];
-[CCCameraConnection sharedLibrarySupportDidChange];
-[CCCameraConnection burstCaptureWillStart];
-[CCCameraConnection delegate];
-[CCCameraConnection _significantZoomMagnifications];
-[CCCameraConnection _toggleCameraDeviceSupport];
-[CCCameraConnection _sharedLibrarySupport];
-[CCCameraConnection xpc_setFlashMode:];
-[CCCameraConnection hdrModeDidChange];
-[CCCameraConnection _minimumZoomMagnification];
-[CCCameraConnection _irisSupport];
-[CCCameraConnection _hdrMode];
-[CCCameraConnection xpc_beginBurstCaptureWithReply:];
-[CCCameraConnection irisModeDidChange];
-[CCCameraConnection didStopPersonalPhotographerCapture];
-[CCCameraConnection cameraViewfinder:viewfinderSessionDidEnd:];
-[CCCameraConnection willStartCapturing];
-[CCCameraConnection photoTaken:];
-[CCCameraConnection _zoomSupport];
-[CCCameraConnection cameraViewfinder:viewfinderSessionDidBegin:];
-[CCCameraConnection xpc_setCaptureDevice:reply:];
-[CCCameraConnection xpc_suspend];
-[CCCameraConnection _zoomTimerFired];
-[CCCameraConnection _personalPhotographerSupport];
-[CCCameraConnection xpc_fetchCurrentStateIncludingSupportedCaptureModes:reply:];
-[CCCameraConnection didUpdateStereoCaptureStatus:];
-[CCCameraConnection cameraViewfinderSession:previewStreamDidCloseWithStatus:];
-[CCCameraConnection captureDeviceDidChange];
-[CCCameraConnection _personalPhotographerStatus];
-[CCCameraConnection xpc_resumeCaptureWithReply:];
-[CCCameraConnection takePhotoWithCountdown:];
-[CCCameraConnection _supportedCaptureModes];
-[CCCameraConnection _supportsZoomMagnification];
-[CCCameraConnection _currentOrientation];
-[CCCameraConnection personalPhotographerSessionTimerStateDidChange:];
-[CCCameraConnection _checkin];
-[CCCameraConnection flashModeDidChange];
-[CCCameraConnection _hdrSupport];
-[CCCameraConnection personalPhotographerStatusDidChange:];
-[CCCameraConnection xpc_setZoomMagnification:reply:];
-[CCCameraConnection _burstSupport];
-[CCCameraConnection burstCaptureDidStop];
-[CCCameraConnection isOpen];
-[CCCameraConnection willStartPersonalPhotographerCapture];
-[CCCameraConnection didUpdateThumbnailWithData:isVideo:];
-[CCCameraConnection _performPreviewStateTransitionsIfNeeded];
```
