# `_MTLIndirectArgumentBufferLayout`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 8 properties, 24 instance methods, 0 class methods

## Instance variables

```
^v _private;
```

## Properties

```
@property (TB,R,D) bufferLayoutMatchesFrontEndLayout;
@property (TQ,R,D) encodedLength;
@property (TQ,R,D) alignment;
@property (TI,R) hashValue;
@property (TI,R) hashOffset;
@property (TI,R) hashMask;
@property (TI,R) hashSignature;
@property (T@"<MTLDeviceSPI>",R,N) device;
```

## Instance methods

```
-[_MTLIndirectArgumentBufferLayout device];
-[_MTLIndirectArgumentBufferLayout init];
-[_MTLIndirectArgumentBufferLayout dealloc];
-[_MTLIndirectArgumentBufferLayout alignment];
-[_MTLIndirectArgumentBufferLayout encodedLength];
-[_MTLIndirectArgumentBufferLayout bufferLayoutForResourceAtIndex:];
-[_MTLIndirectArgumentBufferLayout bufferLayoutMatchesFrontEndLayout];
-[_MTLIndirectArgumentBufferLayout constantOffsetAtIndex:];
-[_MTLIndirectArgumentBufferLayout hashMask];
-[_MTLIndirectArgumentBufferLayout hashOffset];
-[_MTLIndirectArgumentBufferLayout hashSignature];
-[_MTLIndirectArgumentBufferLayout hashValue];
-[_MTLIndirectArgumentBufferLayout setStructType:withDevice:];
-[_MTLIndirectArgumentBufferLayout uniqueIdentifierForComputePipelineAtIndex:inIndirectArgumentBuffer:atOffset:];
-[_MTLIndirectArgumentBufferLayout uniqueIdentifierForDepthStencilStateAtIndex:inIndirectArgumentBuffer:atOffset:];
-[_MTLIndirectArgumentBufferLayout uniqueIdentifierForIndirectCommandBufferAtIndex:inIndirectArgumentBuffer:atOffset:];
-[_MTLIndirectArgumentBufferLayout uniqueIdentifierForInstanceAccelerationStructureAtIndex:inIndirectArgumentBuffer:atOffset:];
-[_MTLIndirectArgumentBufferLayout uniqueIdentifierForIntersectionFunctionTableAtIndex:inIndirectArgumentBuffer:atOffset:];
-[_MTLIndirectArgumentBufferLayout uniqueIdentifierForPrimitiveAccelerationStructureAtIndex:inIndirectArgumentBuffer:atOffset:];
-[_MTLIndirectArgumentBufferLayout uniqueIdentifierForRenderPipelineAtIndex:inIndirectArgumentBuffer:atOffset:];
-[_MTLIndirectArgumentBufferLayout uniqueIdentifierForSamplerAtIndex:inIndirectArgumentBuffer:atOffset:];
-[_MTLIndirectArgumentBufferLayout uniqueIdentifierForTextureAtIndex:inIndirectArgumentBuffer:atOffset:];
-[_MTLIndirectArgumentBufferLayout uniqueIdentifierForVisibleFunctionTableAtIndex:inIndirectArgumentBuffer:atOffset:];
-[_MTLIndirectArgumentBufferLayout virtualAddressForBufferAtIndex:inIndirectArgumentBuffer:atOffset:];
```
