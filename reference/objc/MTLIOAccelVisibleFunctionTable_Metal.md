# `MTLIOAccelVisibleFunctionTable`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLIOAccelResource`
- Protocols: `MTLVisibleFunctionTableSPI`
- 0 instance variables, 20 properties, 16 instance methods, 0 class methods

## Properties

```
@property (T@"<MTLBuffer>",&,N) globalBuffer;
@property (TQ,N) globalBufferOffset;
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (TQ,R,N) gpuAddress;
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
-[MTLIOAccelVisibleFunctionTable setBuffers:offsets:withRange:];
-[MTLIOAccelVisibleFunctionTable setValue:atIndex:];
-[MTLIOAccelVisibleFunctionTable setVisibleFunctionTables:withBufferRange:];
-[MTLIOAccelVisibleFunctionTable setBuffer:offset:atIndex:];
-[MTLIOAccelVisibleFunctionTable setVisibleFunctionTable:atBufferIndex:];
-[MTLIOAccelVisibleFunctionTable globalBuffer];
-[MTLIOAccelVisibleFunctionTable setGlobalBuffer:];
-[MTLIOAccelVisibleFunctionTable gpuAddress];
-[MTLIOAccelVisibleFunctionTable setFunction:atIndex:];
-[MTLIOAccelVisibleFunctionTable setValue:withRange:];
-[MTLIOAccelVisibleFunctionTable gpuHandle];
-[MTLIOAccelVisibleFunctionTable bufferAddressAtIndex:];
-[MTLIOAccelVisibleFunctionTable setFunctions:withRange:];
-[MTLIOAccelVisibleFunctionTable gpuResourceID];
-[MTLIOAccelVisibleFunctionTable globalBufferOffset];
-[MTLIOAccelVisibleFunctionTable setGlobalBufferOffset:];
```
