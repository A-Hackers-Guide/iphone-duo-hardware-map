# `MTL4DebugCommandBuffer`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4ToolsCommandBuffer`
- 9 instance variables, 2 properties, 31 instance methods, 0 class methods

## Instance variables

```
Q _currentState;
@"<MTL4CommandEncoder>" _currentEncoder;
Q _aggregatedEncoderMask;
@"MTL4DebugCommandAllocator" _debugCommandAllocator;
Q _allocatorGeneration;
{unordered_multiset<AttachmentDescriptorSimple, AttachmentDescriptorSimple::hash_t, AttachmentDescriptorSimple::equal_t, std::allocator<AttachmentDescriptorSimple>>="__table_"{__hash_table<AttachmentDescriptorSimple, AttachmentDescriptorSimple::hash_t, AttachmentDescriptorSimple::equal_t, std::allocator<AttachmentDescriptorSimple>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<AttachmentDescriptorSimple, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<AttachmentDescriptorSimple, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<AttachmentDescriptorSimple, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<AttachmentDescriptorSimple, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _attachmentSet;
{array<AttachmentDescriptorSimple, 8UL>="__elems_"[8{AttachmentDescriptorSimple="texture"^v"level"Q"sliceRange"{_NSRange="location"Q"length"Q}"depthPlaneRange"{_NSRange="location"Q"length"Q}"storeAction"Q}]} _prevAttachments;
{array<AttachmentDescriptorSimple, 8UL>="__elems_"[8{AttachmentDescriptorSimple="texture"^v"level"Q"sliceRange"{_NSRange="location"Q"length"Q}"depthPlaneRange"{_NSRange="location"Q"length"Q}"storeAction"Q}]} _currentAttachments;
{MTL4DebugRenderPassInfo="resumingRenderPassDescriptor"@"MTL4RenderPassDescriptor""suspendingRenderPassDescriptor"@"MTL4RenderPassDescriptor"} _suspendResumeRenderPassInfo;
```

## Properties

```
@property (TQ,N,V_currentState) currentState;
@property (TQ,R,N,V_aggregatedEncoderMask) aggregatedEncoderMask;
```

## Instance methods

```
-[MTL4DebugCommandBuffer useInternalResidencySet:];
-[MTL4DebugCommandBuffer pushDebugGroup:];
-[MTL4DebugCommandBuffer sampledRenderCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTL4DebugCommandBuffer useResidencySet:];
-[MTL4DebugCommandBuffer useResidencySets:count:];
-[MTL4DebugCommandBuffer popDebugGroup];
-[MTL4DebugCommandBuffer useInternalResidencySets:count:];
-[MTL4DebugCommandBuffer computeCommandEncoder];
-[MTL4DebugCommandBuffer dealloc];
-[MTL4DebugCommandBuffer setCurrentState:];
-[MTL4DebugCommandBuffer currentState];
-[MTL4DebugCommandBuffer renderCommandEncoderWithDescriptor:];
-[MTL4DebugCommandBuffer writeTimestampIntoHeap:atIndex:];
-[MTL4DebugCommandBuffer beginCommandBufferWithAllocator:];
-[MTL4DebugCommandBuffer beginCommandBufferWithAllocator:options:];
-[MTL4DebugCommandBuffer endCommandBuffer];
-[MTL4DebugCommandBuffer machineLearningCommandEncoder];
-[MTL4DebugCommandBuffer renderCommandEncoderWithDescriptor:options:];
-[MTL4DebugCommandBuffer resolveCounterHeap:withRange:intoBuffer:waitFence:updateFence:];
-[MTL4DebugCommandBuffer commandAllocator];
-[MTL4DebugCommandBuffer computeCommandEncoderWithSubstreamCount:];
-[MTL4DebugCommandBuffer resolveCounterHeap:withRange:intoBuffer:atOffset:waitFence:updateFence:];
-[MTL4DebugCommandBuffer sampledComputeCommandEncoder:capacity:];
-[MTL4DebugCommandBuffer _clearSuspendResumeRenderPassInfo];
-[MTL4DebugCommandBuffer _resetRenderPassAttachmentTracking];
-[MTL4DebugCommandBuffer aggregatedEncoderMask];
-[MTL4DebugCommandBuffer attachmentSet];
-[MTL4DebugCommandBuffer initWithCommandBuffer:device:];
-[MTL4DebugCommandBuffer isAllocatorGenerationValid];
-[MTL4DebugCommandBuffer onCurrentEncoderEnded];
-[MTL4DebugCommandBuffer suspendResumeRenderPassInfo];
```
