# `AGXG19FamilyResourceStateContext`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalResourceStateCommandEncoder`
- Protocols: `MTLResourceStateCommandEncoderSPI`
- 2 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
^v _impl;
^v _ctx_common;
```

## Properties

```
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AGXG19FamilyResourceStateContext waitForFence:];
-[AGXG19FamilyResourceStateContext updateFence:];
-[AGXG19FamilyResourceStateContext initWithCommandBuffer:descriptor:];
-[AGXG19FamilyResourceStateContext endEncoding];
-[AGXG19FamilyResourceStateContext updateTextureMappings:mode:regions:mipLevels:slices:numRegions:];
-[AGXG19FamilyResourceStateContext barrierAfterQueueStages:beforeStages:];
-[AGXG19FamilyResourceStateContext initWithCommandBuffer:];
-[AGXG19FamilyResourceStateContext moveTextureMappingsFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[AGXG19FamilyResourceStateContext updateTextureMapping:mode:indirectBuffer:indirectBufferOffset:];
-[AGXG19FamilyResourceStateContext updateTextureMapping:mode:region:mipLevel:slice:];
-[AGXG19FamilyResourceStateContext updateTextureMapping:mode:region:mipLevel:slice:heap:rangeOffset:];
```
