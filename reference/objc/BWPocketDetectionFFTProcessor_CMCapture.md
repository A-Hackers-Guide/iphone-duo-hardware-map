# `BWPocketDetectionFFTProcessor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 0 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"FigMetalContext" _metalContext;
@"<MTLCommandQueue>" _metalCommandQueue;
[2@"<MTLComputePipelineState>"] _computePipelines;
@"<CMIFFTTransform>" _fftTransform;
@"<MTLBuffer>" _fftMetalBuffer;
@"<MTLTexture>" _fftMetalTexture;
@"<MTLBuffer>" _fftResultAccumulationMetalBuffer;
@"<MTLTexture>" _fftResultAccumulationMetalTexture;
^{OpaqueVTPixelRotationSession=} _cropSession;
@"BWPixelBufferPool" _fftBufferPool;
B _useMetalForScalingAndResultAccumulation;
B _resourcesCleaned;
```

## Class methods

```
+[BWPocketDetectionFFTProcessor initialize];
+[BWPocketDetectionFFTProcessor prewarmShaders];
```

## Instance methods

```
-[BWPocketDetectionFFTProcessor dealloc];
-[BWPocketDetectionFFTProcessor cleanupResources];
-[BWPocketDetectionFFTProcessor allocateResources];
-[BWPocketDetectionFFTProcessor _setupPipelines];
-[BWPocketDetectionFFTProcessor _loadKernel:name:];
-[BWPocketDetectionFFTProcessor _processFFTOnInputPixelBuffer:usingSourceRect:cumulativeScoreOut:];
-[BWPocketDetectionFFTProcessor _processMetalOptimizedFFTOnInputPixelBuffer:usingSourceRect:cumulativeScoreOut:];
-[BWPocketDetectionFFTProcessor initWithMetalCommandQueue:];
-[BWPocketDetectionFFTProcessor processFFTOnInputPixelBuffer:usingSourceRect:cumulativeScoreOut:];
```
