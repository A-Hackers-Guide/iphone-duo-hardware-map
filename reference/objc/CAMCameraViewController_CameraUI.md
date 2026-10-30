# `CAMCameraViewController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `CAMCaptureResultDelegate`, `CAMPersistenceResultDelegate`, `CAMCVCStillImageResultCoordinatorDelegate`, `CAMCaptureDelegate`, `CAMViewfinderPresentationDelegate`, `NSCoding`, `NSSecureCoding`
- 22 instance variables, 44 properties, 116 instance methods, 2 class methods

## Instance variables

```
B _automaticallyManagesCameraSession;
@"PAImageConversionServiceClient" __imageConversionClient;
@"PAVideoConversionServiceClient" __videoConversionClient;
@"<CAMCameraCaptureDelegate>" _captureDelegate;
@"CUCaptureController" _captureController;
@"CAMTimelapseController" _timelapseController;
@"CAMMotionController" _motionController;
@"CAMLocationController" _locationController;
@"CAMPowerController" _powerController;
@"CAMBurstController" _burstController;
@"CAMKeepAliveController" _keepAliveController;
@"CAMProtectionController" _protectionController;
@"CAMRemoteShutterController" _remoteShutterController;
@"CAMNebulaDaemonProxyManager" _nebulaDaemonProxyManager;
@"NSObject<OS_dispatch_queue>" __resultProcessingQueue;
@"NSMutableDictionary" __resultQueueStillImageResultCoordinators;
@"CAMThumbnailGenerator" __resultQueueThumbnailGenerator;
@"NSTimer" __spinnerTimer;
@"CAMViewfinderViewController" _viewfinderViewController;
@"<CAMCameraViewControllerPresentationDelegate>" _presentationDelegate;
@"<CAMCameraViewControllerCameraSessionDelegate>" _cameraSessionDelegate;
@"CAMPersistenceController" _persistenceController;
```

## Properties

```
@property (T@"CUCaptureController",R,N,V_captureController) captureController;
@property (T@"CAMTimelapseController",R,N,V_timelapseController) timelapseController;
@property (T@"CAMMotionController",R,N,V_motionController) motionController;
@property (T@"CAMLocationController",R,N,V_locationController) locationController;
@property (T@"CAMPowerController",R,N,V_powerController) powerController;
@property (T@"CAMBurstController",R,N,V_burstController) burstController;
@property (T@"CAMKeepAliveController",R,N,V_keepAliveController) keepAliveController;
@property (T@"CAMProtectionController",R,N,V_protectionController) protectionController;
@property (T@"CAMRemoteShutterController",R,N,V_remoteShutterController) remoteShutterController;
@property (T@"CAMNebulaDaemonProxyManager",R,N,V_nebulaDaemonProxyManager) nebulaDaemonProxyManager;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__resultProcessingQueue) _resultProcessingQueue;
@property (T@"NSMutableDictionary",R,N,V__resultQueueStillImageResultCoordinators) _resultQueueStillImageResultCoordinators;
@property (T@"CAMThumbnailGenerator",R,N,V__resultQueueThumbnailGenerator) _resultQueueThumbnailGenerator;
@property (T@"PAImageConversionServiceClient",R,N,V__imageConversionClient) _imageConversionClient;
@property (T@"PAVideoConversionServiceClient",R,N,V__videoConversionClient) _videoConversionClient;
@property (T@"NSTimer",&,N,V__spinnerTimer) _spinnerTimer;
@property (T@"CAMViewfinderViewController",R,N,V_viewfinderViewController) viewfinderViewController;
@property (TB,N,GisDisablingMultipleCaptureFeatures) disablingMultipleCaptureFeatures;
@property (TB,N,GisDisablingAdditionalCaptures) disablingAdditionalCaptures;
@property (TB,R,N,GisPreventingAdditionalCaptures) preventingAdditionalCaptures;
@property (TQ,N) persistenceBehavior;
@property (TB,N) automaticallyAdjustsApplicationIdleTimer;
@property (T@"<CAMCameraViewControllerPresentationDelegate>",W,N,V_presentationDelegate) presentationDelegate;
@property (TB,N,V_automaticallyManagesCameraSession) automaticallyManagesCameraSession;
@property (T@"<CAMCameraViewControllerCameraSessionDelegate>",W,N,V_cameraSessionDelegate) cameraSessionDelegate;
@property (Tq,R,N) messagesTransitionState;
@property (T@"CAMPersistenceController",R,N,V_persistenceController) persistenceController;
@property (T@"<CAMCameraConfigurationDelegate>",W,N) configurationDelegate;
@property (Tq,R,N) captureMode;
@property (Tq,R,N) captureDevice;
@property (Tq,N) flashMode;
@property (Tq,N) torchMode;
@property (Tq,N,SsetHDRMode:) hdrMode;
@property (Tq,N) timerDuration;
@property (Tq,N) livePhotoMode;
@property (Tq,N) photoModeAspectRatioCrop;
@property (T@"<CAMCameraCaptureDelegate>",W,N,V_captureDelegate) captureDelegate;
@property (TB,R,N,GisCapturingPhoto) capturingPhoto;
@property (TB,R,N,GisCapturingLivePhoto) capturingLivePhoto;
@property (TB,R,N,GisRecording) recording;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAMCameraViewController supportsSecureCoding];
+[CAMCameraViewController isEmulatingImagePicker];
```

## Instance methods

```
-[CAMCameraViewController hdrMode];
-[CAMCameraViewController isCapturingLivePhoto];
-[CAMCameraViewController setPersistenceBehavior:];
-[CAMCameraViewController setDisablingMultipleCaptureFeatures:];
-[CAMCameraViewController persistenceBehavior];
-[CAMCameraViewController captureDelegate];
-[CAMCameraViewController isCapturingPhoto];
-[CAMCameraViewController setTimerDuration:];
-[CAMCameraViewController configurationDelegate];
-[CAMCameraViewController startRecording];
-[CAMCameraViewController setConfigurationDelegate:];
-[CAMCameraViewController presentationDelegate];
-[CAMCameraViewController livePhotoMode];
-[CAMCameraViewController stopRecording];
-[CAMCameraViewController preferredStatusBarUpdateAnimation];
-[CAMCameraViewController photoModeAspectRatioCrop];
-[CAMCameraViewController capturePhoto];
-[CAMCameraViewController isRecording];
-[CAMCameraViewController setPresentationDelegate:];
-[CAMCameraViewController childViewControllerForHomeIndicatorAutoHidden];
-[CAMCameraViewController timerDuration];
-[CAMCameraViewController setHDRMode:];
-[CAMCameraViewController automaticallyAdjustsApplicationIdleTimer];
-[CAMCameraViewController captureDevice];
-[CAMCameraViewController locationController];
-[CAMCameraViewController nebulaDaemonProxyManager];
-[CAMCameraViewController dealloc];
-[CAMCameraViewController viewDidLoad];
-[CAMCameraViewController setMessagesTransitionState:animated:];
-[CAMCameraViewController captureController:didGenerateStillImageCaptureResult:fromRequest:];
-[CAMCameraViewController setTorchMode:];
-[CAMCameraViewController childViewControllerForStatusBarHidden];
-[CAMCameraViewController isDisablingAdditionalCaptures];
-[CAMCameraViewController protectionController];
-[CAMCameraViewController initWithNibName:bundle:];
-[CAMCameraViewController setCaptureDelegate:];
-[CAMCameraViewController motionController];
-[CAMCameraViewController viewWillAppear:];
-[CAMCameraViewController setAutomaticallyAdjustsApplicationIdleTimer:];
-[CAMCameraViewController setLivePhotoMode:];
-[CAMCameraViewController isDisablingMultipleCaptureFeatures];
-[CAMCameraViewController powerController];
-[CAMCameraViewController persistenceController];
-[CAMCameraViewController messagesTransitionState];
-[CAMCameraViewController viewfinderViewController];
-[CAMCameraViewController burstController];
-[CAMCameraViewController torchMode];
-[CAMCameraViewController keepAliveController];
-[CAMCameraViewController childViewControllerForScreenEdgesDeferringSystemGestures];
-[CAMCameraViewController setPhotoModeAspectRatioCrop:];
-[CAMCameraViewController captureMode];
-[CAMCameraViewController loadView];
-[CAMCameraViewController setFlashMode:];
-[CAMCameraViewController didReceiveMemoryWarning];
-[CAMCameraViewController viewDidDisappear:];
-[CAMCameraViewController flashMode];
-[CAMCameraViewController isPreventingAdditionalCaptures];
-[CAMCameraViewController initWithCoder:];
-[CAMCameraViewController remoteShutterController];
-[CAMCameraViewController timelapseController];
-[CAMCameraViewController setDisablingAdditionalCaptures:];
-[CAMCameraViewController captureController];
-[CAMCameraViewController handleReviewButtonReleased:];
-[CAMCameraViewController persistenceController:didCompleteAllLocalPersistenceForRequest:];
-[CAMCameraViewController _behaviorDefinedDestinationURLForRequest:withLocalDestinationURL:linkedDestinationURL:];
-[CAMCameraViewController _capturePersistenceBehaviorForViewfinderPersistenceBehavior:];
-[CAMCameraViewController _clientPropertiesForLivePhotoVideoURL:duration:stillDisplayTime:error:];
-[CAMCameraViewController _clientPropertiesForPhotoProperties:withFilteredImageURL:conversionOutputInfo:error:];
-[CAMCameraViewController _clientPropertiesForStillImageWithURL:captureMode:captureOrientation:previewSurface:previewOrientation:uniqueIdentifier:savedToPhotoLibrary:captureResult:];
-[CAMCameraViewController _clientPropertiesForVideoURL:renderedURL:duration:size:creationDate:captureOrientation:previewOrientation:adjustments:uniqueIdentifier:savedToPhotoLibrary:];
-[CAMCameraViewController _commonCAMCameraViewControllerInitializationWithOverrides:usingEmulationMode:initialLayoutStyle:privateOptions:];
-[CAMCameraViewController _exportPropertiesForClientProperties:];
-[CAMCameraViewController _handleCTMVideoLocalPersistenceResult:forCaptureResult:fromRequest:];
-[CAMCameraViewController _handleCTMVideoLocalPersistenceResult:forCaptureResult:fromRequest:size:videoURL:renderedToURL:renderedAdjustments:];
-[CAMCameraViewController _handleLivePhotoVideoLocalPersistenceResult:forCaptureResult:fromRequest:];
-[CAMCameraViewController _handlePhotoProperties:videoProperties:unfilteredPhotoProperties:unfilteredVideoProperties:assetAdjustments:attemptPairingVideo:error:];
-[CAMCameraViewController _handleVideoLocalPersistenceResult:forCaptureResult:fromRequest:];
-[CAMCameraViewController _imageConversionClient];
-[CAMCameraViewController _mediaConversionOptionsForAdjustments:mediaType:description:];
-[CAMCameraViewController _notifyCaptureDelegateOfCompletedCaptureOfLivePhoto:withProperties:error:];
-[CAMCameraViewController _notifyCaptureDelegateOfCompletedCaptureOfPhoto:withProperties:error:];
-[CAMCameraViewController _notifyCaptureDelegateOfCompletedCaptureOfVideo:withProperties:error:];
-[CAMCameraViewController _previewImageFromVideoURL:];
-[CAMCameraViewController _renderLivePhotoWithCoordinator:specifiers:photoProperties:videoProperties:adjustments:];
-[CAMCameraViewController _resultProcessingQueue];
-[CAMCameraViewController _resultQueueSafeImageFromSurface:imageOrientation:];
-[CAMCameraViewController _resultQueueStillImageResultCoordinators];
-[CAMCameraViewController _resultQueueThumbnailGenerator];
-[CAMCameraViewController _resultQueue_forceCompletionIfPossibleForRequest:];
-[CAMCameraViewController _resultQueue_getOrCreateStillImageResultCoordinatorForRequest:captureTimeExpectedResultSpecifiers:isExpectingPairedVideo:isDisablingMultipleCaptures:isGeneratingFilteredMedia:];
-[CAMCameraViewController _resultQueue_getStillImageResultCoordinatorForRequest:];
-[CAMCameraViewController _resultQueue_removeStillImageResultCoordinatorForIdentifier:];
-[CAMCameraViewController _spinnerTimer];
-[CAMCameraViewController _startShutterButtonSpinning:];
-[CAMCameraViewController _stopShutterButtonSpinning];
-[CAMCameraViewController _videoConversionClient];
-[CAMCameraViewController _viewfinderDidUpdateTransform];
-[CAMCameraViewController _viewfinderPersistenceBehaviorForCapturePersistenceBehavior:];
-[CAMCameraViewController automaticallyManagesCameraSession];
-[CAMCameraViewController cameraSessionDelegate];
-[CAMCameraViewController configureForCaptureMode:captureDevice:];
-[CAMCameraViewController initWithOverrides:initialLayoutStyle:privateOptions:];
-[CAMCameraViewController initWithOverrides:usingEmulationMode:];
-[CAMCameraViewController initWithOverrides:usingEmulationMode:privateOptions:];
-[CAMCameraViewController persistenceController:didGenerateStillImageLocalPersistenceResult:forCaptureResult:fromRequest:];
-[CAMCameraViewController persistenceController:didGenerateVideoLocalPersistenceResult:forCaptureResult:fromRequest:];
-[CAMCameraViewController resumeCameraSession];
-[CAMCameraViewController setAutomaticallyManagesCameraSession:];
-[CAMCameraViewController setCameraSessionDelegate:];
-[CAMCameraViewController set_spinnerTimer:];
-[CAMCameraViewController stillImagePersistenceCoordinator:requestsDispatchForResultSpecifiers:photoProperties:videoProperties:unfilteredPhotoProperties:unfilteredVideoProperties:assetAdjustments:error:];
-[CAMCameraViewController stillImagePersistenceCoordinatorDidCompleteAllDispatches:];
-[CAMCameraViewController suspendCameraSession];
-[CAMCameraViewController viewfinderViewControllerDidCompleteStillImageCapture:];
-[CAMCameraViewController viewfinderViewControllerDidUpdateViewportTransform:];
-[CAMCameraViewController viewfinderViewControllerRequestedDismissal:];
```
