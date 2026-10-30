# `/System/Library/VideoProcessors/FPDisparityV3.bundle/FPDisparityV3`

iOS 27.2 dyld shared cache image. Version `764.42.9.0.0`. **[DSC]**

## Linked libraries (10)

- `/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics`
- `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`
- `/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging`
- `/System/Library/Frameworks/CoreMedia.framework/CoreMedia`
- `/System/Library/Frameworks/CoreVideo.framework/CoreVideo`
- `/System/Library/Frameworks/Metal.framework/Metal`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 18 classes, 2 protocols, 424 methods, 128 properties

### Class pages

Every class and protocol, with its methods: [`FPDisparityEstimator`](../objc/FPDisparityEstimator_FPDisparityV3.md), [`FPDisparityEstimator_CostLevelParameters`](../objc/FPDisparityEstimator_CostLevelParameters_FPDisparityV3.md), [`FPDisparityEstimator_CostParameters`](../objc/FPDisparityEstimator_CostParameters_FPDisparityV3.md), [`FPDisparityEstimator_LevelParameters`](../objc/FPDisparityEstimator_LevelParameters_FPDisparityV3.md), [`FPDisparityEstimator_Parameters`](../objc/FPDisparityEstimator_Parameters_FPDisparityV3.md), [`FPDisparityEstimator_PostprocessingParameters`](../objc/FPDisparityEstimator_PostprocessingParameters_FPDisparityV3.md), [`FPDisparityEstimator_PreprocessingParameters`](../objc/FPDisparityEstimator_PreprocessingParameters_FPDisparityV3.md), [`FPDisparityEstimator_RegularizationParameters`](../objc/FPDisparityEstimator_RegularizationParameters_FPDisparityV3.md), [`FigFocusPixelDisparityGenerator`](../objc/FigFocusPixelDisparityGenerator_FPDisparityV3.md), [`FocusPixelDisparityDemosaic`](../objc/FocusPixelDisparityDemosaic_FPDisparityV3.md), [`FocusPixelDisparityTuningParameters`](../objc/FocusPixelDisparityTuningParameters_FPDisparityV3.md), [`HBFGPU`](../objc/HBFGPU_FPDisparityV3.md), [`HBFGPUParameters`](../objc/HBFGPUParameters_FPDisparityV3.md), [`ImageBufferProcessor`](../objc/ImageBufferProcessor_FPDisparityV3.protocol.md), [`NSObject`](../objc/NSObject_FPDisparityV3.protocol.md), [`PyrGPU`](../objc/PyrGPU_FPDisparityV3.md), [`TVL1_v3`](../objc/TVL1_v3_FPDisparityV3.md), [`TVL1_v3_RegularizationParameters`](../objc/TVL1_v3_RegularizationParameters_FPDisparityV3.md), [`TVL1_v3_SolverParameters`](../objc/TVL1_v3_SolverParameters_FPDisparityV3.md), [`disparityDebugUtils`](../objc/disparityDebugUtils_FPDisparityV3.md)

### Classes

`FPDisparityEstimator`, `FPDisparityEstimator_CostLevelParameters`, `FPDisparityEstimator_CostParameters`, `FPDisparityEstimator_LevelParameters`, `FPDisparityEstimator_Parameters`, `FPDisparityEstimator_PostprocessingParameters`, `FPDisparityEstimator_PreprocessingParameters`, `FPDisparityEstimator_RegularizationParameters`, `FigFocusPixelDisparityGenerator`, `FocusPixelDisparityDemosaic`, `FocusPixelDisparityTuningParameters`, `HBFGPU`, `HBFGPUParameters`, `PyrGPU`, `TVL1_v3`, `TVL1_v3_RegularizationParameters`, `TVL1_v3_SolverParameters`, `disparityDebugUtils`

### Protocols

`ImageBufferProcessor`, `NSObject`

### Properties

```
@property (T@"NSDictionary",&,N) tuningParameters;
@property (T@"NSDictionary",&,N) cameraInfoByPortType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"FPDisparityEstimator_Parameters",N,V_fpDisparityEstimatorParams) fpDisparityEstimatorParams;
@property (T{CGSize=dd},R,N,V_outputDisparityResolution) outputDisparityResolution;
@property (T@"PyrGPU",&,N,V_imagePyramid) imagePyramid;
@property (T@"NSArray",&,N,V_GChannelPyramid) GChannelPyramid;
@property (T@"<MTLTexture>",&,N,V_H0ImTexture) H0ImTexture;
@property (T@"<MTLTexture>",&,N,V_H1ImTexture) H1ImTexture;
@property (T@"<MTLTexture>",&,N,V_V0ImTexture) V0ImTexture;
@property (T@"<MTLTexture>",&,N,V_V1ImTexture) V1ImTexture;
@property (T@"<MTLTexture>",&,N,V_binaryLambdaTexture) binaryLambdaTexture;
@property (T{?=IIII},N,V_H0Metadata) H0Metadata;
@property (T{?=IIII},N,V_H1Metadata) H1Metadata;
@property (T{?=IIII},N,V_V0Metadata) V0Metadata;
@property (T{?=IIII},N,V_V1Metadata) V1Metadata;
@property (T@"<MTLTexture>",&,N,V_segmentationTexture) segmentationTexture;
@property (T@"<MTLTexture>",&,N,V_segmentationConfidenceTexture) segmentationConfidenceTexture;
@property (TS,N,V_quadraBinningFactor) quadraBinningFactor;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_sensorCropRect) sensorCropRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_sensorReadoutRect) sensorReadoutRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_totalSensorCropRect) totalSensorCropRect;
@property (TI,N,V_imageAGC) imageAGC;
@property (Tf,N,V_step) step;
@property (Tf,N,V_stepLowlight) stepLowlight;
@property (Tf,N,V_lambda) lambda;
@property (Tf,N,V_lambda_foreground) lambda_foreground;
@property (Tf,N,V_lambda_background) lambda_background;
@property (TI,N,V_nView) nView;
@property (Tf,N,V_microlensSpatialOffset) microlensSpatialOffset;
@property (Tf,N,V_foregroundPush) foregroundPush;
@property (Tf,N,V_backgroundPush) backgroundPush;
@property (TI,N,V_rigidWindowSupport) rigidWindowSupport;
@property (Tf,N,V_costMapAntialiasingStrength) costMapAntialiasingStrength;
@property (Tf,N,V_costEpsilon) costEpsilon;
@property (Tf,N,V_lensFieldCurvatureA0) lensFieldCurvatureA0;
@property (Tf,N,V_lensFieldCurvatureA1) lensFieldCurvatureA1;
@property (Tf,N,V_lensFieldCurvatureA2) lensFieldCurvatureA2;
@property (Tf,N,V_lensFieldCurvatureA3) lensFieldCurvatureA3;
@property (Tf,N,V_lensFieldCurvatureA4) lensFieldCurvatureA4;
@property (Tf,N,V_circleOfConfusionGain) circleOfConfusionGain;
@property (Tf,N,V_circleOfConfusionOffset) circleOfConfusionOffset;
@property (Tf,N,V_radialExponent) radialExponent;
@property (Tf,N,V_radialGain) radialGain;
@property (Tf,N,V_radialMin) radialMin;
@property (Tf,N,V_AGCLow) AGCLow;
@property (Tf,N,V_AGCHigh) AGCHigh;
@property (T@"NSArray",&,N,V_correctionCoefficientsWeights) correctionCoefficientsWeights;
@property (T@"FPDisparityEstimator_RegularizationParameters",&,N,V_regularizationParameters) regularizationParameters;
@property (T@"TVL1_v3_SolverParameters",&,N,V_solverParameters) solverParameters;
@property (T@"HBFGPUParameters",&,N,V_hbfParameters) hbfParameters;
@property (T@"FPDisparityEstimator_CostLevelParameters",&,N,V_costParameters) costParameters;
@property (T@"FPDisparityEstimator_CostParameters",&,N,V_FPcostParameters) FPcostParameters;
@property (T@"FPDisparityEstimator_PreprocessingParameters",&,N,V_FPpreprocessingParameters) FPpreprocessingParameters;
@property (T@"NSArray",&,N,V_levelsParameters) levelsParameters;
@property (T@"FPDisparityEstimator_PostprocessingParameters",&,N,V_FPpostprocessingParameters) FPpostprocessingParameters;
@property (Tf,N,V_shiftToDisparityRatio) shiftToDisparityRatio;
@property (Tf,N,V_calibrationMaxResidual1) calibrationMaxResidual1;
@property (Tf,N,V_calibrationMaxResidual2) calibrationMaxResidual2;
@property (Tf,N,V_blackLevelOffset) blackLevelOffset;
@property (Tf,N,V_blackLevelScaling) blackLevelScaling;
@property (Tf,N,V_alpha) alpha;
@property (Tf,N,V_beta) beta;
@property (Tf,N,V_gain) gain;
@property (Tf,N,V_offset) offset;
@property (Tf,N,V_segmentation_bias_foreground) segmentation_bias_foreground;
@property (Tf,N,V_segmentation_bias_background) segmentation_bias_background;
@property (T@"FigMetalContext",&,N,V_metalContext) metalContext;
@property (T^{opaqueCMSampleBuffer=},N,V_imageSampleBuffer) imageSampleBuffer;
@property (T^{__CVBuffer=},N,V_rawImagePixelBufferBuffer) rawImagePixelBufferBuffer;
@property (T^{__CVBuffer=},N,V_focusPixelBuffer) focusPixelBuffer;
@property (T@"NSDictionary",&,N,V_focusPixelMetadata) focusPixelMetadata;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_notUsedFocusPixelValidArea) focusPixelValidArea;
@property (T^{__CVBuffer=},N,V_personSegmentationPixelBuffer) personSegmentationPixelBuffer;
@property (T^{__CVBuffer=},N,V_personSegmentationConfidencePixelBuffer) personSegmentationConfidencePixelBuffer;
@property (T^{__CVBuffer=},N,V_outDisparity) outDisparity;
@property (T^{__CVBuffer=},N,V_binaryLambdaPixelBuffer) binaryLambdaPixelBuffer;
@property (T^{__CVBuffer=},N,V_H0) H0;
@property (T^{__CVBuffer=},N,V_H1) H1;
@property (T^{__CVBuffer=},N,V_V0) V0;
@property (T^{__CVBuffer=},N,V_V1) V1;
@property (Ti,R,N,V_disparityQuality) disparityQuality;
@property (TB,N,V_qualityEstimationEnabled) qualityEstimationEnabled;
@property (T@"NSDictionary",&,N,V_options) options;
@property (T@"NSDictionary",&,N,V_tuningParameters) tuningParameters;
@property (T@"NSDictionary",&,N,V_cameraInfoByPortType) cameraInfoByPortType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"FPDisparityEstimator_Parameters",R,N,V_FPDisparityEstimator_Config) FPDisparityEstimator_Config;
@property (T@"HBFGPUParameters",N,V_params) params;
@property (Ti,N,V_iterations) iterations;
@property (Ti,N,V_scales) scales;
@property (Ti,N,V_radius) radius;
@property (Ti,N,V_padding) padding;
@property (Tf,N,V_sigma_0) sigma_0;
@property (Tf,N,V_sigma_1) sigma_1;
@property (Tf,N,V_sigma_2) sigma_2;
@property (Tf,N,V_sigma_w) sigma_w;
@property (Tf,N,V_conf_min) conf_min;
@property (Tf,N,V_conf_max) conf_max;
@property (Tf,N,V_occ_thres) occ_thres;
@property (TB,R,N,V_isValid) isValid;
@property (Ti,R,N,V_countScales) countScales;
@property (T^{CGSize=dd},R,N) pyramidDimensions;
@property (T^{CGSize=dd},R,N) realPyramidDimensions;
@property (TB,N,V_useAntialiasingForDownsamplingToFinestResolution) useAntialiasingForDownsamplingToFinestResolution;
@property (TB,R,N,V_isValid) isValid;
@property (Ti,R,N,V_countScales) countScales;
@property (T{CGSize=dd},R,N,V_outputDisparityResolution) outputDisparityResolution;
@property (T@"PyrGPU",&,N,V_pyramidReference) pyramidReference;
@property (Tf,N,V_alpha) alpha;
@property (Tf,N,V_beta) beta;
@property (Tf,N,V_gain) gain;
@property (Tf,N,V_offset) offset;
@property (Tf,N,V_diffusion_eps) diffusion_eps;
@property (Tf,N,V_tau) tau;
@property (Tf,N,V_sigma) sigma;
@property (Tf,N,V_theta) theta;
@property (Tf,N,V_huber_eps) huber_eps;
@property (Ti,N,V_warpings) warpings;
@property (Ti,N,V_iterations) iterations;
@property (Tf,N,V_a_checkerboard) a_checkerboard;
@property (Tf,N,V_b_checkerboard) b_checkerboard;
```

## Strings (390)

```
bail
preprocessingDict
microlens_spatial_offset
lens_field_curvature_a2
_greenChannelPyramid
greenSizeDict
V1
v8@?0
_tvl1Instance
_setupTexture failed
fdp_local_regularization_kernel
reg
correction_coefficients_weights
gain
(HWidth == w) && (HHeight == h)
_downscale2X420fTBGRAEqualWithCommandBuffer failed
%s_L.ppm
demosaicHamiltonAdam
Could not create DEMOSAIC_HAMILTON pipeline
filterHorz
hbfDict
%s_R.f32
sizesDict
green_size
raw_size
_populateRawGreenChannelPyramid failed
wb
computePipelineState
\r
FPCostParameters
offset
metadata is nil
idx_swap_p invalid
tvl1_init_primal_dual
%s_L_%dx%d.%@
_proximityOperatorPipelineState
a_checkerboard
huber_eps
width
_binaryLambdaTexture
could not create out_tmp_u32_alias_tex
costEpsilon:                    %f \r
Could not create constantValues
costDict
circle_of_confusion_offset
_greenChannelPyramid[1]
TVL1GPUV3.m
commandBuffer
filterVert
_disparitySumBuffer
_fpDisparityEstimator != ((void *)0)
_rawImageTexture failed
renderPassDescriptor
f16
circle_of_confusion_gain
max_residual1
FocusPixelDisparityV3_tuningparameters.m
defaultsolverParameters
%s assert: \"%s\" at %s (%s:%d) - %s%s(err=%d)
(scale >= 0) && (scale < _countScales)
cost_epsilon
(idx_swap_p >= 0) && (idx_swap_p <= 1)
_regularizationPipelineState
texTcLrc2
basisImagesTexture
solver
padding
_focusPixelViews[0]
i
tvl1_upscale_single_kernel
defaultRegularizationParameters
regParameters
FragmentRescale
(scales >= 1) && (scales <= MAX_SCALES)
interpolateAndSet
<<<< FocusPixelDisparity >>>>
outTex is nil
out_tmp_u32_alias_tex
HBF:waitUntilCompleted
pyr_downscale_2x_equal_kernel
black_level_scaling
(idx_swap_uv >= 0) && (idx_swap_uv <= 1)
hbf_build_error_map_kernel
%s_L.f32
%u 
computePipelineState nil
_hbfgpuInstance
defaultCostLevelParameters
defaultPreprocessingParameters
dict
sigma_2
_focusPixelViews[1]
H1
rangeCG >= 0
shift_to_disparity_ratio
_setupImagePyramid failed
_pipelineStates[DISPARITY_QUALITY]
hbf_occlusion_handling_kernel
scale invalid
_binaryLambdaTexture failed
a_checkerboard >= 0.0f
rangeRM >= 0
pyrInfo->idx_ref != -1
_filterVertPipelineState
<<<< FocusPixelDisparity Tuning >>>> Fig
pyramidLevelsParams
FPDisparity
[self readSizeFromDictionary:greenSizeDict toWidth:&_gTopLevelImageWidth toHeight:&_gTopLevelImageHeight] == 0 
_pyramidReference != ((void *)0)
defaultPostprocessingParameters
sigma_0
((_gTopLevelDisparityWidth == 400) && (_gTopLevelDisparityHeight == 300))
_allocateResources failed
%s_F_%dx%d.%@
P5 %u %u 65535\n
\xa1
correction_map_generation_kernel
resourcesPath is nil
in_u32_alias_tex
idx_swap_uv invalid
disparityDebugUtils.m
defaultFPCostParameters
lambda_background
disparityIn is nil
fileBuf0_f32
cmdEnc
constantValues
preprocessing
foreground_push
FocusPixelDisparityV3: allocating resources for TVL1_v3 failed
Step
[self readSizeFromDictionary:disparitySize toWidth:&_gTopLevelDisparityWidth toHeight:&_gTopLevelDisparityHeight] == 0 
[self readSizeFromDictionary:colorSizeDict toWidth:&_gGuideImageWidth toHeight:&_gGuideImageHeight] == 0 
(Fig)
CorrectionMapData is not the right size
fpPatterns
imageSampleBuffer is nil
invalid format for focus pixel data.
Could not allocate rgbaImagesData
Could not allocate fileBuf
PyrGPUV3.m
%s signalled err=%d at <>:%d
rangeGY >= 0
count > 0
FPDisparityEstimator allocateResources failed
_greenChannelPyramidCVP[0]
_imageSampleBuffer != ((void *)0)
inUV is nil
0
costMapAntialiasingStrength:    %f \r
texTcLrc1
_pyr_image
Populate Image Pyramid failed
setOutputDisparity failed
_pipelineStates[DOWNSCALE_2X_402F_TO_BGRA]
hbf_compute_residual_error_offset_kernel
_setupFPPipelines failed
rpdDownscaleImage1
nview
alpha
X
_bufTcLrc2
radial_gain
_focusPixelViews[2]
FPDisparityV3 : Could not init _pyr_image
patternDict
P7\nWIDTH %u\nHEIGHT %u\nDEPTH 4\nMAXVAL 255\nTUPLTYPE RGB_ALPHA\nENDHDR
warpings
_disparityCountBuffer
Y
color_size
downscale_2x_equal_420ToRGB_kernel
(inputRaw.width&1) == 0 && (inputRaw.height&1) == 0
rigid_window_support
max_residual2
Patterns
Top Level Disparity size different than expected for estimation.
legacyLog
Fig
_isValid == __objc_yes
lens_field_curvature_a0
AGC_low
_rawImageTexture != ((void *)0)
Failed to decode total sensor crop rect
FigColorsWheel.c
(k >= 0) && (k < ColorsWheelContext_countColorsTransitions(ctx))
_filterHorzPipelineState
lens_field_curvature_a1
tau
CGRectMakeWithDictionaryRepresentation( (CFDictionaryRef)metadata[(id)kFigCaptureStreamMetadata_SensorCropRect], &sensorCropRect )
Device does not have enough ThreadgroupMemory
_computePipelines[k]
rigidWindowSupport:             %d \r
radial_min
radius
step_lowlight
PixelType
rawImagePixelBufferBuffer is nil
_segmentationTexture is nil. Will not compute the quality
P6 %u %u 255\n
FPDisparityEstimatorV3.m
FocusPixelDisparityV3: Could not allocate _fpDisparityEstimator.
Disparity estimation failed
Could not allocate imagesData_F16
Could not allocate srcPtr
black_level_offset
<<<< FocusPixelDisparity >>>> Fig
_isValid
imagesData_F16
CorrectionMapData.length == expectedBufferSize
b_checkerboard
found
Failed to decode sensor readout rect
_gChannelRescale
%s
%s_R_%dx%d.%@
<<<< FPDisparityEstimator (V3) >>>> Fig
((int)CVPixelBufferGetWidth(out_disparity) == (int)_outputDisparityResolution.width) && ((int)CVPixelBufferGetHeight(out_disparity) == (int)_outputDisparityResolution.height)
postprocessing
_costNCCPipelineState
cost_map_antialiasing_strength
FPPostprocessingParameters
lambda
FocusPixelDisparityV3: Failed to allocate Focus Pixel textures
_initShaders failed
height
H0
(v >= 0.f) && (v <= 1.f)
direction != kFigCaptureStreamFocusPixelDirection_None
disparityIn.width <= maxTotalThreadsPerThreadgroup
disparityIn.width > maxTotalThreadsPerThreadgroup
a_checkerboard + b_checkerboard <= 1.0f
<<<< FPDisparityEstimator (V3) >>>>
_interpolateAndSetPipelineState
theta
imageFull != ((void *)0)
outTex
_segmentationTexture
disparityIn.width <= 400
%s_W.f32
_bufTcLrc1
FPDisparityV3 : Could not init Metal context
FPDisparityV3 : Could not init _fpdDemosaic
sizes
status == FigFocusPixelDisparityStatusNoError
metadata
CGRectMakeWithDictionaryRepresentation( (CFDictionaryRef)metadata[(id)kFigCaptureStreamMetadata_SensorReadoutRect], &sensorReadoutRect )
v16@?0@\"<MTLCommandBuffer>\"8
lambda_foreground
entry
inY
_greenChannelPyramid[idx]
nView:                          %u \r
_allocateFPCostWorkBuffer failed
_costsBuffer
P5 %u %u 255\n
rangeMB >= 0
_interpolateAndAccumPipelineState
cmdBuffer is nil
hbf
solverParameters
rgbaImagesData
f32
CorrectionMapData
Failed to load CorrectionMapData
cost
FPPreprocessingParameters
Start
Failed to demosaic
could not create outTex
hbf_compute_residual_error_kernel
proximityOperator
disparity_size
outputDisparity != ((void *)0)
could not create in_u32_alias_tex
%s_C_%dx%d.%@
solverDict
disparityPixelSum
fileBuf1_f32
((int)input_res.width <= _max_input_res.width) && ((int)input_res.height <= _max_input_res.height)
sigma_1
CGRectMakeWithDictionaryRepresentation( (CFDictionaryRef)metadata[(id)kFigCaptureStreamMetadata_TotalSensorCropRect], &totalSensorCropRect )
downscale2XEqualWithCommandBuffer failed
pipelineDescriptor
HBFGPUV3.m
%@/zernike_basis.f16
<<<< FocusPixelDisparity Tuning >>>>
_metalContext
outDisparity is nil
disparityIn
%s.%c%c%c%c
err == 0 
ColorsWheelContext_computeColorComponent
textureDesc
segmentation_bias_foreground
_greenChannelPyramid[%d] is nil
fpPatterns.count <= 16
(w <= 32) && (h <= 32)
Could not allocate fileBuf1_f32
_correctionMapGenerationPipelineState
texTcLrc3
background_push
radial_exponent
costParameters
renderCommand
fp
_disparityCorrectionTex
disparitySize
rawSizeDict
the kernel only support disparityIn.width<=TOP_LEVEL_DISPARITY_WIDTH
_metalContext.device.maxThreadgroupMemoryLength >= 400*(2*sizeof(float)+2*sizeof(uint))
level invalid
_pipelineStates[DEMOSAIC_HAMILTON]
sigma
_disparityCountBuffer is nil
Failed to decode sensor crop rect
srcPtr
createColorsWheel_
regDict
lens_field_curvature_a4
hbfParameters
beta
segmentation_bias_background
pipelineDescriptor.fragmentFunction
%s_L_%dx%d.ppm
(in_tex.pixelFormat == MTLPixelFormatRGBA8Unorm) || (in_tex.pixelFormat == MTLPixelFormatBGRA8Unorm)
com.apple.cameracapture
scales
VertexPassthrough
b_checkerboard >= 0.0f
(level >= 0) && (level < (_countScales - 1))
_FPDisparityEstimator_Config
rangeBC >= 0
setColorsWheelComponent_
defaultHBFParameters
step
level < [valueArray count]
AGC
Could not create output file
pyr_downscale_2x_below_kernel
_setupBuffer failed
_focusPixelViews[3]
_gChannelTexture
V0
Top Level Disparity size different than expected for factory/calibration.
pipelineDescriptor.vertexFunction
instance not valid
Count
[self readSizeFromDictionary:rawSizeDict toWidth:&_gRawImageWidth toHeight:&_gRawImageHeight] == 0 
mtlCommandBuffer
inY is nil
tvl1_local_regularization_kernel
tvl1_upscale_dual_kernel
cmdBuffer
FPDDemosaicV3.m
FocusPixelDisparityV3: _fpdDemosaic allocateResources
imageFull is nil
err == noErr
postprocessingDict
AGC_high
_rawImagePixelBufferBuffer != ((void *)0)
Could not allocate fileBuf0_f32
KTRACE_MTLCMDBUF
resourcesPath
iterations
value != ((void *)0)
FocusPixelDisparityV3.m
tvl1_solver_kernel
levelParameters
use_correction
inUV
(level >= 0) && (level < _countScales)
hbf_filter_kernel
cmdBuf
costNCC
interpolateAndAccum
_disparitySumBuffer is nil
_fpdDemosaic
pixelTypeName
((_gTopLevelDisparityWidth == 208) && (_gTopLevelDisparityHeight == 156))
format != MTLPixelFormatInvalid
rangeYR >= 0
lens_field_curvature_a3
(VWidth == w) && (VHeight == h)
%s_C.f32
fileBuf
Failed to create directory \"%@\". Error: %@
Could not write %s
Could not allocate rgbaImagesData
Could not create %s
```
