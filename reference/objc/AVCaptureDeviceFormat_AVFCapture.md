# `AVCaptureDeviceFormat`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 35 properties, 186 instance methods, 1 class methods

## Instance variables

```
@"AVCaptureDeviceFormatInternal" _internal;
```

## Properties

```
@property (T@"NSString",R,N) mediaType;
@property (T^{opaqueCMFormatDescription=},R,N) formatDescription;
@property (T@"NSArray",R,N) videoSupportedFrameRateRanges;
@property (Tf,R,N) videoFieldOfView;
@property (TB,R,N,GisVideoBinned) videoBinned;
@property (TB,R,N,GisVideoStabilizationSupported) videoStabilizationSupported;
@property (Td,R,N) videoMaxZoomFactor;
@property (Td,R,N) videoZoomFactorUpscaleThreshold;
@property (T@"AVZoomRange",R,N) systemRecommendedVideoZoomRange;
@property (T@"NSArray",R,N) recommendedLensApertureStops;
@property (Tf,R,N) minLensAperture;
@property (Tf,R,N) maxLensAperture;
@property (Tf,R,N) defaultLensAperture;
@property (T{?=qiIq},R,N) minExposureDuration;
@property (T{?=qiIq},R,N) maxExposureDuration;
@property (T@"AVExposureBiasRange",R,N) systemRecommendedExposureBiasRange;
@property (Tf,R,N) minISO;
@property (Tf,R,N) maxISO;
@property (TB,R,N,GisGlobalToneMappingSupported) globalToneMappingSupported;
@property (TB,R,N,GisVideoHDRSupported) videoHDRSupported;
@property (T{?=ii},R,N) highResolutionStillImageDimensions;
@property (TB,R,N,GisHighPhotoQualitySupported) highPhotoQualitySupported;
@property (TB,R,N,GisHighestPhotoQualitySupported) highestPhotoQualitySupported;
@property (Tq,R,N) autoFocusSystem;
@property (T@"NSArray",R,N) supportedColorSpaces;
@property (Td,R,N) videoMinZoomFactorForDepthDataDelivery;
@property (Td,R,N) videoMaxZoomFactorForDepthDataDelivery;
@property (T@"NSArray",R,N) supportedVideoZoomFactorsForDepthDataDelivery;
@property (T@"NSArray",R,N) supportedVideoZoomRangesForDepthDataDelivery;
@property (TB,R,N) zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported;
@property (T@"NSArray",R,N) supportedDepthDataFormats;
@property (T@"NSArray",R,N) unsupportedCaptureOutputClasses;
@property (T@"NSArray",R,N) supportedMaxPhotoDimensions;
@property (T@"NSArray",R,N) secondaryNativeResolutionZoomFactors;
@property (TB,R,N,GisAutoVideoFrameRateSupported) autoVideoFrameRateSupported;
```

## Class methods

```
+[AVCaptureDeviceFormat initialize];
```

## Instance methods

```
-[AVCaptureDeviceFormat reactionEffectsSupported];
-[AVCaptureDeviceFormat formatDescription];
-[AVCaptureDeviceFormat isZeroShutterLagSupported];
-[AVCaptureDeviceFormat isPhotoFormat];
-[AVCaptureDeviceFormat isSpatialOverCaptureSupported];
-[AVCaptureDeviceFormat sensorDimensions];
-[AVCaptureDeviceFormat maxExposureDuration];
-[AVCaptureDeviceFormat isDeepFusionSupported];
-[AVCaptureDeviceFormat isConstantColorSupported];
-[AVCaptureDeviceFormat isContentAwareDistortionCorrectionSupported];
-[AVCaptureDeviceFormat isSmartCropSupported];
-[AVCaptureDeviceFormat isSecureSigningPhotoCaptureSupported];
-[AVCaptureDeviceFormat isUltraHighResolutionZeroShutterLagSupported];
-[AVCaptureDeviceFormat isLowLightVideoCaptureSupported];
-[AVCaptureDeviceFormat isSmartStyleRenderingSupported];
-[AVCaptureDeviceFormat isVideoGreenGhostMitigationSupported];
-[AVCaptureDeviceFormat isPersonalPhotographerSupported];
-[AVCaptureDeviceFormat isCameraCalibrationDataDeliverySupported];
-[AVCaptureDeviceFormat isStudioLightSupported];
-[AVCaptureDeviceFormat isStillImageDisparitySupported];
-[AVCaptureDeviceFormat debugDescription];
-[AVCaptureDeviceFormat isContinuousZoomWithDepthSupported];
-[AVCaptureDeviceFormat isIrisVideoStabilizationSupported];
-[AVCaptureDeviceFormat ispPowerConsumption];
-[AVCaptureDeviceFormat maxPortraitLightingEffectStrength];
-[AVCaptureDeviceFormat supportedColorSpaces];
-[AVCaptureDeviceFormat isStereoFusionSupported];
-[AVCaptureDeviceFormat isBackgroundReplacementSupported];
-[AVCaptureDeviceFormat previewDimensions];
-[AVCaptureDeviceFormat isStereoVideoCaptureSupported];
-[AVCaptureDeviceFormat isPortraitAutoSuggestSupported];
-[AVCaptureDeviceFormat minSimulatedAperture];
-[AVCaptureDeviceFormat minISO];
-[AVCaptureDeviceFormat minLensAperture];
-[AVCaptureDeviceFormat setContinuousZoomWithDepthEnabled:];
-[AVCaptureDeviceFormat dealloc];
-[AVCaptureDeviceFormat isDeferredPhotoProcessingSupported];
-[AVCaptureDeviceFormat isHDRSupported];
-[AVCaptureDeviceFormat isWideColorSupported];
-[AVCaptureDeviceFormat isStillImageDepthSupported];
-[AVCaptureDeviceFormat isCinematicVideoCaptureSupported];
-[AVCaptureDeviceFormat isHighPhotoQualitySupported];
-[AVCaptureDeviceFormat maxLensAperture];
-[AVCaptureDeviceFormat supportedDemosaicedRawPixelFormat];
-[AVCaptureDeviceFormat isMomentCaptureMovieRecordingSupported];
-[AVCaptureDeviceFormat internalDemosaicedRawPixelFormat];
-[AVCaptureDeviceFormat isCenterStageSupported];
-[AVCaptureDeviceFormat uniqueID];
-[AVCaptureDeviceFormat hardwareCost];
-[AVCaptureDeviceFormat defaultPortraitLightingEffectStrength];
-[AVCaptureDeviceFormat isVideoStabilizationSupported];
-[AVCaptureDeviceFormat isIrisSupported];
-[AVCaptureDeviceFormat minExposureDuration];
-[AVCaptureDeviceFormat spatialOverCapturePercentage];
-[AVCaptureDeviceFormat isZeroShutterLagWithDepthSupported];
-[AVCaptureDeviceFormat isCinematicFramingSupported];
-[AVCaptureDeviceFormat isStreamingDepthSupported];
-[AVCaptureDeviceFormat isLowLightVideoNoiseReductionSupported];
-[AVCaptureDeviceFormat isManualFramingSupported];
-[AVCaptureDeviceFormat isVideoStabilizationStrengthSupported:];
-[AVCaptureDeviceFormat isBackgroundBlurSupported];
-[AVCaptureDeviceFormat isApplyStandardSmartStyleForStillsWhenNoStyleRequestedSupported];
-[AVCaptureDeviceFormat supportedRawPixelFormat];
-[AVCaptureDeviceFormat description];
-[AVCaptureDeviceFormat isStreamingDisparitySupported];
-[AVCaptureDeviceFormat isDigitalFlashSupported];
-[AVCaptureDeviceFormat isContinuousAutoFocusTrackingSupported];
-[AVCaptureDeviceFormat isExposureModeSupported:];
-[AVCaptureDeviceFormat isFastCapturePrioritizationSupported];
-[AVCaptureDeviceFormat isBroadcastVideoOutputSupported];
-[AVCaptureDeviceFormat recommendedLensApertureStops];
-[AVCaptureDeviceFormat isTextureStyleSupported];
-[AVCaptureDeviceFormat isMultiCamSupported];
-[AVCaptureDeviceFormat isStudioLightingSupported];
-[AVCaptureDeviceFormat isContinuousZoomWithDepthEnabled];
-[AVCaptureDeviceFormat isVariableFrameRateVideoCaptureSupported];
-[AVCaptureDeviceFormat mediaType];
-[AVCaptureDeviceFormat AVCaptureSessionPresets];
-[AVCaptureDeviceFormat autoFocusSystem];
-[AVCaptureDeviceFormat isEqual:];
-[AVCaptureDeviceFormat isFaceIDCoexistenceSupported];
-[AVCaptureDeviceFormat secondaryNativeResolutionZoomFactors];
-[AVCaptureDeviceFormat supportedDepthDataFormats];
-[AVCaptureDeviceFormat minPortraitLightingEffectStrength];
-[AVCaptureDeviceFormat baseSensorPowerConsumption];
-[AVCaptureDeviceFormat isSISSupported];
-[AVCaptureDeviceFormat isNonDestructiveCropSupported];
-[AVCaptureDeviceFormat isDemosaicedRawSupported];
-[AVCaptureDeviceFormat variableSensorPowerConsumption];
-[AVCaptureDeviceFormat isSmartFramingSupported];
-[AVCaptureDeviceFormat maxISO];
-[AVCaptureDeviceFormat defaultSimulatedAperture];
-[AVCaptureDeviceFormat defaultLensAperture];
-[AVCaptureDeviceFormat isSemanticStyleRenderingSupported];
-[AVCaptureDeviceFormat maxSimulatedAperture];
-[AVCaptureDeviceFormat isVideoBinned];
-[AVCaptureDeviceFormat supportedMaxPhotoDimensions];
-[AVCaptureDeviceFormat videoMaxZoomFactor];
-[AVCaptureDeviceFormat videoSupportedFrameRateRanges];
-[AVCaptureDeviceFormat videoFieldOfView];
-[AVCaptureDeviceFormat systemRecommendedVideoZoomRange];
-[AVCaptureDeviceFormat figCaptureSourceDepthDataFormat];
-[AVCaptureDeviceFormat unsupportedCaptureOutputClasses];
-[AVCaptureDeviceFormat videoFieldOfViewForAspectRatio:];
-[AVCaptureDeviceFormat videoZoomFactorUpscaleThreshold];
-[AVCaptureDeviceFormat _checkCustomExposureModeWithLensAperture:duration:ISO:entryPoint:];
-[AVCaptureDeviceFormat _defaultPhotoDimensionsInNativeSensorOrientationWithHighResolutionCaptureEnabled:];
-[AVCaptureDeviceFormat _initializeSupportedMaxPhotoDimensions];
-[AVCaptureDeviceFormat _stringForMediaType:formatDescription:frameRateRanges:];
-[AVCaptureDeviceFormat _supportedMaxPhotoDimensionsPrivateDimensionsEnabled:];
-[AVCaptureDeviceFormat defaultActiveMaxFrameDurationForSessionPreset:];
-[AVCaptureDeviceFormat defaultActiveMinFrameDurationForSessionPreset:];
-[AVCaptureDeviceFormat defaultPhotoDimensionsWithHighResolutionCaptureEnabled:];
-[AVCaptureDeviceFormat figCaptureSourceVideoFormat];
-[AVCaptureDeviceFormat focalLengthIn35mmFilmWithGeometricDistortionCorrection:];
-[AVCaptureDeviceFormat geometricDistortionCorrectedVideoFieldOfView];
-[AVCaptureDeviceFormat geometricDistortionCorrectedVideoFieldOfViewForAspectRatio:];
-[AVCaptureDeviceFormat highResolutionStillImageDimensions];
-[AVCaptureDeviceFormat highestSupportedVideoFrameDuration];
-[AVCaptureDeviceFormat initWithFigCaptureSourceFormat:fcSourceAttributes:];
-[AVCaptureDeviceFormat isAutoVideoFrameRateSupported];
-[AVCaptureDeviceFormat isBackgroundBlurApertureSupported];
-[AVCaptureDeviceFormat isBackgroundBlurSupportedForContinuityCamera];
-[AVCaptureDeviceFormat isBackgroundReplacementSupportedForContinuityCamera];
-[AVCaptureDeviceFormat isCameraLensSmudgeDetectionSupported];
-[AVCaptureDeviceFormat isCenterStageSupportedForContinuityCamera];
-[AVCaptureDeviceFormat isCinematicVideoMetadataCaptureSupported];
-[AVCaptureDeviceFormat isDCProcessingWithDepthSupported];
-[AVCaptureDeviceFormat isDefaultActiveFormat];
-[AVCaptureDeviceFormat isDemosaicedRawConfigurationWithDepthSupported];
-[AVCaptureDeviceFormat isEdgeLightSupported];
-[AVCaptureDeviceFormat isExperimental];
-[AVCaptureDeviceFormat isGlobalToneMappingSupported];
-[AVCaptureDeviceFormat isHighestPhotoQualitySupported];
-[AVCaptureDeviceFormat isMountedInPortraitOrientation];
-[AVCaptureDeviceFormat isPortraitEffectSupported];
-[AVCaptureDeviceFormat isPortraitEffectsMatteStillImageDeliverySupported];
-[AVCaptureDeviceFormat isSpatialVideoCaptureSupported];
-[AVCaptureDeviceFormat isStereoCaptureSupported];
-[AVCaptureDeviceFormat isStudioLightingIntensitySupported];
-[AVCaptureDeviceFormat isStudioLightingSupportedForContinuityCamera];
-[AVCaptureDeviceFormat isVideoHDRSupported];
-[AVCaptureDeviceFormat isVideoHDRSuspensionSupported];
-[AVCaptureDeviceFormat isVideoStabilizationModeSupported:];
-[AVCaptureDeviceFormat isVisionDataDeliverySupported];
-[AVCaptureDeviceFormat lowestSupportedVideoFrameDuration];
-[AVCaptureDeviceFormat maxPhotoDimensionsAreUltraHighResolution:privateDimensionsEnabled:];
-[AVCaptureDeviceFormat optimizedPhotoFilterNames];
-[AVCaptureDeviceFormat optimizedVideoPreviewFilterNames];
-[AVCaptureDeviceFormat prefersVideoHDREnabledForSessionPreset:];
-[AVCaptureDeviceFormat reactionEffectsSupportedForContinuityCamera];
-[AVCaptureDeviceFormat supportedDynamicAspectRatios];
-[AVCaptureDeviceFormat supportedMaxPhotoDimensionsPrivate];
-[AVCaptureDeviceFormat supportedOutputAspectRatios];
-[AVCaptureDeviceFormat supportedSemanticSegmentationMatteTypes];
-[AVCaptureDeviceFormat supportedStabilizationMethod];
-[AVCaptureDeviceFormat supportedVideoZoomFactorsForDepthDataDelivery];
-[AVCaptureDeviceFormat supportedVideoZoomRangesForDepthDataDelivery];
-[AVCaptureDeviceFormat supportedZoomRangesForCinematicVideo];
-[AVCaptureDeviceFormat supportsExposureModeCustomWithLensAperture:duration:ISO:];
-[AVCaptureDeviceFormat supportsHighResolutionStillImageOutput];
-[AVCaptureDeviceFormat supportsQuadraHighResolutionStillImageOutput];
-[AVCaptureDeviceFormat supportsRedEyeReduction];
-[AVCaptureDeviceFormat systemRecommendedExposureBiasRange];
-[AVCaptureDeviceFormat validateMaxPhotoDimensions:privateDimensionsEnabled:];
-[AVCaptureDeviceFormat videoFieldOfViewForAspectRatio:geometricDistortionCorrected:];
-[AVCaptureDeviceFormat videoFrameRateRangeForBackgroundBlur];
-[AVCaptureDeviceFormat videoFrameRateRangeForBackgroundReplacement];
-[AVCaptureDeviceFormat videoFrameRateRangeForCenterStage];
-[AVCaptureDeviceFormat videoFrameRateRangeForCenterStageForContinuityCamera];
-[AVCaptureDeviceFormat videoFrameRateRangeForCinematicVideo];
-[AVCaptureDeviceFormat videoFrameRateRangeForPortraitEffect];
-[AVCaptureDeviceFormat videoFrameRateRangeForReactionEffectsInProgress];
-[AVCaptureDeviceFormat videoFrameRateRangeForStudioLight];
-[AVCaptureDeviceFormat videoFrameRateRangeForStudioLighting];
-[AVCaptureDeviceFormat videoHDRFlavor];
-[AVCaptureDeviceFormat videoMaxZoomFactorForCameraCalibrationDataDelivery];
-[AVCaptureDeviceFormat videoMaxZoomFactorForCenterStage];
-[AVCaptureDeviceFormat videoMaxZoomFactorForCinematicVideo];
-[AVCaptureDeviceFormat videoMaxZoomFactorForDepthDataDelivery];
-[AVCaptureDeviceFormat videoMinZoomFactorForCameraCalibrationDataDelivery];
-[AVCaptureDeviceFormat videoMinZoomFactorForCenterStage];
-[AVCaptureDeviceFormat videoMinZoomFactorForCinematicVideo];
-[AVCaptureDeviceFormat videoMinZoomFactorForDepthDataDelivery];
-[AVCaptureDeviceFormat vtScalingMode];
-[AVCaptureDeviceFormat zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported];
```
