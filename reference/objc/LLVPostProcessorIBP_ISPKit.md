# `LLVPostProcessorIBP`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MetalImageBufferProcessor`
- 18 instance variables, 10 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"FrameOutCombinedEncoder" _frameOutEncoder;
@"NSObject<OS_os_log>" _logger;
^{__CVMetalTextureCache=} _textureCache;
@"<MTLCommandBuffer>" _commandBufferPostProcessor;
@"LLVUserDefaults" _userDefaults;
@"LLVTuningParameters" _llvTuningParameters;
@"<MTLTexture>" _linear2sRGBLUT;
@"<MTLTexture>" _sRGB2linearLUT;
@"<MTLTexture>" _cGamma2linearLUT;
@"<MTLTexture>" _linear2cGammaLUT;
@"<MTLBuffer>" _shaderModelInfo;
B _useGPUGammaCalculation;
Q _scale0Width;
Q _scale0Height;
@"<MTLCommandQueue>" metalCommandQueue;
@"LLVPostProcessorFrameParameters" _frameParameters;
@"NSDictionary" _tuningParameters;
@"NSDictionary" _cameraInfoByPortType;
```

## Properties

```
@property (T@"LLVPostProcessorFrameParameters",&,N,V_frameParameters) frameParameters;
@property (T@"NSDictionary",&,N,V_tuningParameters) tuningParameters;
@property (T@"NSDictionary",&,N,V_cameraInfoByPortType) cameraInfoByPortType;
@property (T@"<MTLCommandQueue>",&,N,VmetalCommandQueue) metalCommandQueue;
@property (TB,?,R,N) supportsExternalMemoryResource;
@property (T@"CMIExternalMemoryResource",?,&,N) externalMemoryResource;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LLVPostProcessorIBP resetState];
-[LLVPostProcessorIBP tuningParameters];
-[LLVPostProcessorIBP finishProcessing];
-[LLVPostProcessorIBP purgeResources];
-[LLVPostProcessorIBP setMetalCommandQueue:];
-[LLVPostProcessorIBP setCameraInfoByPortType:];
-[LLVPostProcessorIBP prewarm];
-[LLVPostProcessorIBP prepareToProcess:];
-[LLVPostProcessorIBP setup];
-[LLVPostProcessorIBP metalCommandQueue];
-[LLVPostProcessorIBP cameraInfoByPortType];
-[LLVPostProcessorIBP setTuningParameters:];
-[LLVPostProcessorIBP process];
-[LLVPostProcessorIBP dealloc];
-[LLVPostProcessorIBP initWithMetalCommandQueue:];
-[LLVPostProcessorIBP initWithMetalCommandQueue:textureCache:resolution:];
-[LLVPostProcessorIBP setFrameParameters:];
-[LLVPostProcessorIBP frameParameters];
-[LLVPostProcessorIBP initWithMetalCommandQueue:textureCache:];
```
