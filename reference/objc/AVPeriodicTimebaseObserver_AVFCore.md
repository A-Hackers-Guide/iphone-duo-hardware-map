# `AVPeriodicTimebaseObserver`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVTimebaseObserver`
- 8 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
{?="value"q"timescale"i"flags"I"epoch"q} _intervalRequested;
{?="value"q"timescale"i"flags"I"epoch"q} _lastIntervalUsed;
{?="value"q"timescale"i"flags"I"epoch"q} _lastPeriodicFireTime;
{?="value"q"timescale"i"flags"I"epoch"q} _lastNonperiodicFireTime;
{?="value"q"timescale"i"flags"I"epoch"q} _lastStopTime;
{?="value"q"timescale"i"flags"I"epoch"q} _nonPeriodicOffset;
I _sequenceNum;
@? _block;
```

## Instance methods

```
-[AVPeriodicTimebaseObserver initWithTimebase:interval:offset:queue:block:];
-[AVPeriodicTimebaseObserver initGutsWithTimebase:interval:offset:queue:block:];
-[AVPeriodicTimebaseObserver _fireBlockForTime:];
-[AVPeriodicTimebaseObserver dealloc];
-[AVPeriodicTimebaseObserver initWithTimebase:interval:queue:block:];
-[AVPeriodicTimebaseObserver _effectiveRateChanged];
-[AVPeriodicTimebaseObserver _handleTimeDiscontinuity];
-[AVPeriodicTimebaseObserver _resetNextFireTime];
```
