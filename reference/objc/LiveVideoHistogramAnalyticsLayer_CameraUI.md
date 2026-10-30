# `LiveVideoHistogramAnalyticsLayer`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMetalLayer`
- Protocols: `CAMetalDisplayLinkDelegate`, `LiveVideoAnalyticsAdaptorRendering`
- 32 instance variables, 10 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"LiveVideoHistogramAnalyticsLayerAppearance" _appearance;
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
q _videoRotationAngle;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _videoRotationAngleLock;
@"<MTLBuffer>" _accessibilityReadbackBuffer;
@"NSData" _accessibilityBinsSnapshot;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _accessibilityBinsLock;
d _lastAccessibilityReadbackTime;
B _accessibilityBinCaptureEnabled;
```

## Properties

```
@property (T@"LiveVideoHistogramAnalyticsLayerAppearance",&,N,V_appearance) appearance;
@property (Tq,N) videoRotationAngle;
@property (TB,N) accessibilityBinCaptureEnabled;
@property (T@"NSData",R,C,N) accessibilityHistogramBins;
@property (TQ,R,N) accessibilityHistogramBinCount;
@property (TQ,R,N) accessibilityHistogramChannelCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LiveVideoHistogramAnalyticsLayer videoRotationAngle];
-[LiveVideoHistogramAnalyticsLayer setVideoRotationAngle:];
-[LiveVideoHistogramAnalyticsLayer setAppearance:];
-[LiveVideoHistogramAnalyticsLayer init];
-[LiveVideoHistogramAnalyticsLayer dealloc];
-[LiveVideoHistogramAnalyticsLayer metalDisplayLink:needsUpdate:];
-[LiveVideoHistogramAnalyticsLayer layoutSublayers];
-[LiveVideoHistogramAnalyticsLayer appearance];
-[LiveVideoHistogramAnalyticsLayer _createGraphicsPipelinesWithBlendMode:];
-[LiveVideoHistogramAnalyticsLayer _easeAndDrawWithDrawable:commandBuffer:easeAlpha:];
-[LiveVideoHistogramAnalyticsLayer _ensureSplineTextureForWidth:];
-[LiveVideoHistogramAnalyticsLayer _initializeHistogramTextures];
-[LiveVideoHistogramAnalyticsLayer _initializeRenderingPipeline];
-[LiveVideoHistogramAnalyticsLayer _pauseDisplayLink];
-[LiveVideoHistogramAnalyticsLayer _resumeDisplayLink];
-[LiveVideoHistogramAnalyticsLayer _setupDisplayLink];
-[LiveVideoHistogramAnalyticsLayer _teardownDisplayLink];
-[LiveVideoHistogramAnalyticsLayer didMoveToSuperlayer];
-[LiveVideoHistogramAnalyticsLayer renderWithSampleImage:commandBuffer:];
-[LiveVideoHistogramAnalyticsLayer setSolidFillForChannel:color:];
-[LiveVideoHistogramAnalyticsLayer _captureAccessibilityBinsWithCommandBuffer:];
-[LiveVideoHistogramAnalyticsLayer accessibilityBinCaptureEnabled];
-[LiveVideoHistogramAnalyticsLayer accessibilityHistogramBinCount];
-[LiveVideoHistogramAnalyticsLayer accessibilityHistogramBins];
-[LiveVideoHistogramAnalyticsLayer accessibilityHistogramChannelCount];
-[LiveVideoHistogramAnalyticsLayer setAccessibilityBinCaptureEnabled:];
```
