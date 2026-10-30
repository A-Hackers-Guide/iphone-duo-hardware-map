# `AVVideoCompositionRenderContext`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 7 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"AVVideoCompositionRenderContextInternal" _internal;
```

## Properties

```
@property (T{CGSize=dd},R,N) size;
@property (T{CGAffineTransform=dddddd},R,N) renderTransform;
@property (Tf,R,N) renderScale;
@property (T{?=qq},R,N) pixelAspectRatio;
@property (T{?=dddd},R,N) edgeWidths;
@property (TB,R,N) highQualityRendering;
@property (T@"AVVideoComposition",R,N) videoComposition;
```

## Class methods

```
+[AVVideoCompositionRenderContext renderContextPropertiesFromFigCompositor:];
```

## Instance methods

```
-[AVVideoCompositionRenderContext pixelBufferPool];
-[AVVideoCompositionRenderContext dealloc];
-[AVVideoCompositionRenderContext newPixelBuffer];
-[AVVideoCompositionRenderContext size];
-[AVVideoCompositionRenderContext pixelAspectRatio];
-[AVVideoCompositionRenderContext _willDeallocOrFinalize];
-[AVVideoCompositionRenderContext videoComposition];
-[AVVideoCompositionRenderContext renderScale];
-[AVVideoCompositionRenderContext renderTransform];
-[AVVideoCompositionRenderContext edgeWidths];
-[AVVideoCompositionRenderContext hasEqualPropertiesToFigVideoCompositor:];
-[AVVideoCompositionRenderContext highQualityRendering];
-[AVVideoCompositionRenderContext initWithFigVideoCompositor:clientRequiredPixelBufferAttributes:videoComposition:pixelBufferPool:];
-[AVVideoCompositionRenderContext isBufferYCbCr:];
```
