# `MTLIntersectionFunctionTableSPI` (protocol)

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLIntersectionFunctionTable`
- 0 instance variables, 5 properties, 8 instance methods, 0 class methods

## Properties

```
@property (TQ,?,R,N) resourceIndex;
@property (TQ,?,R) uniqueIdentifier;
@property (T@"<MTLBuffer>",?,&,N) globalBuffer;
@property (TQ,?,N) globalBufferOffset;
@property (TQ,R) gpuHandle;
```

## Instance methods

```
-[MTLIntersectionFunctionTableSPI gpuHandle];
-[MTLIntersectionFunctionTableSPI bufferAddressAtIndex:];
-[MTLIntersectionFunctionTableSPI resourceIndex];
-[MTLIntersectionFunctionTableSPI globalBuffer];
-[MTLIntersectionFunctionTableSPI setGlobalBuffer:];
-[MTLIntersectionFunctionTableSPI uniqueIdentifier];
-[MTLIntersectionFunctionTableSPI globalBufferOffset];
-[MTLIntersectionFunctionTableSPI setGlobalBufferOffset:];
```
