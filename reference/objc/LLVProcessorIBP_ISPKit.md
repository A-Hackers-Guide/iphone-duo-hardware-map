# `LLVProcessorIBP`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MetalImageBufferProcessor`
- 50 instance variables, 17 properties, 34 instance methods, 0 class methods

## Instance variables

```
@"YUV6ChDownscaleEncoder" _downscaleEncoder;
@"YPyramidEncoder" _pyramidEncoder;
@"YUV6ChFillEncoder" _fillEncoder;
@"YUV6ChBlenderEncoder" _blenderEncoder;
@"CondFillZoomMapEncoder" _condFillZoomMapEncoder;
@"<MTLCommandBuffer>" _commandBufferProcessorGPU;
@"<MTLCommandBuffer>" _commandBufferProcessorGPUHybridWarper;
@"<MTLCommandBuffer>" _commandBufferProcessorAfterANE;
@"EITAlignEncoder" _eitAlignEncoder;
@"MVDSuperWide0_5X" _modelSuperWide0_5X;
@"MVDSuperWide1X" _modelSuperWide1X;
@"MVDTele4X" _modelTele4X;
@"MVDTele8X" _modelTele8X;
@"MVDWide1X" _modelWide1X;
@"MVDWide2X" _modelWide2X;
@"MVD" _modelCurrent;
@"MVDANEMemoryProvider" _aneMemoryProvider;
^{__CVMetalTextureCache=} _textureCache;
@"NSString" _dumpDirectoryPath;
@"NSObject<OS_os_log>" _logger;
_sensorReadoutCropPositionPrev;
_fesCropPositionPrev;
_fesCropDimensionsPrev;
_fesOutDimensionsPrev;
_sensorArrayOutputRectPositionPrev;
@"NSString" _portTypePrev;
Q _quadraBinFactorPrev;
S _preIspDGainPrev;
@"<MTLBuffer>" _shaderModelInfo;
f _eitPrev;
@"<MTLTexture>" _linear2sRGBLUT;
@"<MTLTexture>" _sRGB2linearLUT;
@"<MTLTexture>" _cGamma2linearLUT;
@"<MTLTexture>" _linear2cGammaLUT;
@"LLVUserDefaults" _userDefaults;
@"LLVTuningParameters" _tuningParameters;
Q _scale1Width;
Q _scale1Height;
Q _opticalFlowWidth;
Q _opticalFlowHeight;
@"<MTLCommandQueue>" metalCommandQueue;
@"NSDictionary" cameraInfoByPortType;
@"NSDictionary" tuningParameters;
@"LLVProcessorFrameParameters" _frameParameters;
@"LLVTuningParameters" _llvTuningParameters;
@"<MTLBuffer>" _homographyBuffer;
@"LLVProcessorBufferManager" _bufferManager;
@"HybridWarper" _hybridWarper;
@"OpticalFlowPortraitLKT" _opticalFlow;
@"<LLVGuidedFilter>" _guidedFilter;
```

## Properties

```
@property (T@"LLVUserDefaults",&,N,V_userDefaults) userDefaults;
@property (T@"LLVTuningParameters",&,N,V_llvTuningParameters) llvTuningParameters;
@property (T@"<MTLBuffer>",&,N,V_homographyBuffer) homographyBuffer;
@property (T@"LLVProcessorBufferManager",&,N,V_bufferManager) bufferManager;
@property (T@"HybridWarper",&,N,V_hybridWarper) hybridWarper;
@property (T@"OpticalFlowPortraitLKT",&,N,V_opticalFlow) opticalFlow;
@property (T@"<LLVGuidedFilter>",&,N,V_guidedFilter) guidedFilter;
@property (T@"LLVProcessorFrameParameters",&,N,V_frameParameters) frameParameters;
@property (T@"<MTLCommandQueue>",&,N,VmetalCommandQueue) metalCommandQueue;
@property (TB,?,R,N) supportsExternalMemoryResource;
@property (T@"CMIExternalMemoryResource",?,&,N) externalMemoryResource;
@property (T@"NSDictionary",&,N,VtuningParameters) tuningParameters;
@property (T@"NSDictionary",&,N,VcameraInfoByPortType) cameraInfoByPortType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LLVProcessorIBP resetState];
-[LLVProcessorIBP tuningParameters];
-[LLVProcessorIBP finishProcessing];
-[LLVProcessorIBP purgeResources];
-[LLVProcessorIBP setMetalCommandQueue:];
-[LLVProcessorIBP setCameraInfoByPortType:];
-[LLVProcessorIBP prewarm];
-[LLVProcessorIBP prepareToProcess:];
-[LLVProcessorIBP setup];
-[LLVProcessorIBP userDefaults];
-[LLVProcessorIBP metalCommandQueue];
-[LLVProcessorIBP cameraInfoByPortType];
-[LLVProcessorIBP setTuningParameters:];
-[LLVProcessorIBP process];
-[LLVProcessorIBP dealloc];
-[LLVProcessorIBP setUserDefaults:];
-[LLVProcessorIBP opticalFlow];
-[LLVProcessorIBP setOpticalFlow:];
-[LLVProcessorIBP initWithMetalCommandQueue:];
-[LLVProcessorIBP initWithMetalCommandQueue:textureCache:resolution:];
-[LLVProcessorIBP setFrameParameters:];
-[LLVProcessorIBP frameParameters];
-[LLVProcessorIBP bufferManager];
-[LLVProcessorIBP getModelWithPortType:andQuadraBinFactor:];
-[LLVProcessorIBP guidedFilter];
-[LLVProcessorIBP homographyBuffer];
-[LLVProcessorIBP hybridWarper];
-[LLVProcessorIBP initWithMetalCommandQueue:textureCache:];
-[LLVProcessorIBP llvTuningParameters];
-[LLVProcessorIBP setBufferManager:];
-[LLVProcessorIBP setGuidedFilter:];
-[LLVProcessorIBP setHomographyBuffer:];
-[LLVProcessorIBP setHybridWarper:];
-[LLVProcessorIBP setLlvTuningParameters:];
```
