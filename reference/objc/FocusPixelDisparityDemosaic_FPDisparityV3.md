# `FocusPixelDisparityDemosaic`

- Image: [`/System/Library/VideoProcessors/FPDisparityV3.bundle/FPDisparityV3`](../userland/System__Library__VideoProcessors__FPDisparityV3.bundle__FPDisparityV3.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"FigMetalContext" _mtlContext;
@"<MTLCommandQueue>" _commandQueue;
[1@"<MTLComputePipelineState>"] _pipelineStates;
```

## Instance methods

```
-[FocusPixelDisparityDemosaic releaseResources];
-[FocusPixelDisparityDemosaic dealloc];
-[FocusPixelDisparityDemosaic allocateResources];
-[FocusPixelDisparityDemosaic initWithMetalContext:];
-[FocusPixelDisparityDemosaic demosaicGreenOnly:fromL00h:validRect:waitForCompletion:];
```
