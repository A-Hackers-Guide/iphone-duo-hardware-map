# `BWPhotonicEngineNodeSampleBufferAndInputQueue`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _sampleBufferAndInputQueue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _sampleBufferAndInputQueueLock;
```

## Class methods

```
+[BWPhotonicEngineNodeSampleBufferAndInputQueue initialize];
```

## Instance methods

```
-[BWPhotonicEngineNodeSampleBufferAndInputQueue init];
-[BWPhotonicEngineNodeSampleBufferAndInputQueue dealloc];
-[BWPhotonicEngineNodeSampleBufferAndInputQueue enqueue:];
-[BWPhotonicEngineNodeSampleBufferAndInputQueue newDequeuedSampleBufferAndInput];
-[BWPhotonicEngineNodeSampleBufferAndInputQueue newSampleBuffersAndInputsWithPredicate:];
```
