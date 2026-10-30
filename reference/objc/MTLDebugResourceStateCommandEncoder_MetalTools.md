# `MTLDebugResourceStateCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsResourceStateCommandEncoder`
- 4 instance variables, 0 properties, 14 instance methods, 0 class methods

## Instance variables

```
B canDealloc;
B canEndEncoding;
B hasEndedEncoding;
{deque<id, std::allocator<id>>="__map_"{__split_buffer<id *, std::allocator<id *>>="__first_"^^@"__begin_"^^@"__end_"^^@""{?="__cap_"^^@}}"__start_"Q""{?="__size_"Q}} updatedFences;
```

## Instance methods

```
-[MTLDebugResourceStateCommandEncoder waitForFence:];
-[MTLDebugResourceStateCommandEncoder updateFence:];
-[MTLDebugResourceStateCommandEncoder endEncoding];
-[MTLDebugResourceStateCommandEncoder dealloc];
-[MTLDebugResourceStateCommandEncoder updateTextureMappings:mode:regions:mipLevels:slices:numRegions:];
-[MTLDebugResourceStateCommandEncoder barrierAfterQueueStages:beforeStages:];
-[MTLDebugResourceStateCommandEncoder moveTextureMappingsFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTLDebugResourceStateCommandEncoder updateTextureMapping:mode:indirectBuffer:indirectBufferOffset:];
-[MTLDebugResourceStateCommandEncoder updateTextureMapping:mode:region:mipLevel:slice:];
-[MTLDebugResourceStateCommandEncoder _setDefaults];
-[MTLDebugResourceStateCommandEncoder checkEncoderState];
-[MTLDebugResourceStateCommandEncoder initWithResourceStateCommandEncoder:commandBuffer:descriptor:];
-[MTLDebugResourceStateCommandEncoder validateSparseTextureMappingMode:];
-[MTLDebugResourceStateCommandEncoder validateTextureAccess:region:mipLevel:slice:];
```
