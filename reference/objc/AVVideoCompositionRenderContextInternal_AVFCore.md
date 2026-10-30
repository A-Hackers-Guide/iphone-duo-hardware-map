# `AVVideoCompositionRenderContextInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 21 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _basisProperties;
{CGSize="width"d"height"d} _size;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _renderTransform;
f _renderScale;
{?="horizontalSpacing"q"verticalSpacing"q} _pixelAspectRatio;
{?="left"d"top"d"right"d"bottom"d} _edgeWidths;
B _highQualityRendering;
@"NSDictionary" _clientRequiredPixelBufferAttributes;
@"NSDictionary" _destinationDesiredPixelBufferAttributes;
@"NSString" _destinationDesiredPixelBufferYCbCrMatrix;
@"NSString" _destinationDesiredPixelBufferColorPrimaries;
@"NSString" _destinationDesiredPixelBufferTransferFunction;
@"NSString" _blendingTransferFunction;
i pixelFormatFamily;
^{__CFDictionary=} _pixelAspectRatioDict;
^{__CFDictionary=} _cleanApertureDict;
{?="width"i"height"i} _destinationPixelBufferDimensions;
^{OpaqueFigSimpleMutex=} _bufferPoollInitMutex;
@"NSObject<OS_dispatch_queue>" _pixelBufferPoolQ;
^{__CVPixelBufferPool=} _pixelBufferPool;
@"AVVideoComposition" _videoComposition;
```

## Instance methods

```
-[AVVideoCompositionRenderContextInternal dealloc];
-[AVVideoCompositionRenderContextInternal _willDeallocOrFinalize];
```
