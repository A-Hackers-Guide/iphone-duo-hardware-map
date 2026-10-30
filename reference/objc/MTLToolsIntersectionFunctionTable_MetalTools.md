# `MTLToolsIntersectionFunctionTable`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsResource`
- Protocols: `MTLIntersectionFunctionTableSPI`
- 1 instance variables, 19 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"<MTLBuffer>" _globalBuffer;
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
-[MTLToolsIntersectionFunctionTable setBuffers:offsets:withRange:];
-[MTLToolsIntersectionFunctionTable resourceIndex];
-[MTLToolsIntersectionFunctionTable setVisibleFunctionTables:withBufferRange:];
-[MTLToolsIntersectionFunctionTable setBuffer:offset:atIndex:];
-[MTLToolsIntersectionFunctionTable setVisibleFunctionTable:atBufferIndex:];
-[MTLToolsIntersectionFunctionTable globalBuffer];
-[MTLToolsIntersectionFunctionTable setGlobalBuffer:];
-[MTLToolsIntersectionFunctionTable dealloc];
-[MTLToolsIntersectionFunctionTable setFunction:atIndex:];
-[MTLToolsIntersectionFunctionTable uniqueIdentifier];
-[MTLToolsIntersectionFunctionTable gpuHandle];
-[MTLToolsIntersectionFunctionTable bufferAddressAtIndex:];
-[MTLToolsIntersectionFunctionTable setFunctions:withRange:];
-[MTLToolsIntersectionFunctionTable gpuResourceID];
-[MTLToolsIntersectionFunctionTable globalBufferOffset];
-[MTLToolsIntersectionFunctionTable setGlobalBufferOffset:];
-[MTLToolsIntersectionFunctionTable setOpaqueCurveIntersectionFunctionWithSignature:atIndex:];
-[MTLToolsIntersectionFunctionTable setOpaqueCurveIntersectionFunctionWithSignature:withRange:];
-[MTLToolsIntersectionFunctionTable setOpaqueTriangleIntersectionFunctionWithSignature:atIndex:];
-[MTLToolsIntersectionFunctionTable setOpaqueTriangleIntersectionFunctionWithSignature:withRange:];
```
