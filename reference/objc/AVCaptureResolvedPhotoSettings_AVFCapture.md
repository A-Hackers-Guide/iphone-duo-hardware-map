# `AVCaptureResolvedPhotoSettings`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 18 properties, 39 instance methods, 2 class methods

## Instance variables

```
@"AVCaptureResolvedPhotoSettingsInternal" _internal;
B _fastCapturePrioritizationEnabled;
```

## Properties

```
@property (Tq,R) uniqueID;
@property (T{?=ii},R) photoDimensions;
@property (T{?=ii},R) rawPhotoDimensions;
@property (T{?=ii},R) previewDimensions;
@property (T{?=ii},R) embeddedThumbnailDimensions;
@property (T{?=ii},R) rawEmbeddedThumbnailDimensions;
@property (T{?=ii},R) portraitEffectsMatteDimensions;
@property (T{?=ii},R) livePhotoMovieDimensions;
@property (TB,R,GisFlashEnabled) flashEnabled;
@property (TB,R,GisRedEyeReductionEnabled) redEyeReductionEnabled;
@property (T{?=ii},R) deferredPhotoProxyDimensions;
@property (TB,R,GisStillImageStabilizationEnabled) stillImageStabilizationEnabled;
@property (TB,R,GisVirtualDeviceFusionEnabled) virtualDeviceFusionEnabled;
@property (TB,R,GisDualCameraFusionEnabled) dualCameraFusionEnabled;
@property (TQ,R) expectedPhotoCount;
@property (T{?={?=qiIq}{?=qiIq}},R) photoProcessingTimeRange;
@property (TB,R,GisContentAwareDistortionCorrectionEnabled) contentAwareDistortionCorrectionEnabled;
@property (TB,R,GisFastCapturePrioritizationEnabled,V_fastCapturePrioritizationEnabled) fastCapturePrioritizationEnabled;
```

## Class methods

```
+[AVCaptureResolvedPhotoSettings initialize];
+[AVCaptureResolvedPhotoSettings resolvedSettingsWithUniqueID:photoDimensions:rawPhotoDimensions:previewDimensions:embeddedThumbnailDimensions:rawEmbeddedThumbnailDimensions:livePhotoMovieEnabled:livePhotoMovieDimensions:livePhotoAssetIdentifier:portraitEffectsMatteDimensions:hairSegmentationMatteDimensions:skinSegmentationMatteDimensions:teethSegmentationMatteDimensions:glassesSegmentationMatteDimensions:spatialOverCapturePhotoDimensions:turboModeEnabled:flashEnabled:redEyeReductionEnabled:HDREnabled:adjustedPhotoFiltersEnabled:EV0PhotoDeliveryEnabled:stillImageStabilizationEnabled:virtualDeviceFusionEnabled:squareCropEnabled:deferredPhotoProxyDimensions:photoProcessingTimeRange:contentAwareDistortionCorrectionEnabled:spatialPhotoCaptureEnabled:photoManifest:digitalFlashUserInterfaceHints:digitalFlashUserInterfaceRGBEstimate:captureBeforeResolvingSettingsEnabled:secureSigningPhotoCapturePhotoEnabled:personalPhotographerDuplicateInfo:];
```

## Instance methods

```
-[AVCaptureResolvedPhotoSettings isSpatialPhotoCaptureEnabled];
-[AVCaptureResolvedPhotoSettings debugDescription];
-[AVCaptureResolvedPhotoSettings previewDimensions];
-[AVCaptureResolvedPhotoSettings dealloc];
-[AVCaptureResolvedPhotoSettings isFastCapturePrioritizationEnabled];
-[AVCaptureResolvedPhotoSettings uniqueID];
-[AVCaptureResolvedPhotoSettings isContentAwareDistortionCorrectionEnabled];
-[AVCaptureResolvedPhotoSettings isSquareCropEnabled];
-[AVCaptureResolvedPhotoSettings deferredPhotoProxyDimensions];
-[AVCaptureResolvedPhotoSettings isTurboModeEnabled];
-[AVCaptureResolvedPhotoSettings photoManifest];
-[AVCaptureResolvedPhotoSettings description];
-[AVCaptureResolvedPhotoSettings expectedPhotoCount];
-[AVCaptureResolvedPhotoSettings isEV0PhotoDeliveryEnabled];
-[AVCaptureResolvedPhotoSettings isSecureSigningPhotoCaptureEnabled];
-[AVCaptureResolvedPhotoSettings livePhotoMovieDimensions];
-[AVCaptureResolvedPhotoSettings isHDREnabled];
-[AVCaptureResolvedPhotoSettings photoDimensions];
-[AVCaptureResolvedPhotoSettings _initWithUniqueID:photoDimensions:rawPhotoDimensions:previewDimensions:embeddedThumbnailDimensions:rawEmbeddedThumbnailDimensions:livePhotoMovieEnabled:livePhotoMovieDimensions:livePhotoAssetIdentifier:portraitEffectsMatteDimensions:hairSegmentationMatteDimensions:skinSegmentationMatteDimensions:teethSegmentationMatteDimensions:glassesSegmentationMatteDimensions:spatialOverCapturePhotoDimensions:turboModeEnabled:flashEnabled:redEyeReductionEnabled:HDREnabled:adjustedPhotoFiltersEnabled:EV0PhotoDeliveryEnabled:stillImageStabilizationEnabled:virtualDeviceFusionEnabled:squareCropEnabled:deferredPhotoProxyDimensions:photoProcessingTimeRange:contentAwareDistortionCorrectionEnabled:spatialPhotoCaptureEnabled:photoManifest:digitalFlashUserInterfaceHints:digitalFlashUserInterfaceRGBEstimate:captureBeforeResolvingSettingsEnabled:secureSigningPhotoCapturePhotoEnabled:personalPhotographerDuplicateInfo:];
-[AVCaptureResolvedPhotoSettings digitalFlashRGBEstimate];
-[AVCaptureResolvedPhotoSettings digitalFlashUserInterfaceHints];
-[AVCaptureResolvedPhotoSettings digitalFlashUserInterfaceRGBEstimate];
-[AVCaptureResolvedPhotoSettings dimensionsForSemanticSegmentationMatteOfType:];
-[AVCaptureResolvedPhotoSettings embeddedThumbnailDimensions];
-[AVCaptureResolvedPhotoSettings isAdjustedPhotoFilterRenderingEnabled];
-[AVCaptureResolvedPhotoSettings isCaptureBeforeResolvingSettingsEnabled];
-[AVCaptureResolvedPhotoSettings isDualCameraFusionEnabled];
-[AVCaptureResolvedPhotoSettings isFlashEnabled];
-[AVCaptureResolvedPhotoSettings isRedEyeReductionEnabled];
-[AVCaptureResolvedPhotoSettings isStillImageStabilizationEnabled];
-[AVCaptureResolvedPhotoSettings isVirtualDeviceFusionEnabled];
-[AVCaptureResolvedPhotoSettings livePhotoAssetIdentifier];
-[AVCaptureResolvedPhotoSettings livePhotoMovieEnabled];
-[AVCaptureResolvedPhotoSettings personalPhotographerDuplicateInfo];
-[AVCaptureResolvedPhotoSettings photoProcessingTimeRange];
-[AVCaptureResolvedPhotoSettings portraitEffectsMatteDimensions];
-[AVCaptureResolvedPhotoSettings rawEmbeddedThumbnailDimensions];
-[AVCaptureResolvedPhotoSettings rawPhotoDimensions];
-[AVCaptureResolvedPhotoSettings spatialOverCapturePhotoDimensions];
```
