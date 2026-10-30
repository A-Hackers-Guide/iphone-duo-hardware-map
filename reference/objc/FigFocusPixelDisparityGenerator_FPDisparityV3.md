# `FigFocusPixelDisparityGenerator`

- Image: [`/System/Library/VideoProcessors/FPDisparityV3.bundle/FPDisparityV3`](../userland/System__Library__VideoProcessors__FPDisparityV3.bundle__FPDisparityV3.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ImageBufferProcessor`
- 54 instance variables, 23 properties, 67 instance methods, 0 class methods

## Instance variables

```
[3@"<MTLComputePipelineState>"] _pipelineStates;
@"<MTLRenderPipelineState>" _gChannelRescale;
@"NSMutableArray" _greenChannelPyramid;
[2^{__CVBuffer}] _greenChannelPyramidCVP;
@"FocusPixelDisparityDemosaic" _fpdDemosaic;
@"PyrGPU" _pyr_image;
@"FPDisparityEstimator" _fpDisparityEstimator;
[4@"<MTLTexture>"] _focusPixelViews;
@"<MTLTexture>" _gChannelTexture;
@"<MTLTexture>" _rawImageTexture;
@"<MTLTexture>" _segmentationTexture;
@"<MTLTexture>" _segmentationConfidenceTexture;
@"<MTLBuffer>" _disparitySumBuffer;
@"<MTLBuffer>" _disparityCountBuffer;
@"<MTLTexture>" _binaryLambdaTexture;
@"FocusPixelDisparityTuningParameters" _fpDisparityTuningParameters;
[20f] _correctionBasisCoefficients;
B _correctionBasisCoefficientsPresent;
I _processingType;
^{?=IiiIIIIII} _focusPixelLocationDescriptors;
@"NSString" _moduleSerialNumber;
^{__CVBuffer=} _disparityPixelBufferForCalibration;
I gNumViews;
I gHxFocusPixelViewWidth;
I gHxFocusPixelViewHeight;
I gVxFocusPixelViewWidth;
I gVxFocusPixelViewHeight;
I _gTopLevelImageWidth;
I _gTopLevelImageHeight;
I _gTopLevelDisparityWidth;
I _gTopLevelDisparityHeight;
I _gRawImageWidth;
I _gRawImageHeight;
I _gGuideImageWidth;
I _gGuideImageHeight;
B _qualityEstimationEnabled;
i _disparityQuality;
@"NSDictionary" _tuningParameters;
@"NSDictionary" _cameraInfoByPortType;
@"FigMetalContext" _metalContext;
^{opaqueCMSampleBuffer=} _imageSampleBuffer;
^{__CVBuffer=} _rawImagePixelBufferBuffer;
^{__CVBuffer=} _focusPixelBuffer;
@"NSDictionary" _focusPixelMetadata;
^{__CVBuffer=} _personSegmentationPixelBuffer;
^{__CVBuffer=} _personSegmentationConfidencePixelBuffer;
^{__CVBuffer=} _outDisparity;
^{__CVBuffer=} _binaryLambdaPixelBuffer;
^{__CVBuffer=} _H0;
^{__CVBuffer=} _H1;
^{__CVBuffer=} _V0;
^{__CVBuffer=} _V1;
@"NSDictionary" _options;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _notUsedFocusPixelValidArea;
```

## Properties

```
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
```

## Instance methods

```
-[FigFocusPixelDisparityGenerator resetState];
-[FigFocusPixelDisparityGenerator tuningParameters];
-[FigFocusPixelDisparityGenerator finishProcessing];
-[FigFocusPixelDisparityGenerator purgeResources];
-[FigFocusPixelDisparityGenerator setCameraInfoByPortType:];
-[FigFocusPixelDisparityGenerator prewarm];
-[FigFocusPixelDisparityGenerator prepareToProcess:];
-[FigFocusPixelDisparityGenerator setup];
-[FigFocusPixelDisparityGenerator cameraInfoByPortType];
-[FigFocusPixelDisparityGenerator setTuningParameters:];
-[FigFocusPixelDisparityGenerator setOptions:];
-[FigFocusPixelDisparityGenerator init];
-[FigFocusPixelDisparityGenerator _allocateResources];
-[FigFocusPixelDisparityGenerator initWithCommandQueue:];
-[FigFocusPixelDisparityGenerator process];
-[FigFocusPixelDisparityGenerator dealloc];
-[FigFocusPixelDisparityGenerator metalContext];
-[FigFocusPixelDisparityGenerator setV1:];
-[FigFocusPixelDisparityGenerator options];
-[FigFocusPixelDisparityGenerator prewarmWithTuningParameters:];
-[FigFocusPixelDisparityGenerator setH1:];
-[FigFocusPixelDisparityGenerator _initShaders];
-[FigFocusPixelDisparityGenerator disparityQuality];
-[FigFocusPixelDisparityGenerator setFocusPixelBuffer:];
-[FigFocusPixelDisparityGenerator setFocusPixelMetadata:];
-[FigFocusPixelDisparityGenerator setFocusPixelValidArea:];
-[FigFocusPixelDisparityGenerator setH0:];
-[FigFocusPixelDisparityGenerator setImageSampleBuffer:];
-[FigFocusPixelDisparityGenerator setOutDisparity:];
-[FigFocusPixelDisparityGenerator setPersonSegmentationConfidencePixelBuffer:];
-[FigFocusPixelDisparityGenerator setPersonSegmentationPixelBuffer:];
-[FigFocusPixelDisparityGenerator setQualityEstimationEnabled:];
-[FigFocusPixelDisparityGenerator setRawImagePixelBufferBuffer:];
-[FigFocusPixelDisparityGenerator outDisparity];
-[FigFocusPixelDisparityGenerator _allocateTextures];
-[FigFocusPixelDisparityGenerator setMetalContext:];
-[FigFocusPixelDisparityGenerator H1];
-[FigFocusPixelDisparityGenerator H0];
-[FigFocusPixelDisparityGenerator _populateRawGreenChannelPyramid];
-[FigFocusPixelDisparityGenerator V0];
-[FigFocusPixelDisparityGenerator V1];
-[FigFocusPixelDisparityGenerator _computeDisparityQuality:];
-[FigFocusPixelDisparityGenerator _createTextureOfWidth:andHeight:withFormat:];
-[FigFocusPixelDisparityGenerator _createTextureOfWidth:andHeight:withFormat:textureUsage:];
-[FigFocusPixelDisparityGenerator _downscale2X420fTBGRAEqualWithCommandBuffer:in_Ytex:in_UVtex:out_tex:cropRect:];
-[FigFocusPixelDisparityGenerator _extractFocusPixelMetadata];
-[FigFocusPixelDisparityGenerator _overrideTuningParametersForFactory];
-[FigFocusPixelDisparityGenerator _populateImagePyramidFrom420fPixelBuffer:cropRect:];
-[FigFocusPixelDisparityGenerator _populateImagePyramidFrom:];
-[FigFocusPixelDisparityGenerator _setupImagePyramid];
-[FigFocusPixelDisparityGenerator binaryLambdaPixelBuffer];
-[FigFocusPixelDisparityGenerator focusPixelBuffer];
-[FigFocusPixelDisparityGenerator focusPixelMetadata];
-[FigFocusPixelDisparityGenerator focusPixelValidArea];
-[FigFocusPixelDisparityGenerator getFPBuffersSizeFromOptions:];
-[FigFocusPixelDisparityGenerator getFrameSizesFromOptions:];
-[FigFocusPixelDisparityGenerator getPatternDetailsFrom:outTypeName:outCountX:outCountY:outStartX:outStartY:outStepX:outStepY:];
-[FigFocusPixelDisparityGenerator getSequenceDetailsFrom:withName:outCount:outStart:outStep:];
-[FigFocusPixelDisparityGenerator imageSampleBuffer];
-[FigFocusPixelDisparityGenerator mapPixelTypeNameToDirection:];
-[FigFocusPixelDisparityGenerator personSegmentationConfidencePixelBuffer];
-[FigFocusPixelDisparityGenerator personSegmentationPixelBuffer];
-[FigFocusPixelDisparityGenerator qualityEstimationEnabled];
-[FigFocusPixelDisparityGenerator rawImagePixelBufferBuffer];
-[FigFocusPixelDisparityGenerator readSizeFromDictionary:toWidth:toHeight:];
-[FigFocusPixelDisparityGenerator setBinaryLambdaPixelBuffer:];
-[FigFocusPixelDisparityGenerator setV0:];
```
