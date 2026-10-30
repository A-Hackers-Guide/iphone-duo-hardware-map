# `BWDeferredContainerManagerBase`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
{_opaque_pthread_rwlock_t="__sig"q"__opaque"[192c]} _lock;
@"NSObject<OS_dispatch_queue>" _timerQueue;
@"NSObject<OS_dispatch_queue>" _deletionQueue;
```

## Class methods

```
+[BWDeferredContainerManagerBase initialize];
```

## Instance methods

```
-[BWDeferredContainerManagerBase dealloc];
-[BWDeferredContainerManagerBase deleteContainerForApplicationID:captureRequestIdentifier:];
-[BWDeferredContainerManagerBase initWithQueuePriority:];
-[BWDeferredContainerManagerBase manifestForApplicationID:captureRequestIdentifier:err:];
-[BWDeferredContainerManagerBase manifestsForApplicationID:err:];
```
