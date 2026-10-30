# `AGXG19FamilyCommandBuffer_mtlnext`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetal4CommandBuffer`
- Protocols: `MTL4CommandBufferGGDSPI`
- 6 instance variables, 11 properties, 25 instance methods, 0 class methods

## Instance variables

```
^v _impl;
^v _device_impl;
@"AGXG19FamilyComputeContext_mtlnext" _internalSparseMappingEncoder;
{unique_ptr<AGX::HAL400::RenderContextB, std::function<void (AGX::HAL400::RenderContextB *)>>=""{?="__ptr_"^{RenderContextB}"__deleter_"{function<void (AGX::HAL400::RenderContextB *)>="__f_"{__value_func<void (AGX::HAL400::RenderContextB *)>="__buf_"(type="__data"[24C])"__f_"^v}}}} _mergeable_render;
{unique_ptr<AGX::HAL400::Framebuffer, std::function<void (AGX::HAL400::Framebuffer *)>>=""{?="__ptr_"^{Framebuffer}"__deleter_"{function<void (AGX::HAL400::Framebuffer *)>="__f_"{__value_func<void (AGX::HAL400::Framebuffer *)>="__buf_"(type="__data"[24C])"__f_"^v}}}} _mergeable_framebuffer;
@"MTL4CommandBufferOptions" _options;
```

## Properties

```
@property (T@"<MTLBuffer>",&,N) privateData;
@property (TQ,N) privateDataOffset;
@property (T@"<MTL4CommandAllocator>",R,N) commandAllocator;
@property (TQ,R) globalTraceObjectID;
@property (TQ,R,N) currentGeneration;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AGXG19FamilyCommandBuffer_mtlnext initWithDevice:];
-[AGXG19FamilyCommandBuffer_mtlnext sampledRenderCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[AGXG19FamilyCommandBuffer_mtlnext computeCommandEncoder];
-[AGXG19FamilyCommandBuffer_mtlnext dealloc];
-[AGXG19FamilyCommandBuffer_mtlnext commitEncoder];
-[AGXG19FamilyCommandBuffer_mtlnext renderCommandEncoderWithDescriptor:];
-[AGXG19FamilyCommandBuffer_mtlnext writeTimestampIntoHeap:atIndex:];
-[AGXG19FamilyCommandBuffer_mtlnext beginCommandBufferWithAllocator:];
-[AGXG19FamilyCommandBuffer_mtlnext beginCommandBufferWithAllocator:options:];
-[AGXG19FamilyCommandBuffer_mtlnext endCommandBuffer];
-[AGXG19FamilyCommandBuffer_mtlnext machineLearningCommandEncoder];
-[AGXG19FamilyCommandBuffer_mtlnext renderCommandEncoderWithDescriptor:options:];
-[AGXG19FamilyCommandBuffer_mtlnext resolveCounterHeap:withRange:intoBuffer:waitFence:updateFence:];
-[AGXG19FamilyCommandBuffer_mtlnext reserveKernelCommandBufferSpace:];
-[AGXG19FamilyCommandBuffer_mtlnext resolveCounterHeap:withRange:intoBuffer:atOffset:waitFence:updateFence:];
-[AGXG19FamilyCommandBuffer_mtlnext sampledComputeCommandEncoder:capacity:];
-[AGXG19FamilyCommandBuffer_mtlnext fillCommandBufferArgs:];
-[AGXG19FamilyCommandBuffer_mtlnext allocateInternalSparseMappingEncoder];
-[AGXG19FamilyCommandBuffer_mtlnext closeKernelCommands:kernelCommand:];
-[AGXG19FamilyCommandBuffer_mtlnext encodeSSTTFlushInvalidateCompute];
-[AGXG19FamilyCommandBuffer_mtlnext encodeSyncComputeWithBackFacingBarrierSrcMask:BackFacingBarrierDstMask:FrontFacingBarrierSrcMask:FrontFacingBarrierDstMask:];
-[AGXG19FamilyCommandBuffer_mtlnext endCommandBufferInternal];
-[AGXG19FamilyCommandBuffer_mtlnext releaseMergeableRender];
-[AGXG19FamilyCommandBuffer_mtlnext sampledComputeCommandEncoder];
-[AGXG19FamilyCommandBuffer_mtlnext sampledRenderCommandEncoderWithDescriptor:];
```
