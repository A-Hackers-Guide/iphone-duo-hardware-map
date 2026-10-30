# `MTLCountersResourceStateCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsResourceStateCommandEncoder`
- 1 instance variables, 0 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"MTLCountersTraceResourceStateCommandEncoder" _traceEncoder;
```

## Instance methods

```
-[MTLCountersResourceStateCommandEncoder waitForFence:];
-[MTLCountersResourceStateCommandEncoder insertDebugSignpost:];
-[MTLCountersResourceStateCommandEncoder updateFence:];
-[MTLCountersResourceStateCommandEncoder pushDebugGroup:];
-[MTLCountersResourceStateCommandEncoder popDebugGroup];
-[MTLCountersResourceStateCommandEncoder setLabel:];
-[MTLCountersResourceStateCommandEncoder endEncoding];
-[MTLCountersResourceStateCommandEncoder dealloc];
-[MTLCountersResourceStateCommandEncoder updateTextureMappings:mode:regions:mipLevels:slices:numRegions:];
-[MTLCountersResourceStateCommandEncoder moveTextureMappingsFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTLCountersResourceStateCommandEncoder updateTextureMapping:mode:indirectBuffer:indirectBufferOffset:];
-[MTLCountersResourceStateCommandEncoder updateTextureMapping:mode:region:mipLevel:slice:];
-[MTLCountersResourceStateCommandEncoder copyMappingStateFromTexture:mipLevel:slice:toBuffer:offset:numTiles:];
-[MTLCountersResourceStateCommandEncoder initWithResourceStateCommandEncoder:commandBuffer:descriptor:];
```
