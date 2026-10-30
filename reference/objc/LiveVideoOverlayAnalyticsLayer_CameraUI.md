# `LiveVideoOverlayAnalyticsLayer`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMetalLayer`
- Protocols: `CAMetalDisplayLinkDelegate`, `LiveVideoAnalyticsAdaptorRendering`
- 15 instance variables, 7 properties, 32 instance methods, 0 class methods

## Instance variables

```
@"CAMetalDisplayLink" _displayLink;
{?="backPressureSemaphore"@"NSObject<OS_dispatch_semaphore>""startTime"d"renderTimeout"{?="value"q"timescale"i"flags"I"epoch"q}"frameID"Q"lastDrawableSize"{CGSize="width"d"height"d}"latestSourceTexture"@"<MTLTexture>""latestUVTexture"@"<MTLTexture>""latestPixelFormat"I"latestColorMapping"{?="matrix"{?="columns"[3]}"offset""rangeMin"f"rangeMax"f}"hasNewFrame"B} _drawableState;
@"<MTLLibrary>" _inlineLibrary;
@"<MTLFunction>" _vertexShaderFunction;
@"<MTLFunction>" _fragmentShaderFunction;
@"<MTLRenderPipelineState>" _renderPSO;
@"<MTLComputePipelineState>" _rowUploadPSO;
@"<MTLCommandQueue>" _computeQueue;
@"<MTLTexture>" _registrationMapLookupTexture;
{?="current"Q"previous"Q"transitionProgress"f"transitionStartTime"d} _compositeState;
f _underlayOpacity;
f _underlaySaturation;
{?="value"q"timescale"i"flags"I"epoch"q} _overlayTransitionDuration;
q _videoRotationAngle;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _videoRotationAngleLock;
```

## Properties

```
@property (TQ,N) mode;
@property (T{?=qiIq},N) overlayTransitionDuration;
@property (Tq,N) videoRotationAngle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LiveVideoOverlayAnalyticsLayer videoRotationAngle];
-[LiveVideoOverlayAnalyticsLayer setVideoRotationAngle:];
-[LiveVideoOverlayAnalyticsLayer init];
-[LiveVideoOverlayAnalyticsLayer dealloc];
-[LiveVideoOverlayAnalyticsLayer metalDisplayLink:needsUpdate:];
-[LiveVideoOverlayAnalyticsLayer setMode:];
-[LiveVideoOverlayAnalyticsLayer mode];
-[LiveVideoOverlayAnalyticsLayer layoutSublayers];
-[LiveVideoOverlayAnalyticsLayer _handleMemoryPressure];
-[LiveVideoOverlayAnalyticsLayer _pauseDisplayLink];
-[LiveVideoOverlayAnalyticsLayer _resumeDisplayLink];
-[LiveVideoOverlayAnalyticsLayer _setupDisplayLink];
-[LiveVideoOverlayAnalyticsLayer _teardownDisplayLink];
-[LiveVideoOverlayAnalyticsLayer didMoveToSuperlayer];
-[LiveVideoOverlayAnalyticsLayer renderWithSampleImage:commandBuffer:];
-[LiveVideoOverlayAnalyticsLayer underlayOpacity];
-[LiveVideoOverlayAnalyticsLayer _buildInlineLibraryIfNeeded];
-[LiveVideoOverlayAnalyticsLayer _buildRowUploadComputeIfNeeded];
-[LiveVideoOverlayAnalyticsLayer _encodeAnalyticsPassIntoDrawableWithCommandBuffer:drawable:sourceTexture:uvTexture:uniforms:displayTime:];
-[LiveVideoOverlayAnalyticsLayer _initializePipelineIfNeeded];
-[LiveVideoOverlayAnalyticsLayer _newRegistrationMapLookupTexture];
-[LiveVideoOverlayAnalyticsLayer _newSRGB8TextureFromCGImage:];
-[LiveVideoOverlayAnalyticsLayer _replaceRowInRegistrationMap:lookup:];
-[LiveVideoOverlayAnalyticsLayer _setDisplayLinkVisible:];
-[LiveVideoOverlayAnalyticsLayer overlayTransitionDuration];
-[LiveVideoOverlayAnalyticsLayer removeRegistrationMapForMode:];
-[LiveVideoOverlayAnalyticsLayer renderWithSourceTexture:uvTexture:pixelFormat:colorMapping:];
-[LiveVideoOverlayAnalyticsLayer setOverlayTransitionDuration:];
-[LiveVideoOverlayAnalyticsLayer setRegistrationMap:forMode:];
-[LiveVideoOverlayAnalyticsLayer setUnderlayOpacity:];
-[LiveVideoOverlayAnalyticsLayer setUnderlaySaturation:];
-[LiveVideoOverlayAnalyticsLayer underlaySaturation];
```
