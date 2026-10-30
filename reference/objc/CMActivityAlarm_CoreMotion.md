# `CMActivityAlarm`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 3 properties, 12 instance methods, 2 class methods

## Instance variables

```
B fIsValid;
^{__CFRunLoop=} fRunLoop;
@"NSObject<OS_dispatch_queue>" fQueue;
@? fHandler;
I _trigger;
d _duration;
d _activityDuration;
```

## Properties

```
@property (Td,N,V_duration) duration;
@property (TI,N,V_trigger) trigger;
@property (Td,N,V_activityDuration) activityDuration;
```

## Class methods

```
+[CMActivityAlarm activityAlarmAvailable];
+[CMActivityAlarm activityAlarmInfo];
```

## Instance methods

```
-[CMActivityAlarm trigger];
-[CMActivityAlarm fire];
-[CMActivityAlarm dealloc];
-[CMActivityAlarm duration];
-[CMActivityAlarm invalidate];
-[CMActivityAlarm isValid];
-[CMActivityAlarm setDuration:];
-[CMActivityAlarm setTrigger:];
-[CMActivityAlarm activityDuration];
-[CMActivityAlarm initWithTrigger:duration:onQueue:withHandler:];
-[CMActivityAlarm initWithTrigger:duration:onRunLoop:withHandler:];
-[CMActivityAlarm setActivityDuration:];
```
