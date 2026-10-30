# `_MTLAccelerationStructureCommandEncoder`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLCommandEncoder`
- Protocols: `MTLAccelerationStructureCommandEncoderSPI`
- 0 instance variables, 6 properties, 34 instance methods, 0 class methods

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
-[_MTLAccelerationStructureCommandEncoder waitForFence:];
-[_MTLAccelerationStructureCommandEncoder useResources:count:usage:];
-[_MTLAccelerationStructureCommandEncoder useResource:usage:];
-[_MTLAccelerationStructureCommandEncoder updateFence:];
-[_MTLAccelerationStructureCommandEncoder useHeap:];
-[_MTLAccelerationStructureCommandEncoder useHeaps:count:];
-[_MTLAccelerationStructureCommandEncoder sampleCountersInBuffer:atSampleIndex:withBarrier:];
-[_MTLAccelerationStructureCommandEncoder serializeAccelerationStructure:toBuffer:serializedBufferOffset:];
-[_MTLAccelerationStructureCommandEncoder buildAccelerationStructure:descriptor:scratchBuffer:scratchBufferOffset:];
-[_MTLAccelerationStructureCommandEncoder copyAccelerationStructure:toAccelerationStructure:];
-[_MTLAccelerationStructureCommandEncoder copyAndCompactAccelerationStructure:toAccelerationStructure:];
-[_MTLAccelerationStructureCommandEncoder deserializeAccelerationStructure:fromBuffer:serializedBufferOffset:];
-[_MTLAccelerationStructureCommandEncoder deserializeAccelerationStructure:primitiveAccelerationStructures:fromBuffer:serializedBufferOffset:];
-[_MTLAccelerationStructureCommandEncoder deserializeInstanceAccelerationStructure:primitiveAccelerationStructures:fromBuffer:serializedBufferOffset:];
-[_MTLAccelerationStructureCommandEncoder deserializeInstanceAccelerationStructure:primitiveAccelerationStructures:fromBuffer:serializedBufferOffset:withDescriptor:];
-[_MTLAccelerationStructureCommandEncoder deserializePrimitiveAccelerationStructure:fromBuffer:serializedBufferOffset:];
-[_MTLAccelerationStructureCommandEncoder deserializePrimitiveAccelerationStructure:fromBuffer:serializedBufferOffset:withDescriptor:];
-[_MTLAccelerationStructureCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:scratchBufferOffset:];
-[_MTLAccelerationStructureCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:scratchBufferOffset:options:];
-[_MTLAccelerationStructureCommandEncoder serializeInstanceAccelerationStructure:primitiveAccelerationStructures:toBuffer:serializedBufferOffset:];
-[_MTLAccelerationStructureCommandEncoder serializePrimitiveAccelerationStructure:toBuffer:serializedBufferOffset:];
-[_MTLAccelerationStructureCommandEncoder writeAccelerationStructureSerializationData:toBuffer:offset:];
-[_MTLAccelerationStructureCommandEncoder writeAccelerationStructureTraversalDepth:toBuffer:offset:];
-[_MTLAccelerationStructureCommandEncoder writeCompactedAccelerationStructureSize:toBuffer:offset:];
-[_MTLAccelerationStructureCommandEncoder writeCompactedAccelerationStructureSize:toBuffer:offset:sizeDataType:];
-[_MTLAccelerationStructureCommandEncoder writeDeserializedAccelerationStructureSize:serializedOffset:toBuffer:sizeBufferOffset:];
-[_MTLAccelerationStructureCommandEncoder writeDeserializedPrimitiveAccelerationStructureSizes:serializedOffset:toBuffer:sizesBufferOffset:];
-[_MTLAccelerationStructureCommandEncoder writeGenericBVHStructureOfAccelerationStructure:headerBuffer:headerBufferOffset:innerNodeBuffer:innerNodeBufferOffset:leafNodeBuffer:leafNodeBufferOffset:primitiveBuffer:primitiveBufferOffset:geometryBuffer:geometryOffset:instanceTransformBuffer:instanceTransformOffset:controlPointBuffer:controlPointBufferOffset:];
-[_MTLAccelerationStructureCommandEncoder writeGenericBVHStructureOfAccelerationStructure:into:];
-[_MTLAccelerationStructureCommandEncoder writeGenericBVHStructureSizesOfAccelerationStructure:into:];
-[_MTLAccelerationStructureCommandEncoder writeGenericBVHStructureSizesOfAccelerationStructure:toBuffer:sizesBufferOffset:];
-[_MTLAccelerationStructureCommandEncoder writeGeometryOfAccelerationStructure:toBuffer:geometryBufferOffset:];
-[_MTLAccelerationStructureCommandEncoder writeGeometrySizeOfAccelerationStructure:toBuffer:sizeBufferOffset:];
-[_MTLAccelerationStructureCommandEncoder writeSerializedAccelerationStructureSize:toBuffer:sizeBufferOffset:];
```
