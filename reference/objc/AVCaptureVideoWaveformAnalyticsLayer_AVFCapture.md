# `AVCaptureVideoWaveformAnalyticsLayer`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMetalLayer`
- Protocols: `AVCaptureVideoAnalyticsAdaptorRendering`
- 10 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"AVCaptureVideoWaveformAnalyticsLayerAppearance" _appearance;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _appearanceLock;
{CGSize="width"d"height"d} _lastDrawableSize;
d _displayScale;
d _videoRotationAngle;
B _mirrored;
@"<MTLTexture>" _precursorTexture;
@"<MTLBuffer>" _filamentVertexBuffer;
@"<MTLBuffer>" _filamentVertexCountBuffer;
@"<MTLBuffer>" _indirectCommandBuffer;
```

## Properties

```
@property (T@"AVCaptureVideoWaveformAnalyticsLayerAppearance",&,N) appearance;
@property (Td,N) videoRotationAngle;
@property (TB,N,GisMirrored) mirrored;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVCaptureVideoWaveformAnalyticsLayer videoRotationAngle];
-[AVCaptureVideoWaveformAnalyticsLayer setVideoRotationAngle:];
-[AVCaptureVideoWaveformAnalyticsLayer setAppearance:];
-[AVCaptureVideoWaveformAnalyticsLayer init];
-[AVCaptureVideoWaveformAnalyticsLayer dealloc];
-[AVCaptureVideoWaveformAnalyticsLayer isMirrored];
-[AVCaptureVideoWaveformAnalyticsLayer setMirrored:];
-[AVCaptureVideoWaveformAnalyticsLayer layoutSublayers];
-[AVCaptureVideoWaveformAnalyticsLayer appearance];
-[AVCaptureVideoWaveformAnalyticsLayer renderWithSampleImage:commandBuffer:];
```
