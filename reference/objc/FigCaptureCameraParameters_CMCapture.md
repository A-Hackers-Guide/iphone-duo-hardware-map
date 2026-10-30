# `FigCaptureCameraParameters`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 26 instance variables, 25 properties, 71 instance methods, 13 class methods

## Instance variables

```
@"NSString" _modelSpecificName;
@"NSDictionary" _cameraParameters;
@"NSDictionary" _commonNRFParameters;
@"NSDictionary" _hvsParameters;
@"NSDictionary" _commonDistortionCorrectionParameters;
@"NSDictionary" _meteorParameters;
@"NSDictionary" _motionAttachmentsParameters;
@"NSDictionary" _videoStabilizationParameters;
@"NSDictionary" _previewStabilizationParameters;
@"NSDictionary" _stereoDisparityParameters;
@"NSDictionary" _monocularStreamingDepthParameters;
@"NSDictionary" _depthProcessingParameters;
@"NSDictionary" _landmarksParameters;
@"NSDictionary" _commonMattingParameters;
@"NSDictionary" _learnedMattingParameters;
@"NSDictionary" _personSemanticsParameters;
@"NSDictionary" _coreImagePortraitFilterParameters;
@"NSDictionary" _commonVideoGreenGhostMitigationParameters;
@"NSDictionary" _commonDeepZoomParameters;
@"NSDictionary" _photoEncoderParameters;
@"NSDictionary" _portraitSceneMonitoringParametersByZoomFactor;
@"NSDictionary" _commonLensSmudgeDetectionParameters;
@"NSDictionary" _temporalNoiseReductionParameters;
@"NSDictionary" _commonPersonalPhotographerParameters;
@"NSDictionary" _lowLightVideoNoiseReductionParameters;
@"NSDictionary" _optimizedProcessingWithCropAndDownscaleDimensions;
```

## Properties

```
@property (Ti,R,N) meteorHeadroomProcessingType;
@property (T@"NSDictionary",R,N,V_cameraParameters) cameraParameters;
@property (T@"NSDictionary",R,N) cameraTuningParameters;
@property (T@"NSDictionary",R,N,V_motionAttachmentsParameters) motionAttachmentsParameters;
@property (T@"NSDictionary",R,N,V_videoStabilizationParameters) videoStabilizationParameters;
@property (T@"NSDictionary",R,N,V_previewStabilizationParameters) previewStabilizationParameters;
@property (T@"NSDictionary",R,N) videoStabilizationSTFParameters;
@property (T@"NSDictionary",R,N,V_hvsParameters) hvsParameters;
@property (T@"NSDictionary",R,N) stereoDisparityParameters;
@property (T@"NSDictionary",R,N,V_commonNRFParameters) commonNRFParameters;
@property (Ti,R,N) nrfVersion;
@property (Ti,R,N) deviceGeneration;
@property (Ti,R,N) gainMapVersion;
@property (Ti,R,N) distortionCorrectionVersion;
@property (T@"NSDictionary",R,N,V_commonVideoGreenGhostMitigationParameters) commonVideoGreenGhostMitigationParameters;
@property (Ti,R,N) videoGreenGhostBrightLightMitigationVersion;
@property (Ti,R,N) videoGreenGhostLowLightMitigationVersion;
@property (T@"NSDictionary",R,N,V_photoEncoderParameters) photoEncoderParameters;
@property (Ti,R,N) lensSmudgeDetectionVersion;
@property (T@"NSDictionary",R,N,V_temporalNoiseReductionParameters) temporalNoiseReductionParameters;
@property (T@"NSDictionary",R,N,V_lowLightVideoNoiseReductionParameters) lowLightVideoNoiseReductionParameters;
@property (T{?=ii},R,N) maxFocusPixelHorizontalPixelBufferDimensions;
@property (Ti,R,N) deepZoomVersion;
@property (TB,R,N) portraitTapToRefocusPrevented;
@property (Ti,R,N) personalPhotographerVersion;
```

## Class methods

```
+[FigCaptureCameraParameters sharedInstance];
+[FigCaptureCameraParameters initialize];
+[FigCaptureCameraParameters stillImageMaxLossyCompressionLevel];
+[FigCaptureCameraParameters previewMaxLossyCompressionLevel];
+[FigCaptureCameraParameters movieFileMaxLossyCompressionLevelForPixelFormat:];
+[FigCaptureCameraParameters videoDataMaxLossyCompressionLevel];
+[FigCaptureCameraParameters cinematicFramingVirtualCameraConfigurationForPortType:sensorIDString:];
+[FigCaptureCameraParameters sdofTuningParametersForSensorIDDictionary:zoomFactor:];
+[FigCaptureCameraParameters sensorIDFromSensorIDString:];
+[FigCaptureCameraParameters sensorIDStringFromMetadata:];
+[FigCaptureCameraParameters sensorIDStringFromModuleInfo:];
+[FigCaptureCameraParameters sharedInstanceWithModelSpecificName:parametersWereReset:];
+[FigCaptureCameraParameters temporalFilterSessionConfigurationForPortType:sensorIDString:];
```

## Instance methods

```
-[FigCaptureCameraParameters personSemanticsVersion];
-[FigCaptureCameraParameters distortionCorrectionVersion];
-[FigCaptureCameraParameters temporalNoiseReductionParameters];
-[FigCaptureCameraParameters motionAttachmentsParameters];
-[FigCaptureCameraParameters nrfVersion];
-[FigCaptureCameraParameters sdofRenderingVersionForPortType:sensorIDString:zoomFactor:];
-[FigCaptureCameraParameters chromaticDefringingEnabledForSlomoForPortType:sensorIDString:];
-[FigCaptureCameraParameters focusPixelDisparityTuningParametersForPortType:sensorIDString:zoomFactor:];
-[FigCaptureCameraParameters meteorHeadroomProcessingType];
-[FigCaptureCameraParameters stereoDisparityParameters];
-[FigCaptureCameraParameters videoGreenGhostLowLightMitigationVersion];
-[FigCaptureCameraParameters depthProcessorVersion];
-[FigCaptureCameraParameters deepZoomVersion];
-[FigCaptureCameraParameters portraitSceneMonitorVersionForPortType:sensorIDString:];
-[FigCaptureCameraParameters coreImagePortraitFilterVersion];
-[FigCaptureCameraParameters focusPixelDisparityVersionForPortType:sensorIDString:];
-[FigCaptureCameraParameters portraitTapToRefocusPrevented];
-[FigCaptureCameraParameters init];
-[FigCaptureCameraParameters videoStabilizationSTFParameters];
-[FigCaptureCameraParameters deepZoomTransferWithZoomedImageEnabledForPortType:sensorIDString:];
-[FigCaptureCameraParameters initWithContentsOfFile:];
-[FigCaptureCameraParameters lcbMinApertureRatioForDetectionForPortType:sensorIDString:];
-[FigCaptureCameraParameters panoramaRequiresLTMLockingForPortType:sensorIDString:];
-[FigCaptureCameraParameters dealloc];
-[FigCaptureCameraParameters chromaticDefringingParametersForPortType:sensorIDString:];
-[FigCaptureCameraParameters quadraSubPixelSwitchingParametersForPortType:sensorIDString:];
-[FigCaptureCameraParameters fsdNetStereoImagesAlignmentForPortType:sensorIDString:];
-[FigCaptureCameraParameters landmarksConstellationPointCountForInferenceType:];
-[FigCaptureCameraParameters monocularStreamingDepthType];
-[FigCaptureCameraParameters commonNRFParameters];
-[FigCaptureCameraParameters sensorIDDictionaryForStream:];
-[FigCaptureCameraParameters stereoVideoCaptureSceneMonitoringParametersForPortType:sensorIDString:];
-[FigCaptureCameraParameters gainMapVersion];
-[FigCaptureCameraParameters mattingVersion];
-[FigCaptureCameraParameters videoStabilizationParameters];
-[FigCaptureCameraParameters lcbSupportedForPortType:sensorIDString:];
-[FigCaptureCameraParameters complementMatteSuppressionDecisionWithISPDetectedFaces];
-[FigCaptureCameraParameters softISPCropDimensionsForOptimizedLearnedFusionForPortType:];
-[FigCaptureCameraParameters personalPhotographerVersion];
-[FigCaptureCameraParameters learnedMattingVersion];
-[FigCaptureCameraParameters focalLengthCharacterizationForStream:];
-[FigCaptureCameraParameters lensSmudgeDetectionParametersForPortType:sensorIDString:];
-[FigCaptureCameraParameters lowLightVideoNoiseReductionParameters];
-[FigCaptureCameraParameters initWithModelSpecificName:];
-[FigCaptureCameraParameters commonVideoGreenGhostMitigationParameters];
-[FigCaptureCameraParameters cameraParameters];
-[FigCaptureCameraParameters hvsParameters];
-[FigCaptureCameraParameters actionCameraSceneMonitoringParametersForPortType:sensorIDString:];
-[FigCaptureCameraParameters stereoPhotoCaptureSceneMonitoringParametersForPortType:sensorIDString:];
-[FigCaptureCameraParameters cameraTuningParameters];
-[FigCaptureCameraParameters portraitSceneMonitoringParametersForPortType:sensorIDString:zoomFactorRelativeToWidePortType:];
-[FigCaptureCameraParameters sensorIDDictionaryForPortType:sensorIDString:];
-[FigCaptureCameraParameters chromaticDefringingEnabledForVideoForPortType:sensorIDString:];
-[FigCaptureCameraParameters disparityRefinementTypeForPortType:sensorIDString:zoomFactor:];
-[FigCaptureCameraParameters landmarksVersionForInferenceType:];
-[FigCaptureCameraParameters nrfProcessingDimensionsForOptimizedLearnedFusionForPortType:];
-[FigCaptureCameraParameters videoStabilizationProcessorVersion];
-[FigCaptureCameraParameters deviceGeneration];
-[FigCaptureCameraParameters depthScalingTuneParametersForPortType:sensorIDString:];
-[FigCaptureCameraParameters maxFocusPixelHorizontalPixelBufferDimensions];
-[FigCaptureCameraParameters udnetEnabledForPortType:sensorIDString:];
-[FigCaptureCameraParameters portraitPreviewForegroundBlurEnabledForPortType:sensorIDString:zoomFactor:];
-[FigCaptureCameraParameters mattingVersionForPortType:sensorIDString:];
-[FigCaptureCameraParameters disparityVersionForPortType:sensorIDString:];
-[FigCaptureCameraParameters videoGreenGhostBrightLightMitigationVersion];
-[FigCaptureCameraParameters lensSmudgeDetectionVersion];
-[FigCaptureCameraParameters disparityVersion];
-[FigCaptureCameraParameters previewStabilizationParameters];
-[FigCaptureCameraParameters focusPixelsPatternsForPortType:sensorIDString:];
-[FigCaptureCameraParameters personalPhotographerSceneMonitoringParametersForPortType:sensorIDString:];
-[FigCaptureCameraParameters photoEncoderParameters];
```
