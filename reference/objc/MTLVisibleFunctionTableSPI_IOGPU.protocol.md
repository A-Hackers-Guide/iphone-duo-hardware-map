# `MTLVisibleFunctionTableSPI` (protocol)

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLVisibleFunctionTable`
- 0 instance variables, 6 properties, 15 instance methods, 0 class methods

## Properties

```
@property (TQ,?,R,N) resourceIndex;
@property (TQ,?,R) uniqueIdentifier;
@property (T@"<MTLBuffer>",?,&,N) globalBuffer;
@property (TQ,?,N) globalBufferOffset;
@property (TQ,R) gpuHandle;
@property (TQ,R,N) gpuAddress;
```

## Instance methods

```
-[MTLVisibleFunctionTableSPI setBuffers:offsets:withRange:];
-[MTLVisibleFunctionTableSPI setValue:atIndex:];
-[MTLVisibleFunctionTableSPI setVisibleFunctionTables:withBufferRange:];
-[MTLVisibleFunctionTableSPI setBuffer:offset:atIndex:];
-[MTLVisibleFunctionTableSPI setVisibleFunctionTable:atBufferIndex:];
-[MTLVisibleFunctionTableSPI gpuAddress];
-[MTLVisibleFunctionTableSPI setValue:withRange:];
-[MTLVisibleFunctionTableSPI gpuHandle];
-[MTLVisibleFunctionTableSPI bufferAddressAtIndex:];
-[MTLVisibleFunctionTableSPI resourceIndex];
-[MTLVisibleFunctionTableSPI globalBuffer];
-[MTLVisibleFunctionTableSPI setGlobalBuffer:];
-[MTLVisibleFunctionTableSPI uniqueIdentifier];
-[MTLVisibleFunctionTableSPI globalBufferOffset];
-[MTLVisibleFunctionTableSPI setGlobalBufferOffset:];
```
