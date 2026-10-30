# `IOGPUMetalIOCommandQueue`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLIOCommandQueue`
- 13 instance variables, 0 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"IOGPUMetalDevice<MTLDevice>" _device;
^{__IOGPUIOCommandQueue=} _ioCommandQueueRef;
@"IOGPUMetalCommandQueue<MTLCommandQueue>" _gpuQueue;
@"NSMutableArray" _pendingQueue;
@"NSMutableArray" _submittedQueue;
{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]} _pendingQueueLock;
{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]} _submittedQueueLock;
@"NSObject<OS_dispatch_queue>" _submissionQueueDispatch;
@"NSObject<OS_dispatch_queue>" _completionQueueDispatch;
@"NSObject<OS_dispatch_source>" _commandQueueEventSource;
@"NSObject<OS_dispatch_queue>" _ioThreadDispatch;
@"NSObject<OS_dispatch_queue>" _decompressionQueue;
Q _globalTraceObjectID;
```

## Instance methods

```
-[IOGPUMetalIOCommandQueue barrier];
-[IOGPUMetalIOCommandQueue enqueueCommandBuffer:];
-[IOGPUMetalIOCommandQueue initWithDevice:descriptor:];
-[IOGPUMetalIOCommandQueue setLabel:];
-[IOGPUMetalIOCommandQueue globalTraceObjectID];
-[IOGPUMetalIOCommandQueue dealloc];
-[IOGPUMetalIOCommandQueue getPriority];
-[IOGPUMetalIOCommandQueue commandBuffer];
-[IOGPUMetalIOCommandQueue commandBufferWithUnretainedReferences];
-[IOGPUMetalIOCommandQueue didComplete:withStatus:];
-[IOGPUMetalIOCommandQueue enqueueBarrier];
-[IOGPUMetalIOCommandQueue launchIOWorkerThreads];
-[IOGPUMetalIOCommandQueue _submitAvailableCommands:];
-[IOGPUMetalIOCommandQueue commandBufferComplete];
-[IOGPUMetalIOCommandQueue commitCommandBuffer:];
-[IOGPUMetalIOCommandQueue getDecompressionQueue];
-[IOGPUMetalIOCommandQueue launchIOGPUIOThreads];
-[IOGPUMetalIOCommandQueue submitAvailableCommands];
```
