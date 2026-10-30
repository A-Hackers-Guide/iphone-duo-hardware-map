# `MTLDebugIndirectComputeCommand`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsIndirectComputeCommand`
- 3 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"MTLIndirectCommandBufferDescriptor" _desc;
Q _index;
@"<MTLIndirectCommandBufferSPI>" _iCB;
```

## Properties

```
@property (TQ,R) index;
@property (T@"<MTLIndirectCommandBuffer>",R) indirectCommandBuffer;
```

## Instance methods

```
-[MTLDebugIndirectComputeCommand dealloc];
-[MTLDebugIndirectComputeCommand setThreadgroupMemoryLength:atIndex:];
-[MTLDebugIndirectComputeCommand index];
-[MTLDebugIndirectComputeCommand setComputePipelineState:];
-[MTLDebugIndirectComputeCommand setKernelBuffer:offset:atIndex:];
-[MTLDebugIndirectComputeCommand concurrentDispatchThreadgroups:threadsPerThreadgroup:];
-[MTLDebugIndirectComputeCommand concurrentDispatchThreads:threadsPerThreadgroup:];
-[MTLDebugIndirectComputeCommand setKernelBuffer:offset:attributeStride:atIndex:];
-[MTLDebugIndirectComputeCommand indirectCommandBuffer];
-[MTLDebugIndirectComputeCommand initWithBaseObject:descriptor:indexCount:indirectCommandBuffer:];
```
