# `FlowMaskSumReduceEncoder`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 2 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
@"NSObject<OS_os_log>" _logger;
@"<MTLBuffer>" _bgPixelCountBuffer;
@"<MTLComputePipelineState>" _reduceMaskedFlowPipeline;
@"<MTLComputePipelineState>" _reducePartialSumsPipeline;
```

## Properties

```
@property (T@"<MTLComputePipelineState>",R,N,V_reduceMaskedFlowPipeline) reduceMaskedFlowPipeline;
@property (T@"<MTLComputePipelineState>",R,N,V_reducePartialSumsPipeline) reducePartialSumsPipeline;
```

## Instance methods

```
-[FlowMaskSumReduceEncoder initWithDevice:];
-[FlowMaskSumReduceEncoder encodeToCommandBuffer:opticalFlowTexture:anstRawMaskTexture:globalSumBackgroundMean:params:];
-[FlowMaskSumReduceEncoder reduceMaskedFlowPipeline];
-[FlowMaskSumReduceEncoder reducePartialSumsPipeline];
```
