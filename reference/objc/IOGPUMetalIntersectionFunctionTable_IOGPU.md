# `IOGPUMetalIntersectionFunctionTable`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalResource`
- Protocols: `MTLIntersectionFunctionTableSPI`
- 1 instance variables, 20 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"IOGPUMetalResource<MTLVisibleFunctionTableSPI>" _visibleFunctionTable;
```

## Properties

```
@property (T@"<MTLBuffer>",&,N) globalBuffer;
@property (TQ,N) globalBufferOffset;
@property (TQ,R,N) resourceIndex;
@property (TQ,R) uniqueIdentifier;
@property (TQ,R,N) gpuHandle;
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (T@"IOGPUMetalResource<MTLVisibleFunctionTableSPI>",R,N) visibleFunctionTable;
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
-[IOGPUMetalIntersectionFunctionTable setBuffers:offsets:withRange:];
-[IOGPUMetalIntersectionFunctionTable resourceIndex];
-[IOGPUMetalIntersectionFunctionTable setVisibleFunctionTables:withBufferRange:];
-[IOGPUMetalIntersectionFunctionTable setBuffer:offset:atIndex:];
-[IOGPUMetalIntersectionFunctionTable setVisibleFunctionTable:atBufferIndex:];
-[IOGPUMetalIntersectionFunctionTable globalBuffer];
-[IOGPUMetalIntersectionFunctionTable setGlobalBuffer:];
-[IOGPUMetalIntersectionFunctionTable dealloc];
-[IOGPUMetalIntersectionFunctionTable setFunction:atIndex:];
-[IOGPUMetalIntersectionFunctionTable uniqueIdentifier];
-[IOGPUMetalIntersectionFunctionTable gpuHandle];
-[IOGPUMetalIntersectionFunctionTable bufferAddressAtIndex:];
-[IOGPUMetalIntersectionFunctionTable setFunctions:withRange:];
-[IOGPUMetalIntersectionFunctionTable gpuResourceID];
-[IOGPUMetalIntersectionFunctionTable globalBufferOffset];
-[IOGPUMetalIntersectionFunctionTable setGlobalBufferOffset:];
-[IOGPUMetalIntersectionFunctionTable initWithVisibleFunctionTable:];
-[IOGPUMetalIntersectionFunctionTable setOpaqueCurveIntersectionFunctionWithSignature:atIndex:];
-[IOGPUMetalIntersectionFunctionTable setOpaqueCurveIntersectionFunctionWithSignature:withRange:];
-[IOGPUMetalIntersectionFunctionTable setOpaqueTriangleIntersectionFunctionWithSignature:atIndex:];
-[IOGPUMetalIntersectionFunctionTable setOpaqueTriangleIntersectionFunctionWithSignature:withRange:];
-[IOGPUMetalIntersectionFunctionTable visibleFunctionTable];
```
