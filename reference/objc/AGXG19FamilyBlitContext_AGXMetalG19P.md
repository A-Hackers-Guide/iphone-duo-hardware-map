# `AGXG19FamilyBlitContext`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalBlitCommandEncoder`
- Protocols: `MTLBlitCommandEncoderSPI`
- 4 instance variables, 6 properties, 47 instance methods, 0 class methods

## Instance variables

```
^v _impl_compute;
^v _impl;
^v _ctx_compute;
B encodingLegacyBlit;
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
-[AGXG19FamilyBlitContext waitForFence:];
-[AGXG19FamilyBlitContext updateFence:];
-[AGXG19FamilyBlitContext sampleCountersInBuffer:atSampleIndex:withBarrier:];
-[AGXG19FamilyBlitContext initWithCommandBuffer:descriptor:];
-[AGXG19FamilyBlitContext endEncoding];
-[AGXG19FamilyBlitContext dealloc];
-[AGXG19FamilyBlitContext copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:];
-[AGXG19FamilyBlitContext optimizeContentsForCPUAccess:slice:level:];
-[AGXG19FamilyBlitContext optimizeIndirectCommandBuffer:withRange:];
-[AGXG19FamilyBlitContext optimizeContentsForGPUAccess:];
-[AGXG19FamilyBlitContext fillBuffer:range:pattern4:];
-[AGXG19FamilyBlitContext fillTexture:level:slice:region:bytes:length:];
-[AGXG19FamilyBlitContext resolveCounters:inRange:destinationBuffer:destinationOffset:];
-[AGXG19FamilyBlitContext copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:];
-[AGXG19FamilyBlitContext resetCommandsInBuffer:withRange:];
-[AGXG19FamilyBlitContext optimizeContentsForCPUAccess:];
-[AGXG19FamilyBlitContext optimizeContentsForGPUAccess:slice:level:];
-[AGXG19FamilyBlitContext copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:];
-[AGXG19FamilyBlitContext copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[AGXG19FamilyBlitContext generateMipmapsForTexture:];
-[AGXG19FamilyBlitContext updateTextureMappings:mode:regions:mipLevels:slices:numRegions:];
-[AGXG19FamilyBlitContext barrierAfterQueueStages:beforeStages:];
-[AGXG19FamilyBlitContext commandBatchIdOffset];
-[AGXG19FamilyBlitContext commandBatchIdRangeMin:max:];
-[AGXG19FamilyBlitContext copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[AGXG19FamilyBlitContext copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
-[AGXG19FamilyBlitContext copyFromTensor:sourceOrigin:sourceDimensions:sourcePlane:toTensor:destinationOrigin:destinationDimensions:destinationPlane:];
-[AGXG19FamilyBlitContext copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:];
-[AGXG19FamilyBlitContext copyFromTensor:sourceSlice:toTensor:destinationSlice:];
-[AGXG19FamilyBlitContext copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:];
-[AGXG19FamilyBlitContext copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:];
-[AGXG19FamilyBlitContext fillBuffer:range:value:];
-[AGXG19FamilyBlitContext filterCounterRangeWithFirstBatch:lastBatch:filterIndex:];
-[AGXG19FamilyBlitContext invalidateCompressedTexture:];
-[AGXG19FamilyBlitContext invalidateCompressedTexture:slice:level:];
-[AGXG19FamilyBlitContext moveTextureMappingsFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[AGXG19FamilyBlitContext optimizeContentsForTexture:readAccessPattern:readAccessor:];
-[AGXG19FamilyBlitContext optimizeContentsForTexture:readAccessPattern:readAccessor:slice:level:];
-[AGXG19FamilyBlitContext updateTextureMapping:mode:indirectBuffer:indirectBufferOffset:];
-[AGXG19FamilyBlitContext updateTextureMapping:mode:region:mipLevel:slice:];
-[AGXG19FamilyBlitContext getTextureAccessCounters:region:mipLevel:slice:resetCounters:countersBuffer:countersBufferOffset:];
-[AGXG19FamilyBlitContext resetTextureAccessCounters:region:mipLevel:slice:];
-[AGXG19FamilyBlitContext addProtectedContentBarrier];
-[AGXG19FamilyBlitContext copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
-[AGXG19FamilyBlitContext deferredEndEncoding];
-[AGXG19FamilyBlitContext reInitWithCommandBuffer:];
-[AGXG19FamilyBlitContext setMTLCounterSampleLocationWithBuffer:startIndex:endIndex:];
```
