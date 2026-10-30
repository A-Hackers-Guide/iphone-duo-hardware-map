# `MTLVisibleFunctionTableSPI` (protocol)

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
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
