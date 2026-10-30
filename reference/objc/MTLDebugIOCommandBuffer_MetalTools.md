# `MTLDebugIOCommandBuffer`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsIOCommandBuffer`
- 0 instance variables, 0 properties, 16 instance methods, 0 class methods

## Instance methods

```
-[MTLDebugIOCommandBuffer addCompletedHandler:];
-[MTLDebugIOCommandBuffer commit];
-[MTLDebugIOCommandBuffer tryCancel];
-[MTLDebugIOCommandBuffer encodeSignalEvent:value:];
-[MTLDebugIOCommandBuffer encodeWaitForEvent:value:];
-[MTLDebugIOCommandBuffer signalEvent:value:];
-[MTLDebugIOCommandBuffer waitForEvent:value:];
-[MTLDebugIOCommandBuffer loadBuffer:offset:size:handle:handleOffset:];
-[MTLDebugIOCommandBuffer loadBuffer:offset:size:sourceHandle:sourceHandleOffset:];
-[MTLDebugIOCommandBuffer loadBytes:size:sourceHandle:sourceHandleOffset:];
-[MTLDebugIOCommandBuffer loadTexture:slice:level:size:bytesPerRow:bytesPerImage:dstOrigin:handle:handleOffset:];
-[MTLDebugIOCommandBuffer loadTexture:slice:level:size:sourceBytesPerRow:sourceBytesPerImage:destinationOrigin:sourceHandle:sourceHandleOffset:];
-[MTLDebugIOCommandBuffer internalValidateLoadBytes:size:sourceHandle:sourceHandleOffset:];
-[MTLDebugIOCommandBuffer internalValidateEvent:];
-[MTLDebugIOCommandBuffer internalValidateLoadBuffer:offset:size:sourceHandle:sourceHandleOffset:];
-[MTLDebugIOCommandBuffer internalValidateLoadTexture:slice:level:size:sourceBytesPerRow:sourceBytesPerImage:destinationOrigin:sourceHandle:sourceHandleOffset:];
```
