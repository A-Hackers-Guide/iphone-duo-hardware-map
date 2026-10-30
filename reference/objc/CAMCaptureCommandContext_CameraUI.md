# `CAMCaptureCommandContext`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 28 instance variables, 32 properties, 94 instance methods, 0 class methods

## Instance variables

```
@"AVCaptureSession" _currentCaptureSession;
@"AVCaptureDevice" _currentVideoDevice;
@"AVCaptureDeviceFormat" _currentVideoDeviceFormat;
@"AVCaptureDeviceFormat" _currentDepthDataFormat;
@"NSString" _currentVideoDevicePreset;
@"AVCaptureDeviceInput" _currentVideoDeviceInput;
@"AVCaptureDevice" _currentSecondaryVideoDevice;
@"AVCaptureDeviceFormat" _currentSecondaryVideoDeviceFormat;
@"AVCaptureDeviceInput" _currentSecondaryVideoDeviceInput;
@"AVCaptureDevice" _currentAudioDevice;
@"AVCaptureDeviceInput" _currentAudioDeviceInput;
@"AVCapturePhotoOutput" _currentStillImageOutput;
@"AVCaptureMovieFileOutput" _currentMovieFileOutput;
@"CAMPanoramaOutput" _currentPanoramaOutput;
@"AVCaptureMetadataOutput" _currentMetadataOutput;
@"AVCaptureVideoDataOutput" _currentEffectsPreviewOutput;
@"AVCaptureVideoThumbnailOutput" _currentVideoThumbnailOutput;
@"AVCaptureSystemZoomSlider" _systemZoomSlider;
@"AVCaptureSystemExposureBiasSlider" _systemExposureBiasSlider;
@"AVCaptureSlider" _apertureSlider;
@"AVCaptureSlider" _emulatedZoomSlider;
@"AVCaptureSystemLensSelector" _lensSelector;
@"AVCaptureVideoPreviewLayer" _currentVideoPreviewLayer;
@"AVCaptureVideoPreviewLayer" _currentDuplicateVideoPreviewLayer;
@"AVCaptureVideoPreviewLayer" _currentSecondaryVideoPreviewLayer;
@"LiveVideoAnalyticsAdaptor" _currentVideoAnalyticsAdaptor;
@"CAMCaptureEngine" __captureEngine;
@"AVCaptureSystemLensSelector" _systemLensSelector;
```

## Properties

```
@property (T@"CAMCaptureEngine",R,W,N,V__captureEngine) _captureEngine;
@property (T@"AVCaptureSession",&,N,V_currentCaptureSession) currentCaptureSession;
@property (T@"AVCaptureDevice",&,N,V_currentVideoDevice) currentVideoDevice;
@property (T@"AVCaptureDeviceFormat",&,N,V_currentVideoDeviceFormat) currentVideoDeviceFormat;
@property (T@"AVCaptureDeviceFormat",&,N,V_currentDepthDataFormat) currentDepthDataFormat;
@property (T@"NSString",&,N,V_currentVideoDevicePreset) currentVideoDevicePreset;
@property (T@"AVCaptureDeviceInput",&,N,V_currentVideoDeviceInput) currentVideoDeviceInput;
@property (T@"AVCaptureDevice",&,N,V_currentSecondaryVideoDevice) currentSecondaryVideoDevice;
@property (T@"AVCaptureDeviceFormat",&,N,V_currentSecondaryVideoDeviceFormat) currentSecondaryVideoDeviceFormat;
@property (T@"AVCaptureDeviceInput",&,N,V_currentSecondaryVideoDeviceInput) currentSecondaryVideoDeviceInput;
@property (T@"AVCaptureDevice",&,N,V_currentAudioDevice) currentAudioDevice;
@property (T@"AVCaptureDeviceInput",&,N,V_currentAudioDeviceInput) currentAudioDeviceInput;
@property (T@"AVCapturePhotoOutput",&,N,V_currentStillImageOutput) currentStillImageOutput;
@property (T@"AVCaptureMovieFileOutput",&,N,V_currentMovieFileOutput) currentMovieFileOutput;
@property (T@"CAMPanoramaOutput",&,N,V_currentPanoramaOutput) currentPanoramaOutput;
@property (T@"AVCaptureMetadataOutput",&,N,V_currentMetadataOutput) currentMetadataOutput;
@property (T@"AVCaptureVideoDataOutput",&,N,V_currentEffectsPreviewOutput) currentEffectsPreviewOutput;
@property (T@"AVCaptureVideoThumbnailOutput",&,N,V_currentVideoThumbnailOutput) currentVideoThumbnailOutput;
@property (T@"LiveVideoAnalyticsAdaptor",&,N,V_currentVideoAnalyticsAdaptor) currentVideoAnalyticsAdaptor;
@property (T@"AVCaptureSystemZoomSlider",&,N,V_systemZoomSlider) systemZoomSlider;
@property (T@"AVCaptureSystemLensSelector",&,N,V_systemLensSelector) systemLensSelector;
@property (T@"AVCaptureSystemExposureBiasSlider",&,N,V_systemExposureBiasSlider) systemExposureBiasSlider;
@property (T@"AVCaptureSlider",&,N,V_apertureSlider) apertureSlider;
@property (T@"AVCaptureSlider",&,N,V_emulatedZoomSlider) emulatedZoomSlider;
@property (T@"AVCaptureVideoPreviewLayer",&,N,V_currentVideoPreviewLayer) currentVideoPreviewLayer;
@property (T@"AVCaptureVideoPreviewLayer",&,N,V_currentDuplicateVideoPreviewLayer) currentDuplicateVideoPreviewLayer;
@property (T@"AVCaptureVideoPreviewLayer",&,N,V_currentSecondaryVideoPreviewLayer) currentSecondaryVideoPreviewLayer;
@property (T@"AVCaptureSystemLensSelector",R,N,V_lensSelector) lensSelector;
@property (T@"<AVCaptureFileOutputRecordingDelegatePrivate>",R,W,N) currentRecordingDelegate;
@property (T@"CAMPanoramaConfiguration",R,N) currentPanoramaConfiguration;
@property (T@"<AVCapturePhotoCaptureDelegatePrivate>",R,W,N) currentStillImageDelegate;
@property (T@"<AVMomentCaptureMovieRecordingDelegate>",R,W,N) currentMomentCaptureMovieRecordingDelegate;
```

## Instance methods

```
-[CAMCaptureCommandContext currentStillImageDelegate];
-[CAMCaptureCommandContext currentVideoThumbnailOutput];
-[CAMCaptureCommandContext currentRecordingDelegate];
-[CAMCaptureCommandContext _shouldEnableApertureSliderForMode:devicePosition:depthSuggestionEnabled:recording:];
-[CAMCaptureCommandContext clear];
-[CAMCaptureCommandContext systemZoomSlider];
-[CAMCaptureCommandContext setSystemExposureBiasSlider:];
-[CAMCaptureCommandContext initWithCaptureEngine:];
-[CAMCaptureCommandContext registerPersonalPhotographerCaptureRequest:withSettings:];
-[CAMCaptureCommandContext setCurrentSecondaryVideoDeviceFormat:];
-[CAMCaptureCommandContext _captureEngineDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:resolvedDevice:];
-[CAMCaptureCommandContext setSystemLensSelector:];
-[CAMCaptureCommandContext _shouldEnableSystemZoomSliderForMode:devicePosition:];
-[CAMCaptureCommandContext updateControlEnablementForRecording:mode:devicePosition:depthSuggestionEnabled:styledCaptureAllowed:];
-[CAMCaptureCommandContext videoDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:resolvedDevice:];
-[CAMCaptureCommandContext _isPersonalPhotographerSessionActive];
-[CAMCaptureCommandContext currentMomentCaptureMovieRecordingDelegate];
-[CAMCaptureCommandContext setCurrentVideoDeviceFormat:];
-[CAMCaptureCommandContext setCurrentSecondaryVideoPreviewLayer:];
-[CAMCaptureCommandContext setSystemZoomSlider:];
-[CAMCaptureCommandContext currentSecondaryVideoPreviewLayer];
-[CAMCaptureCommandContext currentMetadataOutput];
-[CAMCaptureCommandContext apertureSlider];
-[CAMCaptureCommandContext setCurrentVideoDevice:];
-[CAMCaptureCommandContext primaryOutputForMode:graphConfiguration:];
-[CAMCaptureCommandContext clearCachedMomentCaptureSettingsForIdentifier:];
-[CAMCaptureCommandContext setCurrentVideoPreviewLayer:];
-[CAMCaptureCommandContext setCurrentVideoAnalyticsAdaptor:];
-[CAMCaptureCommandContext currentEffectsPreviewOutput];
-[CAMCaptureCommandContext stopPanoramaCaptureInterrupted:];
-[CAMCaptureCommandContext setCurrentAudioDevice:];
-[CAMCaptureCommandContext setEmulatedZoomSlider:];
-[CAMCaptureCommandContext setCurrentVideoThumbnailOutput:];
-[CAMCaptureCommandContext startPanoramaCaptureWithRequest:];
-[CAMCaptureCommandContext currentStillImageOutput];
-[CAMCaptureCommandContext updateOverlayStylePickerSelectionForSmartStyle:];
-[CAMCaptureCommandContext currentAudioDevice];
-[CAMCaptureCommandContext updateStyleControlEnablementForCaptureMode:styledCaptureAllowed:recording:];
-[CAMCaptureCommandContext currentPanoramaOutput];
-[CAMCaptureCommandContext updateLensSelectorForRecording:mode:devicePosition:];
-[CAMCaptureCommandContext registerStillImageCaptureRequest:withSettings:];
-[CAMCaptureCommandContext _shouldEnableStyleControlsForMode:recording:styledCaptureAllowed:];
-[CAMCaptureCommandContext detachVideoAnalyticsAdaptorFromEffectsPreview];
-[CAMCaptureCommandContext setCurrentPanoramaOutput:];
-[CAMCaptureCommandContext currentSecondaryVideoDevice];
-[CAMCaptureCommandContext emulatedZoomSlider];
-[CAMCaptureCommandContext _shouldEnableSystemExposureForRecording:mode:];
-[CAMCaptureCommandContext currentVideoPreviewLayer];
-[CAMCaptureCommandContext setCurrentVideoDeviceInput:];
-[CAMCaptureCommandContext _metadataOutputForMode:];
-[CAMCaptureCommandContext secondaryVideoPreviewLayerForGraphConfiguration:];
-[CAMCaptureCommandContext setCurrentEffectsPreviewOutput:];
-[CAMCaptureCommandContext setCurrentSecondaryVideoDevice:];
-[CAMCaptureCommandContext currentDuplicateVideoPreviewLayer];
-[CAMCaptureCommandContext systemExposureBiasSlider];
-[CAMCaptureCommandContext cachedMomentCaptureSettingsForIdentifier:];
-[CAMCaptureCommandContext setCurrentVideoDevicePreset:];
-[CAMCaptureCommandContext setCurrentMovieFileOutput:];
-[CAMCaptureCommandContext currentCaptureSession];
-[CAMCaptureCommandContext audioDeviceInput];
-[CAMCaptureCommandContext primaryVideoPreviewLayerForGraphConfiguration:];
-[CAMCaptureCommandContext currentAudioDeviceInput];
-[CAMCaptureCommandContext systemLensSelector];
-[CAMCaptureCommandContext currentVideoDevice];
-[CAMCaptureCommandContext currentVideoDeviceInput];
-[CAMCaptureCommandContext registerVideoEndZoomFactor:];
-[CAMCaptureCommandContext currentVideoAnalyticsAdaptor];
-[CAMCaptureCommandContext attachVideoAnalyticsAdaptorToEffectsPreview];
-[CAMCaptureCommandContext controlsForGraphConfiguration:recording:];
-[CAMCaptureCommandContext currentVideoDeviceFormat];
-[CAMCaptureCommandContext createVideoAnalyticsAdaptorIfNeeded];
-[CAMCaptureCommandContext _captureEngine];
-[CAMCaptureCommandContext currentVideoDevicePreset];
-[CAMCaptureCommandContext setCurrentMetadataOutput:];
-[CAMCaptureCommandContext outputsForGraphConfiguration:];
-[CAMCaptureCommandContext _shouldEnableLensSelectorForMode:devicePosition:recording:];
-[CAMCaptureCommandContext currentSecondaryVideoDeviceInput];
-[CAMCaptureCommandContext setCurrentCaptureSession:];
-[CAMCaptureCommandContext duplicateVideoPreviewLayerForGraphConfiguration:];
-[CAMCaptureCommandContext cacheMomentCaptureSettings:forIdentifier:];
-[CAMCaptureCommandContext registerVideoCaptureRequest:];
-[CAMCaptureCommandContext setCurrentSecondaryVideoDeviceInput:];
-[CAMCaptureCommandContext setCurrentAudioDeviceInput:];
-[CAMCaptureCommandContext lensSelector];
-[CAMCaptureCommandContext setCurrentDepthDataFormat:];
-[CAMCaptureCommandContext setApertureSlider:];
-[CAMCaptureCommandContext currentDepthDataFormat];
-[CAMCaptureCommandContext currentPanoramaConfiguration];
-[CAMCaptureCommandContext setCurrentStillImageOutput:];
-[CAMCaptureCommandContext ensureMultiCamPictureInPictureCompositingResources];
-[CAMCaptureCommandContext currentSecondaryVideoDeviceFormat];
-[CAMCaptureCommandContext setCurrentDuplicateVideoPreviewLayer:];
-[CAMCaptureCommandContext _shouldOfferStyleControlsForMode:device:];
-[CAMCaptureCommandContext currentMovieFileOutput];
```
