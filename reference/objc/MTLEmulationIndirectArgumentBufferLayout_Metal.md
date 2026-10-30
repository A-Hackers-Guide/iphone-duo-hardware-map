# `MTLEmulationIndirectArgumentBufferLayout`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLIndirectArgumentBufferLayout`
- 18 instance variables, 1 properties, 24 instance methods, 0 class methods

## Instance variables

```
Q _stride;
Q _alignment;
^v _bufferIndices;
^v _textureIndices;
^v _samplerIndices;
^v _constantIndices;
^v _constantOffsets;
^v _visibleFunctionTableIndices;
^v _intersectionFunctionTableIndices;
^v _primitiveAccelerationStructureIndices;
^v _instanceAccelerationStructureIndices;
Q _bufferOffset;
Q _textureOffset;
Q _samplerOffset;
Q _visibleFunctionTableOffset;
Q _intersectionFunctionTableOffset;
Q _primitiveAccelerationStructureOffset;
Q _instanceAccelerationStructureOffset;
```

## Properties

```
@property (TQ,R,N,V_stride) stride;
```

## Instance methods

```
-[MTLEmulationIndirectArgumentBufferLayout dealloc];
-[MTLEmulationIndirectArgumentBufferLayout alignment];
-[MTLEmulationIndirectArgumentBufferLayout stride];
-[MTLEmulationIndirectArgumentBufferLayout encodedLength];
-[MTLEmulationIndirectArgumentBufferLayout bufferLayoutMatchesFrontEndLayout];
-[MTLEmulationIndirectArgumentBufferLayout constantOffsetAtIndex:];
-[MTLEmulationIndirectArgumentBufferLayout hashMask];
-[MTLEmulationIndirectArgumentBufferLayout hashOffset];
-[MTLEmulationIndirectArgumentBufferLayout hashSignature];
-[MTLEmulationIndirectArgumentBufferLayout hashValue];
-[MTLEmulationIndirectArgumentBufferLayout initWithStructType:];
-[MTLEmulationIndirectArgumentBufferLayout offsetForBuffer:];
-[MTLEmulationIndirectArgumentBufferLayout offsetForConstant:];
-[MTLEmulationIndirectArgumentBufferLayout offsetForInstanceAccelerationStructure:];
-[MTLEmulationIndirectArgumentBufferLayout offsetForIntersectionFunctionTable:];
-[MTLEmulationIndirectArgumentBufferLayout offsetForPrimitiveAccelerationStructure:];
-[MTLEmulationIndirectArgumentBufferLayout offsetForSampler:];
-[MTLEmulationIndirectArgumentBufferLayout offsetForTexture:];
-[MTLEmulationIndirectArgumentBufferLayout offsetForVisibleFunctionTable:];
-[MTLEmulationIndirectArgumentBufferLayout uniqueIdentifierForComputePipelineAtIndex:inIndirectArgumentBuffer:atOffset:];
-[MTLEmulationIndirectArgumentBufferLayout uniqueIdentifierForRenderPipelineAtIndex:inIndirectArgumentBuffer:atOffset:];
-[MTLEmulationIndirectArgumentBufferLayout uniqueIdentifierForSamplerAtIndex:inIndirectArgumentBuffer:atOffset:];
-[MTLEmulationIndirectArgumentBufferLayout uniqueIdentifierForTextureAtIndex:inIndirectArgumentBuffer:atOffset:];
-[MTLEmulationIndirectArgumentBufferLayout virtualAddressForBufferAtIndex:inIndirectArgumentBuffer:atOffset:];
```
