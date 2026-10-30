# `CMMotionAlarm`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 8 instance variables, 8 properties, 22 instance methods, 1 class methods

## Instance variables

```
B _repeats;
I _duration;
I _type;
i _state;
@"NSString" _name;
Q _alarmId;
@"NSString" _bundleId;
@"CMMotionAlarmManager" _manager;
```

## Properties

```
@property (TQ,N,V_alarmId) alarmId;
@property (T@"NSString",&,N,V_bundleId) bundleId;
@property (Ti,N,V_state) state;
@property (T@"CMMotionAlarmManager",&,N,V_manager) manager;
@property (T@"NSString",R,&,N,V_name) name;
@property (TI,R,N,V_duration) duration;
@property (TB,R,N,V_repeats) repeats;
@property (TI,R,N,V_type) type;
```

## Class methods

```
+[CMMotionAlarm supportsSecureCoding];
```

## Instance methods

```
-[CMMotionAlarm repeats];
-[CMMotionAlarm setState:];
-[CMMotionAlarm setManager:];
-[CMMotionAlarm dealloc];
-[CMMotionAlarm setBundleId:];
-[CMMotionAlarm manager];
-[CMMotionAlarm duration];
-[CMMotionAlarm type];
-[CMMotionAlarm bundleId];
-[CMMotionAlarm encodeWithCoder:];
-[CMMotionAlarm isValid];
-[CMMotionAlarm description];
-[CMMotionAlarm initWithCoder:];
-[CMMotionAlarm name];
-[CMMotionAlarm state];
-[CMMotionAlarm alarmId];
-[CMMotionAlarm acknowledgeWithError:];
-[CMMotionAlarm copyPropertiesFromAlarm:];
-[CMMotionAlarm initWithName:type:duration:repeats:];
-[CMMotionAlarm initWithName:type:duration:repeats:alarmId:bundleId:state:];
-[CMMotionAlarm setAlarmId:];
-[CMMotionAlarm unregisterWithError:];
```
