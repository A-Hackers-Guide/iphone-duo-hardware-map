# `DupDownscaleHalfConvert`

- Image: [`/System/Library/VideoProcessors/DisparityV5.bundle/DisparityV5`](../userland/System__Library__VideoProcessors__DisparityV5.bundle__DisparityV5.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"FigMetalContext" _MetalContext;
@"<MTLComputePipelineState>" _KernelYUVA;
@"<MTLComputePipelineState>" _KernelY;
@"<MTLComputePipelineState>" _KernelDownscaleConvertAndCenterCrop;
@"<MTLComputePipelineState>" _KernelDownscaleAndCrop;
B _ContextAvailable;
B _ResourcesAvailable;
```

## Instance methods

```
-[DupDownscaleHalfConvert dealloc];
-[DupDownscaleHalfConvert initWithMetalContext:];
-[DupDownscaleHalfConvert DownscaleAndCrop:outY:inYuv420:];
-[DupDownscaleHalfConvert AllocateResources];
-[DupDownscaleHalfConvert DownscaleConvertAndCenterCrop:outCroppedLuma:inYuv420:];
-[DupDownscaleHalfConvert GenerateImageYUVA:outY:inYuv420:waitForCompletion:];
-[DupDownscaleHalfConvert ReleaseResources];
-[DupDownscaleHalfConvert GenerateImageY:inYuv420:waitForCompletion:];
-[DupDownscaleHalfConvert GenerateImageYUVA:outYuvaWidth:outYuvaHeight:outY:inYuv420:gainToApplyToOutputs:waitForCompletion:];
```
