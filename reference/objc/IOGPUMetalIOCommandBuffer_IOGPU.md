# `IOGPUMetalIOCommandBuffer`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLIOCommandBuffer`
- 19 instance variables, 0 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"IOGPUMetalDevice<MTLDevice>" _device;
@"IOGPUMetalIOCommandQueue" _queue;
@"IOGPUMetalDeviceShmem" _ioKernelCommandShmem;
* _ioKernelCommandShmemStart;
* _ioKernelCommandShmemCurrent;
* _ioKernelCommandShmemEnd;
^{IOGPUIOKernelCommandListHeader=II} _commandListHeader;
@"IOGPUMetalCommandBuffer<MTLCommandBuffer>" _gpuCommandBuffer;
@"IOGPUMetalCommandEncoder<MTLBlitCommandEncoder>" _gpuBlitEncoder;
@"NSMutableArray" _stagingBuffers;
@"NSObject<OS_dispatch_group>" _ioCompletionGroup;
AI _notificationCount;
I _lastBarrierNotificationCount;
I _commandBufferID;
Q _globalTraceObjectID;
B _hasFollowOnGPUWork;
B _committed;
B _tryCancel;
{vector<IOGPUIOCommandQueueCommandBufferCallbackBlock, std::allocator<IOGPUIOCommandQueueCommandBufferCallbackBlock>>="__begin_"^(?)"__end_"^(?)""{?="__cap_"^(?)}} _commandCallbackBlocks;
```

## Instance methods

```
-[IOGPUMetalIOCommandBuffer barrier];
-[IOGPUMetalIOCommandBuffer initWithQueue:];
-[IOGPUMetalIOCommandBuffer enqueue];
-[IOGPUMetalIOCommandBuffer commit];
-[IOGPUMetalIOCommandBuffer isCommitted];
-[IOGPUMetalIOCommandBuffer tryCancel];
-[IOGPUMetalIOCommandBuffer encodeSignalEvent:value:];
-[IOGPUMetalIOCommandBuffer setLabel:];
-[IOGPUMetalIOCommandBuffer globalTraceObjectID];
-[IOGPUMetalIOCommandBuffer dealloc];
-[IOGPUMetalIOCommandBuffer growKernelCommandBuffer:];
-[IOGPUMetalIOCommandBuffer encodeWaitForEvent:value:];
-[IOGPUMetalIOCommandBuffer signalEvent:value:];
-[IOGPUMetalIOCommandBuffer waitForEvent:value:];
-[IOGPUMetalIOCommandBuffer addBarrier];
-[IOGPUMetalIOCommandBuffer didCompleteWithStatus:];
-[IOGPUMetalIOCommandBuffer initWithQueue:resourceList:retained:];
-[IOGPUMetalIOCommandBuffer loadBuffer:offset:size:handle:handleOffset:];
-[IOGPUMetalIOCommandBuffer loadBuffer:offset:size:sourceHandle:sourceHandleOffset:];
-[IOGPUMetalIOCommandBuffer loadBytes:size:sourceHandle:sourceHandleOffset:];
-[IOGPUMetalIOCommandBuffer loadTexture:slice:level:size:bytesPerRow:bytesPerImage:dstOrigin:handle:handleOffset:];
-[IOGPUMetalIOCommandBuffer loadTexture:slice:level:size:sourceBytesPerRow:sourceBytesPerImage:destinationOrigin:sourceHandle:sourceHandleOffset:];
-[IOGPUMetalIOCommandBuffer hasFollowOnWork];
-[IOGPUMetalIOCommandBuffer barrierComplete:];
-[IOGPUMetalIOCommandBuffer completeCommandCallbackBlocks];
-[IOGPUMetalIOCommandBuffer createCommandList];
-[IOGPUMetalIOCommandBuffer getCommandBufferBytes:];
-[IOGPUMetalIOCommandBuffer validateNotificationCount];
```
