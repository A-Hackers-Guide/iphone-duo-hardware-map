# `MTLCountersTraceBlitCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLCountersTraceCommandEncoder`
- 0 instance variables, 0 properties, 26 instance methods, 0 class methods

## Instance methods

```
-[MTLCountersTraceBlitCommandEncoder waitForFence:];
-[MTLCountersTraceBlitCommandEncoder updateFence:];
-[MTLCountersTraceBlitCommandEncoder synchronizeResource:];
-[MTLCountersTraceBlitCommandEncoder copyFromTexture:toTexture:];
-[MTLCountersTraceBlitCommandEncoder synchronizeTexture:slice:level:];
-[MTLCountersTraceBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:];
-[MTLCountersTraceBlitCommandEncoder optimizeContentsForCPUAccess:slice:level:];
-[MTLCountersTraceBlitCommandEncoder fillTexture:level:slice:region:color:];
-[MTLCountersTraceBlitCommandEncoder optimizeContentsForGPUAccess:];
-[MTLCountersTraceBlitCommandEncoder fillBuffer:range:pattern4:];
-[MTLCountersTraceBlitCommandEncoder init:];
-[MTLCountersTraceBlitCommandEncoder fillTexture:level:slice:region:bytes:length:];
-[MTLCountersTraceBlitCommandEncoder fillTexture:level:slice:region:color:pixelFormat:];
-[MTLCountersTraceBlitCommandEncoder optimizeContentsForCPUAccess:];
-[MTLCountersTraceBlitCommandEncoder optimizeContentsForGPUAccess:slice:level:];
-[MTLCountersTraceBlitCommandEncoder copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:];
-[MTLCountersTraceBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTLCountersTraceBlitCommandEncoder generateMipmapsForTexture:];
-[MTLCountersTraceBlitCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTLCountersTraceBlitCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
-[MTLCountersTraceBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:];
-[MTLCountersTraceBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:];
-[MTLCountersTraceBlitCommandEncoder fillBuffer:range:value:];
-[MTLCountersTraceBlitCommandEncoder getTextureAccessCounters:region:mipLevel:slice:resetCounters:countersBuffer:countersBufferOffset:];
-[MTLCountersTraceBlitCommandEncoder resetTextureAccessCounters:region:mipLevel:slice:];
-[MTLCountersTraceBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
```
