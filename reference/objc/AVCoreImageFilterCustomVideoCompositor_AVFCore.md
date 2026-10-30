# `AVCoreImageFilterCustomVideoCompositor`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVVideoCompositing`
- 4 instance variables, 12 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_group>" _filteringRequestsInFlight;
B _shouldCancelAllRequests;
@"NSObject<OS_dispatch_queue>" _defaultCIContextThreadSafety;
@"CIContext" _defaultCIContext;
```

## Properties

```
@property (TB,V_shouldCancelAllRequests) shouldCancelAllRequests;
@property (T@"NSObject<OS_dispatch_group>",R,V_filteringRequestsInFlight) filteringRequestsInFlight;
@property (T@"NSDictionary",R,N) sourcePixelBufferAttributes;
@property (T@"NSDictionary",R,N) requiredPixelBufferAttributesForRenderContext;
@property (TB,?,R,N) supportsWideColorSourceFrames;
@property (TB,?,R,N) supportsHDRSourceFrames;
@property (TB,?,R,N) supportsSourceTaggedBuffers;
@property (TB,?,R,N) canConformColorOfSourceFrames;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVCoreImageFilterCustomVideoCompositor initialize];
```

## Instance methods

```
-[AVCoreImageFilterCustomVideoCompositor init];
-[AVCoreImageFilterCustomVideoCompositor dealloc];
-[AVCoreImageFilterCustomVideoCompositor _willDeallocOrFinalize];
-[AVCoreImageFilterCustomVideoCompositor sourcePixelBufferAttributes];
-[AVCoreImageFilterCustomVideoCompositor cancelAllPendingVideoCompositionRequests];
-[AVCoreImageFilterCustomVideoCompositor defaultCIContext];
-[AVCoreImageFilterCustomVideoCompositor filteringRequestsInFlight];
-[AVCoreImageFilterCustomVideoCompositor renderContextChanged:];
-[AVCoreImageFilterCustomVideoCompositor requiredPixelBufferAttributesForRenderContext];
-[AVCoreImageFilterCustomVideoCompositor setShouldCancelAllRequests:];
-[AVCoreImageFilterCustomVideoCompositor shouldCancelAllRequests];
-[AVCoreImageFilterCustomVideoCompositor startVideoCompositionRequest:];
-[AVCoreImageFilterCustomVideoCompositor supportsHDRSourceFrames];
-[AVCoreImageFilterCustomVideoCompositor supportsWideColorSourceFrames];
```
