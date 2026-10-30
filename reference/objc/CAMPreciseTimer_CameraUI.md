# `CAMPreciseTimer`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _fired;
d _delay;
d _interval;
@? __handler;
@"NSObject<OS_dispatch_source>" __currentTimer;
```

## Properties

```
@property (T@?,R,C,N,V__handler) _handler;
@property (T@"NSObject<OS_dispatch_source>",&,N,S_setCurrentTimer:,V__currentTimer) _currentTimer;
@property (TB,N,S_setFired:,V_fired) fired;
@property (Td,R,N,V_delay) delay;
@property (Td,R,N,V_interval) interval;
```

## Instance methods

```
-[CAMPreciseTimer interval];
-[CAMPreciseTimer init];
-[CAMPreciseTimer start];
-[CAMPreciseTimer delay];
-[CAMPreciseTimer invalidate];
-[CAMPreciseTimer _handler];
-[CAMPreciseTimer initWithDelay:interval:handler:];
-[CAMPreciseTimer _currentTimer];
-[CAMPreciseTimer _setCurrentTimer:];
-[CAMPreciseTimer _setFired:];
-[CAMPreciseTimer fired];
```
