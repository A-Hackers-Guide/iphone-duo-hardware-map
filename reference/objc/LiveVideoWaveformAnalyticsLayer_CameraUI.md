# `LiveVideoWaveformAnalyticsLayer`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMetalLayer`
- Protocols: `LiveVideoAnalyticsAdaptorRendering`
- 10 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"LiveVideoWaveformAnalyticsLayerAppearance" _appearance;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _appearanceLock;
{CGSize="width"d"height"d} _lastDrawableSize;
d _displayScale;
q _videoRotationAngle;
B _mirrored;
@"<MTLTexture>" _precursorTexture;
@"<MTLBuffer>" _filamentVertexBuffer;
@"<MTLBuffer>" _filamentVertexCountBuffer;
@"<MTLBuffer>" _indirectCommandBuffer;
```

## Properties

```
@property (T@"LiveVideoWaveformAnalyticsLayerAppearance",&,N) appearance;
@property (Tq,N) videoRotationAngle;
@property (TB,N,GisMirrored) mirrored;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LiveVideoWaveformAnalyticsLayer videoRotationAngle];
-[LiveVideoWaveformAnalyticsLayer setVideoRotationAngle:];
-[LiveVideoWaveformAnalyticsLayer setAppearance:];
-[LiveVideoWaveformAnalyticsLayer init];
-[LiveVideoWaveformAnalyticsLayer dealloc];
-[LiveVideoWaveformAnalyticsLayer isMirrored];
-[LiveVideoWaveformAnalyticsLayer setMirrored:];
-[LiveVideoWaveformAnalyticsLayer layoutSublayers];
-[LiveVideoWaveformAnalyticsLayer appearance];
-[LiveVideoWaveformAnalyticsLayer renderWithSampleImage:commandBuffer:];
```
