# `MTLDebugParallelRenderCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsParallelRenderCommandEncoder`
- 3 instance variables, 1 properties, 18 instance methods, 0 class methods

## Instance variables

```
I _unknownStoreActions;
{atomic<unsigned long long>="__a_"{__cxx_atomic_impl<unsigned long long, std::__cxx_atomic_base_impl<unsigned long long>>="__a_value"AQ}} _attachmentWriteMask;
@"MTLRenderPassDescriptor" _descriptor;
```

## Properties

```
@property (T@"MTLRenderPassDescriptor",R,C,N,V_descriptor) descriptor;
```

## Instance methods

```
-[MTLDebugParallelRenderCommandEncoder setColorStoreAction:atIndex:];
-[MTLDebugParallelRenderCommandEncoder descriptor];
-[MTLDebugParallelRenderCommandEncoder formattedDescription:];
-[MTLDebugParallelRenderCommandEncoder endEncoding];
-[MTLDebugParallelRenderCommandEncoder dealloc];
-[MTLDebugParallelRenderCommandEncoder setStencilStoreActionOptions:];
-[MTLDebugParallelRenderCommandEncoder setStencilStoreAction:];
-[MTLDebugParallelRenderCommandEncoder description];
-[MTLDebugParallelRenderCommandEncoder setDepthStoreAction:];
-[MTLDebugParallelRenderCommandEncoder setDepthStoreActionOptions:];
-[MTLDebugParallelRenderCommandEncoder setColorStoreActionOptions:atIndex:];
-[MTLDebugParallelRenderCommandEncoder endEncodingAndRetrieveProgramAddressTable];
-[MTLDebugParallelRenderCommandEncoder filterCounterRangeWithFirstBatch:lastBatch:filterIndex:];
-[MTLDebugParallelRenderCommandEncoder renderCommandEncoder];
-[MTLDebugParallelRenderCommandEncoder sampledRenderCommandEncoderWithProgramInfoBuffer:capacity:];
-[MTLDebugParallelRenderCommandEncoder endEncoding_private];
-[MTLDebugParallelRenderCommandEncoder initWithBaseRenderPass:commandBuffer:descriptor:];
-[MTLDebugParallelRenderCommandEncoder mergeAttachmentWriteMask:];
```
