# `MTLToolsBlitCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsCommandEncoder`
- Protocols: `MTLBlitCommandEncoderSPI`
- 0 instance variables, 7 properties, 44 instance methods, 0 class methods

## Properties

```
@property (T@"MTLToolsCommandBuffer",R,D,N) commandBuffer;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsBlitCommandEncoder waitForFence:];
-[MTLToolsBlitCommandEncoder insertDebugSignpost:];
-[MTLToolsBlitCommandEncoder updateFence:];
-[MTLToolsBlitCommandEncoder sampleCountersInBuffer:atSampleIndex:withBarrier:];
-[MTLToolsBlitCommandEncoder pushDebugGroup:];
-[MTLToolsBlitCommandEncoder synchronizeResource:];
-[MTLToolsBlitCommandEncoder popDebugGroup];
-[MTLToolsBlitCommandEncoder endEncoding];
-[MTLToolsBlitCommandEncoder copyFromTexture:toTexture:];
-[MTLToolsBlitCommandEncoder synchronizeTexture:slice:level:];
-[MTLToolsBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:];
-[MTLToolsBlitCommandEncoder optimizeContentsForCPUAccess:slice:level:];
-[MTLToolsBlitCommandEncoder optimizeIndirectCommandBuffer:withRange:];
-[MTLToolsBlitCommandEncoder fillTexture:level:slice:region:color:];
-[MTLToolsBlitCommandEncoder optimizeContentsForGPUAccess:];
-[MTLToolsBlitCommandEncoder fillBuffer:range:pattern4:];
-[MTLToolsBlitCommandEncoder fillTexture:level:slice:region:bytes:length:];
-[MTLToolsBlitCommandEncoder resolveCounters:inRange:destinationBuffer:destinationOffset:];
-[MTLToolsBlitCommandEncoder fillTexture:level:slice:region:color:pixelFormat:];
-[MTLToolsBlitCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:];
-[MTLToolsBlitCommandEncoder resetCommandsInBuffer:withRange:];
-[MTLToolsBlitCommandEncoder optimizeContentsForCPUAccess:];
-[MTLToolsBlitCommandEncoder optimizeContentsForGPUAccess:slice:level:];
-[MTLToolsBlitCommandEncoder copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:];
-[MTLToolsBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTLToolsBlitCommandEncoder generateMipmapsForTexture:];
-[MTLToolsBlitCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTLToolsBlitCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
-[MTLToolsBlitCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:sourcePlane:toTensor:destinationOrigin:destinationDimensions:destinationPlane:];
-[MTLToolsBlitCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:];
-[MTLToolsBlitCommandEncoder copyFromTensor:sourceSlice:toTensor:destinationSlice:];
-[MTLToolsBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:];
-[MTLToolsBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:];
-[MTLToolsBlitCommandEncoder endEncodingAndRetrieveProgramAddressTable];
-[MTLToolsBlitCommandEncoder fillBuffer:range:value:];
-[MTLToolsBlitCommandEncoder initWithBaseObject:parent:];
-[MTLToolsBlitCommandEncoder invalidateCompressedTexture:];
-[MTLToolsBlitCommandEncoder invalidateCompressedTexture:slice:level:];
-[MTLToolsBlitCommandEncoder optimizeContentsForTexture:readAccessPattern:readAccessor:];
-[MTLToolsBlitCommandEncoder optimizeContentsForTexture:readAccessPattern:readAccessor:slice:level:];
-[MTLToolsBlitCommandEncoder getTextureAccessCounters:region:mipLevel:slice:resetCounters:countersBuffer:countersBufferOffset:];
-[MTLToolsBlitCommandEncoder resetTextureAccessCounters:region:mipLevel:slice:];
-[MTLToolsBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
-[MTLToolsBlitCommandEncoder initWithBlitCommandEncoder:parent:descriptor:];
```
