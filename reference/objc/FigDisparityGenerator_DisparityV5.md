# `FigDisparityGenerator`

- Image: [`/System/Library/VideoProcessors/DisparityV5.bundle/DisparityV5`](../userland/System__Library__VideoProcessors__DisparityV5.bundle__DisparityV5.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MetalImageBufferProcessor`
- 63 instance variables, 21 properties, 48 instance methods, 0 class methods

## Instance variables

```
@"GDCTransform" _gdcTransform;
@"Demosaic" _referenceDemosaic;
@"Demosaic" _auxiliaryDemosaic;
@"Calibration" _calibration;
@"AdaptiveClamping" _clamping;
@"FigRegToolboxGPU" _keypointDetRtb;
^{?=ffffff} _keypointListRtb;
I _keypointGridWidth;
I _keypointGridHeight;
I _keypointsCount;
I _keypointsTemplateRadius;
I _keypointsSearchRadius;
f _keypointsMinCornerScore;
f _keypointsMinNccScore;
f _keypointsMinSelectionScore;
B _useLktKeypoints;
@"LKTKeypointDetector" _lktKeypointDetector;
I _inputCalibrationWidth;
I _inputCalibrationHeight;
I _scalerOutputWidth;
I _scalerOutputHeight;
I _rectifiedOutputWidth;
I _rectifiedOutputHeight;
I _auxiliaryPaddedHalfResWidth;
I _auxiliaryPaddedHalfResHeight;
I _disparityWidth;
I _disparityHeight;
@"<MTLTexture>" _refHalfResRGBATexture;
@"<MTLTexture>" _auxHalfResRGBATexture;
^{__CVBuffer=} _refHalfResLumaPixelBuffer;
^{__CVBuffer=} _refHalfResRectifiedRGBAPixelBuffer;
^{__CVBuffer=} _auxHalfResRectifiedRGBAPixelBuffer;
^{__CVBuffer=} _refLowResRectifiedRGBAPixelBuffer;
^{__CVBuffer=} _auxLowResRectifiedRGBAPixelBuffer;
^{__CVBuffer=} _rectifiedDisparityMap;
@"FigMetalContext" _metalContext;
@"NSDictionary" _auxiliaryMeta;
@"NSDictionary" _referenceMeta;
^d _adaptiveCorrectionKeypointsReferenceDistorted;
^d _adaptiveCorrectionKeypointsAuxiliaryDistorted;
@"DisparityDiagnostics" _diagnostics;
@"NSArray" _portsToConfig;
@"NSMutableDictionary" _disparityTuningParameters;
B _isPrewarming;
{CalModel="focalLengthPix"[2d]"opticalCenterX"[2d]"opticalCenterY"[2d]"extrinRotRefefenceToAuxiliary"[12d]"canonicalDisparityScale"d"calibrationDimensions"[2d]"pixelSize_um"[2d]} _correctedCalibration;
{?="distortPolynomCoefficients"[8f]"undistortPolynomCoefficients"[8f]"centerX"f"centerY"f"originalImageOriginX"f"originalImageOriginY"f"originalImageWidth"f"originalImageHeight"f"pixelSize"f"homography"[9f]"inverseHomography"[9f]"canvasResolution"{CGSize="width"d"height"d}"applyZTransform"B"samplerType"i"rollingShutterCorrectionHomographies"^{?}"numRollingShutterCorrectionHomographies"i"rollingShutterCorrectionHomographyStep"f"applyRollingShutterCorrection"B"focalLengthPix"f"originalCropRect"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}} _gdcParametersReference;
{?="distortPolynomCoefficients"[8f]"undistortPolynomCoefficients"[8f]"centerX"f"centerY"f"originalImageOriginX"f"originalImageOriginY"f"originalImageWidth"f"originalImageHeight"f"pixelSize"f"homography"[9f]"inverseHomography"[9f]"canvasResolution"{CGSize="width"d"height"d}"applyZTransform"B"samplerType"i"rollingShutterCorrectionHomographies"^{?}"numRollingShutterCorrectionHomographies"i"rollingShutterCorrectionHomographyStep"f"applyRollingShutterCorrection"B"focalLengthPix"f"originalCropRect"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}} _gdcParametersAuxiliary;
f _canonicalDisparityScaleFactorOut;
@"<DisparityProcessorInferenceDelegate>" _disparityInferenceProcessorDelegate;
B _isShaderHarvesting;
B _shouldComputeDisparityWhenCalibrationFails;
B _equalizeTeleGainToMatchReference;
@"NSDictionary" _tuningParameters;
@"NSDictionary" _cameraInfoByPortType;
@"<MTLCommandQueue>" _metalCommandQueue;
@"FigDisparityMetadata" _shiftMapMetadata;
@"NSDictionary" _options;
@"NSDictionary" _disparityDiagnosticMetadata;
^{opaqueCMSampleBuffer=} _referenceSampleBuffer;
^{opaqueCMSampleBuffer=} _auxiliarySampleBuffer;
^{__CVBuffer=} _outputShiftmap;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _normalizedReferenceCropRect;
{?="inputImageWidth"Q"inputImageHeight"Q"inputIsLinearRGB"B"outputDisparityWidth"Q"outputDisparityHeight"Q"maxPaddingFactor"f"keypointGridWidth"I"keypointGridHeight"I} _disparityConfig;
```

## Properties

```
@property (T@"FigDisparityMetadata",R,N,V_shiftMapMetadata) shiftMapMetadata;
@property (T@"NSDictionary",&,N,V_options) options;
@property (TB,N,V_shouldComputeDisparityWhenCalibrationFails) shouldComputeDisparityWhenCalibrationFails;
@property (TB,N,V_equalizeTeleGainToMatchReference) equalizeTeleGainToMatchReference;
@property (T@"FigMetalContext",R,N,V_metalContext) metalContext;
@property (T@"NSDictionary",R,N,V_disparityDiagnosticMetadata) disparityDiagnosticMetadata;
@property (T^{opaqueCMSampleBuffer=},N,V_referenceSampleBuffer) referenceSampleBuffer;
@property (T^{opaqueCMSampleBuffer=},N,V_auxiliarySampleBuffer) auxiliarySampleBuffer;
@property (T^{__CVBuffer=},N,V_outputShiftmap) outputShiftmap;
@property (T@"<DisparityProcessorInferenceDelegate>",W,N,V_disparityInferenceProcessorDelegate) disparityInferenceProcessorDelegate;
@property (T{?=QQBQQfII},N,V_disparityConfig) disparityConfig;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_normalizedReferenceCropRect) normalizedReferenceCropRect;
@property (T@"<MTLCommandQueue>",&,N,V_metalCommandQueue) metalCommandQueue;
@property (TB,?,R,N) supportsExternalMemoryResource;
@property (T@"CMIExternalMemoryResource",?,&,N) externalMemoryResource;
@property (T@"NSDictionary",&,N,V_tuningParameters) tuningParameters;
@property (T@"NSDictionary",&,N,V_cameraInfoByPortType) cameraInfoByPortType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FigDisparityGenerator resetState];
-[FigDisparityGenerator releaseResources];
-[FigDisparityGenerator tuningParameters];
-[FigDisparityGenerator finishProcessing];
-[FigDisparityGenerator purgeResources];
-[FigDisparityGenerator setMetalCommandQueue:];
-[FigDisparityGenerator setCameraInfoByPortType:];
-[FigDisparityGenerator prewarm];
-[FigDisparityGenerator prepareToProcess:];
-[FigDisparityGenerator setup];
-[FigDisparityGenerator metalCommandQueue];
-[FigDisparityGenerator cameraInfoByPortType];
-[FigDisparityGenerator setTuningParameters:];
-[FigDisparityGenerator selectTuningParametersForCapture];
-[FigDisparityGenerator setEqualizeTeleGainToMatchReference:];
-[FigDisparityGenerator setOptions:];
-[FigDisparityGenerator setNormalizedReferenceCropRect:];
-[FigDisparityGenerator _extractAndRunSanityChecks];
-[FigDisparityGenerator _detectKeypointsLKTFlow:preShift:parameters:];
-[FigDisparityGenerator allocateResources:];
-[FigDisparityGenerator initWithCommandQueue:];
-[FigDisparityGenerator process];
-[FigDisparityGenerator dealloc];
-[FigDisparityGenerator shiftMapMetadata];
-[FigDisparityGenerator outputShiftmap];
-[FigDisparityGenerator setDisparityInferenceProcessorDelegate:];
-[FigDisparityGenerator metalContext];
-[FigDisparityGenerator setShouldComputeDisparityWhenCalibrationFails:];
-[FigDisparityGenerator isImageScalerOutputResolution:];
-[FigDisparityGenerator allocateResources];
-[FigDisparityGenerator setOutputShiftmap:];
-[FigDisparityGenerator disparityConfig];
-[FigDisparityGenerator fillShiftMapMetadataWithCalModel:referenceGDC:auxiliaryGDC:];
-[FigDisparityGenerator disparityInferenceProcessorDelegate];
-[FigDisparityGenerator normalizedReferenceCropRect];
-[FigDisparityGenerator isTextureScalerOutputResolution:];
-[FigDisparityGenerator setAuxiliarySampleBuffer:];
-[FigDisparityGenerator options];
-[FigDisparityGenerator equalizeTeleGainToMatchReference];
-[FigDisparityGenerator prewarmWithTuningParameters:];
-[FigDisparityGenerator setDisparityConfig:];
-[FigDisparityGenerator referenceSampleBuffer];
-[FigDisparityGenerator auxiliarySampleBuffer];
-[FigDisparityGenerator _detectKeypoints:preShift:];
-[FigDisparityGenerator shouldComputeDisparityWhenCalibrationFails];
-[FigDisparityGenerator disparityDiagnosticMetadata];
-[FigDisparityGenerator setReferenceSampleBuffer:];
-[FigDisparityGenerator _demosaic:andPreshift:tuningParameters:];
```
