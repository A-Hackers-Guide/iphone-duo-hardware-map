# `MTL3On4BlitCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MTL3On4.framework/MTL3On4`](../userland/System__Library__PrivateFrameworks__MTL3On4.framework__MTL3On4.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL3On4CommandEncoder`
- Protocols: `MTLBlitCommandEncoderSPI`
- 0 instance variables, 6 properties, 38 instance methods, 0 class methods

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
-[MTL3On4BlitCommandEncoder waitForFence:];
-[MTL3On4BlitCommandEncoder updateFence:];
-[MTL3On4BlitCommandEncoder sampleCountersInBuffer:atSampleIndex:withBarrier:];
-[MTL3On4BlitCommandEncoder synchronizeResource:];
-[MTL3On4BlitCommandEncoder copyFromTexture:toTexture:];
-[MTL3On4BlitCommandEncoder synchronizeTexture:slice:level:];
-[MTL3On4BlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:];
-[MTL3On4BlitCommandEncoder optimizeContentsForCPUAccess:slice:level:];
-[MTL3On4BlitCommandEncoder optimizeIndirectCommandBuffer:withRange:];
-[MTL3On4BlitCommandEncoder fillTexture:level:slice:region:color:];
-[MTL3On4BlitCommandEncoder optimizeContentsForGPUAccess:];
-[MTL3On4BlitCommandEncoder fillBuffer:range:pattern4:];
-[MTL3On4BlitCommandEncoder fillTexture:level:slice:region:bytes:length:];
-[MTL3On4BlitCommandEncoder resolveCounters:inRange:destinationBuffer:destinationOffset:];
-[MTL3On4BlitCommandEncoder fillTexture:level:slice:region:color:pixelFormat:];
-[MTL3On4BlitCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:];
-[MTL3On4BlitCommandEncoder resetCommandsInBuffer:withRange:];
-[MTL3On4BlitCommandEncoder optimizeContentsForCPUAccess:];
-[MTL3On4BlitCommandEncoder optimizeContentsForGPUAccess:slice:level:];
-[MTL3On4BlitCommandEncoder copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:];
-[MTL3On4BlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTL3On4BlitCommandEncoder generateMipmapsForTexture:];
-[MTL3On4BlitCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTL3On4BlitCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
-[MTL3On4BlitCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:sourcePlane:toTensor:destinationOrigin:destinationDimensions:destinationPlane:];
-[MTL3On4BlitCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:];
-[MTL3On4BlitCommandEncoder copyFromTensor:sourceSlice:toTensor:destinationSlice:];
-[MTL3On4BlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:];
-[MTL3On4BlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:];
-[MTL3On4BlitCommandEncoder fillBuffer:range:value:];
-[MTL3On4BlitCommandEncoder invalidateCompressedTexture:];
-[MTL3On4BlitCommandEncoder invalidateCompressedTexture:slice:level:];
-[MTL3On4BlitCommandEncoder optimizeContentsForTexture:readAccessPattern:readAccessor:];
-[MTL3On4BlitCommandEncoder optimizeContentsForTexture:readAccessPattern:readAccessor:slice:level:];
-[MTL3On4BlitCommandEncoder getTextureAccessCounters:region:mipLevel:slice:resetCounters:countersBuffer:countersBufferOffset:];
-[MTL3On4BlitCommandEncoder resetTextureAccessCounters:region:mipLevel:slice:];
-[MTL3On4BlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
-[MTL3On4BlitCommandEncoder initWithMTL3On4CommandBuffer:commandEncoder:residencySet:];
```
