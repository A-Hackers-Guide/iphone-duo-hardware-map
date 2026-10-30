# `AVCapturePhotoOutputReadinessCoordinator`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 12 instance methods, 2 class methods

## Instance variables

```
@"AVWeakReferencingDelegateStorage" _delegateStorage;
q _captureReadiness;
{AVCapturePhotoOutputCaptureReadinessState="sessionIsRunning"B"autoDeferredPhotoDeliveryEnabled"B"responsiveCaptureEnabled"B"numberOfPhotoCapturesInflight"i"latestCaptureUniqueID"q"inflightNonOverlappingCaptureUniqueID"q"inflightUniqueIDWaitingForCapture"q"inflightUniqueIDWaitingForProcessing"q} _captureReadinessState;
@"NSMutableArray" _trackedPhotoSettingsArray;
```

## Properties

```
@property (T@"<AVCapturePhotoOutputReadinessCoordinatorDelegate>",W) delegate;
@property (Tq,R,N) captureReadiness;
```

## Class methods

```
+[AVCapturePhotoOutputReadinessCoordinator _captureReadinessFromReadinessState:];
+[AVCapturePhotoOutputReadinessCoordinator _isOverlappingCaptureSupportedForPhotoSettings:autoDeferredPhotoDeliveryEnabled:responsiveCaptureEnabled:];
```

## Instance methods

```
-[AVCapturePhotoOutputReadinessCoordinator dealloc];
-[AVCapturePhotoOutputReadinessCoordinator captureReadiness];
-[AVCapturePhotoOutputReadinessCoordinator setDelegate:];
-[AVCapturePhotoOutputReadinessCoordinator _queue];
-[AVCapturePhotoOutputReadinessCoordinator delegate];
-[AVCapturePhotoOutputReadinessCoordinator initWithPhotoOutput:];
-[AVCapturePhotoOutputReadinessCoordinator _invokeDelegateCallbackWithBlock:];
-[AVCapturePhotoOutputReadinessCoordinator _photoOutputDidUpdateCaptureReadinessState:];
-[AVCapturePhotoOutputReadinessCoordinator _setDelegate:queue:];
-[AVCapturePhotoOutputReadinessCoordinator _updateCaptureReadinessWithDelegate:];
-[AVCapturePhotoOutputReadinessCoordinator startTrackingCaptureRequestUsingPhotoSettings:];
-[AVCapturePhotoOutputReadinessCoordinator stopTrackingCaptureRequestUsingPhotoSettingsUniqueID:];
```
