# `BWDeferredCaptureContainerManager`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWDeferredContainerManagerBase`
- 14 instance variables, 1 properties, 19 instance methods, 1 class methods

## Instance variables

```
I _cacheSize;
I _cacheResidencySeconds;
@"NSObject<OS_dispatch_source>" _cacheExpiryTimer;
@"NSMutableArray" _stagedContainers;
@"NSMutableArray" _inflightContainers;
@"NSMutableArray" _cachedContainers;
@"NSObject<OS_dispatch_queue>" _flushQueue;
@"NSObject<OS_dispatch_queue>" _flushQueueReducedPriority;
@"NSObject<OS_dispatch_queue>" _flushQueueBackground;
B _usesReducedPriorityFlushQueue;
Q _cachedLowDiskThresholdBytes;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _storageLock;
Q _lastAvailableBytes;
@"NSMutableDictionary" _pools;
```

## Properties

```
@property (TB,N,V_usesReducedPriorityFlushQueue) usesReducedPriorityFlushQueue;
```

## Class methods

```
+[BWDeferredCaptureContainerManager sharedInstance];
```

## Instance methods

```
-[BWDeferredCaptureContainerManager init];
-[BWDeferredCaptureContainerManager newPixelBuffer:];
-[BWDeferredCaptureContainerManager abortContainer:error:];
-[BWDeferredCaptureContainerManager addBufferPool:];
-[BWDeferredCaptureContainerManager addCaptureContainer:];
-[BWDeferredCaptureContainerManager canDeferUsingActiveFSCheck:];
-[BWDeferredCaptureContainerManager commitContainer:];
-[BWDeferredCaptureContainerManager containerWaitForFlush:];
-[BWDeferredCaptureContainerManager copyRemoteContainerForApplicationID:captureRequestIdentifier:err:];
-[BWDeferredCaptureContainerManager createCaptureContainerWithApplicationID:captureRequestIdentifier:err:];
-[BWDeferredCaptureContainerManager deleteContainerForApplicationID:captureRequestIdentifier:];
-[BWDeferredCaptureContainerManager flush:toMinimumCapacity:];
-[BWDeferredCaptureContainerManager lookupCaptureContainer:];
-[BWDeferredCaptureContainerManager manifestsForApplicationID:err:];
-[BWDeferredCaptureContainerManager queryContainerStatusForApplicationID:captureRequestIdentifier:status:];
-[BWDeferredCaptureContainerManager releaseRemoteContainerForApplicationID:captureRequestIdentifier:];
-[BWDeferredCaptureContainerManager removeBufferPool:];
-[BWDeferredCaptureContainerManager setUsesReducedPriorityFlushQueue:];
-[BWDeferredCaptureContainerManager usesReducedPriorityFlushQueue];
```
