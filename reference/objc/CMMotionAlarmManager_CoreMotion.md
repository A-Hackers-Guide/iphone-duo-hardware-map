# `CMMotionAlarmManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 12 instance methods, 2 class methods

## Instance variables

```
@"<CMMotionAlarmDelegateProtocol>" _delegate;
@"NSString" _name;
```

## Properties

```
@property (T@"<CMMotionAlarmDelegateProtocol>",N,V_delegate) delegate;
@property (T@"NSString",R,N,V_name) name;
```

## Class methods

```
+[CMMotionAlarmManager isAvailable];
+[CMMotionAlarmManager defaultManager];
```

## Instance methods

```
-[CMMotionAlarmManager init];
-[CMMotionAlarmManager dealloc];
-[CMMotionAlarmManager setDelegate:];
-[CMMotionAlarmManager delegate];
-[CMMotionAlarmManager name];
-[CMMotionAlarmManager initWithName:];
-[CMMotionAlarmManager acknowledgeAlarmWithName:error:];
-[CMMotionAlarmManager acknowledgeAlarm:error:];
-[CMMotionAlarmManager launchRemoteAppWithError:];
-[CMMotionAlarmManager registerAlarmWithName:type:duration:repeats:error:];
-[CMMotionAlarmManager unregisterAlarm:error:];
-[CMMotionAlarmManager unregisterAlarmWithName:error:];
```
