# `MTLIntersectionFunctionTableSPI` (protocol)

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
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
