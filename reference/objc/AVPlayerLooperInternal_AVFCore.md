# `AVPlayerLooperInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
@"AVQueuePlayer" loopingPlayer;
@"AVPlayerItem" loopingItem;
@"NSMutableArray" loopingItemCopies;
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} loopRange;
q loopCount;
@"NSObject<OS_dispatch_queue>" ivarAccessQueue;
q playerOriginalActionAtItemEnd;
{?="value"q"timescale"i"flags"I"epoch"q} forwardPlaybackStartTime;
@"AVPlayerItem" lastEnqueuedLoopingItem;
B waitingForLastLoopingCopyToFinish;
q status;
@"NSError" error;
@"<AVCallbackCancellation>" playerCurrentItemKVOInvoker;
@"NSMutableArray" loopingItemStatusKVOInvokers;
@"AVWeakReference" weakReference;
B existingItemsPrecede;
B listeningForItemFailedToPlayToEndTime;
```
