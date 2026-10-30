# `LLVPreProcessorIBP`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MetalImageBufferProcessor`
- 16 instance variables, 10 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"FrameInCombinedEncoder" _frameInEncoder;
@"NSObject<OS_os_log>" _logger;
^{__CVMetalTextureCache=} _textureCache;
@"<MTLCommandBuffer>" _commandBufferPreProcessor;
@"LLVUserDefaults" _userDefaults;
@"<MTLTexture>" _linear2sRGBLUT;
@"<MTLTexture>" _sRGB2linearLUT;
@"<MTLTexture>" _cGamma2linearLUT;
@"<MTLTexture>" _linear2cGammaLUT;
@"<MTLBuffer>" _shaderModelInfo;
Q _scale0Width;
Q _scale0Height;
@"<MTLCommandQueue>" metalCommandQueue;
@"LLVPreProcessorFrameParameters" _frameParameters;
@"NSDictionary" _tuningParameters;
@"NSDictionary" _cameraInfoByPortType;
```

## Properties

```
@property (T@"LLVPreProcessorFrameParameters",&,N,V_frameParameters) frameParameters;
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
-[LLVPreProcessorIBP resetState];
-[LLVPreProcessorIBP tuningParameters];
-[LLVPreProcessorIBP finishProcessing];
-[LLVPreProcessorIBP purgeResources];
-[LLVPreProcessorIBP setMetalCommandQueue:];
-[LLVPreProcessorIBP setCameraInfoByPortType:];
-[LLVPreProcessorIBP prewarm];
-[LLVPreProcessorIBP prepareToProcess:];
-[LLVPreProcessorIBP setup];
-[LLVPreProcessorIBP metalCommandQueue];
-[LLVPreProcessorIBP cameraInfoByPortType];
-[LLVPreProcessorIBP setTuningParameters:];
-[LLVPreProcessorIBP process];
-[LLVPreProcessorIBP dealloc];
-[LLVPreProcessorIBP initWithMetalCommandQueue:];
-[LLVPreProcessorIBP initWithMetalCommandQueue:textureCache:resolution:];
-[LLVPreProcessorIBP setFrameParameters:];
-[LLVPreProcessorIBP frameParameters];
-[LLVPreProcessorIBP initWithMetalCommandQueue:textureCache:];
```
