# `MTL4ComputeCommandEncoder` (protocol)

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTL4CommandEncoder`
- 0 instance variables, 0 properties, 37 instance methods, 0 class methods

## Instance methods

```
-[MTL4ComputeCommandEncoder executeCommandsInBuffer:withRange:];
-[MTL4ComputeCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:];
-[MTL4ComputeCommandEncoder copyFromTexture:toTexture:];
-[MTL4ComputeCommandEncoder setThreadgroupMemoryLength:atIndex:];
-[MTL4ComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:];
-[MTL4ComputeCommandEncoder dispatchThreads:threadsPerThreadgroup:];
-[MTL4ComputeCommandEncoder optimizeContentsForCPUAccess:slice:level:];
-[MTL4ComputeCommandEncoder optimizeIndirectCommandBuffer:withRange:];
-[MTL4ComputeCommandEncoder setComputePipelineState:];
-[MTL4ComputeCommandEncoder setImageblockWidth:height:];
-[MTL4ComputeCommandEncoder optimizeContentsForGPUAccess:];
-[MTL4ComputeCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:];
-[MTL4ComputeCommandEncoder resetCommandsInBuffer:withRange:];
-[MTL4ComputeCommandEncoder optimizeContentsForCPUAccess:];
-[MTL4ComputeCommandEncoder optimizeContentsForGPUAccess:slice:level:];
-[MTL4ComputeCommandEncoder copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:];
-[MTL4ComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTL4ComputeCommandEncoder generateMipmapsForTexture:];
-[MTL4ComputeCommandEncoder stages];
-[MTL4ComputeCommandEncoder setArgumentTable:];
-[MTL4ComputeCommandEncoder buildAccelerationStructure:descriptor:scratchBuffer:];
-[MTL4ComputeCommandEncoder copyAccelerationStructure:toAccelerationStructure:];
-[MTL4ComputeCommandEncoder copyAndCompactAccelerationStructure:toAccelerationStructure:];
-[MTL4ComputeCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTL4ComputeCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
-[MTL4ComputeCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:sourcePlane:toTensor:destinationOrigin:destinationDimensions:destinationPlane:];
-[MTL4ComputeCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:];
-[MTL4ComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:];
-[MTL4ComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:];
-[MTL4ComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:threadsPerThreadgroup:];
-[MTL4ComputeCommandEncoder dispatchThreadsWithIndirectBuffer:];
-[MTL4ComputeCommandEncoder executeCommandsInBuffer:indirectBuffer:];
-[MTL4ComputeCommandEncoder fillBuffer:range:value:];
-[MTL4ComputeCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:];
-[MTL4ComputeCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:options:];
-[MTL4ComputeCommandEncoder writeCompactedAccelerationStructureSize:toBuffer:];
-[MTL4ComputeCommandEncoder writeTimestampWithGranularity:intoHeap:atIndex:];
```
