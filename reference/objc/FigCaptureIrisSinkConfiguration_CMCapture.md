# `FigCaptureIrisSinkConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureSinkConfiguration`
- Protocols: `NSSecureCoding`
- 42 instance variables, 42 properties, 94 instance methods, 1 class methods

## Instance variables

```
B _movieCaptureEnabled;
B _movieCaptureSuspended;
{?="value"q"timescale"i"flags"I"epoch"q} _movieDuration;
{?="value"q"timescale"i"flags"I"epoch"q} _movieVideoFrameDuration;
i _movieAutoTrimMethod;
@"FigCaptureIrisPreparedSettings" _preparedSettings;
B _optimizesImagesForOfflineVideoStabilization;
B _depthDataDeliveryEnabled;
B _portraitEffectsMatteDeliveryEnabled;
@"NSArray" _enabledSemanticSegmentationMatteURNs;
B _filterRenderingEnabled;
B _bravoConstituentPhotoDeliveryEnabled;
B _momentCaptureMovieRecordingEnabled;
B _spatialOverCaptureEnabled;
i _maxQualityPrioritization;
B _deferredProcessingEnabled;
B _digitalFlashCaptureEnabled;
B _intelligentDistortionCorrectionEnabled;
B _demosaicedRawEnabled;
B _focusPixelBlurScoreEnabled;
B _previewQualityAdjustedPhotoFilterRenderingEnabled;
B _zeroShutterLagEnabled;
B _ultraHighResolutionZeroShutterLagSupportEnabled;
B _responsiveCaptureEnabled;
B _fastCapturePrioritizationEnabled;
B _semanticStyleRenderingEnabled;
{?="width"i"height"i} _maxPhotoDimensions;
@"NSDictionary" _exifFocalLengthsByZoomFactor;
B _constantColorEnabled;
B _constantColorClippingRecoveryEnabled;
B _constantColorSaturationBoostEnabled;
B _stereoPhotoCaptureEnabled;
B _applyStandardSmartStyleForStillsWhenNoStyleRequested;
B _multiCamClientCompositingEnabled;
@"NSString" _multiCamClientCompositingPrimaryConnectionID;
B _cameraSensorOrientationCompensationEnabled;
B _personalPhotographerEnabled;
B _secureSigningPhotoCaptureSupportEnabled;
B _preservesIrisMovieCaptureSuspendedOnSessionStop;
B _irisFrameHarvestingEnabled;
B _irisApplyPreviewShift;
B _textOrientationPrioritizationEnabled;
```

## Properties

```
@property (TB,N,V_movieCaptureEnabled) irisMovieCaptureEnabled;
@property (TB,N,V_movieCaptureSuspended) irisMovieCaptureSuspended;
@property (TB,N,V_preservesIrisMovieCaptureSuspendedOnSessionStop) preservesIrisMovieCaptureSuspendedOnSessionStop;
@property (T{?=qiIq},N,V_movieDuration) irisMovieDuration;
@property (T{?=qiIq},N,V_movieVideoFrameDuration) irisMovieVideoFrameDuration;
@property (Ti,N,V_movieAutoTrimMethod) irisMovieAutoTrimMethod;
@property (TB,N,V_irisFrameHarvestingEnabled) irisFrameHarvestingEnabled;
@property (T@"FigCaptureIrisPreparedSettings",&,N,V_preparedSettings) irisPreparedSettings;
@property (TB,N,V_irisApplyPreviewShift) irisApplyPreviewShift;
@property (TB,N,V_optimizesImagesForOfflineVideoStabilization) optimizesImagesForOfflineVideoStabilization;
@property (TB,N,V_depthDataDeliveryEnabled) depthDataDeliveryEnabled;
@property (TB,N,V_portraitEffectsMatteDeliveryEnabled) portraitEffectsMatteDeliveryEnabled;
@property (T@"NSArray",&,N,V_enabledSemanticSegmentationMatteURNs) enabledSemanticSegmentationMatteURNs;
@property (TB,N,V_filterRenderingEnabled) filterRenderingEnabled;
@property (TB,N,V_bravoConstituentPhotoDeliveryEnabled) bravoConstituentPhotoDeliveryEnabled;
@property (TB,N,V_momentCaptureMovieRecordingEnabled) momentCaptureMovieRecordingEnabled;
@property (TB,N,V_spatialOverCaptureEnabled) spatialOverCaptureEnabled;
@property (Ti,N,V_maxQualityPrioritization) maxQualityPrioritization;
@property (TB,N,V_deferredProcessingEnabled) deferredProcessingEnabled;
@property (TB,N,V_digitalFlashCaptureEnabled) digitalFlashCaptureEnabled;
@property (TB,N,V_intelligentDistortionCorrectionEnabled) intelligentDistortionCorrectionEnabled;
@property (TB,N,V_demosaicedRawEnabled) demosaicedRawEnabled;
@property (TB,N,V_focusPixelBlurScoreEnabled) focusPixelBlurScoreEnabled;
@property (TB,N,V_previewQualityAdjustedPhotoFilterRenderingEnabled) previewQualityAdjustedPhotoFilterRenderingEnabled;
@property (TB,N,V_zeroShutterLagEnabled) zeroShutterLagEnabled;
@property (TB,N,V_ultraHighResolutionZeroShutterLagSupportEnabled) ultraHighResolutionZeroShutterLagSupportEnabled;
@property (TB,N,V_responsiveCaptureEnabled) responsiveCaptureEnabled;
@property (TB,N,V_fastCapturePrioritizationEnabled) fastCapturePrioritizationEnabled;
@property (TB,N,V_semanticStyleRenderingEnabled) semanticStyleRenderingEnabled;
@property (TB,N,V_textOrientationPrioritizationEnabled) textOrientationPrioritizationEnabled;
@property (T{?=ii},N,V_maxPhotoDimensions) maxPhotoDimensions;
@property (T@"NSDictionary",&,N,V_exifFocalLengthsByZoomFactor) exifFocalLengthsByZoomFactor;
@property (TB,N,V_constantColorEnabled) constantColorEnabled;
@property (TB,N,V_constantColorClippingRecoveryEnabled) constantColorClippingRecoveryEnabled;
@property (TB,N,V_constantColorSaturationBoostEnabled) constantColorSaturationBoostEnabled;
@property (TB,N,V_stereoPhotoCaptureEnabled) stereoPhotoCaptureEnabled;
@property (TB,N,V_applyStandardSmartStyleForStillsWhenNoStyleRequested) applyStandardSmartStyleForStillsWhenNoStyleRequested;
@property (TB,N,V_multiCamClientCompositingEnabled) multiCamClientCompositingEnabled;
@property (T@"NSString",C,N,V_multiCamClientCompositingPrimaryConnectionID) multiCamClientCompositingPrimaryConnectionID;
@property (TB,N,V_cameraSensorOrientationCompensationEnabled) cameraSensorOrientationCompensationEnabled;
@property (TB,N,V_personalPhotographerEnabled) personalPhotographerEnabled;
@property (TB,N,V_secureSigningPhotoCaptureSupportEnabled) secureSigningPhotoCaptureSupportEnabled;
```

## Class methods

```
+[FigCaptureIrisSinkConfiguration supportsSecureCoding];
```

## Instance methods

```
-[FigCaptureIrisSinkConfiguration setIrisFrameHarvestingEnabled:];
-[FigCaptureIrisSinkConfiguration semanticStyleRenderingEnabled];
-[FigCaptureIrisSinkConfiguration personalPhotographerEnabled];
-[FigCaptureIrisSinkConfiguration ultraHighResolutionZeroShutterLagSupportEnabled];
-[FigCaptureIrisSinkConfiguration constantColorSaturationBoostEnabled];
-[FigCaptureIrisSinkConfiguration setExifFocalLengthsByZoomFactor:];
-[FigCaptureIrisSinkConfiguration focusPixelBlurScoreEnabled];
-[FigCaptureIrisSinkConfiguration bravoConstituentPhotoDeliveryEnabled];
-[FigCaptureIrisSinkConfiguration irisFrameHarvestingEnabled];
-[FigCaptureIrisSinkConfiguration setSpatialOverCaptureEnabled:];
-[FigCaptureIrisSinkConfiguration setConstantColorClippingRecoveryEnabled:];
-[FigCaptureIrisSinkConfiguration setPersonalPhotographerEnabled:];
-[FigCaptureIrisSinkConfiguration setFastCapturePrioritizationEnabled:];
-[FigCaptureIrisSinkConfiguration setDemosaicedRawEnabled:];
-[FigCaptureIrisSinkConfiguration setStereoPhotoCaptureEnabled:];
-[FigCaptureIrisSinkConfiguration sinkType];
-[FigCaptureIrisSinkConfiguration fastCapturePrioritizationEnabled];
-[FigCaptureIrisSinkConfiguration exifFocalLengthsByZoomFactor];
-[FigCaptureIrisSinkConfiguration reasonForNotEqualingConfiguration:];
-[FigCaptureIrisSinkConfiguration secureSigningPhotoCaptureSupportEnabled];
-[FigCaptureIrisSinkConfiguration setDeferredProcessingEnabled:];
-[FigCaptureIrisSinkConfiguration setApplyStandardSmartStyleForStillsWhenNoStyleRequested:];
-[FigCaptureIrisSinkConfiguration setMultiCamClientCompositingPrimaryConnectionID:];
-[FigCaptureIrisSinkConfiguration irisMovieDuration];
-[FigCaptureIrisSinkConfiguration setConstantColorSaturationBoostEnabled:];
-[FigCaptureIrisSinkConfiguration setFocusPixelBlurScoreEnabled:];
-[FigCaptureIrisSinkConfiguration optimizesImagesForOfflineVideoStabilization];
-[FigCaptureIrisSinkConfiguration constantColorClippingRecoveryEnabled];
-[FigCaptureIrisSinkConfiguration setUltraHighResolutionZeroShutterLagSupportEnabled:];
-[FigCaptureIrisSinkConfiguration stereoPhotoCaptureEnabled];
-[FigCaptureIrisSinkConfiguration setIntelligentDistortionCorrectionEnabled:];
-[FigCaptureIrisSinkConfiguration setSemanticStyleRenderingEnabled:];
-[FigCaptureIrisSinkConfiguration digitalFlashCaptureEnabled];
-[FigCaptureIrisSinkConfiguration multiCamClientCompositingPrimaryConnectionID];
-[FigCaptureIrisSinkConfiguration setIrisMovieVideoFrameDuration:];
-[FigCaptureIrisSinkConfiguration zeroShutterLagEnabled];
-[FigCaptureIrisSinkConfiguration setBravoConstituentPhotoDeliveryEnabled:];
-[FigCaptureIrisSinkConfiguration setPreservesIrisMovieCaptureSuspendedOnSessionStop:];
-[FigCaptureIrisSinkConfiguration irisMovieCaptureSuspended];
-[FigCaptureIrisSinkConfiguration setEnabledSemanticSegmentationMatteURNs:];
-[FigCaptureIrisSinkConfiguration irisMovieAutoTrimMethod];
-[FigCaptureIrisSinkConfiguration setSecureSigningPhotoCaptureSupportEnabled:];
-[FigCaptureIrisSinkConfiguration dealloc];
-[FigCaptureIrisSinkConfiguration setIrisApplyPreviewShift:];
-[FigCaptureIrisSinkConfiguration setZeroShutterLagEnabled:];
-[FigCaptureIrisSinkConfiguration multiCamClientCompositingEnabled];
-[FigCaptureIrisSinkConfiguration demosaicedRawEnabled];
-[FigCaptureIrisSinkConfiguration setResponsiveCaptureEnabled:];
-[FigCaptureIrisSinkConfiguration setMomentCaptureMovieRecordingEnabled:];
-[FigCaptureIrisSinkConfiguration setIrisMovieAutoTrimMethod:];
-[FigCaptureIrisSinkConfiguration irisMovieCaptureEnabled];
-[FigCaptureIrisSinkConfiguration deferredProcessingEnabled];
-[FigCaptureIrisSinkConfiguration setMaxQualityPrioritization:];
-[FigCaptureIrisSinkConfiguration spatialOverCaptureEnabled];
-[FigCaptureIrisSinkConfiguration setPortraitEffectsMatteDeliveryEnabled:];
-[FigCaptureIrisSinkConfiguration irisApplyPreviewShift];
-[FigCaptureIrisSinkConfiguration setMultiCamClientCompositingEnabled:];
-[FigCaptureIrisSinkConfiguration setTextOrientationPrioritizationEnabled:];
-[FigCaptureIrisSinkConfiguration textOrientationPrioritizationEnabled];
-[FigCaptureIrisSinkConfiguration previewQualityAdjustedPhotoFilterRenderingEnabled];
-[FigCaptureIrisSinkConfiguration setDigitalFlashCaptureEnabled:];
-[FigCaptureIrisSinkConfiguration irisMovieVideoFrameDuration];
-[FigCaptureIrisSinkConfiguration irisPreparedSettings];
-[FigCaptureIrisSinkConfiguration setIrisMovieCaptureEnabled:];
-[FigCaptureIrisSinkConfiguration setIrisMovieDuration:];
-[FigCaptureIrisSinkConfiguration setPreviewQualityAdjustedPhotoFilterRenderingEnabled:];
-[FigCaptureIrisSinkConfiguration setIrisPreparedSettings:];
-[FigCaptureIrisSinkConfiguration momentCaptureMovieRecordingEnabled];
-[FigCaptureIrisSinkConfiguration preservesIrisMovieCaptureSuspendedOnSessionStop];
-[FigCaptureIrisSinkConfiguration encodeWithCoder:];
-[FigCaptureIrisSinkConfiguration intelligentDistortionCorrectionEnabled];
-[FigCaptureIrisSinkConfiguration setCameraSensorOrientationCompensationEnabled:];
-[FigCaptureIrisSinkConfiguration responsiveCaptureEnabled];
-[FigCaptureIrisSinkConfiguration copyXPCEncoding];
-[FigCaptureIrisSinkConfiguration description];
-[FigCaptureIrisSinkConfiguration setFilterRenderingEnabled:];
-[FigCaptureIrisSinkConfiguration initWithXPCEncoding:];
-[FigCaptureIrisSinkConfiguration initWithCoder:];
-[FigCaptureIrisSinkConfiguration maxPhotoDimensions];
-[FigCaptureIrisSinkConfiguration constantColorEnabled];
-[FigCaptureIrisSinkConfiguration setConstantColorEnabled:];
-[FigCaptureIrisSinkConfiguration maxQualityPrioritization];
-[FigCaptureIrisSinkConfiguration setDepthDataDeliveryEnabled:];
-[FigCaptureIrisSinkConfiguration setIrisMovieCaptureSuspended:];
-[FigCaptureIrisSinkConfiguration applyStandardSmartStyleForStillsWhenNoStyleRequested];
-[FigCaptureIrisSinkConfiguration setMaxPhotoDimensions:];
-[FigCaptureIrisSinkConfiguration setOptimizesImagesForOfflineVideoStabilization:];
-[FigCaptureIrisSinkConfiguration copyWithZone:];
-[FigCaptureIrisSinkConfiguration portraitEffectsMatteDeliveryEnabled];
-[FigCaptureIrisSinkConfiguration isEqual:];
-[FigCaptureIrisSinkConfiguration enabledSemanticSegmentationMatteURNs];
-[FigCaptureIrisSinkConfiguration depthDataDeliveryEnabled];
-[FigCaptureIrisSinkConfiguration cameraSensorOrientationCompensationEnabled];
-[FigCaptureIrisSinkConfiguration filterRenderingEnabled];
```
