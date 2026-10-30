# `AGXG19FamilyThreadedRenderPass`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalParallelRenderCommandEncoder`
- Protocols: `MTLParallelRenderCommandEncoderSPI`
- 4 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
^v _impl;
@"NSObject<OS_dispatch_queue>" dispatchQueue;
{vector<AGXG19FamilyRenderContext *, std::allocator<AGXG19FamilyRenderContext *>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} _subOBJCRenderCommandEncoders;
{vector<AGX::HAL400::RenderContextA *, std::allocator<AGX::HAL400::RenderContextA *>>="__begin_"^^{RenderContextA}"__end_"^^{RenderContextA}""{?="__cap_"^^{RenderContextA}}} _subRenderCommandEncoders;
```

## Properties

```
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AGXG19FamilyThreadedRenderPass setColorStoreAction:atIndex:];
-[AGXG19FamilyThreadedRenderPass endEncoding];
-[AGXG19FamilyThreadedRenderPass dealloc];
-[AGXG19FamilyThreadedRenderPass setStencilStoreAction:];
-[AGXG19FamilyThreadedRenderPass setDepthStoreAction:];
-[AGXG19FamilyThreadedRenderPass isMemorylessRender];
-[AGXG19FamilyThreadedRenderPass barrierAfterQueueStages:beforeStages:];
-[AGXG19FamilyThreadedRenderPass filterCounterRangeWithFirstBatch:lastBatch:filterIndex:];
-[AGXG19FamilyThreadedRenderPass initWithCommandBuffer:renderPassDescriptor:];
-[AGXG19FamilyThreadedRenderPass renderCommandEncoder];
-[AGXG19FamilyThreadedRenderPass sampledRenderCommandEncoderWithProgramInfoBuffer:capacity:];
-[AGXG19FamilyThreadedRenderPass setMTLCounterSampleLocationWithBuffer:startIndex:endIndex:];
```
