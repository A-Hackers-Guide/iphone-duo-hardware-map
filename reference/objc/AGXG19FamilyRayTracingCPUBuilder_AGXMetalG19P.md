# `AGXG19FamilyRayTracingCPUBuilder`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLAccelerationStructureCommandEncoder`
- Protocols: `MTLAccelerationStructureCommandEncoderSPI`
- 1 instance variables, 6 properties, 33 instance methods, 1 class methods

## Instance variables

```
{RayTracingCPUBuilder="riaBvhGen"I} _impl;
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

## Class methods

```
+[AGXG19FamilyRayTracingCPUBuilder calcAllocSizesFromDescriptor:];
```

## Instance methods

```
-[AGXG19FamilyRayTracingCPUBuilder waitForFence:];
-[AGXG19FamilyRayTracingCPUBuilder useResources:count:usage:];
-[AGXG19FamilyRayTracingCPUBuilder useResource:usage:];
-[AGXG19FamilyRayTracingCPUBuilder insertDebugSignpost:];
-[AGXG19FamilyRayTracingCPUBuilder updateFence:];
-[AGXG19FamilyRayTracingCPUBuilder useHeap:];
-[AGXG19FamilyRayTracingCPUBuilder useHeaps:count:];
-[AGXG19FamilyRayTracingCPUBuilder sampleCountersInBuffer:atSampleIndex:withBarrier:];
-[AGXG19FamilyRayTracingCPUBuilder pushDebugGroup:];
-[AGXG19FamilyRayTracingCPUBuilder popDebugGroup];
-[AGXG19FamilyRayTracingCPUBuilder init];
-[AGXG19FamilyRayTracingCPUBuilder endEncoding];
-[AGXG19FamilyRayTracingCPUBuilder serializeAccelerationStructure:toBuffer:serializedBufferOffset:];
-[AGXG19FamilyRayTracingCPUBuilder barrierAfterQueueStages:beforeStages:];
-[AGXG19FamilyRayTracingCPUBuilder buildAccelerationStructure:descriptor:scratchBuffer:scratchBufferOffset:];
-[AGXG19FamilyRayTracingCPUBuilder copyAccelerationStructure:toAccelerationStructure:];
-[AGXG19FamilyRayTracingCPUBuilder copyAndCompactAccelerationStructure:toAccelerationStructure:];
-[AGXG19FamilyRayTracingCPUBuilder deserializeAccelerationStructure:fromBuffer:serializedBufferOffset:];
-[AGXG19FamilyRayTracingCPUBuilder deserializeAccelerationStructure:primitiveAccelerationStructures:fromBuffer:serializedBufferOffset:];
-[AGXG19FamilyRayTracingCPUBuilder deserializeInstanceAccelerationStructure:primitiveAccelerationStructures:fromBuffer:serializedBufferOffset:];
-[AGXG19FamilyRayTracingCPUBuilder deserializePrimitiveAccelerationStructure:fromBuffer:serializedBufferOffset:];
-[AGXG19FamilyRayTracingCPUBuilder refitAccelerationStructure:descriptor:destination:scratchBuffer:scratchBufferOffset:];
-[AGXG19FamilyRayTracingCPUBuilder serializeInstanceAccelerationStructure:primitiveAccelerationStructures:toBuffer:serializedBufferOffset:];
-[AGXG19FamilyRayTracingCPUBuilder serializePrimitiveAccelerationStructure:toBuffer:serializedBufferOffset:];
-[AGXG19FamilyRayTracingCPUBuilder writeCompactedAccelerationStructureSize:toBuffer:offset:];
-[AGXG19FamilyRayTracingCPUBuilder writeCompactedAccelerationStructureSize:toBuffer:offset:sizeDataType:];
-[AGXG19FamilyRayTracingCPUBuilder writeDeserializedAccelerationStructureSize:serializedOffset:toBuffer:sizeBufferOffset:];
-[AGXG19FamilyRayTracingCPUBuilder writeDeserializedPrimitiveAccelerationStructureSizes:serializedOffset:toBuffer:sizesBufferOffset:];
-[AGXG19FamilyRayTracingCPUBuilder writeGenericBVHStructureOfAccelerationStructure:headerBuffer:headerBufferOffset:innerNodeBuffer:innerNodeBufferOffset:leafNodeBuffer:leafNodeBufferOffset:primitiveBuffer:primitiveBufferOffset:geometryBuffer:geometryOffset:instanceTransformBuffer:instanceTransformOffset:controlPointBuffer:controlPointBufferOffset:];
-[AGXG19FamilyRayTracingCPUBuilder writeGenericBVHStructureSizesOfAccelerationStructure:toBuffer:sizesBufferOffset:];
-[AGXG19FamilyRayTracingCPUBuilder writeGeometryOfAccelerationStructure:toBuffer:geometryBufferOffset:];
-[AGXG19FamilyRayTracingCPUBuilder writeGeometrySizeOfAccelerationStructure:toBuffer:sizeBufferOffset:];
-[AGXG19FamilyRayTracingCPUBuilder writeSerializedAccelerationStructureSize:toBuffer:sizeBufferOffset:];
```
