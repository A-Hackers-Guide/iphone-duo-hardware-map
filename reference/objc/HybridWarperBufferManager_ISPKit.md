# `HybridWarperBufferManager`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 7 properties, 12 instance methods, 0 class methods

## Instance variables

```
^{__CVMetalTextureCache=} _textureCache;
{?="width"Q"height"Q"depth"Q} _band0Size;
{?="width"Q"height"Q"depth"Q} _band1Size;
{?="width"Q"height"Q"depth"Q} _opticalFlowSize;
{?="width"Q"height"Q"depth"Q} _blendingMapSize;
@"NSObject<OS_os_log>" _logger;
@"PixelMetalBufferPair" _sparseBlendingMapPair;
@"PixelMetalBufferPair" _blendingWeightPair;
@"PixelMetalBufferPair" _historyYPair;
@"PixelMetalBufferPair" _historyUVPair;
@"PixelMetalBufferPair" _warpedYPair;
@"PixelMetalBufferPair" _warpedUVPair;
@"<MTLBuffer>" _globalSumBackgroundMeanBuffer;
```

## Properties

```
@property (T@"PixelMetalBufferPair",R,N,V_sparseBlendingMapPair) sparseBlendingMapPair;
@property (T@"PixelMetalBufferPair",R,N,V_blendingWeightPair) blendingWeightPair;
@property (T@"PixelMetalBufferPair",R,N,V_historyYPair) historyYPair;
@property (T@"PixelMetalBufferPair",R,N,V_historyUVPair) historyUVPair;
@property (T@"PixelMetalBufferPair",R,N,V_warpedYPair) warpedYPair;
@property (T@"PixelMetalBufferPair",R,N,V_warpedUVPair) warpedUVPair;
@property (T@"<MTLBuffer>",R,N,V_globalSumBackgroundMeanBuffer) globalSumBackgroundMeanBuffer;
```

## Instance methods

```
-[HybridWarperBufferManager dealloc];
-[HybridWarperBufferManager releaseIntermediateBuffers];
-[HybridWarperBufferManager blendingWeightPair];
-[HybridWarperBufferManager createIntermediateBuffers];
-[HybridWarperBufferManager dumpAllBuffersToDirectory:frameIndex:];
-[HybridWarperBufferManager globalSumBackgroundMeanBuffer];
-[HybridWarperBufferManager historyUVPair];
-[HybridWarperBufferManager historyYPair];
-[HybridWarperBufferManager initWithTextureCache:band0Size:band1Size:opticalFlowSize:blendingMapSize:];
-[HybridWarperBufferManager sparseBlendingMapPair];
-[HybridWarperBufferManager warpedUVPair];
-[HybridWarperBufferManager warpedYPair];
```
