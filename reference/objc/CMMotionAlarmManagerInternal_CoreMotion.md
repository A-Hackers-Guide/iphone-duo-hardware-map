# `CMMotionAlarmManagerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 10 instance methods, 1 class methods

## Instance variables

```
^v fLocationdConnection;
@"NSObject<OS_dispatch_queue>" fInternalQueue;
@"NSMutableDictionary" fAlarms;
B fListening;
```

## Class methods

```
+[CMMotionAlarmManagerInternal instance];
```

## Instance methods

```
-[CMMotionAlarmManagerInternal init];
-[CMMotionAlarmManagerInternal dealloc];
-[CMMotionAlarmManagerInternal _teardown];
-[CMMotionAlarmManagerInternal _startListeners];
-[CMMotionAlarmManagerInternal _acknowledgeAlarm:error:];
-[CMMotionAlarmManagerInternal _handleAlarmFire:];
-[CMMotionAlarmManagerInternal _launchRemoteAppWithError:delegate:];
-[CMMotionAlarmManagerInternal _registerAlarm:error:];
-[CMMotionAlarmManagerInternal _stopListeners];
-[CMMotionAlarmManagerInternal _unregisterAlarm:error:];
```
