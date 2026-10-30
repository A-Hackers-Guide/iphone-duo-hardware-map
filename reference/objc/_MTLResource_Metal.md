# `_MTLResource`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLAllocation`
- 0 instance variables, 9 properties, 13 instance methods, 0 class methods

## Properties

```
@property (TQ,R) allocationID;
@property (Tq,R) compressionType;
@property (TQ,R,N) compressionFootprint;
@property (Tf,R) minLOD;
@property (TQ,R,N) colorSpaceConversionMatrix;
@property (TQ,R,N) accelerationStructureUniqueIdentifier;
@property (Tq,R) sparseBufferTier;
@property (Tq,R) sparseTextureTier;
@property (TQ,R) bufferOffset;
```

## Instance methods

```
-[_MTLResource compressionType];
-[_MTLResource init];
-[_MTLResource compressionFootprint];
-[_MTLResource newTextureViewWithDescriptor:];
-[_MTLResource colorSpaceConversionMatrix];
-[_MTLResource bufferOffset];
-[_MTLResource minLOD];
-[_MTLResource sparseTextureTier];
-[_MTLResource newTensorWithDescriptor:offset:error:];
-[_MTLResource sparseBufferTier];
-[_MTLResource accelerationStructureUniqueIdentifier];
-[_MTLResource allocationID];
-[_MTLResource compressionMetadata];
```
