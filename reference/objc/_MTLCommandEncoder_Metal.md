# `_MTLCommandEncoder`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- 9 instance variables, 6 properties, 90 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
@"_MTLCommandBuffer<MTLCommandBuffer>" _commandBuffer;
Q _numThisEncoder;
Q _globalTraceObjectID;
Q _labelTraceID;
@"<MTLFence>" _progressFence;
B _needsFrameworkAssistedErrorTracking;
B _isProgressTrackingEncoder;
@"NSMutableArray" _debugSignposts;
```

## Properties

```
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C,D) label;
@property (TQ,R,N,V_globalTraceObjectID) globalTraceObjectID;
@property (TQ,R,N,GgetType) type;
@property (TQ,N,V_numThisEncoder) numThisEncoder;
@property (TQ,R,D) dispatchType;
```

## Instance methods

```
-[_MTLCommandEncoder insertDebugSignpost:];
-[_MTLCommandEncoder setAccelerationStructure:atBufferIndex:];
-[_MTLCommandEncoder setMeshIntersectionFunctionTables:withBufferRange:];
-[_MTLCommandEncoder setVertexBufferOffset:attributeStride:atIndex:];
-[_MTLCommandEncoder pushDebugGroup:];
-[_MTLCommandEncoder setObjectAccelerationStructure:atBufferIndex:];
-[_MTLCommandEncoder setMeshSamplerStates:lodMinClamps:lodMaxClamps:withRange:];
-[_MTLCommandEncoder useResidencySet:];
-[_MTLCommandEncoder setObjectBufferOffset:atIndex:];
-[_MTLCommandEncoder useResidencySets:count:];
-[_MTLCommandEncoder popDebugGroup];
-[_MTLCommandEncoder formattedDescription:];
-[_MTLCommandEncoder device];
-[_MTLCommandEncoder setObjectIntersectionFunctionTables:withBufferRange:];
-[_MTLCommandEncoder setVertexBuffer:offset:attributeStride:atIndex:];
-[_MTLCommandEncoder setTileAccelerationStructure:atBufferIndex:];
-[_MTLCommandEncoder endEncoding];
-[_MTLCommandEncoder globalTraceObjectID];
-[_MTLCommandEncoder drawMeshThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[_MTLCommandEncoder setVertexBytes:length:attributeStride:atIndex:];
-[_MTLCommandEncoder dealloc];
-[_MTLCommandEncoder setObjectSamplerState:atIndex:];
-[_MTLCommandEncoder setVertexBuffers:offsets:attributeStrides:withRange:];
-[_MTLCommandEncoder setObjectBuffer:offset:atIndex:];
-[_MTLCommandEncoder setMeshBuffer:offset:atIndex:];
-[_MTLCommandEncoder setBuffer:offset:attributeStride:atIndex:];
-[_MTLCommandEncoder getType];
-[_MTLCommandEncoder setObjectBuffers:offsets:withRange:];
-[_MTLCommandEncoder setMeshSamplerState:atIndex:];
-[_MTLCommandEncoder setObjectIntersectionFunctionTable:atBufferIndex:];
-[_MTLCommandEncoder optimizeContentsForCPUAccess:slice:level:];
-[_MTLCommandEncoder setVertexAccelerationStructure:atBufferIndex:];
-[_MTLCommandEncoder dispatchType];
-[_MTLCommandEncoder setMeshAccelerationStructure:atBufferIndex:];
-[_MTLCommandEncoder drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[_MTLCommandEncoder setBuffers:offsets:attributeStrides:withRange:];
-[_MTLCommandEncoder optimizeContentsForGPUAccess:];
-[_MTLCommandEncoder setObjectSamplerStates:withRange:];
-[_MTLCommandEncoder commandBuffer];
-[_MTLCommandEncoder setMeshBufferOffset:atIndex:];
-[_MTLCommandEncoder setBufferOffset:attributeStride:atIndex:];
-[_MTLCommandEncoder description];
-[_MTLCommandEncoder setObjectSamplerState:lodMinClamp:lodMaxClamp:atIndex:];
-[_MTLCommandEncoder setMeshTextures:withRange:];
-[_MTLCommandEncoder setBytes:length:attributeStride:atIndex:];
-[_MTLCommandEncoder setMeshBuffers:offsets:withRange:];
-[_MTLCommandEncoder setObjectTexture:atIndex:];
-[_MTLCommandEncoder setObjectThreadgroupMemoryLength:atIndex:];
-[_MTLCommandEncoder setObjectTextures:withRange:];
-[_MTLCommandEncoder setMeshSamplerStates:withRange:];
-[_MTLCommandEncoder setObjectBytes:length:atIndex:];
-[_MTLCommandEncoder setMeshTexture:atIndex:];
-[_MTLCommandEncoder optimizeContentsForCPUAccess:];
-[_MTLCommandEncoder setMeshIntersectionFunctionTable:atBufferIndex:];
-[_MTLCommandEncoder setObjectSamplerStates:lodMinClamps:lodMaxClamps:withRange:];
-[_MTLCommandEncoder drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[_MTLCommandEncoder setMeshSamplerState:lodMinClamp:lodMaxClamp:atIndex:];
-[_MTLCommandEncoder setFragmentAccelerationStructure:atBufferIndex:];
-[_MTLCommandEncoder setMeshBytes:length:atIndex:];
-[_MTLCommandEncoder optimizeContentsForGPUAccess:slice:level:];
-[_MTLCommandEncoder setThreadgroupDistributionMode:];
-[_MTLCommandEncoder barrierAfterQueueStages:beforeStages:];
-[_MTLCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:sourcePlane:toTensor:destinationOrigin:destinationDimensions:destinationPlane:];
-[_MTLCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:];
-[_MTLCommandEncoder copyFromTensor:sourceSlice:toTensor:destinationSlice:];
-[_MTLCommandEncoder endEncodingAndRetrieveProgramAddressTable];
-[_MTLCommandEncoder filterCounterRangeWithFirstBatch:lastBatch:filterIndex:];
-[_MTLCommandEncoder getDriverUniqueID];
-[_MTLCommandEncoder initWithCommandBuffer:];
-[_MTLCommandEncoder insertSplit];
-[_MTLCommandEncoder invalidateCompressedTexture:];
-[_MTLCommandEncoder invalidateCompressedTexture:slice:level:];
-[_MTLCommandEncoder memoryBarrierNotificationWithResources:count:];
-[_MTLCommandEncoder memoryBarrierNotificationWithScope:];
-[_MTLCommandEncoder numThisEncoder];
-[_MTLCommandEncoder optimizeContentsForTexture:readAccessPattern:];
-[_MTLCommandEncoder optimizeContentsForTexture:readAccessPattern:readAccessor:];
-[_MTLCommandEncoder optimizeContentsForTexture:readAccessPattern:readAccessor:slice:level:];
-[_MTLCommandEncoder optimizeContentsForTexture:readAccessPattern:slice:level:];
-[_MTLCommandEncoder preEndEncoding];
-[_MTLCommandEncoder setColorAttachmentMap:];
-[_MTLCommandEncoder setMeshVisibleFunctionTable:atBufferIndex:];
-[_MTLCommandEncoder setMeshVisibleFunctionTables:withBufferRange:];
-[_MTLCommandEncoder setNumThisEncoder:];
-[_MTLCommandEncoder setObjectVisibleFunctionTable:atBufferIndex:];
-[_MTLCommandEncoder setObjectVisibleFunctionTables:withBufferRange:];
-[_MTLCommandEncoder setThreadgroupDistributionModeWithClusterGroupIndex:];
-[_MTLCommandEncoder setThreadgroupPackingDisabled:];
-[_MTLCommandEncoder setToolsDispatchBufferSPI:atIndex:];
-[_MTLCommandEncoder setToolsDispatchBufferSPI:atIndex:stages:];
```
