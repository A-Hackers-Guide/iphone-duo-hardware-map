# `AVCapturePhotoSettings`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 38 properties, 160 instance methods, 14 class methods

## Instance variables

```
@"AVCapturePhotoSettingsInternal" _internal;
```

## Properties

```
@property (Tq,R) uniqueID;
@property (T@"NSDictionary",R,C) format;
@property (T@"NSDictionary",C,N) rawFileFormat;
@property (T@"NSString",R) processedFileType;
@property (TI,R) rawPhotoPixelFormatType;
@property (T@"NSString",R) rawFileType;
@property (Tq,N) flashMode;
@property (TB,N,GisAutoRedEyeReductionEnabled) autoRedEyeReductionEnabled;
@property (Tq,N) photoQualityPrioritization;
@property (TB,N,GisAutoStillImageStabilizationEnabled) autoStillImageStabilizationEnabled;
@property (TB,N,GisAutoVirtualDeviceFusionEnabled) autoVirtualDeviceFusionEnabled;
@property (TB,N,GisAutoDualCameraFusionEnabled) autoDualCameraFusionEnabled;
@property (T@"NSArray",C,N) virtualDeviceConstituentPhotoDeliveryEnabledDevices;
@property (TB,N,GisDualCameraDualPhotoDeliveryEnabled) dualCameraDualPhotoDeliveryEnabled;
@property (TB,N,GisHighResolutionPhotoEnabled) highResolutionPhotoEnabled;
@property (T{?=ii},N) maxPhotoDimensions;
@property (TB,N,GisDepthDataDeliveryEnabled) depthDataDeliveryEnabled;
@property (TB,N) embedsDepthDataInPhoto;
@property (TB,N,GisDepthDataFiltered) depthDataFiltered;
@property (TB,N,GisCameraCalibrationDataDeliveryEnabled) cameraCalibrationDataDeliveryEnabled;
@property (TB,N,GisPortraitEffectsMatteDeliveryEnabled) portraitEffectsMatteDeliveryEnabled;
@property (TB,N) embedsPortraitEffectsMatteInPhoto;
@property (T@"NSArray",C,N) enabledSemanticSegmentationMatteTypes;
@property (TB,N) embedsSemanticSegmentationMattesInPhoto;
@property (T@"NSDictionary",C,N) metadata;
@property (T@"NSURL",C,N) livePhotoMovieFileURL;
@property (T@"NSString",C,N) livePhotoVideoCodecType;
@property (T@"NSArray",C,N) livePhotoMovieMetadata;
@property (T@"NSArray",R,N) availablePreviewPhotoPixelFormatTypes;
@property (T@"NSDictionary",C,N) previewPhotoFormat;
@property (T@"NSArray",R,N) availableEmbeddedThumbnailPhotoCodecTypes;
@property (T@"NSDictionary",C,N) embeddedThumbnailPhotoFormat;
@property (T@"NSArray",R,N) availableRawEmbeddedThumbnailPhotoCodecTypes;
@property (T@"NSDictionary",C,N) rawEmbeddedThumbnailPhotoFormat;
@property (TB,N,GisAutoContentAwareDistortionCorrectionEnabled) autoContentAwareDistortionCorrectionEnabled;
@property (TB,N,GisConstantColorEnabled) constantColorEnabled;
@property (TB,N,GisConstantColorFallbackPhotoDeliveryEnabled) constantColorFallbackPhotoDeliveryEnabled;
@property (TB,N,GisShutterSoundSuppressionEnabled) shutterSoundSuppressionEnabled;
```

## Class methods

```
+[AVCapturePhotoSettings initialize];
+[AVCapturePhotoSettings uniqueID];
+[AVCapturePhotoSettings photoSettings];
+[AVCapturePhotoSettings photoSettingsWithFormat:];
+[AVCapturePhotoSettings photoSettingsFromPhotoSettings:];
+[AVCapturePhotoSettings burstQualityPhotoSettings];
+[AVCapturePhotoSettings incrementUniqueIDToValue:];
+[AVCapturePhotoSettings photoSettingsFromMomentCaptureSettings:withFormat:];
+[AVCapturePhotoSettings photoSettingsFromMomentCaptureSettings:withRawPixelFormatType:rawFileType:format:];
+[AVCapturePhotoSettings photoSettingsFromPhotoInitiationSettings:format:];
+[AVCapturePhotoSettings photoSettingsFromPhotoSettings:uniqueID:];
+[AVCapturePhotoSettings photoSettingsWithRawPixelFormatType:];
+[AVCapturePhotoSettings photoSettingsWithRawPixelFormatType:processedFormat:];
+[AVCapturePhotoSettings photoSettingsWithRawPixelFormatType:rawFileType:processedFormat:processedFileType:];
```

## Instance methods

```
-[AVCapturePhotoSettings videoFormat];
-[AVCapturePhotoSettings photoQualityPrioritization];
-[AVCapturePhotoSettings setVideoFormat:];
-[AVCapturePhotoSettings setVideoFileURL:];
-[AVCapturePhotoSettings rawFileType];
-[AVCapturePhotoSettings setConstantColorFallbackPhotoDeliveryEnabled:];
-[AVCapturePhotoSettings livePhotoContentIdentifier];
-[AVCapturePhotoSettings videoFileURL];
-[AVCapturePhotoSettings spatialOverCaptureMetadata];
-[AVCapturePhotoSettings setDualCameraDualPhotoDeliveryEnabled:];
-[AVCapturePhotoSettings previewFormatFourCC];
-[AVCapturePhotoSettings HEICSFileURL];
-[AVCapturePhotoSettings isPortraitEffectsMatteDeliveryEnabled];
-[AVCapturePhotoSettings setSemanticStyle:];
-[AVCapturePhotoSettings spatialOverCaptureLivePhotoMovieMetadataForOriginalPhoto];
-[AVCapturePhotoSettings isAutoDeferredProcessingEnabled];
-[AVCapturePhotoSettings rawEmbeddedThumbnailCGSize];
-[AVCapturePhotoSettings setSpatialOverCaptureLivePhotoMovieMetadataForOriginalPhoto:];
-[AVCapturePhotoSettings isBurstQualityCaptureEnabled];
-[AVCapturePhotoSettings spatialOverCaptureGroupIdentifierForOriginalPhoto];
-[AVCapturePhotoSettings _initWithFormat:processedFileType:rawPixelFormatType:rawFileType:burstQualityCaptureEnabled:uniqueID:exceptionReason:];
-[AVCapturePhotoSettings livePhotoVideoCodecType];
-[AVCapturePhotoSettings photoQualityPrioritizationIsSetByClient];
-[AVCapturePhotoSettings debugDescription];
-[AVCapturePhotoSettings spatialOverCaptureMetadataForOriginalPhoto];
-[AVCapturePhotoSettings setSpatialOverCaptureLivePhotoMovieFileURL:];
-[AVCapturePhotoSettings setHDRMode:];
-[AVCapturePhotoSettings isTextOrientationPrioritizationEnabled];
-[AVCapturePhotoSettings setSpatialOverCaptureLivePhotoMovieFileURLForOriginalPhoto:];
-[AVCapturePhotoSettings digitalFlashMode];
-[AVCapturePhotoSettings setEmbedsDepthDataInPhoto:];
-[AVCapturePhotoSettings init];
-[AVCapturePhotoSettings embeddedThumbnailPhotoFormat];
-[AVCapturePhotoSettings isProcessedPhotoZoomWithoutUpscalingEnabled];
-[AVCapturePhotoSettings embeddedThumbnailCGSize];
-[AVCapturePhotoSettings livePhotoMovieFileURLForOriginalPhoto];
-[AVCapturePhotoSettings setAutoDualCameraFusionEnabled:];
-[AVCapturePhotoSettings embedsDepthDataInPhoto];
-[AVCapturePhotoSettings spatialOverCaptureLivePhotoMovieFileURLForOriginalPhoto];
-[AVCapturePhotoSettings spatialOverCaptureLivePhotoContentIdentifier];
-[AVCapturePhotoSettings setSquareCropEnabled:];
-[AVCapturePhotoSettings isAutoVirtualDeviceFusionEnabled];
-[AVCapturePhotoSettings rawEmbeddedThumbnailFormatFourCC];
-[AVCapturePhotoSettings dealloc];
-[AVCapturePhotoSettings arePreviewPhotoFormatDimensionsLimitedToDisplayDimensions];
-[AVCapturePhotoSettings isAutoSecureSigningPhotoCaptureEnabled];
-[AVCapturePhotoSettings setPreviewPhotoFormatDimensionsLimitedToDisplayDimensions:];
-[AVCapturePhotoSettings setRawFileFormat:];
-[AVCapturePhotoSettings isDepthDataFiltered];
-[AVCapturePhotoSettings isAutoSpatialOverCaptureEnabled];
-[AVCapturePhotoSettings setDigitalFlashMode:];
-[AVCapturePhotoSettings formatFourCC];
-[AVCapturePhotoSettings setAutoDeferredProcessingEnabled:];
-[AVCapturePhotoSettings setLivePhotoContentIdentifierForOriginalPhoto:];
-[AVCapturePhotoSettings setPersonalPhotographerCaptureRate:];
-[AVCapturePhotoSettings processedPhotoZoomWithoutUpscalingAspectRatio];
-[AVCapturePhotoSettings spatialOverCaptureLivePhotoMovieFileURL];
-[AVCapturePhotoSettings personalPhotographerCaptureRate];
-[AVCapturePhotoSettings rawEmbeddedThumbnailPhotoFormat];
-[AVCapturePhotoSettings setLivePhotoMovieFileURL:];
-[AVCapturePhotoSettings isDualCameraDualPhotoDeliveryEnabled];
-[AVCapturePhotoSettings uniqueID];
-[AVCapturePhotoSettings metadata];
-[AVCapturePhotoSettings embeddedThumbnailFormatFourCC];
-[AVCapturePhotoSettings setLivePhotoMovieFileURLForOriginalPhoto:];
-[AVCapturePhotoSettings setPreviewPhotoFormat:];
-[AVCapturePhotoSettings isAutoRedEyeReductionEnabled];
-[AVCapturePhotoSettings _setPhotoQualityPrioritization:];
-[AVCapturePhotoSettings isSquareCropEnabled];
-[AVCapturePhotoSettings setHighResolutionPhotoEnabled:];
-[AVCapturePhotoSettings setPortraitEffectsMatteDeliveryEnabled:];
-[AVCapturePhotoSettings adjustedPhotoFilters];
-[AVCapturePhotoSettings setTextOrientationPrioritizationEnabled:];
-[AVCapturePhotoSettings isAutoDualCameraFusionEnabled];
-[AVCapturePhotoSettings _setPropertiesFromMomentCaptureSettings:];
-[AVCapturePhotoSettings rawPhotoPixelFormatType];
-[AVCapturePhotoSettings setVirtualDeviceConstituentPhotoDeliveryEnabledDevices:];
-[AVCapturePhotoSettings embedsSemanticSegmentationMattesInPhoto];
-[AVCapturePhotoSettings isConstantColorFallbackPhotoDeliveryEnabled];
-[AVCapturePhotoSettings isDepthDataDeliveryEnabled];
-[AVCapturePhotoSettings virtualDeviceConstituentPhotoDeliveryEnabledDevices];
-[AVCapturePhotoSettings photoFilters];
-[AVCapturePhotoSettings isConstantColorEnabled];
-[AVCapturePhotoSettings livePhotoMovieMetadataForOriginalPhoto];
-[AVCapturePhotoSettings setPhotoFilters:];
-[AVCapturePhotoSettings spatialOverCaptureLivePhotoContentIdentifierForOriginalPhoto];
-[AVCapturePhotoSettings semanticStyle];
-[AVCapturePhotoSettings shutterSound];
-[AVCapturePhotoSettings isCameraCalibrationDataDeliveryEnabled];
-[AVCapturePhotoSettings isTurboModeEnabled];
-[AVCapturePhotoSettings setProcessedPhotoZoomWithoutUpscalingAspectRatio:];
-[AVCapturePhotoSettings isAutoContentAwareDistortionCorrectionEnabled];
-[AVCapturePhotoSettings setEmbedsPortraitEffectsMatteInPhoto:];
-[AVCapturePhotoSettings setFlashMode:];
-[AVCapturePhotoSettings setEV0PhotoDeliveryEnabled:];
-[AVCapturePhotoSettings setEmbeddedThumbnailPhotoFormat:];
-[AVCapturePhotoSettings spatialOverCaptureLivePhotoMovieMetadata];
-[AVCapturePhotoSettings setMetadata:];
-[AVCapturePhotoSettings setAutoContentAwareDistortionCorrectionEnabled:];
-[AVCapturePhotoSettings _setHighResolutionPhotoEnabled:];
-[AVCapturePhotoSettings rawFileFormat];
-[AVCapturePhotoSettings processedPhotoAspectRatio];
-[AVCapturePhotoSettings setShutterSound:];
-[AVCapturePhotoSettings embedsPortraitEffectsMatteInPhoto];
-[AVCapturePhotoSettings setAutoRedEyeReductionEnabled:];
-[AVCapturePhotoSettings setSpatialOverCaptureLivePhotoMovieMetadata:];
-[AVCapturePhotoSettings description];
-[AVCapturePhotoSettings isShutterSoundSuppressionEnabled];
-[AVCapturePhotoSettings setUserInitiatedPhotoRequestTime:];
-[AVCapturePhotoSettings flashMode];
-[AVCapturePhotoSettings maxPhotoDimensions];
-[AVCapturePhotoSettings availableRawEmbeddedThumbnailPhotoCodecTypes];
-[AVCapturePhotoSettings previewPhotoFormat];
-[AVCapturePhotoSettings setLivePhotoContentIdentifier:];
-[AVCapturePhotoSettings setProcessedPhotoZoomWithoutUpscalingEnabled:];
-[AVCapturePhotoSettings _sanitizedLivePhotoMovieMetadataForArray:exceptionReason:];
-[AVCapturePhotoSettings setConstantColorEnabled:];
-[AVCapturePhotoSettings setDepthDataDeliveryEnabled:];
-[AVCapturePhotoSettings isAutoSpatialPhotoCaptureEnabled];
-[AVCapturePhotoSettings setAutoSpatialPhotoCaptureEnabled:];
-[AVCapturePhotoSettings setLivePhotoMovieMetadata:];
-[AVCapturePhotoSettings previewCGSize];
-[AVCapturePhotoSettings processedFileType];
-[AVCapturePhotoSettings livePhotoMovieMetadata];
-[AVCapturePhotoSettings setAutoStillImageStabilizationEnabled:];
-[AVCapturePhotoSettings setDepthDataFiltered:];
-[AVCapturePhotoSettings setAdjustedPhotoFilters:];
-[AVCapturePhotoSettings setCameraCalibrationDataDeliveryEnabled:];
-[AVCapturePhotoSettings setHEICSFileURL:];
-[AVCapturePhotoSettings setShutterSoundSuppressionEnabled:];
-[AVCapturePhotoSettings setMaxPhotoDimensions:];
-[AVCapturePhotoSettings availablePreviewPhotoPixelFormatTypes];
-[AVCapturePhotoSettings availableEmbeddedThumbnailPhotoCodecTypes];
-[AVCapturePhotoSettings setEnabledSemanticSegmentationMatteTypes:];
-[AVCapturePhotoSettings copyWithZone:];
-[AVCapturePhotoSettings setEmbedsSemanticSegmentationMattesInPhoto:];
-[AVCapturePhotoSettings setLivePhotoVideoCodecType:];
-[AVCapturePhotoSettings setAutoVirtualDeviceFusionEnabled:];
-[AVCapturePhotoSettings setVideoFileMetadata:];
-[AVCapturePhotoSettings setTurboModeEnabled:];
-[AVCapturePhotoSettings isEV0PhotoDeliveryEnabled];
-[AVCapturePhotoSettings setAutoSecureSigningPhotoCaptureEnabled:];
-[AVCapturePhotoSettings setLivePhotoMovieMetadataForOriginalPhoto:];
-[AVCapturePhotoSettings livePhotoContentIdentifierForOriginalPhoto];
-[AVCapturePhotoSettings spatialOverCaptureGroupIdentifier];
-[AVCapturePhotoSettings enabledSemanticSegmentationMatteTypes];
-[AVCapturePhotoSettings setPhotoQualityPrioritization:];
-[AVCapturePhotoSettings setRawEmbeddedThumbnailPhotoFormat:];
-[AVCapturePhotoSettings format];
-[AVCapturePhotoSettings isHighResolutionPhotoEnabled];
-[AVCapturePhotoSettings livePhotoMovieFileURL];
-[AVCapturePhotoSettings videoFileMetadata];
-[AVCapturePhotoSettings userInitiatedPhotoRequestTime];
-[AVCapturePhotoSettings setSpatialOverCaptureMetadata:];
-[AVCapturePhotoSettings setProcessedPhotoAspectRatio:];
-[AVCapturePhotoSettings metadataForOriginalPhoto];
-[AVCapturePhotoSettings isAutoStillImageStabilizationEnabled];
-[AVCapturePhotoSettings HDRMode];
-[AVCapturePhotoSettings setAutoSpatialOverCaptureEnabled:];
-[AVCapturePhotoSettings setSpatialOverCaptureMetadataForOriginalPhoto:];
```
