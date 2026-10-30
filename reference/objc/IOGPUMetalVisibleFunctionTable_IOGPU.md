# `IOGPUMetalVisibleFunctionTable`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalBuffer`
- Protocols: `MTLVisibleFunctionTableSPI`
- 0 instance variables, 20 properties, 16 instance methods, 0 class methods

## Properties

```
@property (T@"<MTLBuffer>",&,N) globalBuffer;
@property (TQ,N) globalBufferOffset;
@property (TQ,R,N) gpuHandle;
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (TQ,R,N) gpuAddress;
@property (TQ,?,R,N) resourceIndex;
@property (TQ,?,R) uniqueIdentifier;
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
-[IOGPUMetalVisibleFunctionTable setBuffers:offsets:withRange:];
-[IOGPUMetalVisibleFunctionTable setValue:atIndex:];
-[IOGPUMetalVisibleFunctionTable setVisibleFunctionTables:withBufferRange:];
-[IOGPUMetalVisibleFunctionTable setBuffer:offset:atIndex:];
-[IOGPUMetalVisibleFunctionTable setVisibleFunctionTable:atBufferIndex:];
-[IOGPUMetalVisibleFunctionTable globalBuffer];
-[IOGPUMetalVisibleFunctionTable setGlobalBuffer:];
-[IOGPUMetalVisibleFunctionTable gpuAddress];
-[IOGPUMetalVisibleFunctionTable setFunction:atIndex:];
-[IOGPUMetalVisibleFunctionTable setValue:withRange:];
-[IOGPUMetalVisibleFunctionTable gpuHandle];
-[IOGPUMetalVisibleFunctionTable bufferAddressAtIndex:];
-[IOGPUMetalVisibleFunctionTable setFunctions:withRange:];
-[IOGPUMetalVisibleFunctionTable gpuResourceID];
-[IOGPUMetalVisibleFunctionTable globalBufferOffset];
-[IOGPUMetalVisibleFunctionTable setGlobalBufferOffset:];
```
