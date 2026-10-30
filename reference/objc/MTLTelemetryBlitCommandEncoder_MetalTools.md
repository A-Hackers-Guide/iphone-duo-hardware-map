# `MTLTelemetryBlitCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsBlitCommandEncoder`
- 3 instance variables, 0 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"MTLTelemetryDevice" _telemetryDevice;
@"MTLTelemetryCommandBuffer" _telemetryCommandBuffer;
I _beBlits;
```

## Instance methods

```
-[MTLTelemetryBlitCommandEncoder endEncoding];
-[MTLTelemetryBlitCommandEncoder copyFromTexture:toTexture:];
-[MTLTelemetryBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:];
-[MTLTelemetryBlitCommandEncoder fillTexture:level:slice:region:color:];
-[MTLTelemetryBlitCommandEncoder fillBuffer:range:pattern4:];
-[MTLTelemetryBlitCommandEncoder fillTexture:level:slice:region:bytes:length:];
-[MTLTelemetryBlitCommandEncoder fillTexture:level:slice:region:color:pixelFormat:];
-[MTLTelemetryBlitCommandEncoder copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:];
-[MTLTelemetryBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTLTelemetryBlitCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTLTelemetryBlitCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
-[MTLTelemetryBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:];
-[MTLTelemetryBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:];
-[MTLTelemetryBlitCommandEncoder fillBuffer:range:value:];
-[MTLTelemetryBlitCommandEncoder accumulateBlitDistribution:samples:bytesPerRow:bytesPerImage:bufferSize:type:option:src:];
-[MTLTelemetryBlitCommandEncoder initWithBlitCommandEncoder:commandBuffer:descriptor:];
```
