# `AVVideoCompositing` (protocol)

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 11 instance methods, 0 class methods

## Properties

```
@property (T@"NSDictionary",R,N) sourcePixelBufferAttributes;
@property (T@"NSDictionary",R,N) requiredPixelBufferAttributesForRenderContext;
@property (TB,?,R,N) supportsWideColorSourceFrames;
@property (TB,?,R,N) supportsHDRSourceFrames;
@property (TB,?,R,N) supportsSourceTaggedBuffers;
@property (TB,?,R,N) canConformColorOfSourceFrames;
```

## Instance methods

```
-[AVVideoCompositing sourcePixelBufferAttributes];
-[AVVideoCompositing renderContextChanged:];
-[AVVideoCompositing requiredPixelBufferAttributesForRenderContext];
-[AVVideoCompositing startVideoCompositionRequest:];
-[AVVideoCompositing anticipateRenderingUsingHint:];
-[AVVideoCompositing canConformColorOfSourceFrames];
-[AVVideoCompositing cancelAllPendingVideoCompositionRequests];
-[AVVideoCompositing prerollForRenderingUsingHint:];
-[AVVideoCompositing supportsHDRSourceFrames];
-[AVVideoCompositing supportsSourceTaggedBuffers];
-[AVVideoCompositing supportsWideColorSourceFrames];
```
