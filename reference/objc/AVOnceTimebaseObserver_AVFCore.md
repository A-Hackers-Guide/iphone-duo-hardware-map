# `AVOnceTimebaseObserver`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVTimebaseObserver`
- 3 instance variables, 1 properties, 8 instance methods, 0 class methods

## Instance variables

```
{?="value"q"timescale"i"flags"I"epoch"q} _fireTime;
@? _block;
B _didFire;
```

## Properties

```
@property (TB,R,N) didFire;
```

## Instance methods

```
-[AVOnceTimebaseObserver dealloc];
-[AVOnceTimebaseObserver invalidate];
-[AVOnceTimebaseObserver _effectiveRateChanged];
-[AVOnceTimebaseObserver _handleTimeDiscontinuity];
-[AVOnceTimebaseObserver _resetNextFireTime];
-[AVOnceTimebaseObserver didFire];
-[AVOnceTimebaseObserver _fireBlock];
-[AVOnceTimebaseObserver initWithTimebase:fireTime:queue:block:];
```
