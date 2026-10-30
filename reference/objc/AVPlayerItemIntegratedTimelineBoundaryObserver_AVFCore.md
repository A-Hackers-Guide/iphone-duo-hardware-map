# `AVPlayerItemIntegratedTimelineBoundaryObserver`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVPlayerItemIntegratedTimelineObserver_Internal`
- 9 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigSimpleMutex=} _mutex;
@"AVPlayerItemSegment" _segment;
@"NSArray" _offsetTimes;
@"NSObject<OS_dispatch_queue>" _queue;
@? _block;
{?="source"{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}}"target"{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}}} _observedTimeMapping;
@"AVOccasionalTimebaseObserver" _boundaryObserver;
B _segmentWasRemoved;
B _hasBeenScheduled;
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
-[AVPlayerItemIntegratedTimelineBoundaryObserver dealloc];
-[AVPlayerItemIntegratedTimelineBoundaryObserver _currentInterstitialIDForSnapshot:];
-[AVPlayerItemIntegratedTimelineBoundaryObserver _ensureItemTimeOffsetLiesInSegment:item:];
-[AVPlayerItemIntegratedTimelineBoundaryObserver _isItemCurrentTimeWithinZeroOffsetBoundaryThreshold:offset:];
-[AVPlayerItemIntegratedTimelineBoundaryObserver ensureBoundaryObserverSegmentStillExistsWithNewSnapshot:];
-[AVPlayerItemIntegratedTimelineBoundaryObserver hasObserverBeenScheduledYet];
-[AVPlayerItemIntegratedTimelineBoundaryObserver initWithSegment:offsetTimes:queue:block:];
-[AVPlayerItemIntegratedTimelineBoundaryObserver rescheduleObserverWithSnapshot:itemToSchedule:];
-[AVPlayerItemIntegratedTimelineBoundaryObserver scheduledSegment];
-[AVPlayerItemIntegratedTimelineBoundaryObserver setOccasionalBoundaryObserver:];
```
