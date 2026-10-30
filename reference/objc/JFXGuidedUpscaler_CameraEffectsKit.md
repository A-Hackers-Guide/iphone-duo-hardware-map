# `JFXGuidedUpscaler`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 11 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
@"MPSImageBilinearScale" _scaler;
@"MPSImageGaussianBlur" _blur;
^{__CVMetalTextureCache=} _textureCache;
@"<MTLCommandQueue>" _commandQueue;
@"JFXMetalHelpers" _helpers;
@"JFXGuidedFilter" _guidedFilter;
B _showSimilarity;
f _updateRate;
f _temporalSmoothing;
f _similarityGaussianBlur;
@"<MTLTexture>" _scaledGuidance;
@"<MTLTexture>" _oldScaledGuidance;
@"<MTLTexture>" _currentOutputTexture;
@"<MTLTexture>" _previousOutputTexture;
@"<MTLTexture>" _similarity;
@"<MTLComputePipelineState>" _pipelineStateSimilarity;
@"<MTLComputePipelineState>" _pipelineStateSmoothing;
```

## Properties

```
@property (T@"<MTLTexture>",&,N,V_scaledGuidance) scaledGuidance;
@property (T@"<MTLTexture>",&,N,V_oldScaledGuidance) oldScaledGuidance;
@property (T@"<MTLTexture>",&,N,V_currentOutputTexture) currentOutputTexture;
@property (T@"<MTLTexture>",&,N,V_previousOutputTexture) previousOutputTexture;
@property (T@"<MTLTexture>",&,N,V_similarity) similarity;
@property (T@"<MTLComputePipelineState>",&,N,V_pipelineStateSimilarity) pipelineStateSimilarity;
@property (T@"<MTLComputePipelineState>",&,N,V_pipelineStateSmoothing) pipelineStateSmoothing;
@property (Tf,N,V_temporalSmoothing) temporalSmoothing;
@property (TB,N,V_showSimilarity) showSimilarity;
@property (Tf,N,V_updateRate) updateRate;
@property (Tf,N,V_similarityGaussianBlur) similarityGaussianBlur;
```

## Instance methods

```
-[JFXGuidedUpscaler initialized];
-[JFXGuidedUpscaler dealloc];
-[JFXGuidedUpscaler setUpdateRate:];
-[JFXGuidedUpscaler updateRate];
-[JFXGuidedUpscaler initWithDiameter:];
-[JFXGuidedUpscaler similarity];
-[JFXGuidedUpscaler setSimilarity:];
-[JFXGuidedUpscaler currentOutputTexture];
-[JFXGuidedUpscaler oldScaledGuidance];
-[JFXGuidedUpscaler pipelineStateSimilarity];
-[JFXGuidedUpscaler pipelineStateSmoothing];
-[JFXGuidedUpscaler previousOutputTexture];
-[JFXGuidedUpscaler scaleImage:guidanceImage:destinationImage:];
-[JFXGuidedUpscaler scaledGuidance];
-[JFXGuidedUpscaler setCurrentOutputTexture:];
-[JFXGuidedUpscaler setOldScaledGuidance:];
-[JFXGuidedUpscaler setPipelineStateSimilarity:];
-[JFXGuidedUpscaler setPipelineStateSmoothing:];
-[JFXGuidedUpscaler setPreviousOutputTexture:];
-[JFXGuidedUpscaler setScaledGuidance:];
-[JFXGuidedUpscaler setShowSimilarity:];
-[JFXGuidedUpscaler setSimilarityGaussianBlur:];
-[JFXGuidedUpscaler setTemporalSmoothing:];
-[JFXGuidedUpscaler showSimilarity];
-[JFXGuidedUpscaler similarityGaussianBlur];
-[JFXGuidedUpscaler temporalSmoothing];
```
