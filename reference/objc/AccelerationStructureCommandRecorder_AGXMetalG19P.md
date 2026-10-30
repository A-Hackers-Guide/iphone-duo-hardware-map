# `AccelerationStructureCommandRecorder`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 3 properties, 48 instance methods, 0 class methods

## Instance variables

```
@"AccelerationStructureBuilder" _builderManager;
^v builder;
{vector<id<MTLResource>, std::allocator<id<MTLResource>>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} _readResources;
{vector<id<MTLResource>, std::allocator<id<MTLResource>>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} _writeResources;
B _checkedIn;
B _dependencyTracking;
@? _statisticsHandler;
{BVHBuilderSAHParameters="sahLeafCost"f"sahCostRatio"f"sahIntersectionCost"f"plocSearchRadius"f"plocSAHCostRatio"f"plocSAHIntersectionCost"f} _sahParameters;
```

## Properties

```
@property (TB,N,V_dependencyTracking) dependencyTracking;
@property (T{BVHBuilderSAHParameters=ffffff},N,V_sahParameters) sahParameters;
@property (T@?,C,N,V_statisticsHandler) statisticsHandler;
```

## Instance methods

```
-[AccelerationStructureCommandRecorder useResources:count:usage:];
-[AccelerationStructureCommandRecorder barrier];
-[AccelerationStructureCommandRecorder useResource:usage:];
-[AccelerationStructureCommandRecorder setStatisticsHandler:];
-[AccelerationStructureCommandRecorder initWithBuilder:];
-[AccelerationStructureCommandRecorder allocator];
-[AccelerationStructureCommandRecorder statisticsHandler];
-[AccelerationStructureCommandRecorder dealloc];
-[AccelerationStructureCommandRecorder deserializePrimitiveAccelerationStructure:fromBuffer:serializedBufferOffset:];
-[AccelerationStructureCommandRecorder serializePrimitiveAccelerationStructure:toBuffer:serializedBufferOffset:];
-[AccelerationStructureCommandRecorder writeAccelerationStructureTraversalDepth:toBuffer:offset:];
-[AccelerationStructureCommandRecorder writeDeserializedAccelerationStructureSize:serializedOffset:toBuffer:sizeBufferOffset:];
-[AccelerationStructureCommandRecorder writeGenericBVHStructureOfAccelerationStructure:into:];
-[AccelerationStructureCommandRecorder writeSerializedAccelerationStructureSize:toBuffer:sizeBufferOffset:];
-[AccelerationStructureCommandRecorder encode:];
-[AccelerationStructureCommandRecorder refitAccelerationStructure:cDescriptor:destination:scratchBufferBaseAddress:scratchBufferOffset:scratchBufferLength:refitFlags:];
-[AccelerationStructureCommandRecorder writeDeserializedAccelerationStructureSize:serializedOffset:serializedLength:toBufferAddress:sizeBufferOffset:sizeBufferLength:];
-[AccelerationStructureCommandRecorder buildAccelerationStructure:cDescriptor:scratchBufferBaseAddress:scratchBufferOffset:scratchBufferLength:];
-[AccelerationStructureCommandRecorder buildAccelerationStructure:descriptor:buildAlgorithm:scratchBufferBaseAddress:scratchBufferOffset:scratchBufferLength:];
-[AccelerationStructureCommandRecorder buildAccelerationStructure:descriptor:scratchBufferBaseAddress:scratchBufferOffset:scratchBufferLength:];
-[AccelerationStructureCommandRecorder checkedIn];
-[AccelerationStructureCommandRecorder copyAccelerationStructure:destinationAccelerationStructure:];
-[AccelerationStructureCommandRecorder copyAndCompactAccelerationStructure:destinationAccelerationStructure:];
-[AccelerationStructureCommandRecorder dependencyTracking];
-[AccelerationStructureCommandRecorder deserializeInstanceAccelerationStructure:referencedAccelerationStructures:fromBuffer:serializedBufferOffset:];
-[AccelerationStructureCommandRecorder deserializeInstanceAccelerationStructure:referencedAccelerationStructures:serializedBufferAddress:serializedBufferOffset:serializedBufferLength:];
-[AccelerationStructureCommandRecorder deserializePrimitiveAccelerationStructure:serializedBufferAddress:serializedBufferOffset:serializedBufferLength:];
-[AccelerationStructureCommandRecorder dumpAccelerationStructure:];
-[AccelerationStructureCommandRecorder hasSAHParametersSet];
-[AccelerationStructureCommandRecorder refitAccelerationStructure:cDescriptor:destination:scratchBufferBaseAddress:scratchBufferOffset:scratchBufferLength:];
-[AccelerationStructureCommandRecorder refitAccelerationStructure:descriptor:destination:scratchBufferBaseAddress:scratchBufferOffset:scratchBufferLength:];
-[AccelerationStructureCommandRecorder refitAccelerationStructure:descriptor:destination:scratchBufferBaseAddress:scratchBufferOffset:scratchBufferLength:refitFlags:];
-[AccelerationStructureCommandRecorder sahParameters];
-[AccelerationStructureCommandRecorder serializeInstanceAccelerationStructure:referencedAccelerationStructures:toBuffer:serializedBufferOffset:];
-[AccelerationStructureCommandRecorder serializeInstanceAccelerationStructure:referencedAccelerationStructures:toBufferAddress:serializedBufferOffset:serializedBufferLength:];
-[AccelerationStructureCommandRecorder serializeInstanceAccelerationStructure:toBuffer:serializedBufferOffset:];
-[AccelerationStructureCommandRecorder serializeInstanceAccelerationStructure:toBufferAddress:serializedBufferOffset:serializedBufferLength:];
-[AccelerationStructureCommandRecorder serializePrimitiveAccelerationStructure:serializedBufferAddress:serializedBufferOffset:serializedBufferLength:];
-[AccelerationStructureCommandRecorder setCheckedIn:];
-[AccelerationStructureCommandRecorder setDependencyTracking:];
-[AccelerationStructureCommandRecorder setSahParameters:];
-[AccelerationStructureCommandRecorder writeAccelerationStructureSerializationData:toBufferAddress:bufferOffset:];
-[AccelerationStructureCommandRecorder writeAccelerationStructureTraversalDepth:toBufferAddress:bufferOffset:bufferLength:];
-[AccelerationStructureCommandRecorder writeCompactedSize:compactedSizeBufferAddress:compactedSizeBufferOffset:compactedSizeBufferLength:];
-[AccelerationStructureCommandRecorder writeGenericBVHStructureOfAccelerationStructure:headerBuffer:headerBufferOffset:innerNodeBuffer:innerNodeBufferOffset:leafNodeBuffer:leafNodeBufferOffset:primitiveBuffer:primitiveBufferOffset:geometryBuffer:geometryBufferOffset:instanceTransformBuffer:instanceTransformOffset:perPrimitiveDataBuffer:perPrimitiveDataBufferOffset:controlPointBuffer:controlPointBufferOffset:version:];
-[AccelerationStructureCommandRecorder writeGenericBVHStructureSizesOfAccelerationStructure:toBuffer:sizesBufferOffset:version:];
-[AccelerationStructureCommandRecorder writeGenericBVHStructureSizesOfAccelerationStructure:toBufferAddress:sizesBufferOffset:sizesBufferLength:version:];
-[AccelerationStructureCommandRecorder writeSerializedAccelerationStructureSize:toBufferAddress:sizeBufferOffset:sizeBufferLength:];
```
