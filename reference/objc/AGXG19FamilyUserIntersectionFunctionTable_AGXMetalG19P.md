# `AGXG19FamilyUserIntersectionFunctionTable`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalIntersectionFunctionTable`
- Protocols: `MTLIntersectionFunctionTableSPI`
- 3 instance variables, 19 properties, 19 instance methods, 0 class methods

## Instance variables

```
^v _impl;
@ _pipelineState;
i _stage;
```

## Properties

```
@property (TQ,?,R,N) resourceIndex;
@property (TQ,?,R) uniqueIdentifier;
@property (T@"<MTLBuffer>",?,&,N) globalBuffer;
@property (TQ,?,N) globalBufferOffset;
@property (TQ,R) gpuHandle;
@property (T{MTLResourceID=Q},R) gpuResourceID;
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
-[AGXG19FamilyUserIntersectionFunctionTable setBuffers:offsets:withRange:];
-[AGXG19FamilyUserIntersectionFunctionTable resourceIndex];
-[AGXG19FamilyUserIntersectionFunctionTable setVisibleFunctionTables:withBufferRange:];
-[AGXG19FamilyUserIntersectionFunctionTable setBuffer:offset:atIndex:];
-[AGXG19FamilyUserIntersectionFunctionTable setVisibleFunctionTable:atBufferIndex:];
-[AGXG19FamilyUserIntersectionFunctionTable dealloc];
-[AGXG19FamilyUserIntersectionFunctionTable setFunction:atIndex:];
-[AGXG19FamilyUserIntersectionFunctionTable uniqueIdentifier];
-[AGXG19FamilyUserIntersectionFunctionTable gpuHandle];
-[AGXG19FamilyUserIntersectionFunctionTable bufferAddressAtIndex:];
-[AGXG19FamilyUserIntersectionFunctionTable setFunctions:withRange:];
-[AGXG19FamilyUserIntersectionFunctionTable gpuResourceID];
-[AGXG19FamilyUserIntersectionFunctionTable setOpaqueCurveIntersectionFunctionWithSignature:atIndex:];
-[AGXG19FamilyUserIntersectionFunctionTable setOpaqueCurveIntersectionFunctionWithSignature:withRange:];
-[AGXG19FamilyUserIntersectionFunctionTable setOpaqueTriangleIntersectionFunctionWithSignature:atIndex:];
-[AGXG19FamilyUserIntersectionFunctionTable setOpaqueTriangleIntersectionFunctionWithSignature:withRange:];
-[AGXG19FamilyUserIntersectionFunctionTable clone:cloneTableHeap:slProgramsTracker:];
-[AGXG19FamilyUserIntersectionFunctionTable initWithDevice:numTableFnSlots:pipelineSets:pipeline:stage:resourceIndex:];
-[AGXG19FamilyUserIntersectionFunctionTable initWithDevice:originalTable:cloneTableHeap:slProgramsTracker:];
```
