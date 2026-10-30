# `MTLToolsIOCommandBuffer`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLIOCommandBufferSPI`
- 3 instance variables, 8 properties, 29 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _handlerLock;
{vector<void (^)(id<MTLIOCommandBuffer>), std::allocator<void (^)(id<MTLIOCommandBuffer>)>>="__begin_"^@?"__end_"^@?""{?="__cap_"^@?}} _completedHandlers;
B _didInvokeCompletedHandlers;
```

## Properties

```
@property (TQ,R,N) globalTraceObjectID;
@property (T@"NSString",C) label;
@property (Tq,R) status;
@property (T@"NSError",R) error;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsIOCommandBuffer barrier];
-[MTLToolsIOCommandBuffer addCompletedHandler:];
-[MTLToolsIOCommandBuffer waitUntilCompleted];
-[MTLToolsIOCommandBuffer pushDebugGroup:];
-[MTLToolsIOCommandBuffer enqueue];
-[MTLToolsIOCommandBuffer commit];
-[MTLToolsIOCommandBuffer isCommitted];
-[MTLToolsIOCommandBuffer popDebugGroup];
-[MTLToolsIOCommandBuffer tryCancel];
-[MTLToolsIOCommandBuffer encodeSignalEvent:value:];
-[MTLToolsIOCommandBuffer label];
-[MTLToolsIOCommandBuffer setLabel:];
-[MTLToolsIOCommandBuffer globalTraceObjectID];
-[MTLToolsIOCommandBuffer dealloc];
-[MTLToolsIOCommandBuffer status];
-[MTLToolsIOCommandBuffer error];
-[MTLToolsIOCommandBuffer encodeWaitForEvent:value:];
-[MTLToolsIOCommandBuffer signalEvent:value:];
-[MTLToolsIOCommandBuffer waitForEvent:value:];
-[MTLToolsIOCommandBuffer addBarrier];
-[MTLToolsIOCommandBuffer copyStatusToBuffer:offset:];
-[MTLToolsIOCommandBuffer initWithBaseObject:parent:];
-[MTLToolsIOCommandBuffer loadBuffer:offset:size:handle:handleOffset:];
-[MTLToolsIOCommandBuffer loadBuffer:offset:size:sourceHandle:sourceHandleOffset:];
-[MTLToolsIOCommandBuffer loadBytes:size:sourceHandle:sourceHandleOffset:];
-[MTLToolsIOCommandBuffer loadTexture:slice:level:size:bytesPerRow:bytesPerImage:dstOrigin:handle:handleOffset:];
-[MTLToolsIOCommandBuffer loadTexture:slice:level:size:sourceBytesPerRow:sourceBytesPerImage:destinationOrigin:sourceHandle:sourceHandleOffset:];
-[MTLToolsIOCommandBuffer invokeCompletedHandlers];
-[MTLToolsIOCommandBuffer preCommit];
```
