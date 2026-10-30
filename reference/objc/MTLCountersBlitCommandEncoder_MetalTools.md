# `MTLCountersBlitCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsBlitCommandEncoder`
- 1 instance variables, 0 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"MTLCountersTraceBlitCommandEncoder" _traceEncoder;
```

## Instance methods

```
-[MTLCountersBlitCommandEncoder waitForFence:];
-[MTLCountersBlitCommandEncoder insertDebugSignpost:];
-[MTLCountersBlitCommandEncoder updateFence:];
-[MTLCountersBlitCommandEncoder pushDebugGroup:];
-[MTLCountersBlitCommandEncoder popDebugGroup];
-[MTLCountersBlitCommandEncoder setLabel:];
-[MTLCountersBlitCommandEncoder endEncoding];
-[MTLCountersBlitCommandEncoder copyFromTexture:toTexture:];
-[MTLCountersBlitCommandEncoder dealloc];
-[MTLCountersBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:];
-[MTLCountersBlitCommandEncoder optimizeContentsForCPUAccess:slice:level:];
-[MTLCountersBlitCommandEncoder fillTexture:level:slice:region:color:];
-[MTLCountersBlitCommandEncoder optimizeContentsForGPUAccess:];
-[MTLCountersBlitCommandEncoder fillBuffer:range:pattern4:];
-[MTLCountersBlitCommandEncoder fillTexture:level:slice:region:bytes:length:];
-[MTLCountersBlitCommandEncoder fillTexture:level:slice:region:color:pixelFormat:];
-[MTLCountersBlitCommandEncoder optimizeContentsForCPUAccess:];
-[MTLCountersBlitCommandEncoder optimizeContentsForGPUAccess:slice:level:];
-[MTLCountersBlitCommandEncoder copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:];
-[MTLCountersBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTLCountersBlitCommandEncoder generateMipmapsForTexture:];
-[MTLCountersBlitCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTLCountersBlitCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
-[MTLCountersBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:];
-[MTLCountersBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:];
-[MTLCountersBlitCommandEncoder fillBuffer:range:value:];
-[MTLCountersBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
-[MTLCountersBlitCommandEncoder initWithBlitCommandEncoder:commandBuffer:descriptor:];
```
