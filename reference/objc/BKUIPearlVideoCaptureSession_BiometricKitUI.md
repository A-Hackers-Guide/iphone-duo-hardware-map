# `BKUIPearlVideoCaptureSession`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKUIPearlVideoCaptureSessionType`
- 12 instance variables, 8 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"AVCaptureSession" _captureSession;
@"AVCaptureDeviceInput" _deviceInput;
@"AVCaptureVideoDataOutput" _outputForSelfieSession;
@"AVCaptureVideoPreviewLayer" _previewLayer;
Q _captureSessionRestarts;
B _captureSessionInterrupted;
B _runningObserverRegistered;
@"NSObject<OS_dispatch_queue>" _captureQueue;
@"AMSUISelfieFaceIDSession" _selfieSession;
B _collectsFramesForAgeVerification;
@"<BKUIVideoCaptureSesssionDelegate>" _delegate;
d _additionalPreviewScalingAllowedByCameraFormat;
```

## Properties

```
@property (T@"<BKUIVideoCaptureSesssionDelegate>",W,N,V_delegate) delegate;
@property (T@"AVCaptureVideoPreviewLayer",&,N,V_previewLayer) previewLayer;
@property (Td,R,N,V_additionalPreviewScalingAllowedByCameraFormat) additionalPreviewScalingAllowedByCameraFormat;
@property (TB,R,N,V_collectsFramesForAgeVerification) collectsFramesForAgeVerification;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKUIPearlVideoCaptureSession observeValueForKeyPath:ofObject:change:context:];
-[BKUIPearlVideoCaptureSession init];
-[BKUIPearlVideoCaptureSession dealloc];
-[BKUIPearlVideoCaptureSession setDelegate:];
-[BKUIPearlVideoCaptureSession delegate];
-[BKUIPearlVideoCaptureSession startCapture];
-[BKUIPearlVideoCaptureSession endCapture];
-[BKUIPearlVideoCaptureSession previewLayer];
-[BKUIPearlVideoCaptureSession _frontCamera];
-[BKUIPearlVideoCaptureSession additionalPreviewScalingAllowedByCameraFormat];
-[BKUIPearlVideoCaptureSession setPreviewLayer:];
-[BKUIPearlVideoCaptureSession supportMultitaskingCameraAccess];
-[BKUIPearlVideoCaptureSession _captureSessionInterrupted:];
-[BKUIPearlVideoCaptureSession _captureSessionStarted:];
-[BKUIPearlVideoCaptureSession _captureSessionStopped:];
-[BKUIPearlVideoCaptureSession _setupCaptureStack];
-[BKUIPearlVideoCaptureSession _stopSessionAndTearDown];
-[BKUIPearlVideoCaptureSession _synchronizedCaptureSessionInterrupted];
-[BKUIPearlVideoCaptureSession collectsFramesForAgeVerification];
-[BKUIPearlVideoCaptureSession configureFaceIDCoexistenceForCamera:];
-[BKUIPearlVideoCaptureSession enableFaceIDCoexistenceForCamera:];
-[BKUIPearlVideoCaptureSession enforceTargetFrameRateForCamera:];
-[BKUIPearlVideoCaptureSession findCoexistenceSupportedFormatForCamera:];
-[BKUIPearlVideoCaptureSession initCollectingFramesForAgeVerification:];
-[BKUIPearlVideoCaptureSession setActiveFormatForCamera:format:];
-[BKUIPearlVideoCaptureSession setupSelfieSession];
-[BKUIPearlVideoCaptureSession updateSelfieSessionWithFaceDetectState:];
```
