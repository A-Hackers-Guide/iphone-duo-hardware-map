# `FPDisparityEstimator`

- Image: [`/System/Library/VideoProcessors/FPDisparityV3.bundle/FPDisparityV3`](../userland/System__Library__VideoProcessors__FPDisparityV3.bundle__FPDisparityV3.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 42 instance variables, 20 properties, 63 instance methods, 0 class methods

## Instance variables

```
@"FigMetalContext" _mtlContext;
@"<MTLCommandQueue>" _commandQueue;
@"<MTLComputePipelineState>" _costNCCPipelineState;
@"<MTLComputePipelineState>" _filterVertPipelineState;
@"<MTLComputePipelineState>" _filterHorzPipelineState;
@"<MTLComputePipelineState>" _interpolateAndSetPipelineState;
@"<MTLComputePipelineState>" _interpolateAndAccumPipelineState;
@"<MTLComputePipelineState>" _proximityOperatorPipelineState;
@"<MTLComputePipelineState>" _regularizationPipelineState;
@"<MTLBuffer>" _costsBuffer;
@"<MTLBuffer>" _bufTcLrc1;
@"<MTLBuffer>" _bufTcLrc2;
^{__CVBuffer=} _res_pxbuf;
[32@"<MTLTexture>"] _res_tex;
^{__CVBuffer=} _Hes_pxbuf;
[32@"<MTLTexture>"] _Hes_tex;
@"<MTLTexture>" _uv_tex_user_ref;
@"TVL1_v3" _tvl1Instance;
@"HBFGPU" _hbfgpuInstance;
@"<MTLTexture>" _disparityCorrectionTex;
[20f] _correctionBasisCoefficients;
@"<MTLComputePipelineState>" _correctionMapGenerationPipelineState;
S _quadraBinningFactor;
I _imageAGC;
@"FPDisparityEstimator_Parameters" _fpDisparityEstimatorParams;
@"PyrGPU" _imagePyramid;
@"NSArray" _GChannelPyramid;
@"<MTLTexture>" _H0ImTexture;
@"<MTLTexture>" _H1ImTexture;
@"<MTLTexture>" _V0ImTexture;
@"<MTLTexture>" _V1ImTexture;
@"<MTLTexture>" _binaryLambdaTexture;
@"<MTLTexture>" _segmentationTexture;
@"<MTLTexture>" _segmentationConfidenceTexture;
{CGSize="width"d"height"d} _outputDisparityResolution;
{?="xRawStep"I"yRawStep"I"xRawBase"I"yRawBase"I} _H0Metadata;
{?="xRawStep"I"yRawStep"I"xRawBase"I"yRawBase"I} _H1Metadata;
{?="xRawStep"I"yRawStep"I"xRawBase"I"yRawBase"I} _V0Metadata;
{?="xRawStep"I"yRawStep"I"xRawBase"I"yRawBase"I} _V1Metadata;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sensorCropRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sensorReadoutRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _totalSensorCropRect;
```

## Properties

```
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
```

## Instance methods

```
-[FPDisparityEstimator releaseResources];
-[FPDisparityEstimator allocateResources:];
-[FPDisparityEstimator dealloc];
-[FPDisparityEstimator setQuadraBinningFactor:];
-[FPDisparityEstimator quadraBinningFactor];
-[FPDisparityEstimator initWithMetalContext:];
-[FPDisparityEstimator _setupBuffer];
-[FPDisparityEstimator setSensorCropRect:];
-[FPDisparityEstimator sensorCropRect];
-[FPDisparityEstimator CreateKernelWithConst:constants:];
-[FPDisparityEstimator H0ImTexture];
-[FPDisparityEstimator H1Metadata];
-[FPDisparityEstimator computeAlignedSize:pixelFormat:];
-[FPDisparityEstimator setH0ImTexture:];
-[FPDisparityEstimator setV1ImTexture:];
-[FPDisparityEstimator GChannelPyramid];
-[FPDisparityEstimator H0Metadata];
-[FPDisparityEstimator H1ImTexture];
-[FPDisparityEstimator setH1ImTexture:];
-[FPDisparityEstimator setV0ImTexture:];
-[FPDisparityEstimator V0ImTexture];
-[FPDisparityEstimator V0Metadata];
-[FPDisparityEstimator V1ImTexture];
-[FPDisparityEstimator V1Metadata];
-[FPDisparityEstimator _allocateFPCostWorkBuffer:];
-[FPDisparityEstimator _computeCost:texGreenPixels:texOutputResU:texOutputHesU:level:resolutionScale:];
-[FPDisparityEstimator _computeFocusPixelDisparityFromResolution:box_cstr_range:disparity_scaling_factor:];
-[FPDisparityEstimator _costNCC:dynCfg:texDisparityIn:texGreenPixelsIn:texFocusPixelsIn:texTcLrcOut:resolutionScale:level:];
-[FPDisparityEstimator _debugInterpolate:texTcLrcIn:dynCfg:debugBuf:];
-[FPDisparityEstimator _doLocalRegularizationWithCommandBuffer:in_tex:level:parameters:];
-[FPDisparityEstimator _filterHorz:texTcLrcIn:texTcLrcOut:dynCfg:];
-[FPDisparityEstimator _filterVert:texTcLrcIn:texTcLrcOut:dynCfg:];
-[FPDisparityEstimator _generateCorrectionMap];
-[FPDisparityEstimator _interpolateAndAccumulate:texTcLrcIn:dynCfg:];
-[FPDisparityEstimator _proximityOperator:dynCfg:texDisparityIn:texOutputResUOut:texOutputHesUOut:level:];
-[FPDisparityEstimator _setCorrectionMapCoefficients:];
-[FPDisparityEstimator _setupFPPipelines];
-[FPDisparityEstimator _setupTexture];
-[FPDisparityEstimator binaryLambdaTexture];
-[FPDisparityEstimator computeFilterCurve:p3:array:];
-[FPDisparityEstimator estimateFocusPixelDisparityWithBox_cstr_range:disparity_scaling_factor:];
-[FPDisparityEstimator fpDisparityEstimatorParams];
-[FPDisparityEstimator imageAGC];
-[FPDisparityEstimator imagePyramid];
-[FPDisparityEstimator outputDisparityResolution];
-[FPDisparityEstimator segmentationConfidenceTexture];
-[FPDisparityEstimator segmentationTexture];
-[FPDisparityEstimator sensorReadoutRect];
-[FPDisparityEstimator setBinaryLambdaTexture:];
-[FPDisparityEstimator setFpDisparityEstimatorParams:];
-[FPDisparityEstimator setGChannelPyramid:];
-[FPDisparityEstimator setH0Metadata:];
-[FPDisparityEstimator setH1Metadata:];
-[FPDisparityEstimator setImageAGC:];
-[FPDisparityEstimator setImagePyramid:];
-[FPDisparityEstimator setOutputDisparity:];
-[FPDisparityEstimator setSegmentationConfidenceTexture:];
-[FPDisparityEstimator setSegmentationTexture:];
-[FPDisparityEstimator setSensorReadoutRect:];
-[FPDisparityEstimator setTotalSensorCropRect:];
-[FPDisparityEstimator setV0Metadata:];
-[FPDisparityEstimator setV1Metadata:];
-[FPDisparityEstimator totalSensorCropRect];
```
