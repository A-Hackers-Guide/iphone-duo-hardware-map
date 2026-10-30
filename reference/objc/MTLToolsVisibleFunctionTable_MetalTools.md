# `MTLToolsVisibleFunctionTable`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsResource`
- Protocols: `MTLVisibleFunctionTableSPI`
- 0 instance variables, 20 properties, 14 instance methods, 0 class methods

## Properties

```
@property (TQ,?,R,N) resourceIndex;
@property (TQ,?,R) uniqueIdentifier;
@property (T@"<MTLBuffer>",?,&,N) globalBuffer;
@property (TQ,?,N) globalBufferOffset;
@property (TQ,R) gpuHandle;
@property (TQ,R,N) gpuAddress;
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
-[MTLToolsVisibleFunctionTable setBuffers:offsets:withRange:];
-[MTLToolsVisibleFunctionTable setValue:atIndex:];
-[MTLToolsVisibleFunctionTable resourceIndex];
-[MTLToolsVisibleFunctionTable setVisibleFunctionTables:withBufferRange:];
-[MTLToolsVisibleFunctionTable setBuffer:offset:atIndex:];
-[MTLToolsVisibleFunctionTable setVisibleFunctionTable:atBufferIndex:];
-[MTLToolsVisibleFunctionTable gpuAddress];
-[MTLToolsVisibleFunctionTable setFunction:atIndex:];
-[MTLToolsVisibleFunctionTable uniqueIdentifier];
-[MTLToolsVisibleFunctionTable setValue:withRange:];
-[MTLToolsVisibleFunctionTable gpuHandle];
-[MTLToolsVisibleFunctionTable bufferAddressAtIndex:];
-[MTLToolsVisibleFunctionTable setFunctions:withRange:];
-[MTLToolsVisibleFunctionTable gpuResourceID];
```
