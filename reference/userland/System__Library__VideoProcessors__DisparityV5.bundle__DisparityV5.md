# `/System/Library/VideoProcessors/DisparityV5.bundle/DisparityV5`

iOS 27.2 dyld shared cache image. Version `764.42.9.0.0`. **[DSC]**

## Linked libraries (12)

- `/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging`
- `/System/Library/PrivateFrameworks/Espresso.framework/Espresso`
- `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`
- `/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics`
- `/System/Library/Frameworks/CoreMedia.framework/CoreMedia`
- `/System/Library/Frameworks/CoreVideo.framework/CoreVideo`
- `/System/Library/Frameworks/Metal.framework/Metal`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 12 classes, 3 protocols, 344 methods, 101 properties

### Class pages

Every class and protocol, with its methods: [`ADCTuningParameters`](../objc/ADCTuningParameters_DisparityV5.md), [`AdaptiveClamping`](../objc/AdaptiveClamping_DisparityV5.md), [`Calibration`](../objc/Calibration_DisparityV5.md), [`Demosaic`](../objc/Demosaic_DisparityV5.md), [`DisparityDiagnostics`](../objc/DisparityDiagnostics_DisparityV5.md), [`DisparityTuningParameters`](../objc/DisparityTuningParameters_DisparityV5.md), [`DupDownscaleHalfConvert`](../objc/DupDownscaleHalfConvert_DisparityV5.md), [`FigDisparityGenerator`](../objc/FigDisparityGenerator_DisparityV5.md), [`FigDisparityMetadata`](../objc/FigDisparityMetadata_DisparityV5.md), [`GDCProcessor`](../objc/GDCProcessor_DisparityV5.md), [`ImageBufferProcessor`](../objc/ImageBufferProcessor_DisparityV5.protocol.md), [`LKTKeypointDetector`](../objc/LKTKeypointDetector_DisparityV5.md), [`MetalImageBufferProcessor`](../objc/MetalImageBufferProcessor_DisparityV5.protocol.md), [`NSObject`](../objc/NSObject_DisparityV5.protocol.md), [`disparityDebugUtils`](../objc/disparityDebugUtils_DisparityV5.md)

### Classes

`ADCTuningParameters`, `AdaptiveClamping`, `Calibration`, `Demosaic`, `DisparityDiagnostics`, `DisparityTuningParameters`, `DupDownscaleHalfConvert`, `FigDisparityGenerator`, `FigDisparityMetadata`, `GDCProcessor`, `LKTKeypointDetector`, `disparityDebugUtils`

### Protocols

`ImageBufferProcessor`, `MetalImageBufferProcessor`, `NSObject`

### Properties

```
@property (T@"NSDictionary",&,N) tuningParameters;
@property (T@"NSDictionary",&,N) cameraInfoByPortType;
@property (T@"<MTLCommandQueue>",&,N) metalCommandQueue;
@property (TB,?,R,N) supportsExternalMemoryResource;
@property (T@"CMIExternalMemoryResource",?,&,N) externalMemoryResource;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tf,R,N,V_keypointsDetectionThreshold) keypointsDetectionThreshold;
@property (Tf,R,N,V_defaultFocalLengthTeleMicrometers) defaultFocalLengthTeleMicrometers;
@property (Tf,R,N,V_defaultFocalLengthTeleMaxDeviationMicrometers) defaultFocalLengthTeleMaxDeviationMicrometers;
@property (Tf,R,N,V_defaultFocalLengthWideMicrometers) defaultFocalLengthWideMicrometers;
@property (Tf,R,N,V_defaultFocalLengthWideMaxDeviationMicrometers) defaultFocalLengthWideMaxDeviationMicrometers;
@property (T{AdaptiveCorrectionConfig=ddddddddddidddBdffffff{ADCPassConfig=BBdddddddddddidii}{ADCPassConfig=BBdddddddddddidii}{ADCPassConfig=BBdddddddddddidii}},R,N,V_adaptiveCorrectionConfig) adaptiveCorrectionConfig;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_referenceFinalCropRect) referenceFinalCropRect;
@property (Tf,R,N) referenceMagnification;
@property (T{CalModel=[2d][2d][2d][12d]d[2d][2d]},R,N,V_initialCalibration) initialCalibration;
@property (T{CalModel=[2d][2d][2d][12d]d[2d][2d]},R,N,V_correctedCalibration) correctedCalibration;
@property (T,N,V_orientationVector) orientationVector;
@property (TB,N,V_distortionCorrectionEnabled) distortionCorrectionEnabled;
@property (TB,N,V_temporalCorrectionEnabled) temporalCorrectionEnabled;
@property (TB,N,V_pixelBufferScalingEnabled) pixelBufferScalingEnabled;
@property (Tf,R,N,V_nearLimitDisparity) nearLimitDisparity;
@property (Tf,R,N,V_midLimitDisparity) midLimitDisparity;
@property (T{?=[3]},R,N,V_auxiliaryPaddingHInv) auxiliaryPaddingHInv;
@property (T{?=[3]},R,N,V_rectReferenceToReference) rectReferenceToReference;
@property (T{?=[3]},R,N,V_rectReferenceToAuxiliary) rectReferenceToAuxiliary;
@property (T{?=[3]},R,N,V_referenceToRectReference) referenceToRectReference;
@property (TI,N,V_outputImageHeight) outputImageHeight;
@property (Tf,N,V_gatNoiseStdInFullResolution) gatNoiseStdInFullResolution;
@property (Tf,N,V_tuningNoiseProcessingScale) tuningNoiseProcessingScale;
@property (Tf,N,V_maxAnalogGain) maxAnalogGain;
@property (Tf,R,N,V_maxAnalogGain) maxAnalogGain;
@property (Tf,R,N,V_nearLimitDistanceMM) nearLimitDistanceMM;
@property (Tf,R,N,V_midLimitDistanceMM) midLimitDistanceMM;
@property (Tf,R,N,V_keypointsDetectionThreshold) keypointsDetectionThreshold;
@property (Tf,R,N,V_defaultFocalLengthTeleMicrometers) defaultFocalLengthTeleMicrometers;
@property (Tf,R,N,V_defaultFocalLengthTeleMaxDeviationMicrometers) defaultFocalLengthTeleMaxDeviationMicrometers;
@property (Tf,R,N,V_defaultFocalLengthWideMicrometers) defaultFocalLengthWideMicrometers;
@property (Tf,R,N,V_defaultFocalLengthWideMaxDeviationMicrometers) defaultFocalLengthWideMaxDeviationMicrometers;
@property (TB,R,N,V_alignAuxiliaryImageForKeypoints) alignAuxiliaryImageForKeypoints;
@property (T{AdaptiveCorrectionConfig=ddddddddddidddBdffffff{ADCPassConfig=BBdddddddddddidii}{ADCPassConfig=BBdddddddddddidii}{ADCPassConfig=BBdddddddddddidii}},R,N,V_adaptiveCorrectionConfig) adaptiveCorrectionConfig;
@property (Tf,R,N,V_minDisparityClampingPercentile) minDisparityClampingPercentile;
@property (Tf,R,N,V_maxDisparityClampingPercentile) maxDisparityClampingPercentile;
@property (Ti,R,N,V_stereoDisparityEstimatorLevels) stereoDisparityEstimatorLevels;
@property (TB,R,N,V_useLKTKeypointDetection) useLKTKeypointDetection;
@property (Tf,R,N,V_bidirectionalError) bidirectionalError;
@property (Tf,R,N,V_confidenceRadialWeight) confidenceRadialWeight;
@property (Tf,R,N,V_confidenceMinimum) confidenceMinimum;
@property (Ti,R,N,V_blockSize) blockSize;
@property (Ti,R,N,V_lastScale) lastScale;
@property (Ti,R,N,V_nwarps) nwarps;
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
@property (TS,N,V_version) version;
@property (Tf,N,V_baseline) baseline;
@property (Tf,N,V_telePixelSizeInMillimeters) telePixelSizeInMillimeters;
@property (Tf,N,V_widePixelSizeInMillimeters) widePixelSizeInMillimeters;
@property (T{?=[3]},N,V_teleIntrinsicMatrix) teleIntrinsicMatrix;
@property (T{?=[3]},N,V_wideIntrinsicMatrix) wideIntrinsicMatrix;
@property (T{CGSize=dd},N,V_teleIntrinsicMatrixReferenceDimensions) teleIntrinsicMatrixReferenceDimensions;
@property (T{CGSize=dd},N,V_wideIntrinsicMatrixReferenceDimensions) wideIntrinsicMatrixReferenceDimensions;
@property (T{?=[4]},N,V_teleExtrinsicMatrix) teleExtrinsicMatrix;
@property (T{?=[4]},N,V_wideExtrinsicMatrix) wideExtrinsicMatrix;
@property (T@"NSArray",C,N,V_teleLensDistortionCoefficients) teleLensDistortionCoefficients;
@property (T@"NSArray",C,N,V_wideLensDistortionCoefficients) wideLensDistortionCoefficients;
@property (T@"NSArray",C,N,V_teleInverseLensDistortionCoefficients) teleInverseLensDistortionCoefficients;
@property (T@"NSArray",C,N,V_wideInverseLensDistortionCoefficients) wideInverseLensDistortionCoefficients;
@property (T{CGPoint=dd},N,V_teleLensDistortionOpticalCenter) teleLensDistortionOpticalCenter;
@property (T{CGPoint=dd},N,V_wideLensDistortionOpticalCenter) wideLensDistortionOpticalCenter;
@property (T{CGSize=dd},R,N,V_ref_size) ref_size;
@property (T{CGSize=dd},R,N,V_aux_size) aux_size;
@property (Ti,R,N,V_nscales) nscales;
@property (Ti,R,N,V_lastScale) lastScale;
@property (Ti,N,V_nwarpings) nwarpings;
@property (T@"<MTLTexture>",R,N) uv_fwd;
@property (T@"<MTLTexture>",R,N) uv_bwd;
@property (T@"<MTLTexture>",R,N) conf_fwd;
@property (T@"<MTLTexture>",R,N) conf_bwd;
@property (T@"<MTLBuffer>",R,N) keypoints;
@property (T@"<MTLBuffer>",R,N) keypoints_confidence;
```

## Strings (719)

```
undistortedReferenceTex != ((void *)0)
rgbaImagesData
out->xyPointsTeleSelection
Calibration: Could not allocate resources for ADC without distortion.
adcStatus.pass1SufficientPoints
Baseline vector cannot be [0,0].
gdcCoeffsTeleUndistortCoordinates
DisparityV5: Could not allocate AdaptiveClamping.
errCode == noErr
extrinRotTeleToWide
_refHalfResRGBATexture is not 10ARGB.
ADC did not converge, applying previous temporal biases to the initial calibration.
Cannot allocate histogram metal buffer
Cannot bind texture mask
passDistSufficientPoints
DisparityV5: Could not allocate GDC.
extrinsicRefToAuxPrime
( _minDisparityClampingPercentile >= 0.0f ) && ( _minDisparityClampingPercentile <= 1.0f )
_blockSize is invalid
disparityDebugUtils.m
resampleKernel
AWBComboBGain
wideImageFull
DisparityV5: Unable to setup metal allocator
( CVPixelBufferGetWidth( auxiliaryImageFullRaw ) == _scalerOutputWidth ) && ( CVPixelBufferGetHeight( auxiliaryImageFullRaw ) == _scalerOutputHeight )
_refHalfResRGBATexture
tuningParameters != ((void *)0)
DisparityV5: Could not allocateResources.
_pipelineStates[RGB_TO_LUMA_KERNEL]
cmdBuf != ((void *)0)
Unplausible rotation likely due to a corrupted calibration model.
focalLengthWidePix
DisparityV5: allocating _rectifiedDisparityMap failed
%s
rangeOCyW
<<<< DisparityAdaptiveClamping >>>>
FragmentGDC_DISTORT
disparityV5.m
%s_F_%dx%d.%@
reprojectedCorner.z > 0
passDistModelTele
lkt_features_derivatives
numPoints <= adc->maxNumPoints
initShaders failed
initialCal
pass1Cal
_rectifiedDisparityMap width is wrong
Provided Wide/Aux intrinsic calibration has a ~0 pixel size.
defaultFocalLengthTeleMicrometers
_pipelineStates[DISPARITY_COMPUTE_CLAMPING]
LSCGainGridData
DisparityV5: allocating resources for keypoint detector failed(FigRegToolbox,Auxiliary)
only RAW (RGG4 & BGG4) inputs are supported
dynamicPolynomialData
_options is nil
histLen > 0
disparityTexture
lumaTexture is nil
_lscGainsTex
( kCVPixelFormatType_OneComponent16Half == CVPixelBufferGetPixelFormatType(_rectifiedDisparityMap) ) || ( kCVPixelFormatType_DisparityFloat16 == CVPixelBufferGetPixelFormatType(_rectifiedDisparityMap) )
Could not bind undistortedReference to texture.
rangePFL_W
overrideConfigPassDist
minDisparityPercentile is invalid
rawExtraPixelsY >=0
pass1AnalyticalPrecond
DisparityV5: Sanity checks failed.
AWBComboRGain
ret
minDisparityPercentile
AGC
out_bgra is nil
outputTex has incorrect pixel format - should be MTLPixelFormatR8Unorm
wideImageFull is not 420YpCbCr8BiPlanarFullRange
auxiliaryMetadata
err == noErr
xyPoints
alignAuxiliaryImageForKeypoints
rangeRM >= 0
rangeMB >= 0
kernelDownscalerConverterYUVA
pflTeleOutOfRange
CVPixelBufferGetBytesPerRow(_auxHalfResRectifiedRGBAPixelBuffer) >= sizeof(uint8_t) * _scalerOutputWidth && CVPixelBufferGetHeight(_auxHalfResRectifiedRGBAPixelBuffer) >= _scalerOutputHeight
Invalid resolution _auxHalfResRectifiedRGBAPixelBuffer.
*buffer != ((void*)0)
__tg_fabs((__typeof__(__tg_promote((refinedCalModel.pixelSize_um[CalBufferTypeAuxiliary]))))(refinedCalModel.pixelSize_um[CalBufferTypeAuxiliary])) > 1e-5
sensorDGain
kernelDownscalerConverterY
auxHalfRectifiedTex != ((void *)0)
out->xyPointsWideTransposed
scaleTuningWithDigitalZoomByFactor
DisparityV5: Could not allocate Calibration.
ub.stereodisparity.fsdnetEnabled
 ], [auxiliary]: [
focusWindowIsValid
Unable to clamp the disparity
+[LKTKeypointDetector _computeScalingFactor:dst_tex:scale_xy_inv:coeff:]
_KernelY
_adaptiveCorrectionKeypointsAuxiliaryDistorted
FigMetalAllocator_Disparity
LKT:waitUntilCompleted
( _nwarps >= 2 )
max clampingPercentiles is invalid, should be [0.0...1.0]
FundamentalDistortionErrorV2.c
EVZeroMetadata
_lscGainsTex is nil
gdcCoefficients
Calibration: ADC did not have enough valid keypoints in distortion pass.
<<<< Disparity >>>>
a > 0
RawSensorWidth not in the metadata
outDisparityTex != ((void *)0)
distortionModel
rectTeleToWide
epErrorLimitWidePix_FirstPass
Unable to create kernel kernelDownscalerConverterYUVA
Reference
f32
_pipelineStates[RESAMPLE_KERNEL]
pass1NumPoints
pass2SPGEvalPre
temporalInitializationFactor
rangeBC >= 0
gdc is nil.
mtlAuxiliaryTex
P6 %u %u 255\n
%s_C.f32
confidenceRadialWeight
AGC not in the metadata
gdcCoeffsWideUndistortCoordinates
DisparityV5: allocating _refHalfResRectifiedRGBAPixelBuffer failed
( _confidenceMinimum >= 0.0f )
_pipelineStates[DISPARITY_COMPUTE_HISTOGRAM]
Expected DDF>0 since distortion has dynamic component. 
initialNumPoints
( _maxDisparityClampingPercentile >= 0.0f ) && ( _maxDisparityClampingPercentile <= 1.0f )
( CVPixelBufferGetPixelFormatType( maskPixelBuffer ) == kCVPixelFormatType_64RGBAHalf )
_metadataParameters.sensorAGC <= _maxAnalogGain
AGC is greater than the maximal value
AWBComboBGain not in the metadata
%s_L.ppm
fileBuf
_ResourcesAvailable = NO
passDistSPGEvalPre
(_disparityConfig.outputDisparityHeight & (8 - 1)) == 0
%s signalled err=%d at <>:%d
Could not compile shaders
ExposureTime
(k >= 0) && (k < ColorsWheelContext_countColorsTransitions(ctx))
oisShiftTeleY
mtlReferenceTex is nil
numPoints > 0
The number of scales specified is too large
H_T_to_corrRectT rectifying homography is invalid.
rangeOCxW_dist
basePolynomialData
DisparityDebugStatus
(_disparityConfig.inputImageWidth & 3) == 0
DisparityV5: allocating resources for keypoint detector failed(FigRegToolbox,Reference)
Could not compute auxiliary image preshift for keypoints.
Auxiliary
,\n intrinsics: \n --> [reference]:\n [ %.3f , %.3f , %.3f ] \n [ %.3f , %.3f , %.3f ] \n [ %.3f , %.3f , %.3f ], \n --> [auxiliary]:\n [ %.3f , %.3f , %.3f ] \n [ %.3f , %.3f , %.3f ] \n [ %.3f , %.3f , %.3f ]
maxNumPoints > 0
kernelDownscaleConvertAndCenterCrop
Unable to create kernel kernelDownscaleConvertAndCenterCrop
(in_w == 2 * out_w) && (in_h == 2 * out_h)
Calibration: AdaptiveCorrection_transformPointsWithMatrix failed.
_auxHalfResRGBATexture
[TotalSensorCropRectForProcessedRaw][Y] not in the metadata
ADC: Adaptive Correction, fullCorrectionWithDistortion failed.
DisparityV5: allocating _refLowResRectifiedRGBAPixelBuffer failed
DisparityV5: allocating _auxLowResRectifiedRGBAPixelBuffer failed
auxiliaryMeta is nil.
$
%s_R.f32
xyPointsIn
histogramBuffer
ReadNoise_1x not in the metadata
(_disparityConfig.outputDisparityWidth <= 768) && (_disparityConfig.outputDisparityHeight <= 576)
_outputShiftmap != ((void*)0)
imagesData_F16
denom > 0
test_H_T_to_corrRectT.z > scale_min && test_H_T_to_corrRectT.z < scale_max
useLKTKeypoints
Calibration: An error occurred in ADC solver pass 2.
f16
LKT::Pyramid
( _blockSize >= 0)
DisparityV5: allocating resources for keypoint detector failed (FigRegToolbox,mem)
_nwarps must be even.
ispDGainRangeExpansionFactor
camInfoByPort
%s_W.f32
rangeOCxW
defaultFocalLengthWideMicrometers
SensorBlackLevel
SensorBlackLevel not in the metadata
xyDistortedPointsWide
Calibration: An error occurred in ADC solver distortion pass.
<<<< GDC >>>> Fig
ocShiftTtoRectT[2] > 0.0f
spgEpsilon
keypointOutliersPercentile
%s assert: \"%s\" at %s (%s:%d) - %s%s(err=%d)
metalContext is nil
v16@?0@\"<MTLCommandBuffer>\"8
Calibration.m
pass2SPGConverged
Could not allocate fileBuf0_f32
lkt_solver_box_y
xyPointsWide
\n
H_W_to_corrRectT rectifying homography is invalid.
rangeOCxT_dist
spgMaxIterations
val
AWBComboRGain not in the metadata
[SBP:DownscaleHalfConvert] Fig
wideImageCropped is NULL
dynamicPolynomialData is nil.
distortionReference
rangePFL_W_dist
image size mismatch. Input must be larger than output
overlapMetadata
passDistNumPoints
referenceMagnification > 0.0f
referenceMagnification is 0
F16Buffer
adcStatus.pass2SufficientPoints
opticalCenterTeleY
_auxLowResRectifiedRGBAPixelBuffer is not RGBAF16.
DisparityV5: could not compute initial Calibration
adcStatus.passDistSufficientPoints
FragmentGDC
Output disparity width is not a multiple of FSDNET_DISPARITY_MULTIPLE_OF
P5 %u %u 255\n
out_bgra
Vaux_3x4 != ((void*)0)
DisparityV5: allocating resources for keypoint detector failed (FigRegToolbox,rsrc)
,\n lens distortion coeffs: [tele]: [
lkt_solver_box_x_and_Axb
rotationAuxToAuxPrime
auxiliarySampleBuffer is null.
downscaleCommandBuffer
failed to bind a pixel buffer to a new texture.
, pixel size: [reference]: %.5f mm (%.2f um) [auxiliary]: %.5f mm (%.2f um)
Unable to allocate buffer.
( CVPixelBufferGetPixelFormatType( inputOutputPixelBuffer ) == kCVPixelFormatType_OneComponent16Half ) || ( CVPixelBufferGetPixelFormatType( inputOutputPixelBuffer ) == kCVPixelFormatType_DisparityFloat16 )
distortionTele
AWBComboGGain not in the metadata
in_luma
_auxiliarySampleBuffer != ((void*)0)
FSDNet processing failed
cmdBuffer
ispDGainRangeExpansionFactor not in metadata
sensorRawValidBufferRect.size.width > 0 && sensorRawValidBufferRect.size.height > 0
simd_length(baselineVector) > 0.0f
<<<< GDC >>>>
DisparityV5 : Could not init Metal context
BaseConfiguration
srcPtr
SushiRawBlackLevel not in the metadata
CVPixelBufferGetPixelFormatType(wideImageFull) == kCVPixelFormatType_420YpCbCr8BiPlanarFullRange
basePolynomial is NULL.
pass2ParallelPctNegative
legacyLog
Provided Wide/Aux distortion has a ~0 pixel size.
spgMaxAlphaIterations
maskPixelBuffer is not rgba/half format
Vref_3x4 != ((void*)0)
( _nwarps % 2 == 0 )
GDCProcessor.m
ShiftmapMin
Config
(_disparityConfig.inputImageHeight & 3) == 0
isRGBA10( referenceImageFullRaw ) && isRGBA10( auxiliaryImageFullRaw )
RGB auxiliary input size is not correct
_metalContext.allocator
outputShiftmap is NULL.
DisparityV5: keypoints computation failed (FigRegToolbox,ref).
LKT:ComputeFlow level %d
downscaleKernel
cmdEnc
Calibration: Could not allocate ADC.
ADC
_adaptiveCorrectionKeypointsReferenceDistorted
DisparityV5: pointer to buffer is NULL when reallocating.
__tg_fabs((__typeof__(__tg_promote((refinedDistortionWide.pixelSizeMM))))(refinedDistortionWide.pixelSizeMM)) > 1e-8
_pipelineStates[DEMOSAIC2X_KERNEL] is nil
inputTex != ((void *)0)
undistortedPaddedAuxiliaryTex != ((void *)0)
,\n extrinsics:\n --> [tele]:\n [ %.3f , %.3f , %.3f ][ %.3f ] \n [ %.3f , %.3f , %.3f ][ %.3f ] \n [ %.3f , %.3f , %.3f ][ %.3f ], \n --> [auxiliary]:\n [ %.3f , %.3f , %.3f ][ %.3f ] \n [ %.3f , %.3f , %.3f ][ %.3f ] \n [ %.3f , %.3f , %.
lkt_solver_prepare_matrices
teleToRectTele
test_H_corrRectT_to_T.z > scale_min && test_H_corrRectT_to_T.z < scale_max
xyDistortedPointsTele
outputTex != ((void *)0)
simd_length(_orientationVector) > 0.0f
_lktKeypointDetector
v8@?0
__tg_fabs((__typeof__(__tg_promote((distortionReference->pixelSizeMM))))(distortionReference->pixelSizeMM)) > 1e-8
pass2ParallelShiftInf
ShiftmapJPEG
tuning parameters are nil
DisparityV5: keypoints computation failed
temporalFilteringStrengthParallel
rangeGY >= 0
DupDownscaleHalfConvert.m
_transposedKeypoints.xyPointsTeleTransposed
extrinsicOutOfRange
polyDynamic
ShiftmapMax
RGB reference input size is not correct
bidirectionalError
inputOutputPixelBuffer width should be a multiple of 4 pixels
_ContextAvailable = NO
out->xyPointsTeleDistortionCorrected
out->xyPointsWideDistortionCorrected
passDistCal
Shiftmap
temporalFilteringStrength
_maxAnalogGain > 0.0f
_KernelDownscaleConvertAndCenterCrop
adcStatus.pass2SPGConverged
Output disparity height is not a multiple of FSDNET_DISPARITY_MULTIPLE_OF
_auxHalfResRectifiedRGBAPixelBuffer is not 10ARGB.
Failed to preProcessMetadata Reference Metadata
extremeMacroDistMM
_metalContext
Failed to update tuning paramters
lkt_keypoints_from_flow
_bidirectionalError is invalid
LSCGains
kernelDownscaleAndCrop
focalLength != ((void *)0)
Calibration: An error occurred in ADC solver pass 1.
auxTex
Could not allocate rgbaImagesData
rangeOCxT
_confidenceRadialWeight must to be within [0..1]
_pipelineStates[DISPARITY_COMPUTE_HISTOGRAM].maxTotalThreadsPerThreadgroup >= 1024
LSCGain not available
overlapRadius != ((void *)0)
pixelSizeMicrometers
((Boolean)(((timestamp).flags & kCMTimeFlags_Valid) != 0))
(Fig)
rotationRefToRefPrime
calRotated
RawSensorWidth
pass2SPGNumIterations
_auxHalfResRGBATexture is not 10ARGB.
DisparityV5: _rectifiedDisparityMap is not float16 nor DisparityFloat16
auxLowRectifiedTex != ((void *)0)
sucess == __objc_yes
Could not allocate fileBuf
adcStatus.passDistSPGConverged
initialDistortionTele
_calibration != ((void *)0)
textureDescriptor
outputTex.pixelFormat == MTLPixelFormatR8Unorm
options
Calibration: ADC did not receive enough initial keypoints.
Calibration: AdaptiveCorrection_fullCorrection did not have enough key points.
passDistSPGEvalPost
Could not allocate srcPtr
bundle
bundle is nil
createColorsWheel_
_KernelDownscaleAndCrop
_gdcTransform != ((void *)0)
CVPixelBufferGetHeight(_rectifiedDisparityMap) == 576
(uint32_t)num_raw_keypoints <= (_keypointGridWidth * _keypointGridHeight)
sensorDGain not in the metadata
(v >= 0.f) && (v <= 1.f)
(f_in_w > f_out_w) && (f_in_h > f_out_h)
Calibration: ADC did not have enough valid keypoints in pass 1.
Calibration: ADC did not have enough valid keypoints in pass 2.
oisShiftWideY
Invalid resolution _auxHalfResRGBATexture.
clampingPercentiles.x >= 0.0f && clampingPercentiles.x <= 1.0f
Cannot allocate command encoder
<<<< STEREODISPARITY DEMOSAIC >>>> Fig
refLowRectifiedTex != ((void *)0)
dwn_err == 0 
Odd image dimensions are not supported
adcSuccessful
errorVal_LessThanExtremeMacro
oisShiftWideX
_referenceDemosaic != ((void *)0)
%s.%c%c%c%c
histLen <= kFMinConSPG_MaxHistoryLength
rgbTexture
rgbTexture is nil
adcRet == ADCResultOK
pass2ParallelCal
DisparityV5: Could not allocate keypoint detector (FigRegToolbox)
lkt_zero_flow
AdaptiveCorrectionV2.c
maskPixelBuffer
inputOutputPixelBuffer is not float16 nor DisparityFloat16
cmdEnc is nil
pass2Cal
out
epErrorLimitTelePix_ParallelCorrection
[self _compileShaders] == 0 
pixelSizeMicrometers != ((void *)0)
adcBail
portsToConfig
inputImagesFormatsAreValid
fileBuf1_f32
AdaptiveClamping.m
Cannot allocate metalContext
Cannot allocate clamping metal buffer
_pipelineStates[DOWNSCALE_KERNEL]
Orientation vector cannot be [0,0].
Could not bind undistortedPaddedAuxiliary to texture.
Number of LKT keypoints is higher than allocated. 
_nwarps must be 2 or higher.
out_luma
outputTex is nil
ADC: Adaptive Correction, applyTemporalCorrectionState failed.
_auxiliaryDemosaic != ((void *)0)
_rectifiedDisparityMap height is wrong
%s_L_%dx%d.ppm
Provided Tele/Ref intrinsic calibration has a ~0 pixel size.
adc->hasTemporalBias
Fig
Could not allocate F16Buffer
cmdBuf is nil
refHalfRectifiedTex != ((void *)0)
%u 
(dst_tex.width == src_tex.width) && (dst_tex.height == src_tex.height)
rangePFL_T
DisparityClamping
rangeCG >= 0
cmdEnc != ((void *)0)
wideImageCropped
ReferenceFrameMetadata
adcStatus.pass1SPGConverged
self
PortType
dynamicPolynomial
Q
_clamping != ((void *)0)
xyPointsTele
AWBComboGGain
pass1SPGConverged
gdcCommandBuffer
,\n distortion optical center: [reference]: (%.3f, %.3f), [auxiliary]: (%.3f, %.3f)
__tg_fabs((__typeof__(__tg_promote((distortionAuxiliary->pixelSizeMM))))(distortionAuxiliary->pixelSizeMM)) > 1e-8
mA_normalization > 0.0f
Calibration
maskPixelBuffer is NULL
Cannot allocate command buffer
pass2SPGEvalPost
opticalCenterWideX
DisparityVersion
<<<< StereoDisparityTuningParameters (V5) >>>> Fig
Calibration: AdaptiveCorrection_computeVerticalBaselineTransform failed.
VertexGDC
__tg_fabs((__typeof__(__tg_promote((refinedDistortionTele.pixelSizeMM))))(refinedDistortionTele.pixelSizeMM)) > 1e-8
minPointsForAdjustment
DisparityHistogramKernel
_maxAnalogGain not set
_ContextAvailable
_ResourcesAvailable
DisparityV5: allocating _auxHalfResLumaPixelBuffer failed
__tg_fabs((__typeof__(__tg_promote((calibration->pixelSize_um[CalBufferTypeReference]))))(calibration->pixelSize_um[CalBufferTypeReference])) > 1e-5
test_H_W_to_corrRectT.z > scale_min && test_H_W_to_corrRectT.z < scale_max
_lastScale is invalid
maxDisparity > 0.0f
_outputImageHeight
referenceMetadata
basePolynomial
stereodisparity.useLKT
__tg_fabs((__typeof__(__tg_promote((distortionTele->pixelSizeMM))))(distortionTele->pixelSizeMM)) > 1e-8
keypointsDetectionThreshold
confidenceMinimum
_pipelineStates[RGB_TO_LUMA_KERNEL] is nil
Y
passDistSPGNumIterations
referenceSampleBuffer is null.
out->epipolarDistance
fmincon_spgV2.c
inputOutputPixelBuffer
cmdEncoder
setColorsWheelComponent_
DisparityV5: Unable to init metal allocator
DisparityV5: Could not extract Parameters from metadata and options
mtlAuxiliaryTex is nil
<%@: %p>: %@%@%@%@%@%@%@
%s_L.f32
ReadNoise_1x
initialDistortionWide
adc
f > 0.0f
disparityV5_tuningparameters.m
lastScale
isPassEnabled
Image width is not a multiple of 4
inDisparityTex != ((void *)0)
calibration
intermediateMacroDistMM
maxDisparity should be higher than 0
<<<< Calibration >>>>
basePolynomialData is nil.
dynamicTermZero || (_ddf[i] > 0.0f)
min clampingPercentiles is invalid, should be [0.0...1.0]
DisparityComputeClampingValues
rawExtraPixelsY is < 0
cmdBuf
 ]
Could not allocate fileBuf1_f32
com.apple.cameracapture
ConversionGain
Calibration: AdaptiveCorrection_rotateCalModel failed.
_keypointListRtb
wb
errorVal_GreaterThanInf
overrideConfigPass2
ValidBufferRectForProcessedRaw
Height
[ValidBufferRectForProcessedRaw][Height] not in the metadata
__tg_fabs((__typeof__(__tg_promote((calibration->pixelSize_um[CalBufferTypeAuxiliary]))))(calibration->pixelSize_um[CalBufferTypeAuxiliary])) > 1e-5
KTRACE_MTLCMDBUF
_outputImageHeight not set
in_chroma is nil
passDistSPGConverged
DisparityV5: allocating _auxHalfResRectifiedRGBAPixelBuffer failed
Can't create an inverse intrinsic matrix for focal length <= 0.
epErrorLimitWidePix_SecondPass
( _bidirectionalError >= 0.0f )
demosaic2xKernel
_pipelineStates[DEMOSAIC2X_KERNEL]
pass2NumPoints
opticalCenterTeleX
The output disparity resolution is larger than the maximum disparity resolution supported by FSDNet
runAnalyticalPreconditioning
numVars > 0
( rgbTexture.width == lumaTexture.width ) && ( rgbTexture.height == lumaTexture.height )
gdcCoeffsWideDistortCoordinates
focalLengthPix
ColorsWheelContext_computeColorComponent
rangeYR >= 0
focalLengthTelePix
,\n inverse lens distortion coeffs: [reference]: [
retGDC
blockSize
in_chroma
ret == 1
_keypointDetRtb
buffer != ((void*)0)
P7\nWIDTH %u\nHEIGHT %u\nDEPTH 4\nMAXVAL 255\nTUPLTYPE RGB_ALPHA\nENDHDR
lkt_downscale_2x
__tg_fabs((__typeof__(__tg_promote((refinedCalModel.pixelSize_um[CalBufferTypeReference]))))(refinedCalModel.pixelSize_um[CalBufferTypeReference])) > 1e-5
mB_normalization > 0.0f
Unable to initialize disparity adaptive clamping class
ReadNoise_8x not in the metadata
pass1SPGEvalPre
opticalCenterX
DisparityV5: _auxHalfResLumaPixelBuffer is not properly aliased
_referenceSampleBuffer != ((void*)0)
baseline: %.3f
P5 %u %u 65535\n
wideImageFull is NULL
CameraViewMatrix
DisparityV5: Could not allocate Reference Demosaic.
_auxiliaryMeta != ((void*)0)
LKT::KeypointsFromFlow
test_H_corrRectT_to_W.z > scale_min && test_H_corrRectT_to_W.z < scale_max
rgbToLumaKernel
status
xyPointsTransformed
DemosaicV5.m
count > 0
oisShiftTeleX
Could not create output file
LKTKeypointDetector.m
lkt_features
AGC is smaller than the minimal value 1.0
Unable to create kernel kernelDownscalerConverterY
image size mismatch
pass1SPGEvalPost
com.apple.coremedia
Failed to preProcessMetadata Auxiliary Metadata
refTex is nil
%s_R_%dx%d.%@
<<<< DisparityAdaptiveClamping >>>> Fig
FigColorsWheel.c
in_luma is nil
IC_ref_rot.z > 0.1
Image height is not a multiple of 4
errorVal_BetweenIntermediate_ExtremeMacro
number != ((void *)0)
mtlReferenceTex
DisparityV5: keypoints computation failed (FigRegToolbox,target).
auxTex is nil
skip_biases
Provided calibration model cannot be NULL.
nwarps
MaxAnalogGain
_pipelineStates[DISPARITY_COMPUTE_CLAMPING_VALUES]
_refLowResRectifiedRGBAPixelBuffer is not RGBAF16.
maxDisparityPercentile
( CVPixelBufferGetWidth( inputOutputPixelBuffer ) % 4 ) == 0
inputTex.pixelFormat == MTLPixelFormatR8Unorm
Calibration: AdaptiveCorrection_fullCorrection pass 2 failed to converge.
opticalCenterY
<<<< Disparity >>>> Fig
DisparityV5: FigMetalAllocatorDescriptor is nil
%s_L_%dx%d.%@
rangeOCyT
CalibrationValidRadius
harvesting.enabled
( _lastScale >= 0 )
dynamicPolynomial is NULL.
adcStatus.initialSufficientPoints
passDistModelWide
_referenceMeta != ((void*)0)
%s_C_%dx%d.%@
Failed to adjust parallel error for infinity.
clampingPercentiles.y >= 0.0f && clampingPercentiles.y <= 1.0f
maskTexture
(_disparityConfig.outputDisparityWidth & (8 - 1)) == 0
DisparityV5: allocating _refHalfResLumaPixelBuffer failed
_options != ((void *)0)
Invalid resolution _refHalfResRGBATexture.
GPU max threads is too small
rgbTexture and lumaTexture have different size
_pixelBufferScalingFactor[i].x <= 10.f && _pixelBufferScalingFactor[i].x > 0.1f
( CVPixelBufferGetWidth( referenceImageFullRaw ) == _scalerOutputWidth ) && ( CVPixelBufferGetHeight( referenceImageFullRaw ) == _scalerOutputHeight )
out->xyPointsTeleTransposed
_pipelineStates[DOWNSCALE_KERNEL] is nil
TotalSensorCropRectForProcessedRaw
polyBase
Provided Tele/Ref distortion has a ~0 pixel size.
epErrorLimitWidePix
err == 0 
RawSensorHeight not in the metadata
_KernelYUVA
Unable to create kernel _KernelDownscaleAndCrop
gdcCoeffsTeleDistortCoordinates
gdcResult == 0 
out->xyPointsWideSelection
ADC: Could not apply the temporal biases after calibration refinement.
lumaTexture
_pipelineStates[RESAMPLE_KERNEL] is nil
RawSensorHeight
referenceMeta is nil.
config
maxDisparityPercentile is invalid
grad || !computeGradient
_transposedKeypoints.xyPointsWideTransposed
DisparityV5: Could not allocate Auxiliary Demosaic.
CVPixelBufferGetWidth(_rectifiedDisparityMap) == 768
refTex
__tg_fabs((__typeof__(__tg_promote((distortionWide->pixelSizeMM))))(distortionWide->pixelSizeMM)) > 1e-8
H_corrRectT_to_T rectifying homography is invalid.
_confidenceMinimum must be non-negative.
out_luma is nil
pass1PrecondCal
pass2SufficientPoints
opticalCenterWideY
defaultFocalLengthTeleMaxDeviationMicrometers
numVars <= kFMinConSPG_MaxNumVariables
pass1SPGNumIterations
Could not allocate imagesData_F16
fp
bail
cal
metalContext
_metadataParameters.sensorAGC >= agc_gains.x
pixelSizeMM
Invalid resolution _refHalfResLumaPixelBuffer.
xyPointsOut
rangePFL_T_dist
DisparityClampingKernel
fileBuf0_f32
Invalid parameter
overrideConfigPass1
Cannot bind texture
<<<< STEREODISPARITY DEMOSAIC >>>>
pass1SufficientPoints
DisparityV5: Could not allocate lktKeypointDetector.
lkt_flow_consistency
inputOutputPixelBuffer is NULL
ispDGain not in metadata
result
disparityV5_diagnostics.m
initialSufficientPoints
LKTParameters
clampingBuffer
ReadNoise_8x
ispDGain
reprojectedCorner.z > 0.f
pflWideOutOfRange
 %.3f,
distortionWide
SushiRawBlackLevel
OIS shift could not be computed!
\xf0\xd2\xf0\xf0\xf0\xf0\xf0\xe1\xf0\xf0\xf0\xf0\xf02
Demosaic failed
defaultFocalLengthWideMaxDeviationMicrometers
ConversionGain not in the metadata
distortionAuxiliary
H_corrRectT_to_W rectifying homography is invalid.
only RGB10A2 inputs are supported
R33 > 0
rectTeleToTele
( _confidenceRadialWeight >= 0.0f && _confidenceRadialWeight <= 1.0f )
inputTex is nil
inputTex has incorrect pixel format - should be MTLPixelFormatR8Unorm
<<<< Calibration >>>> Fig
allocatorDescriptor
Could not write %s
Could not allocate rgbaImagesData
Could not create %s
Failed to create directory \"%@\". Error: %@
%@::threadExecutionWidth = %d, maxTotalThreadsPerThreadgroup = %d
```
