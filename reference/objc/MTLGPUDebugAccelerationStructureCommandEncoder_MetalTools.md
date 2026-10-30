# `MTLGPUDebugAccelerationStructureCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsAccelerationStructureCommandEncoder`
- 9 instance variables, 0 properties, 44 instance methods, 0 class methods

## Instance variables

```
@"MTLGPUDebugCommandBuffer" _commandBuffer;
{list<resourceAndUsage, std::allocator<resourceAndUsage>>="__end_"{__list_node_base<resourceAndUsage, void *>="__prev_"^v"__next_"^v}""{?="__size_"Q}} _resourceAndUsageList;
{list<id<MTLHeap>, std::allocator<id<MTLHeap>>>="__end_"{__list_node_base<id<MTLHeap>, void *>="__prev_"^v"__next_"^v}""{?="__size_"Q}} _heapList;
@"MTLAccelerationStructurePassDescriptor" _accelerationStructurePassDescriptor;
@"<MTLLibrary>" _accelerationStructureSupportLibrary;
@"<MTLFence>" _serializationFence;
{vector<id<MTLFence>, std::allocator<id<MTLFence>>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} _fencesToUpdate;
{vector<id<MTLFence>, std::allocator<id<MTLFence>>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} _fencesToWaitFor;
B _baseEncoderHasCommands;
```

## Instance methods

```
-[MTLGPUDebugAccelerationStructureCommandEncoder waitForFence:];
-[MTLGPUDebugAccelerationStructureCommandEncoder useResources:count:usage:];
-[MTLGPUDebugAccelerationStructureCommandEncoder useResource:usage:];
-[MTLGPUDebugAccelerationStructureCommandEncoder updateFence:];
-[MTLGPUDebugAccelerationStructureCommandEncoder useHeap:];
-[MTLGPUDebugAccelerationStructureCommandEncoder useHeaps:count:];
-[MTLGPUDebugAccelerationStructureCommandEncoder endEncoding];
-[MTLGPUDebugAccelerationStructureCommandEncoder dealloc];
-[MTLGPUDebugAccelerationStructureCommandEncoder serializeAccelerationStructure:toBuffer:serializedBufferOffset:];
-[MTLGPUDebugAccelerationStructureCommandEncoder buildAccelerationStructure:descriptor:scratchBuffer:scratchBufferOffset:];
-[MTLGPUDebugAccelerationStructureCommandEncoder copyAccelerationStructure:toAccelerationStructure:];
-[MTLGPUDebugAccelerationStructureCommandEncoder copyAndCompactAccelerationStructure:toAccelerationStructure:];
-[MTLGPUDebugAccelerationStructureCommandEncoder deserializeAccelerationStructure:fromBuffer:serializedBufferOffset:];
-[MTLGPUDebugAccelerationStructureCommandEncoder deserializeAccelerationStructure:primitiveAccelerationStructures:fromBuffer:serializedBufferOffset:];
-[MTLGPUDebugAccelerationStructureCommandEncoder deserializeInstanceAccelerationStructure:primitiveAccelerationStructures:fromBuffer:serializedBufferOffset:];
-[MTLGPUDebugAccelerationStructureCommandEncoder deserializeInstanceAccelerationStructure:primitiveAccelerationStructures:fromBuffer:serializedBufferOffset:withDescriptor:];
-[MTLGPUDebugAccelerationStructureCommandEncoder deserializePrimitiveAccelerationStructure:fromBuffer:serializedBufferOffset:];
-[MTLGPUDebugAccelerationStructureCommandEncoder deserializePrimitiveAccelerationStructure:fromBuffer:serializedBufferOffset:withDescriptor:];
-[MTLGPUDebugAccelerationStructureCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:scratchBufferOffset:];
-[MTLGPUDebugAccelerationStructureCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:scratchBufferOffset:options:];
-[MTLGPUDebugAccelerationStructureCommandEncoder serializeInstanceAccelerationStructure:primitiveAccelerationStructures:toBuffer:serializedBufferOffset:];
-[MTLGPUDebugAccelerationStructureCommandEncoder serializePrimitiveAccelerationStructure:toBuffer:serializedBufferOffset:];
-[MTLGPUDebugAccelerationStructureCommandEncoder writeAccelerationStructureSerializationData:toBuffer:offset:];
-[MTLGPUDebugAccelerationStructureCommandEncoder writeCompactedAccelerationStructureSize:toBuffer:offset:];
-[MTLGPUDebugAccelerationStructureCommandEncoder writeCompactedAccelerationStructureSize:toBuffer:offset:sizeDataType:];
-[MTLGPUDebugAccelerationStructureCommandEncoder writeDeserializedAccelerationStructureSize:serializedOffset:toBuffer:sizeBufferOffset:];
-[MTLGPUDebugAccelerationStructureCommandEncoder writeDeserializedPrimitiveAccelerationStructureSizes:serializedOffset:toBuffer:sizesBufferOffset:];
-[MTLGPUDebugAccelerationStructureCommandEncoder writeGenericBVHStructureOfAccelerationStructure:headerBuffer:headerBufferOffset:innerNodeBuffer:innerNodeBufferOffset:leafNodeBuffer:leafNodeBufferOffset:primitiveBuffer:primitiveBufferOffset:geometryBuffer:geometryOffset:instanceTransformBuffer:instanceTransformOffset:controlPointBuffer:controlPointBufferOffset:];
-[MTLGPUDebugAccelerationStructureCommandEncoder writeGenericBVHStructureOfAccelerationStructure:into:];
-[MTLGPUDebugAccelerationStructureCommandEncoder writeGenericBVHStructureSizesOfAccelerationStructure:into:];
-[MTLGPUDebugAccelerationStructureCommandEncoder writeGenericBVHStructureSizesOfAccelerationStructure:toBuffer:sizesBufferOffset:];
-[MTLGPUDebugAccelerationStructureCommandEncoder writeGeometryOfAccelerationStructure:toBuffer:geometryBufferOffset:];
-[MTLGPUDebugAccelerationStructureCommandEncoder writeGeometrySizeOfAccelerationStructure:toBuffer:sizeBufferOffset:];
-[MTLGPUDebugAccelerationStructureCommandEncoder writeSerializedAccelerationStructureSize:toBuffer:sizeBufferOffset:];
-[MTLGPUDebugAccelerationStructureCommandEncoder blitAccelerationStructureType:toAccelerationStructure:];
-[MTLGPUDebugAccelerationStructureCommandEncoder blitInstanceTypetoAccelerationStructure:];
-[MTLGPUDebugAccelerationStructureCommandEncoder blitPrimitiveTypetoAccelerationStructure:];
-[MTLGPUDebugAccelerationStructureCommandEncoder blitTypeFromAccelerationStructure:toAccelerationStructure:];
-[MTLGPUDebugAccelerationStructureCommandEncoder blitTypeFromAccelerationStructureDescriptor:toAccelerationStructure:];
-[MTLGPUDebugAccelerationStructureCommandEncoder destroyBaseAccelerationStructureCommandEncoder];
-[MTLGPUDebugAccelerationStructureCommandEncoder initWithAccelerationStructureCommandEncoder:parent:accelerationStructurePassDescriptor:];
-[MTLGPUDebugAccelerationStructureCommandEncoder newBaseAccelerationStructureCommandEncoder];
-[MTLGPUDebugAccelerationStructureCommandEncoder psoWithFunctionName:];
-[MTLGPUDebugAccelerationStructureCommandEncoder serializationFence];
```
