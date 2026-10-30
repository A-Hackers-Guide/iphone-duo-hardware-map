# `ULSleepWakeEventAndDate`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 5 instance methods, 0 class methods

## Instance variables

```
i _sleepWakeState;
{time_point<cl::chrono::CFAbsoluteTimeClock, std::chrono::duration<long double>>="__d_"{duration<long double, std::ratio<1>>="__rep_"D}} _time;
```

## Properties

```
@property (Ti,N,V_sleepWakeState) sleepWakeState;
@property (T{time_point<cl::chrono::CFAbsoluteTimeClock, std::chrono::duration<long double>>={duration<long double, std::ratio<1>>=D}},N,V_time) time;
```

## Instance methods

```
-[ULSleepWakeEventAndDate setTime:];
-[ULSleepWakeEventAndDate time];
-[ULSleepWakeEventAndDate setSleepWakeState:];
-[ULSleepWakeEventAndDate sleepWakeState];
-[ULSleepWakeEventAndDate initWithSleepWakeEvent:andDate:];
```
