# `AGXG19FamilyRayTracingGPUBuilder`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLAccelerationStructureCommandEncoder`
- Protocols: `MTLAccelerationStructureCommandEncoderSPI`
- 7 instance variables, 6 properties, 43 instance methods, 0 class methods

## Instance variables

```
^v _impl;
@"AccelerationStructureCommandRecorder" _recorder;
@"<MTLComputeCommandEncoderSPI>" _computeEncoder;
^v _progressBins;
B virtualSubstreamsEnabled;
B virtualSubstreamOpen;
B _defersCommands;
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
-[AGXG19FamilyRayTracingGPUBuilder waitForFence:];
-[AGXG19FamilyRayTracingGPUBuilder useResources:count:usage:];
-[AGXG19FamilyRayTracingGPUBuilder useResource:usage:];
-[AGXG19FamilyRayTracingGPUBuilder insertDebugSignpost:];
-[AGXG19FamilyRayTracingGPUBuilder updateFence:];
-[AGXG19FamilyRayTracingGPUBuilder useHeap:];
-[AGXG19FamilyRayTracingGPUBuilder useHeaps:count:];
-[AGXG19FamilyRayTracingGPUBuilder sampleCountersInBuffer:atSampleIndex:withBarrier:];
-[AGXG19FamilyRayTracingGPUBuilder pushDebugGroup:];
-[AGXG19FamilyRayTracingGPUBuilder popDebugGroup];
-[AGXG19FamilyRayTracingGPUBuilder initWithCommandBuffer:descriptor:];
-[AGXG19FamilyRayTracingGPUBuilder setLabel:];
-[AGXG19FamilyRayTracingGPUBuilder endEncoding];
-[AGXG19FamilyRayTracingGPUBuilder globalTraceObjectID];
-[AGXG19FamilyRayTracingGPUBuilder dealloc];
-[AGXG19FamilyRayTracingGPUBuilder barrierAfterQueueStages:beforeStages:];
-[AGXG19FamilyRayTracingGPUBuilder buildAccelerationStructure:descriptor:scratchBuffer:scratchBufferOffset:];
-[AGXG19FamilyRayTracingGPUBuilder copyAccelerationStructure:toAccelerationStructure:];
-[AGXG19FamilyRayTracingGPUBuilder copyAndCompactAccelerationStructure:toAccelerationStructure:];
-[AGXG19FamilyRayTracingGPUBuilder deserializeInstanceAccelerationStructure:primitiveAccelerationStructures:fromBuffer:serializedBufferOffset:];
-[AGXG19FamilyRayTracingGPUBuilder deserializeInstanceAccelerationStructure:primitiveAccelerationStructures:fromBuffer:serializedBufferOffset:withDescriptor:];
-[AGXG19FamilyRayTracingGPUBuilder deserializePrimitiveAccelerationStructure:fromBuffer:serializedBufferOffset:];
-[AGXG19FamilyRayTracingGPUBuilder deserializePrimitiveAccelerationStructure:fromBuffer:serializedBufferOffset:withDescriptor:];
-[AGXG19FamilyRayTracingGPUBuilder refitAccelerationStructure:descriptor:destination:scratchBuffer:scratchBufferOffset:];
-[AGXG19FamilyRayTracingGPUBuilder refitAccelerationStructure:descriptor:destination:scratchBuffer:scratchBufferOffset:options:];
-[AGXG19FamilyRayTracingGPUBuilder serializeInstanceAccelerationStructure:primitiveAccelerationStructures:toBuffer:serializedBufferOffset:];
-[AGXG19FamilyRayTracingGPUBuilder serializePrimitiveAccelerationStructure:toBuffer:serializedBufferOffset:];
-[AGXG19FamilyRayTracingGPUBuilder substreamSynchronizeAccelerationStructures:access:];
-[AGXG19FamilyRayTracingGPUBuilder substreamSynchronizeDescriptor:access:];
-[AGXG19FamilyRayTracingGPUBuilder writeAccelerationStructureSerializationData:toBuffer:offset:];
-[AGXG19FamilyRayTracingGPUBuilder writeAccelerationStructureTraversalDepth:toBuffer:offset:];
-[AGXG19FamilyRayTracingGPUBuilder writeCompactedAccelerationStructureSize:toBuffer:offset:];
-[AGXG19FamilyRayTracingGPUBuilder writeCompactedAccelerationStructureSize:toBuffer:offset:sizeDataType:];
-[AGXG19FamilyRayTracingGPUBuilder writeDeserializedAccelerationStructureSize:serializedOffset:toBuffer:sizeBufferOffset:];
-[AGXG19FamilyRayTracingGPUBuilder writeGenericBVHStructureOfAccelerationStructure:headerBuffer:headerBufferOffset:innerNodeBuffer:innerNodeBufferOffset:leafNodeBuffer:leafNodeBufferOffset:primitiveBuffer:primitiveBufferOffset:geometryBuffer:geometryOffset:instanceTransformBuffer:instanceTransformOffset:controlPointBuffer:controlPointBufferOffset:];
-[AGXG19FamilyRayTracingGPUBuilder writeGenericBVHStructureOfAccelerationStructure:into:];
-[AGXG19FamilyRayTracingGPUBuilder writeGenericBVHStructureSizesOfAccelerationStructure:into:];
-[AGXG19FamilyRayTracingGPUBuilder writeGenericBVHStructureSizesOfAccelerationStructure:toBuffer:sizesBufferOffset:];
-[AGXG19FamilyRayTracingGPUBuilder writeGeometryOfAccelerationStructure:toBuffer:geometryBufferOffset:];
-[AGXG19FamilyRayTracingGPUBuilder writeGeometrySizeOfAccelerationStructure:toBuffer:sizeBufferOffset:];
-[AGXG19FamilyRayTracingGPUBuilder writeSerializedAccelerationStructureSize:toBuffer:sizeBufferOffset:];
-[AGXG19FamilyRayTracingGPUBuilder _beginVirtualSubstream];
-[AGXG19FamilyRayTracingGPUBuilder _endVirtualSubstream];
```
