# `MTLToolsAccelerationStructureCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsCommandEncoder`
- Protocols: `MTLAccelerationStructureCommandEncoderSPI`
- 0 instance variables, 6 properties, 36 instance methods, 0 class methods

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
-[MTLToolsAccelerationStructureCommandEncoder waitForFence:];
-[MTLToolsAccelerationStructureCommandEncoder useResources:count:usage:];
-[MTLToolsAccelerationStructureCommandEncoder useResource:usage:];
-[MTLToolsAccelerationStructureCommandEncoder updateFence:];
-[MTLToolsAccelerationStructureCommandEncoder useHeap:];
-[MTLToolsAccelerationStructureCommandEncoder useHeaps:count:];
-[MTLToolsAccelerationStructureCommandEncoder sampleCountersInBuffer:atSampleIndex:withBarrier:];
-[MTLToolsAccelerationStructureCommandEncoder serializeAccelerationStructure:toBuffer:serializedBufferOffset:];
-[MTLToolsAccelerationStructureCommandEncoder buildAccelerationStructure:descriptor:scratchBuffer:scratchBufferOffset:];
-[MTLToolsAccelerationStructureCommandEncoder copyAccelerationStructure:toAccelerationStructure:];
-[MTLToolsAccelerationStructureCommandEncoder copyAndCompactAccelerationStructure:toAccelerationStructure:];
-[MTLToolsAccelerationStructureCommandEncoder deserializeAccelerationStructure:fromBuffer:serializedBufferOffset:];
-[MTLToolsAccelerationStructureCommandEncoder deserializeAccelerationStructure:primitiveAccelerationStructures:fromBuffer:serializedBufferOffset:];
-[MTLToolsAccelerationStructureCommandEncoder deserializeInstanceAccelerationStructure:primitiveAccelerationStructures:fromBuffer:serializedBufferOffset:];
-[MTLToolsAccelerationStructureCommandEncoder deserializeInstanceAccelerationStructure:primitiveAccelerationStructures:fromBuffer:serializedBufferOffset:withDescriptor:];
-[MTLToolsAccelerationStructureCommandEncoder deserializePrimitiveAccelerationStructure:fromBuffer:serializedBufferOffset:];
-[MTLToolsAccelerationStructureCommandEncoder deserializePrimitiveAccelerationStructure:fromBuffer:serializedBufferOffset:withDescriptor:];
-[MTLToolsAccelerationStructureCommandEncoder endEncodingAndRetrieveProgramAddressTable];
-[MTLToolsAccelerationStructureCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:scratchBufferOffset:];
-[MTLToolsAccelerationStructureCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:scratchBufferOffset:options:];
-[MTLToolsAccelerationStructureCommandEncoder serializeInstanceAccelerationStructure:primitiveAccelerationStructures:toBuffer:serializedBufferOffset:];
-[MTLToolsAccelerationStructureCommandEncoder serializePrimitiveAccelerationStructure:toBuffer:serializedBufferOffset:];
-[MTLToolsAccelerationStructureCommandEncoder writeAccelerationStructureSerializationData:toBuffer:offset:];
-[MTLToolsAccelerationStructureCommandEncoder writeAccelerationStructureTraversalDepth:toBuffer:offset:];
-[MTLToolsAccelerationStructureCommandEncoder writeCompactedAccelerationStructureSize:toBuffer:offset:];
-[MTLToolsAccelerationStructureCommandEncoder writeCompactedAccelerationStructureSize:toBuffer:offset:sizeDataType:];
-[MTLToolsAccelerationStructureCommandEncoder writeDeserializedAccelerationStructureSize:serializedOffset:toBuffer:sizeBufferOffset:];
-[MTLToolsAccelerationStructureCommandEncoder writeDeserializedPrimitiveAccelerationStructureSizes:serializedOffset:toBuffer:sizesBufferOffset:];
-[MTLToolsAccelerationStructureCommandEncoder writeGenericBVHStructureOfAccelerationStructure:headerBuffer:headerBufferOffset:innerNodeBuffer:innerNodeBufferOffset:leafNodeBuffer:leafNodeBufferOffset:primitiveBuffer:primitiveBufferOffset:geometryBuffer:geometryOffset:instanceTransformBuffer:instanceTransformOffset:controlPointBuffer:controlPointBufferOffset:];
-[MTLToolsAccelerationStructureCommandEncoder writeGenericBVHStructureOfAccelerationStructure:into:];
-[MTLToolsAccelerationStructureCommandEncoder writeGenericBVHStructureSizesOfAccelerationStructure:into:];
-[MTLToolsAccelerationStructureCommandEncoder writeGenericBVHStructureSizesOfAccelerationStructure:toBuffer:sizesBufferOffset:];
-[MTLToolsAccelerationStructureCommandEncoder writeGeometryOfAccelerationStructure:toBuffer:geometryBufferOffset:];
-[MTLToolsAccelerationStructureCommandEncoder writeGeometrySizeOfAccelerationStructure:toBuffer:sizeBufferOffset:];
-[MTLToolsAccelerationStructureCommandEncoder writeSerializedAccelerationStructureSize:toBuffer:sizeBufferOffset:];
-[MTLToolsAccelerationStructureCommandEncoder initWithAccelerationStructureCommandEncoder:parent:descriptor:];
```
