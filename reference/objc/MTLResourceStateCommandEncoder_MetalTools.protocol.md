# `MTLResourceStateCommandEncoder` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLCommandEncoder`
- 0 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance methods

```
-[MTLResourceStateCommandEncoder waitForFence:];
-[MTLResourceStateCommandEncoder updateFence:];
-[MTLResourceStateCommandEncoder updateTextureMappings:mode:regions:mipLevels:slices:numRegions:];
-[MTLResourceStateCommandEncoder moveTextureMappingsFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTLResourceStateCommandEncoder updateTextureMapping:mode:indirectBuffer:indirectBufferOffset:];
-[MTLResourceStateCommandEncoder updateTextureMapping:mode:region:mipLevel:slice:];
```
