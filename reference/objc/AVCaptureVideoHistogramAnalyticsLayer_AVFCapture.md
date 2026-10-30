# `AVCaptureVideoHistogramAnalyticsLayer`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMetalLayer`
- Protocols: `CAMetalDisplayLinkDelegate`, `AVCaptureVideoAnalyticsAdaptorRendering`
- 25 instance variables, 5 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"AVCaptureVideoHistogramAnalyticsLayerAppearance" _appearance;
@"<MTLLibrary>" _shaderLibrary;
@"<MTLComputePipelineState>" _histogramComputePSO;
@"<MTLComputePipelineState>" _histogramNormalizePSO;
@"<MTLComputePipelineState>" _histogramEaseSmoothPSO;
@"<MTLComputePipelineState>" _histogramSplinePSO;
@"<MTLFunction>" _vertexFunctionFill;
@"<MTLFunction>" _vertexFunctionLine;
@"<MTLFunction>" _fragmentFunction;
@"<MTLRenderPipelineState>" _renderPipelineStateFill;
@"<MTLRenderPipelineState>" _renderPipelineStateLine;
@"<MTLTexture>" _targetHistogramTexture;
@"<MTLTexture>" _displayedHistogramTexture;
@"<MTLTexture>" _smoothedHistogramTexture;
@"<MTLTexture>" _splineHistogramTexture;
@"<MTLBuffer>" _histogramAccumulationBuffer;
@"<MTLBuffer>" _histogramMaxBuffer;
@"CAMetalDisplayLink" _displayLink;
@"NSObject<OS_dispatch_semaphore>" _inFlightSemaphore;
d _lastIngestTime;
d _lastTickTime;
B _needsDisplayedReset;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _timingLock;
{CGSize="width"d"height"d} _lastDrawableSize;
d _displayScale;
```

## Properties

```
@property (T@"AVCaptureVideoHistogramAnalyticsLayerAppearance",&,N,V_appearance) appearance;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVCaptureVideoHistogramAnalyticsLayer setAppearance:];
-[AVCaptureVideoHistogramAnalyticsLayer init];
-[AVCaptureVideoHistogramAnalyticsLayer dealloc];
-[AVCaptureVideoHistogramAnalyticsLayer metalDisplayLink:needsUpdate:];
-[AVCaptureVideoHistogramAnalyticsLayer layoutSublayers];
-[AVCaptureVideoHistogramAnalyticsLayer appearance];
-[AVCaptureVideoHistogramAnalyticsLayer _createGraphicsPipelinesWithBlendMode:];
-[AVCaptureVideoHistogramAnalyticsLayer _easeAndDrawWithDrawable:commandBuffer:easeAlpha:];
-[AVCaptureVideoHistogramAnalyticsLayer _ensureSplineTextureForWidth:];
-[AVCaptureVideoHistogramAnalyticsLayer _initializeHistogramTextures];
-[AVCaptureVideoHistogramAnalyticsLayer _initializeRenderingPipeline];
-[AVCaptureVideoHistogramAnalyticsLayer _pauseDisplayLink];
-[AVCaptureVideoHistogramAnalyticsLayer _resumeDisplayLink];
-[AVCaptureVideoHistogramAnalyticsLayer _setupDisplayLink];
-[AVCaptureVideoHistogramAnalyticsLayer _teardownDisplayLink];
-[AVCaptureVideoHistogramAnalyticsLayer didMoveToSuperlayer];
-[AVCaptureVideoHistogramAnalyticsLayer renderWithSampleImage:commandBuffer:];
-[AVCaptureVideoHistogramAnalyticsLayer setSolidFillForChannel:color:];
```
