# `BWFencedAnimationQueue`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 1 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _fencedAnimationQueue;
@"NSObject<OS_dispatch_semaphore>" _fencedAnimationQueueSemaphore;
I _fencedAnimationFramerateThrottle;
d _timeOfLastFencedAnimation;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _queueLock;
```

## Properties

```
@property (TQ,R) count;
```

## Instance methods

```
-[BWFencedAnimationQueue flush];
-[BWFencedAnimationQueue dealloc];
-[BWFencedAnimationQueue count];
-[BWFencedAnimationQueue initWithQueueSize:];
-[BWFencedAnimationQueue dequeueFencedAnimation];
-[BWFencedAnimationQueue enqueueFencedAnimation:];
```
