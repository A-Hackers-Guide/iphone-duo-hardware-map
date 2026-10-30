# `CMActivityAlarmProxy`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
@ _internal;
^v fLocationdConnection;
i fAlarmCounter;
@"NSMutableDictionary" fAlarms;
@"NSObject<OS_dispatch_queue>" fReplyQueue;
B fAlarmAvailable;
```

## Class methods

```
+[CMActivityAlarmProxy sharedInstance];
```

## Instance methods

```
-[CMActivityAlarmProxy init];
-[CMActivityAlarmProxy dealloc];
-[CMActivityAlarmProxy activityAlarmAvailable];
-[CMActivityAlarmProxy listenForActivityAlarm:];
-[CMActivityAlarmProxy stopListeningForActivityAlarm:];
```
