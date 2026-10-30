# `MTLDebugBlitCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsBlitCommandEncoder`
- 5 instance variables, 0 properties, 44 instance methods, 0 class methods

## Instance variables

```
B canDealloc;
B canEndEncoding;
B hasEndEncoding;
{deque<id, std::allocator<id>>="__map_"{__split_buffer<id *, std::allocator<id *>>="__first_"^^@"__begin_"^^@"__end_"^^@""{?="__cap_"^^@}}"__start_"Q""{?="__size_"Q}} updatedFences;
@"MTLDebugCommandBuffer" _commandBuffer;
```

## Instance methods

```
-[MTLDebugBlitCommandEncoder waitForFence:];
-[MTLDebugBlitCommandEncoder updateFence:];
-[MTLDebugBlitCommandEncoder sampleCountersInBuffer:atSampleIndex:withBarrier:];
-[MTLDebugBlitCommandEncoder endEncoding];
-[MTLDebugBlitCommandEncoder copyFromTexture:toTexture:];
-[MTLDebugBlitCommandEncoder dealloc];
-[MTLDebugBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:];
-[MTLDebugBlitCommandEncoder optimizeContentsForCPUAccess:slice:level:];
-[MTLDebugBlitCommandEncoder optimizeIndirectCommandBuffer:withRange:];
-[MTLDebugBlitCommandEncoder fillTexture:level:slice:region:color:];
-[MTLDebugBlitCommandEncoder optimizeContentsForGPUAccess:];
-[MTLDebugBlitCommandEncoder fillBuffer:range:pattern4:];
-[MTLDebugBlitCommandEncoder fillTexture:level:slice:region:bytes:length:];
-[MTLDebugBlitCommandEncoder resolveCounters:inRange:destinationBuffer:destinationOffset:];
-[MTLDebugBlitCommandEncoder fillTexture:level:slice:region:color:pixelFormat:];
-[MTLDebugBlitCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:];
-[MTLDebugBlitCommandEncoder resetCommandsInBuffer:withRange:];
-[MTLDebugBlitCommandEncoder optimizeContentsForCPUAccess:];
-[MTLDebugBlitCommandEncoder optimizeContentsForGPUAccess:slice:level:];
-[MTLDebugBlitCommandEncoder copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:];
-[MTLDebugBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTLDebugBlitCommandEncoder generateMipmapsForTexture:];
-[MTLDebugBlitCommandEncoder barrierAfterQueueStages:beforeStages:];
-[MTLDebugBlitCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTLDebugBlitCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
-[MTLDebugBlitCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:sourcePlane:toTensor:destinationOrigin:destinationDimensions:destinationPlane:];
-[MTLDebugBlitCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:];
-[MTLDebugBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:];
-[MTLDebugBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:];
-[MTLDebugBlitCommandEncoder fillBuffer:range:value:];
-[MTLDebugBlitCommandEncoder filterCounterRangeWithFirstBatch:lastBatch:filterIndex:];
-[MTLDebugBlitCommandEncoder invalidateCompressedTexture:];
-[MTLDebugBlitCommandEncoder invalidateCompressedTexture:slice:level:];
-[MTLDebugBlitCommandEncoder getTextureAccessCounters:region:mipLevel:slice:resetCounters:countersBuffer:countersBufferOffset:];
-[MTLDebugBlitCommandEncoder resetTextureAccessCounters:region:mipLevel:slice:];
-[MTLDebugBlitCommandEncoder _setDefaults];
-[MTLDebugBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
-[MTLDebugBlitCommandEncoder initWithBlitCommandEncoder:commandBuffer:descriptor:];
-[MTLDebugBlitCommandEncoder internalValidateCopyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
-[MTLDebugBlitCommandEncoder validateCopyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
-[MTLDebugBlitCommandEncoder validateCopyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:];
-[MTLDebugBlitCommandEncoder validateCopyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:move:];
-[MTLDebugBlitCommandEncoder validateCopyFromTexture:sourceSlice:sourceLevel:sourceSize:toTexture:destinationSlice:destinationLevel:options:sliceCount:levelCount:];
-[MTLDebugBlitCommandEncoder validateTextureAccess:region:mipLevel:slice:];
```
