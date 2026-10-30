# `CMSedentaryTimer_Internal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" fClientQueue;
@"NSObject<OS_dispatch_queue>" fDaemonQueue;
^v fLocationdConnection;
B _timerArmed;
```

## Properties

```
@property (TB,N,GisTimerArmed,V_timerArmed) timerArmed;
```

## Instance methods

```
-[CMSedentaryTimer_Internal _isActive];
-[CMSedentaryTimer_Internal init];
-[CMSedentaryTimer_Internal dealloc];
-[CMSedentaryTimer_Internal _teardown];
-[CMSedentaryTimer_Internal _handleAlarmDataResponse:withHandler:];
-[CMSedentaryTimer_Internal _handleStartStopTimerResponse:withHandler:];
-[CMSedentaryTimer_Internal _registerForAlarmsWithHandler:];
-[CMSedentaryTimer_Internal isTimerArmed];
-[CMSedentaryTimer_Internal setTimerArmed:];
```
