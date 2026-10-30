# `LLVProcessorBufferManager`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 21 instance variables, 16 properties, 26 instance methods, 0 class methods

## Instance variables

```
^{__CVMetalTextureCache=} _textureCache;
Q _currentScale1Width;
Q _currentScale1Height;
@"PixelMetalBufferPair" _emptyHumanFullBodiesMask;
@"NSObject<OS_os_log>" _logger;
@"PixelMetalBufferPair" _inputYUV6Ch;
@"PixelMetalBufferPair" _inputHumanFullBodiesMask;
@"PixelMetalBufferPair" _outputYUV6Ch;
@"PixelMetalBufferPair" _currentOpticalFlowInput;
@"PixelMetalBufferPair" _historyOpticalFlowInput;
@"PixelMetalBufferPair" _opticalFlowOutput;
@"PixelMetalBufferPair" _guidedFilterOutput;
@"PixelMetalBufferPair" _dnrZoomFactorMap;
@"PixelMetalBufferPair" _fusionZoomFactorMap;
@"PixelMetalBufferPair" _fusionWeightMap;
@"PixelMetalBufferPair" _warpedYUV6Ch;
@"PixelMetalBufferPair" _historyYUV6Ch;
@"<MTLTexture>" _currentMipmap;
@"<MTLTexture>" _historyMipmap;
@"<MTLTexture>" _currentOpticalFlowScale2TextureView;
@"<MTLTexture>" _historyOpticalFlowScale2TextureView;
```

## Properties

```
@property (T@"PixelMetalBufferPair",&,N,V_inputYUV6Ch) inputYUV6Ch;
@property (T@"PixelMetalBufferPair",&,N,V_inputHumanFullBodiesMask) inputHumanFullBodiesMask;
@property (T@"PixelMetalBufferPair",&,N,V_outputYUV6Ch) outputYUV6Ch;
@property (T@"PixelMetalBufferPair",R,N,V_currentOpticalFlowInput) currentOpticalFlowInput;
@property (T@"PixelMetalBufferPair",R,N,V_historyOpticalFlowInput) historyOpticalFlowInput;
@property (T@"PixelMetalBufferPair",R,N,V_opticalFlowOutput) opticalFlowOutput;
@property (T@"PixelMetalBufferPair",R,N,V_guidedFilterOutput) guidedFilterOutput;
@property (T@"PixelMetalBufferPair",R,N,V_dnrZoomFactorMap) dnrZoomFactorMap;
@property (T@"PixelMetalBufferPair",R,N,V_fusionZoomFactorMap) fusionZoomFactorMap;
@property (T@"PixelMetalBufferPair",R,N,V_fusionWeightMap) fusionWeightMap;
@property (T@"PixelMetalBufferPair",R,N,V_warpedYUV6Ch) warpedYUV6Ch;
@property (T@"PixelMetalBufferPair",R,N,V_historyYUV6Ch) historyYUV6Ch;
@property (T@"<MTLTexture>",R,N,V_currentMipmap) currentMipmap;
@property (T@"<MTLTexture>",R,N,V_historyMipmap) historyMipmap;
@property (T@"<MTLTexture>",R,N,V_currentOpticalFlowScale2TextureView) currentOpticalFlowScale2TextureView;
@property (T@"<MTLTexture>",R,N,V_historyOpticalFlowScale2TextureView) historyOpticalFlowScale2TextureView;
```

## Instance methods

```
-[LLVProcessorBufferManager dealloc];
-[LLVProcessorBufferManager releaseIntermediateBuffers];
-[LLVProcessorBufferManager fusionWeightMap];
-[LLVProcessorBufferManager setInputYUV6Ch:];
-[LLVProcessorBufferManager currentMipmap];
-[LLVProcessorBufferManager currentOpticalFlowInput];
-[LLVProcessorBufferManager currentOpticalFlowScale2TextureView];
-[LLVProcessorBufferManager dnrZoomFactorMap];
-[LLVProcessorBufferManager dumpAllBuffersToDirectory:frameIndex:];
-[LLVProcessorBufferManager emptyHumanFullBodiesMask];
-[LLVProcessorBufferManager fusionZoomFactorMap];
-[LLVProcessorBufferManager guidedFilterOutput];
-[LLVProcessorBufferManager historyMipmap];
-[LLVProcessorBufferManager historyOpticalFlowInput];
-[LLVProcessorBufferManager historyOpticalFlowScale2TextureView];
-[LLVProcessorBufferManager historyYUV6Ch];
-[LLVProcessorBufferManager initWithTextureCache:];
-[LLVProcessorBufferManager inputHumanFullBodiesMask];
-[LLVProcessorBufferManager inputYUV6Ch];
-[LLVProcessorBufferManager opticalFlowOutput];
-[LLVProcessorBufferManager outputYUV6Ch];
-[LLVProcessorBufferManager prepareAllBuffersWithInput:inputHumanFullBodiesMask:output:scale1Width:scale1Height:opticalFlowWidth:opticalFlowHeight:];
-[LLVProcessorBufferManager prepareIntermediateBuffersWithScale1Width:scale1Height:opticalFlowWidth:opticalFlowHeight:];
-[LLVProcessorBufferManager setInputHumanFullBodiesMask:];
-[LLVProcessorBufferManager setOutputYUV6Ch:];
-[LLVProcessorBufferManager warpedYUV6Ch];
```
