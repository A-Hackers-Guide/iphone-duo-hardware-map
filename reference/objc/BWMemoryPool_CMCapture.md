# `BWMemoryPool`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 1 properties, 21 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"IOSurfaceMemoryPool" _pool;
Q _poolId;
B _hasEnsuredTargetSize;
I _flushAssertionCount;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _flushAssertionLock;
@"MMAssertion" _modelManagerAssertion;
d _modelManagerAssertionCreationTime;
@"NSSet" _clientDenyList;
```

## Properties

```
@property (TQ,R,N) poolIdentifier;
```

## Class methods

```
+[BWMemoryPool initialize];
+[BWMemoryPool sharedMemoryPool];
```

## Instance methods

```
-[BWMemoryPool init];
-[BWMemoryPool flush];
-[BWMemoryPool dealloc];
-[BWMemoryPool disableWithCompletionHandler:];
-[BWMemoryPool enableForPixelBufferAttributes:];
-[BWMemoryPool _addFlushAssertion];
-[BWMemoryPool _removeFlushAssertion];
-[BWMemoryPool disableForCaptureDevice:];
-[BWMemoryPool disableForCaptureStream:];
-[BWMemoryPool disableForClientBundleId:];
-[BWMemoryPool enableForCaptureDevice:];
-[BWMemoryPool enableForCaptureStream:];
-[BWMemoryPool ensureMemoryAsyncWithSize:withMaximizeSystemMemory:useOptimizedMemorySizeDistributionsIfAvailable:forClientBundleId:];
-[BWMemoryPool getInUseFootprint:andOutOfUseFootprint:];
-[BWMemoryPool isClientInDenyList:];
-[BWMemoryPool maximizeAvailableSystemMemory];
-[BWMemoryPool modelManagerAssertionHeldDurationInSeconds];
-[BWMemoryPool newFlushAssertion:];
-[BWMemoryPool newMTLBufferWithLength:forDevice:];
-[BWMemoryPool poolIdentifier];
-[BWMemoryPool releaseModelManagerAssertion];
```
