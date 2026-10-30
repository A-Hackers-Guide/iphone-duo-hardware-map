# `MTLLegacySVIndirectCommandBuffer`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsIndirectCommandBuffer`
- Protocols: `MTLLegacySVResource`
- 19 instance variables, 37 properties, 40 instance methods, 0 class methods

## Instance variables

```
B _hasRender;
B _hasCompute;
B _inheritsBuffers;
B _inheritsPipelineState;
@"<MTLBuffer>" _argumentStorage;
@"<MTLBuffer>" _vertexKernelDrawOrDispatchIDBuffer;
@"<MTLBuffer>" _fragmentDrawIDBuffer;
@"<MTLBuffer>" _meshDrawIDBuffer;
@"<MTLBuffer>" _objectDrawIDBuffer;
S _maxCommands;
C _maxVertexBindings;
C _maxFragmentBindings;
C _maxKernelBindings;
C _maxThreadgroupBindings;
C _maxObjectBindings;
C _maxMeshBindings;
B _mayContainDrawMeshes;
S _commandByteStride;
Q _originalResourceOptions;
```

## Properties

```
@property (T@"<MTLBuffer>",R,N) internalICBBuffer;
@property (T@"<MTLBuffer>",R,N) internalDispatchIDBuffer;
@property (T@"<MTLBuffer>",R,N) internalVertexDrawIDBuffer;
@property (T@"<MTLBuffer>",R,N) internalFragmentDrawIDBuffer;
@property (T@"<MTLBuffer>",R,N) internalMeshDrawIDBuffer;
@property (T@"<MTLBuffer>",R,N) internalObjectDrawIDBuffer;
@property (TQ,R,N) maxCommands;
@property (TQ,R,N) maxVertexBindings;
@property (TQ,R,N) maxFragmentBindings;
@property (TQ,R,N) maxKernelBindings;
@property (TQ,R,N) maxObjectBindings;
@property (TQ,R,N) maxMeshBindings;
@property (TB,R,N) mayContainDrawMeshes;
@property (TQ,R,N) commandByteStride;
@property (TB,R,N) inheritsPipelineState;
@property (TB,R,N) inheritsBuffers;
@property (T@"<MTLIndirectCommandBufferSPI>",&,D,N) baseObject;
@property (TQ,R,N) length;
@property (TQ,R,N) gpuAddress;
@property (TQ,R,N) underlyingGPUAddress;
@property (Ti) responsibleProcess;
@property (TQ,R) allocationID;
@property (TQ,R) protectionOptions;
@property (TQ,R) unfilteredResourceOptions;
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) cpuCacheMode;
@property (TQ,R) storageMode;
@property (TQ,R) hazardTrackingMode;
@property (TQ,R) resourceOptions;
@property (T@"<MTLHeap>",R) heap;
@property (TQ,R) heapOffset;
@property (TQ,R) allocatedSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLLegacySVIndirectCommandBuffer resourceOptions];
-[MTLLegacySVIndirectCommandBuffer hazardTrackingMode];
-[MTLLegacySVIndirectCommandBuffer cpuCacheMode];
-[MTLLegacySVIndirectCommandBuffer storageMode];
-[MTLLegacySVIndirectCommandBuffer dealloc];
-[MTLLegacySVIndirectCommandBuffer gpuAddress];
-[MTLLegacySVIndirectCommandBuffer length];
-[MTLLegacySVIndirectCommandBuffer gpuResourceID];
-[MTLLegacySVIndirectCommandBuffer indirectComputeCommandAtIndex:];
-[MTLLegacySVIndirectCommandBuffer indirectRenderCommandAtIndex:];
-[MTLLegacySVIndirectCommandBuffer inheritsBuffers];
-[MTLLegacySVIndirectCommandBuffer maxMeshBindings];
-[MTLLegacySVIndirectCommandBuffer setBuffer:offset:attributeStride:atIndex:forStage:commandIndex:];
-[MTLLegacySVIndirectCommandBuffer commandByteStride];
-[MTLLegacySVIndirectCommandBuffer handleForOffset:];
-[MTLLegacySVIndirectCommandBuffer inheritsPipelineState];
-[MTLLegacySVIndirectCommandBuffer initWithIndirectCommandBuffer:descriptor:maxCommandCount:resourceOptions:device:];
-[MTLLegacySVIndirectCommandBuffer internalDispatchIDBuffer];
-[MTLLegacySVIndirectCommandBuffer internalFragmentDrawIDBuffer];
-[MTLLegacySVIndirectCommandBuffer internalICBBuffer];
-[MTLLegacySVIndirectCommandBuffer internalMeshDrawIDBuffer];
-[MTLLegacySVIndirectCommandBuffer internalObjectDrawIDBuffer];
-[MTLLegacySVIndirectCommandBuffer internalVertexDrawIDBuffer];
-[MTLLegacySVIndirectCommandBuffer maxCommands];
-[MTLLegacySVIndirectCommandBuffer maxFragmentBindings];
-[MTLLegacySVIndirectCommandBuffer maxKernelBindings];
-[MTLLegacySVIndirectCommandBuffer maxObjectBindings];
-[MTLLegacySVIndirectCommandBuffer maxVertexBindings];
-[MTLLegacySVIndirectCommandBuffer mayContainDrawMeshes];
-[MTLLegacySVIndirectCommandBuffer onExecuteWithComputeEncoder:];
-[MTLLegacySVIndirectCommandBuffer onExecuteWithRenderEncoder:];
-[MTLLegacySVIndirectCommandBuffer resetAtIndex:];
-[MTLLegacySVIndirectCommandBuffer setBuffer:offset:atIndex:forStage:commandIndex:];
-[MTLLegacySVIndirectCommandBuffer setComputePipelineStateBuffers:commandIndex:];
-[MTLLegacySVIndirectCommandBuffer setRenderPipelineStateBuffers:commandIndex:];
-[MTLLegacySVIndirectCommandBuffer setTessellationControlPointIndexBuffer:offset:commandIndex:];
-[MTLLegacySVIndirectCommandBuffer setThreadgroupMemoryLength:atIndex:commandIndex:];
-[MTLLegacySVIndirectCommandBuffer underlyingGPUAddress];
-[MTLLegacySVIndirectCommandBuffer useWithComputeEncoder:usage:];
-[MTLLegacySVIndirectCommandBuffer useWithRenderEncoder:usage:stages:];
```
