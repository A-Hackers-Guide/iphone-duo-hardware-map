# `_MTLIOScratchBufferAllocator`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTLIOScratchBufferAllocator`
- 12 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
Q _currentSize;
{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]} _pool_lock;
@"<MTLDevice>" _device;
{MTLIOScratchBufferPrivateQueue="tqh_first"^{MTLIOScratchBufferPrivate}"tqh_last"^^{MTLIOScratchBufferPrivate}} _activeq;
{MTLIOScratchBufferPrivateQueue="tqh_first"^{MTLIOScratchBufferPrivate}"tqh_last"^^{MTLIOScratchBufferPrivate}} _poolq;
{MTLIOScratchBufferPrivateQueue="tqh_first"^{MTLIOScratchBufferPrivate}"tqh_last"^^{MTLIOScratchBufferPrivate}} _volatileq;
Q _age_to_purge;
@"NSObject<OS_dispatch_queue>" _pool_cleanup_queue;
@"NSObject<OS_dispatch_source>" _pool_cleanup_source;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _pool_cleanup_lock;
B _pool_cleanup_scheduled;
B _pool_cleanup_requested;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLIOScratchBufferAllocator initWithDevice:];
-[_MTLIOScratchBufferAllocator dealloc];
-[_MTLIOScratchBufferAllocator kickCleanupQueue];
-[_MTLIOScratchBufferAllocator newScratchBufferWithMinimumSize:];
-[_MTLIOScratchBufferAllocator returnActiveScratchBuffersToPool];
-[_MTLIOScratchBufferAllocator returnPriv:];
-[_MTLIOScratchBufferAllocator updateScratchBuffersPurgeability];
-[_MTLIOScratchBufferAllocator updateScratchBuffersPurgeabilityHandler];
```
