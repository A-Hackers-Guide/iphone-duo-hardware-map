# `CAMCaptureAttributeManagerCaptureControllerProtocol` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 11 properties, 12 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisCapturingBurst) capturingBurst;
@property (TB,R,N,GisCapturingPanorama) capturingPanorama;
@property (TB,R,N,GisCapturingTimelapse) capturingTimelapse;
@property (TB,R,N,GisCapturingVideo) capturingVideo;
@property (TB,R,N,GisFlashActive) flashActive;
@property (TB,R,N) shouldSkipCaptureAttributeResetForOngoingCapture;
@property (T@"CAMVideoCaptureRequest",R,N) activeVideoCaptureRequest;
@property (T@"CAMStillImageCaptureRequest",R,N) activeCTMVideoCaptureRequest;
@property (T{?=qiIq},R,N) lastObservedExposureDuration;
@property (Td,R,N) lastObservedLensAperture;
@property (Td,R,N) lastObservedLensPosition;
```

## Instance methods

```
-[CAMCaptureAttributeManagerCaptureControllerProtocol isCapturingTimelapse];
-[CAMCaptureAttributeManagerCaptureControllerProtocol isCapturingVideo];
-[CAMCaptureAttributeManagerCaptureControllerProtocol lastObservedLensAperture];
-[CAMCaptureAttributeManagerCaptureControllerProtocol lastObservedLensPosition];
-[CAMCaptureAttributeManagerCaptureControllerProtocol isCapturingBurst];
-[CAMCaptureAttributeManagerCaptureControllerProtocol captureAttributeManager:enqueueCommand:];
-[CAMCaptureAttributeManagerCaptureControllerProtocol isCapturingPanorama];
-[CAMCaptureAttributeManagerCaptureControllerProtocol isFlashActive];
-[CAMCaptureAttributeManagerCaptureControllerProtocol activeVideoCaptureRequest];
-[CAMCaptureAttributeManagerCaptureControllerProtocol lastObservedExposureDuration];
-[CAMCaptureAttributeManagerCaptureControllerProtocol shouldSkipCaptureAttributeResetForOngoingCapture];
-[CAMCaptureAttributeManagerCaptureControllerProtocol activeCTMVideoCaptureRequest];
```
