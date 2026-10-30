# `CAMImagePickerCameraViewController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMCameraViewController`
- Protocols: `CAMCameraConfigurationDelegate`, `CAMCameraCaptureDelegate`, `PLVideoViewDelegate`, `PLCropOverlayDelegate`, `UIImagePickerCameraViewController`
- 17 instance variables, 26 properties, 103 instance methods, 1 class methods

## Instance variables

```
B _editingAllowed;
B _videoEditingAllowed;
B _currentlyReviewing;
B _usingTelephonyUI;
B _statusBarWasHidden;
i _photoSavingOptions;
@"UIView" _customOverlayView;
@"PLCropOverlay" __cropOverlay;
@"PLPhotoTileViewController" __photoTileViewController;
@"PLVideoView" __videoView;
@"NSDictionary" _mostRecentPhotoProperties;
@"NSDictionary" _mostRecentVideoProperties;
@"CAMVisualIntelligenceCameraConfiguration" __visualIntelligenceConfiguration;
@"NSDictionary" __fixedImagePickerProperties;
@"UIView" __opaqueBackgroundView;
@"CAMThumbnailGenerator" __visualIntelligenceThumbnailGenerator;
@"<CAMImagePickerCameraViewControllerVisualIntelligenceDelegate>" _visualIntelligenceDelegate;
```

## Properties

```
@property (T@"PLCropOverlay",R,N,V__cropOverlay) _cropOverlay;
@property (T@"PLPhotoTileViewController",R,N,V__photoTileViewController) _photoTileViewController;
@property (T@"PLVideoView",R,N,V__videoView) _videoView;
@property (TB,N,G_isEditingAllowed,S_setEditingAllowed:,V_editingAllowed) editingAllowed;
@property (TB,N,G_isVideoEditingAllowed,S_setVideoEditingAllowed:,V_videoEditingAllowed) videoEditingAllowed;
@property (TB,N,G_isCurrentlyReviewing,S_setCurrentlyReviewing:,V_currentlyReviewing) currentlyReviewing;
@property (TB,N,G_isUsingTelephonyUI,S_setUsingTelephonyUI:,V_usingTelephonyUI) usingTelephonyUI;
@property (Ti,N,G_photoSavingOptions,S_setPhotoSavingOptions:,V_photoSavingOptions) photoSavingOptions;
@property (T@"NSDictionary",C,N,G_mostRecentPhotoProperties,S_setMostRecentPhotoProperties:,V_mostRecentPhotoProperties) mostRecentPhotoProperties;
@property (T@"NSDictionary",C,N,G_mostRecentVideoProperties,S_setMostRecentVideoProperties:,V_mostRecentVideoProperties) mostRecentVideoProperties;
@property (TB,N,G_statusBarWasHidden,S_setStatusBarWasHidden:,V_statusBarWasHidden) statusBarWasHidden;
@property (T@"CAMVisualIntelligenceCameraConfiguration",R,C,N,V__visualIntelligenceConfiguration) _visualIntelligenceConfiguration;
@property (TB,R,N) _isVisualIntelligenceCamera;
@property (T@"NSDictionary",R,C,N,V__fixedImagePickerProperties) _fixedImagePickerProperties;
@property (T@"UIView",&,N,V__opaqueBackgroundView) _opaqueBackgroundView;
@property (T@"CAMThumbnailGenerator",&,N,V__visualIntelligenceThumbnailGenerator) _visualIntelligenceThumbnailGenerator;
@property (T@"<CAMImagePickerCameraViewControllerVisualIntelligenceDelegate>",W,N,V_visualIntelligenceDelegate) visualIntelligenceDelegate;
@property (TB,N,GisShowingStandardControls) showingStandardControls;
@property (Tq,N) imagePickerVideoQuality;
@property (Td,N) maximumVideoRecordingDuration;
@property (T@"UIView",&,N,V_customOverlayView) customOverlayView;
@property (T{CGAffineTransform=dddddd},N) customPreviewViewTransform;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAMImagePickerCameraViewController isEmulatingImagePicker];
```

## Instance methods

```
-[CAMImagePickerCameraViewController maximumVideoRecordingDuration];
-[CAMImagePickerCameraViewController isShowingStandardControls];
-[CAMImagePickerCameraViewController setShowingStandardControls:];
-[CAMImagePickerCameraViewController viewWillDisappear:];
-[CAMImagePickerCameraViewController setMaximumVideoRecordingDuration:];
-[CAMImagePickerCameraViewController viewWillAppear:];
-[CAMImagePickerCameraViewController _canShowWhileLocked];
-[CAMImagePickerCameraViewController setCustomOverlayView:];
-[CAMImagePickerCameraViewController _videoConfigurationForImagePickerQualityType:];
-[CAMImagePickerCameraViewController loadView];
-[CAMImagePickerCameraViewController customPreviewViewTransform];
-[CAMImagePickerCameraViewController setCustomPreviewViewTransform:];
-[CAMImagePickerCameraViewController viewWillLayoutSubviews];
-[CAMImagePickerCameraViewController customOverlayView];
-[CAMImagePickerCameraViewController _setStatusBarHidden:];
-[CAMImagePickerCameraViewController _cameraCaptureMode];
-[CAMImagePickerCameraViewController _cameraDevice];
-[CAMImagePickerCameraViewController _cameraFlashMode];
-[CAMImagePickerCameraViewController _cameraOverlayView];
-[CAMImagePickerCameraViewController _cameraViewTransform];
-[CAMImagePickerCameraViewController _imagePickerSavingOptions];
-[CAMImagePickerCameraViewController _setCameraCaptureMode:];
-[CAMImagePickerCameraViewController _setCameraDevice:];
-[CAMImagePickerCameraViewController _setCameraFlashMode:];
-[CAMImagePickerCameraViewController _setCameraOverlayView:];
-[CAMImagePickerCameraViewController _setCameraViewTransform:];
-[CAMImagePickerCameraViewController _setImagePickerMediaTypes:];
-[CAMImagePickerCameraViewController _setShowsCameraControls:];
-[CAMImagePickerCameraViewController _showsCameraControls];
-[CAMImagePickerCameraViewController _startVideoCapture];
-[CAMImagePickerCameraViewController _stopVideoCapture];
-[CAMImagePickerCameraViewController _takePicture];
-[CAMImagePickerCameraViewController initWithInitialImagePickerProperties:];
-[CAMImagePickerCameraViewController cropOverlayWasCancelled:];
-[CAMImagePickerCameraViewController handleReviewButtonReleased:];
-[CAMImagePickerCameraViewController cropOverlayWasOKed:];
-[CAMImagePickerCameraViewController _applyImagePickerProperties:savingOptions:];
-[CAMImagePickerCameraViewController _captureDeviceForImagePickerCameraDevice:];
-[CAMImagePickerCameraViewController _captureModeForImagePickerCameraCaptureMode:];
-[CAMImagePickerCameraViewController _containingImagePickerController];
-[CAMImagePickerCameraViewController _createCropOverlayIfNecessary];
-[CAMImagePickerCameraViewController _cropOverlay];
-[CAMImagePickerCameraViewController _currentCancelButtonTitle];
-[CAMImagePickerCameraViewController _fixedImagePickerProperties];
-[CAMImagePickerCameraViewController _flashModeForImagePickerCameraFlashMode:];
-[CAMImagePickerCameraViewController _handleCapturedImagePickerPhotoWithCropOverlayOutput:];
-[CAMImagePickerCameraViewController _handleCapturedImagePickerVideoAtPath:withEditingMetadata:];
-[CAMImagePickerCameraViewController _handleEditabilityChanged:];
-[CAMImagePickerCameraViewController _imagePickerCameraCaptureModeForCaptureMode:];
-[CAMImagePickerCameraViewController _imagePickerCameraDeviceForCaptureDevice:];
-[CAMImagePickerCameraViewController _imagePickerCameraFlashModeForFlashMode:];
-[CAMImagePickerCameraViewController _imagePickerProperties];
-[CAMImagePickerCameraViewController _imagePickerQualityTypeForVideoConfiguration:];
-[CAMImagePickerCameraViewController _isCurrentlyReviewing];
-[CAMImagePickerCameraViewController _isEditingAllowed];
-[CAMImagePickerCameraViewController _isUsingTelephonyUI];
-[CAMImagePickerCameraViewController _isVideoEditingAllowed];
-[CAMImagePickerCameraViewController _isVisualIntelligenceCamera];
-[CAMImagePickerCameraViewController _layoutPhotoTileViewController];
-[CAMImagePickerCameraViewController _mostRecentPhotoProperties];
-[CAMImagePickerCameraViewController _mostRecentVideoProperties];
-[CAMImagePickerCameraViewController _notifyVisualIntelligenceDelegateOfCapturedPhotoWithProperties:metadata:];
-[CAMImagePickerCameraViewController _opaqueBackgroundView];
-[CAMImagePickerCameraViewController _photoSavingOptions];
-[CAMImagePickerCameraViewController _photoTileViewController];
-[CAMImagePickerCameraViewController _removeFileAtPath:];
-[CAMImagePickerCameraViewController _resetRecentCaptureProperties];
-[CAMImagePickerCameraViewController _resetReviewViews];
-[CAMImagePickerCameraViewController _setCurrentlyReviewing:];
-[CAMImagePickerCameraViewController _setEditingAllowed:];
-[CAMImagePickerCameraViewController _setMostRecentPhotoProperties:];
-[CAMImagePickerCameraViewController _setMostRecentVideoProperties:];
-[CAMImagePickerCameraViewController _setPhotoSavingOptions:];
-[CAMImagePickerCameraViewController _setStatusBarWasHidden:];
-[CAMImagePickerCameraViewController _setUsingTelephonyUI:];
-[CAMImagePickerCameraViewController _setVideoEditingAllowed:];
-[CAMImagePickerCameraViewController _statusBarWasHidden];
-[CAMImagePickerCameraViewController _updateFromEditabilityChange];
-[CAMImagePickerCameraViewController _videoView];
-[CAMImagePickerCameraViewController _viewfinderDidUpdateTransform];
-[CAMImagePickerCameraViewController _visualIntelligenceConfiguration];
-[CAMImagePickerCameraViewController _visualIntelligenceThumbnailGenerator];
-[CAMImagePickerCameraViewController cameraViewController:didCaptureAVAsset:andAudioMix:withProperties:error:];
-[CAMImagePickerCameraViewController cameraViewController:didCapturePhoto:withProperties:error:];
-[CAMImagePickerCameraViewController cropOverlay:didFinishSaving:];
-[CAMImagePickerCameraViewController cropOverlayPause:];
-[CAMImagePickerCameraViewController cropOverlayPlay:];
-[CAMImagePickerCameraViewController cropOverlayWasToggled:];
-[CAMImagePickerCameraViewController imagePickerVideoQuality];
-[CAMImagePickerCameraViewController initWithInitialImagePickerProperties:options:];
-[CAMImagePickerCameraViewController initWithVisualIntelligenceConfiguration:];
-[CAMImagePickerCameraViewController photoTileViewControllerIsDisplayingLandscape:];
-[CAMImagePickerCameraViewController setImagePickerVideoQuality:];
-[CAMImagePickerCameraViewController setVisualIntelligenceDelegate:];
-[CAMImagePickerCameraViewController set_opaqueBackgroundView:];
-[CAMImagePickerCameraViewController set_visualIntelligenceThumbnailGenerator:];
-[CAMImagePickerCameraViewController videoViewCanBeginPlayback:];
-[CAMImagePickerCameraViewController videoViewDidBeginPlayback:];
-[CAMImagePickerCameraViewController videoViewDidEndPlayback:didFinish:];
-[CAMImagePickerCameraViewController videoViewDidPausePlayback:];
-[CAMImagePickerCameraViewController videoViewIsReadyToBeginPlayback:];
-[CAMImagePickerCameraViewController videoViewScrubberYOrigin:forOrientation:];
-[CAMImagePickerCameraViewController visualIntelligenceDelegate];
```
