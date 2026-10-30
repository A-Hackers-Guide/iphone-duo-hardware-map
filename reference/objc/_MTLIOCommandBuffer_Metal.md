# `_MTLIOCommandBuffer`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTLIOCommandBufferSPI`
- 19 instance variables, 8 properties, 32 instance methods, 0 class methods

## Instance variables

```
@"<MTLIOScratchBuffer>" _currentStagingBuffer;
Q _currentStagingBufferRemainingBytes;
Q _currentStagingBufferOffset;
@"MTLResourceList" _resourceList;
B _retained;
B _enqueued;
Q _labelTraceID;
q _status;
@"_MTLIOCommandQueue" _queue;
^{MTLIOCommandList=^{MTLIOCommand}QQQI{os_unfair_lock_s=I}BBB@@@@} commandList;
^{MTLIODispatch=^{MTLIODispatch}@?} _completedDispatchList;
^{MTLIODispatch=^{MTLIODispatch}@?} _completedDispatchListTail;
B _completedCallbacksDone;
{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]} _mutex;
{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]} _cond;
I _pendingCommands;
{vector<id<MTLIOScratchBuffer>, std::allocator<id<MTLIOScratchBuffer>>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} _activeScratchBuffers;
{vector<id<MTLIOScratchBuffer>, std::allocator<id<MTLIOScratchBuffer>>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} _poolScratchBuffers;
@"NSError" error;
```

## Properties

```
@property (TQ,R,N) globalTraceObjectID;
@property (T@"NSString",C) label;
@property (Tq,R,V_status) status;
@property (T@"NSError",R,Verror) error;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLIOCommandBuffer barrier];
-[_MTLIOCommandBuffer addCompletedHandler:];
-[_MTLIOCommandBuffer waitUntilCompleted];
-[_MTLIOCommandBuffer pushDebugGroup:];
-[_MTLIOCommandBuffer initWithQueue:];
-[_MTLIOCommandBuffer enqueue];
-[_MTLIOCommandBuffer commit];
-[_MTLIOCommandBuffer isCommitted];
-[_MTLIOCommandBuffer popDebugGroup];
-[_MTLIOCommandBuffer tryCancel];
-[_MTLIOCommandBuffer encodeSignalEvent:value:];
-[_MTLIOCommandBuffer globalTraceObjectID];
-[_MTLIOCommandBuffer dealloc];
-[_MTLIOCommandBuffer status];
-[_MTLIOCommandBuffer error];
-[_MTLIOCommandBuffer encodeWaitForEvent:value:];
-[_MTLIOCommandBuffer signalEvent:value:];
-[_MTLIOCommandBuffer waitForEvent:value:];
-[_MTLIOCommandBuffer addBarrier];
-[_MTLIOCommandBuffer clearScratchBufferLists];
-[_MTLIOCommandBuffer copyStatusToBuffer:offset:];
-[_MTLIOCommandBuffer createCommandListWithResourcePool:];
-[_MTLIOCommandBuffer didCompleteWithStatus:];
-[_MTLIOCommandBuffer getCommandList];
-[_MTLIOCommandBuffer getReusableScratchBuffer:];
-[_MTLIOCommandBuffer initWithQueue:resourceList:retained:];
-[_MTLIOCommandBuffer loadBuffer:offset:size:handle:handleOffset:];
-[_MTLIOCommandBuffer loadBuffer:offset:size:sourceHandle:sourceHandleOffset:];
-[_MTLIOCommandBuffer loadBytes:size:sourceHandle:sourceHandleOffset:];
-[_MTLIOCommandBuffer loadTexture:slice:level:size:bytesPerRow:bytesPerImage:dstOrigin:handle:handleOffset:];
-[_MTLIOCommandBuffer loadTexture:slice:level:size:sourceBytesPerRow:sourceBytesPerImage:destinationOrigin:sourceHandle:sourceHandleOffset:];
-[_MTLIOCommandBuffer reuseActiveScratchBuffers];
```
