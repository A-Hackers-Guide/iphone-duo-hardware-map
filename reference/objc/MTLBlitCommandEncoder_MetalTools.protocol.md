# `MTLBlitCommandEncoder` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLCommandEncoder`
- 0 instance variables, 0 properties, 27 instance methods, 0 class methods

## Instance methods

```
-[MTLBlitCommandEncoder waitForFence:];
-[MTLBlitCommandEncoder updateFence:];
-[MTLBlitCommandEncoder sampleCountersInBuffer:atSampleIndex:withBarrier:];
-[MTLBlitCommandEncoder synchronizeResource:];
-[MTLBlitCommandEncoder copyFromTexture:toTexture:];
-[MTLBlitCommandEncoder synchronizeTexture:slice:level:];
-[MTLBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:];
-[MTLBlitCommandEncoder optimizeContentsForCPUAccess:slice:level:];
-[MTLBlitCommandEncoder optimizeIndirectCommandBuffer:withRange:];
-[MTLBlitCommandEncoder optimizeContentsForGPUAccess:];
-[MTLBlitCommandEncoder resolveCounters:inRange:destinationBuffer:destinationOffset:];
-[MTLBlitCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:];
-[MTLBlitCommandEncoder resetCommandsInBuffer:withRange:];
-[MTLBlitCommandEncoder optimizeContentsForCPUAccess:];
-[MTLBlitCommandEncoder optimizeContentsForGPUAccess:slice:level:];
-[MTLBlitCommandEncoder copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:];
-[MTLBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTLBlitCommandEncoder generateMipmapsForTexture:];
-[MTLBlitCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTLBlitCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
-[MTLBlitCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:sourcePlane:toTensor:destinationOrigin:destinationDimensions:destinationPlane:];
-[MTLBlitCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:];
-[MTLBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:];
-[MTLBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:];
-[MTLBlitCommandEncoder fillBuffer:range:value:];
-[MTLBlitCommandEncoder getTextureAccessCounters:region:mipLevel:slice:resetCounters:countersBuffer:countersBufferOffset:];
-[MTLBlitCommandEncoder resetTextureAccessCounters:region:mipLevel:slice:];
```
