# `_MTLIOCommandQueue`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTLIOCommandQueueSPI`
- 22 instance variables, 11 properties, 20 instance methods, 0 class methods

## Instance variables

```
q _type;
q _priority;
@"NSObject<OS_dispatch_queue>" _commitQueue;
Q _maxWorkerThreads;
@"MTLResourceListPool" _resourceListPool;
@"NSObject<OS_dispatch_semaphore>" _commandBufferSemaphore;
{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]} cmdCvar;
{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]} cmdMutex;
@"NSObject<OS_dispatch_queue>" _followonQueue;
Q _labelTraceID;
@"<MTLDevice>" _device;
@"<MTLCommandQueue>" _gpuQueue;
@"<MTLSharedEvent>" _gpuEvent;
@"MTLSharedEventListener" _eventSignalListener;
{MTLIOCommandQueueCommandList="activeq"{?="tqh_first"^{MTLIOCommandQueueCommand}"tqh_last"^^{MTLIOCommandQueueCommand}}"lock"^{_opaque_pthread_mutex_t}"cond"^{_opaque_pthread_cond_t}"queue"@"_MTLIOCommandQueue""exit"B} _commandList;
{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]} _completeQueueMutex;
@"NSMutableArray" _completeQueue;
@"<MTLIOScratchBufferAllocator>" _scratchBufferAllocator;
B _usesPooledScratchBufferAllocator;
@"NSString" description;
# superclass;
Q hash;
```

## Properties

```
@property (T@"<MTLDevice>",R,V_device) device;
@property (T@"<MTLCommandQueue>",R,V_gpuQueue) gpuQueue;
@property (T@"<MTLSharedEvent>",R,V_gpuEvent) gpuEvent;
@property (T@"MTLSharedEventListener",R,V_eventSignalListener) eventSignalListener;
@property (T@"<MTLIOScratchBufferAllocator>",R,V_scratchBufferAllocator) scratchBufferAllocator;
@property (TQ,R,N) globalTraceObjectID;
@property (T@"NSString",C) label;
@property (TQ,R,Vhash) hash;
@property (T#,R,Vsuperclass) superclass;
@property (T@"NSString",R,C,Vdescription) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLIOCommandQueue barrier];
-[_MTLIOCommandQueue superclass];
-[_MTLIOCommandQueue initWithDevice:descriptor:];
-[_MTLIOCommandQueue device];
-[_MTLIOCommandQueue globalTraceObjectID];
-[_MTLIOCommandQueue dealloc];
-[_MTLIOCommandQueue commandBuffer];
-[_MTLIOCommandQueue hash];
-[_MTLIOCommandQueue description];
-[_MTLIOCommandQueue commandBufferWithUnretainedReferences];
-[_MTLIOCommandQueue commit:];
-[_MTLIOCommandQueue didComplete:withStatus:];
-[_MTLIOCommandQueue enqueueBarrier];
-[_MTLIOCommandQueue eventSignalListener];
-[_MTLIOCommandQueue gpuEvent];
-[_MTLIOCommandQueue gpuQueue];
-[_MTLIOCommandQueue kickAllocatorCleanupQueue];
-[_MTLIOCommandQueue launchIOWorkerThreads];
-[_MTLIOCommandQueue returnActiveScratchBuffersToPool];
-[_MTLIOCommandQueue scratchBufferAllocator];
```
