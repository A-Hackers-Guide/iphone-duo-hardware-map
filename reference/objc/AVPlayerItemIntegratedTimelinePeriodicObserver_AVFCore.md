# `AVPlayerItemIntegratedTimelinePeriodicObserver`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVPlayerItemIntegratedTimelineObserver_Internal`
- 8 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigSimpleMutex=} _mutex;
{?="value"q"timescale"i"flags"I"epoch"q} _interval;
@"NSObject<OS_dispatch_queue>" _queue;
@? _block;
{?="source"{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}}"target"{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}}} _observedTimeMapping;
@"AVPeriodicTimebaseObserver" _periodicObserver;
B _hasBeenScheduled;
@"AVPlayerItemIntegratedTimeline" _integratedTimeline;
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
-[AVPlayerItemIntegratedTimelinePeriodicObserver dealloc];
-[AVPlayerItemIntegratedTimelinePeriodicObserver _doesTimeResideInItemIntegratedTimelineOffsets:withOffsets:timeMappingOut:];
-[AVPlayerItemIntegratedTimelinePeriodicObserver _doesTimeResideInPrimarySegment:atTime:timeMappingOut:];
-[AVPlayerItemIntegratedTimelinePeriodicObserver _getNextPeriodicFireTimeFromIntegratedCurrentTime:];
-[AVPlayerItemIntegratedTimelinePeriodicObserver hasObserverBeenScheduledYet];
-[AVPlayerItemIntegratedTimelinePeriodicObserver initWithInterval:queue:block:integratedTimeline:];
-[AVPlayerItemIntegratedTimelinePeriodicObserver rescheduleObserverWithSnapshot:itemToSchedule:];
```
