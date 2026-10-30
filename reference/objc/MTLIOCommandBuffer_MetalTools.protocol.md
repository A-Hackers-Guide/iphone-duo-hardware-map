# `MTLIOCommandBuffer` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 18 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C) label;
@property (Tq,R) status;
@property (T@"NSError",R) error;
```

## Instance methods

```
-[MTLIOCommandBuffer addCompletedHandler:];
-[MTLIOCommandBuffer waitUntilCompleted];
-[MTLIOCommandBuffer pushDebugGroup:];
-[MTLIOCommandBuffer enqueue];
-[MTLIOCommandBuffer commit];
-[MTLIOCommandBuffer popDebugGroup];
-[MTLIOCommandBuffer tryCancel];
-[MTLIOCommandBuffer label];
-[MTLIOCommandBuffer setLabel:];
-[MTLIOCommandBuffer status];
-[MTLIOCommandBuffer error];
-[MTLIOCommandBuffer signalEvent:value:];
-[MTLIOCommandBuffer waitForEvent:value:];
-[MTLIOCommandBuffer addBarrier];
-[MTLIOCommandBuffer copyStatusToBuffer:offset:];
-[MTLIOCommandBuffer loadBuffer:offset:size:sourceHandle:sourceHandleOffset:];
-[MTLIOCommandBuffer loadBytes:size:sourceHandle:sourceHandleOffset:];
-[MTLIOCommandBuffer loadTexture:slice:level:size:sourceBytesPerRow:sourceBytesPerImage:destinationOrigin:sourceHandle:sourceHandleOffset:];
```
