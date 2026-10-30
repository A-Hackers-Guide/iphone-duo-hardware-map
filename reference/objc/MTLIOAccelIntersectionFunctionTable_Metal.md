# `MTLIOAccelIntersectionFunctionTable`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLIOAccelResource`
- Protocols: `MTLIntersectionFunctionTableSPI`
- 1 instance variables, 20 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"MTLIOAccelVisibleFunctionTable<MTLVisibleFunctionTableSPI>" _visibleFunctionTable;
```

## Properties

```
@property (T@"<MTLBuffer>",&,N) globalBuffer;
@property (TQ,N) globalBufferOffset;
@property (T@"MTLIOAccelVisibleFunctionTable<MTLVisibleFunctionTableSPI>",R,N) visibleFunctionTable;
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (TQ,?,R,N) resourceIndex;
@property (TQ,?,R) uniqueIdentifier;
@property (TQ,R) gpuHandle;
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
-[MTLIOAccelIntersectionFunctionTable setBuffers:offsets:withRange:];
-[MTLIOAccelIntersectionFunctionTable resourceIndex];
-[MTLIOAccelIntersectionFunctionTable setVisibleFunctionTables:withBufferRange:];
-[MTLIOAccelIntersectionFunctionTable setBuffer:offset:atIndex:];
-[MTLIOAccelIntersectionFunctionTable setVisibleFunctionTable:atBufferIndex:];
-[MTLIOAccelIntersectionFunctionTable globalBuffer];
-[MTLIOAccelIntersectionFunctionTable setGlobalBuffer:];
-[MTLIOAccelIntersectionFunctionTable dealloc];
-[MTLIOAccelIntersectionFunctionTable setFunction:atIndex:];
-[MTLIOAccelIntersectionFunctionTable uniqueIdentifier];
-[MTLIOAccelIntersectionFunctionTable gpuHandle];
-[MTLIOAccelIntersectionFunctionTable bufferAddressAtIndex:];
-[MTLIOAccelIntersectionFunctionTable setFunctions:withRange:];
-[MTLIOAccelIntersectionFunctionTable gpuResourceID];
-[MTLIOAccelIntersectionFunctionTable globalBufferOffset];
-[MTLIOAccelIntersectionFunctionTable setGlobalBufferOffset:];
-[MTLIOAccelIntersectionFunctionTable initWithVisibleFunctionTable:];
-[MTLIOAccelIntersectionFunctionTable setOpaqueCurveIntersectionFunctionWithSignature:atIndex:];
-[MTLIOAccelIntersectionFunctionTable setOpaqueCurveIntersectionFunctionWithSignature:withRange:];
-[MTLIOAccelIntersectionFunctionTable setOpaqueTriangleIntersectionFunctionWithSignature:atIndex:];
-[MTLIOAccelIntersectionFunctionTable setOpaqueTriangleIntersectionFunctionWithSignature:withRange:];
-[MTLIOAccelIntersectionFunctionTable visibleFunctionTable];
```
