# `MTL4ToolsCommandBuffer`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTL4CommandBufferGGDSPI`
- 4 instance variables, 11 properties, 38 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _usedResidencySets;
@"NSMutableSet" _usedInternalResidencySets;
@"<MTL4CommandAllocator>" _commandAllocator;
@"<MTLBuffer>" _privateData;
```

## Properties

```
@property (T@"NSString",C) label;
@property (T@"<MTL4CommandAllocator>",R) commandAllocator;
@property (TQ,R,N) currentGeneration;
@property (T@"<MTLBuffer>",&,N) privateData;
@property (TQ,N) privateDataOffset;
@property (TQ,R) globalTraceObjectID;
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTL4ToolsCommandBuffer setPrivateDataOffset:];
-[MTL4ToolsCommandBuffer useInternalResidencySet:];
-[MTL4ToolsCommandBuffer pushDebugGroup:];
-[MTL4ToolsCommandBuffer sampledRenderCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTL4ToolsCommandBuffer setPrivateData:];
-[MTL4ToolsCommandBuffer useResidencySet:];
-[MTL4ToolsCommandBuffer privateData];
-[MTL4ToolsCommandBuffer privateDataOffset];
-[MTL4ToolsCommandBuffer useResidencySets:count:];
-[MTL4ToolsCommandBuffer popDebugGroup];
-[MTL4ToolsCommandBuffer encodeSignalEvent:value:];
-[MTL4ToolsCommandBuffer useInternalResidencySets:count:];
-[MTL4ToolsCommandBuffer computeCommandEncoder];
-[MTL4ToolsCommandBuffer label];
-[MTL4ToolsCommandBuffer setLabel:];
-[MTL4ToolsCommandBuffer globalTraceObjectID];
-[MTL4ToolsCommandBuffer dealloc];
-[MTL4ToolsCommandBuffer encodeWaitForEvent:value:];
-[MTL4ToolsCommandBuffer encodeWaitForEvent:value:timeout:];
-[MTL4ToolsCommandBuffer currentGeneration];
-[MTL4ToolsCommandBuffer renderCommandEncoderWithDescriptor:];
-[MTL4ToolsCommandBuffer writeTimestampIntoHeap:atIndex:];
-[MTL4ToolsCommandBuffer beginCommandBufferWithAllocator:];
-[MTL4ToolsCommandBuffer beginCommandBufferWithAllocator:options:];
-[MTL4ToolsCommandBuffer endCommandBuffer];
-[MTL4ToolsCommandBuffer machineLearningCommandEncoder];
-[MTL4ToolsCommandBuffer renderCommandEncoderWithDescriptor:options:];
-[MTL4ToolsCommandBuffer resolveCounterHeap:withRange:intoBuffer:waitFence:updateFence:];
-[MTL4ToolsCommandBuffer addFeedbackHandler:];
-[MTL4ToolsCommandBuffer commandAllocator];
-[MTL4ToolsCommandBuffer computeCommandEncoderWithSubstreamCount:];
-[MTL4ToolsCommandBuffer initWithBaseObject:parent:];
-[MTL4ToolsCommandBuffer resetCommandBuffer];
-[MTL4ToolsCommandBuffer resolveCounterHeap:withRange:intoBuffer:atOffset:waitFence:updateFence:];
-[MTL4ToolsCommandBuffer sampledComputeCommandEncoder:capacity:];
-[MTL4ToolsCommandBuffer unwrappedMTL4RenderPassDescriptor:];
-[MTL4ToolsCommandBuffer usedInternalResidencySets];
-[MTL4ToolsCommandBuffer usedResidencySets];
```
