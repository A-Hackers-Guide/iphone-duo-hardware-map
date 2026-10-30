# `MTL4ToolsCommandQueue`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTL4CommandQueueGGDSPI`
- 3 instance variables, 8 properties, 32 instance methods, 0 class methods

## Instance variables

```
@"NSCountedSet" _addedResidencySets;
@"NSCountedSet" _addedInternalResidencySets;
@"<MTL4CommandBuffer>" _lastCommittedCommandBuffer;
```

## Properties

```
@property (T@"NSString",R) label;
@property (T@"<MTL4CommandBuffer>",R,N) lastCommittedCommandBuffer;
@property (TQ,R,N) lastCommittedCommandBufferGeneration;
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTL4ToolsCommandQueue removeInternalResidencySets:count:];
-[MTL4ToolsCommandQueue removeResidencySet:];
-[MTL4ToolsCommandQueue setGPUPriority:];
-[MTL4ToolsCommandQueue removeInternalResidencySet:];
-[MTL4ToolsCommandQueue addInternalResidencySet:];
-[MTL4ToolsCommandQueue addInternalResidencySets:count:];
-[MTL4ToolsCommandQueue addResidencySets:count:];
-[MTL4ToolsCommandQueue removeResidencySets:count:];
-[MTL4ToolsCommandQueue label];
-[MTL4ToolsCommandQueue addResidencySet:];
-[MTL4ToolsCommandQueue dealloc];
-[MTL4ToolsCommandQueue getBackgroundGPUPriority];
-[MTL4ToolsCommandQueue getGPUPriority];
-[MTL4ToolsCommandQueue setBackgroundGPUPriority:];
-[MTL4ToolsCommandQueue commitBlock:];
-[MTL4ToolsCommandQueue signalEvent:value:];
-[MTL4ToolsCommandQueue waitForEvent:value:];
-[MTL4ToolsCommandQueue signalDrawable:];
-[MTL4ToolsCommandQueue commit:count:];
-[MTL4ToolsCommandQueue commit:count:options:];
-[MTL4ToolsCommandQueue copyBufferMappingsFromBuffer:toBuffer:operations:count:];
-[MTL4ToolsCommandQueue copyTextureMappingsFromTexture:toTexture:operations:count:];
-[MTL4ToolsCommandQueue updateBufferMappings:heap:operations:count:];
-[MTL4ToolsCommandQueue updateTextureMappings:heap:operations:count:];
-[MTL4ToolsCommandQueue waitForDrawable:];
-[MTL4ToolsCommandQueue initWithBaseObject:parent:];
-[MTL4ToolsCommandQueue lastCommittedCommandBuffer];
-[MTL4ToolsCommandQueue lastCommittedCommandBufferGeneration];
-[MTL4ToolsCommandQueue waitForEvent:value:timeout:];
-[MTL4ToolsCommandQueue addedInternalResidencySets];
-[MTL4ToolsCommandQueue addedResidencySets];
-[MTL4ToolsCommandQueue commit:count:options:preprocessHandler:];
```
