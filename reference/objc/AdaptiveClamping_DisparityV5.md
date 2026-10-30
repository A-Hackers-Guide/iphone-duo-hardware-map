# `AdaptiveClamping`

- Image: [`/System/Library/VideoProcessors/DisparityV5.bundle/DisparityV5`](../userland/System__Library__VideoProcessors__DisparityV5.bundle__DisparityV5.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"FigMetalContext" _metalContext;
[3@"<MTLComputePipelineState>"] _pipelineStates;
```

## Instance methods

```
-[AdaptiveClamping initWithMetalContext:];
-[AdaptiveClamping _initShaders];
-[AdaptiveClamping clampFromPixelBuffer:Mask:MaxDisparity:Percentiles:CommandBuffer:];
```
