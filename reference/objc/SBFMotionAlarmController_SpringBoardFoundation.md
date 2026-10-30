# `SBFMotionAlarmController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CMMotionAlarmDelegateProtocol`
- 2 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"<SBFMotionAlarmDelegate>" _delegate;
@"CMMotionAlarmManager" _motionAlarmManager;
```

## Properties

```
@property (T@"CMMotionAlarmManager",&,N,V_motionAlarmManager) motionAlarmManager;
@property (T@"<SBFMotionAlarmDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFMotionAlarmController init];
-[SBFMotionAlarmController dealloc];
-[SBFMotionAlarmController setDelegate:];
-[SBFMotionAlarmController delegate];
-[SBFMotionAlarmController _notifyDelegate];
-[SBFMotionAlarmController alarmDidFire:error:];
-[SBFMotionAlarmController alarmDidRegister:error:];
-[SBFMotionAlarmController alarmDidUnregister:error:];
-[SBFMotionAlarmController remoteAppLaunchedWithResult:error:];
-[SBFMotionAlarmController _registerMotionAlarm];
-[SBFMotionAlarmController _unregisterMotionAlarm];
-[SBFMotionAlarmController motionAlarmManager];
-[SBFMotionAlarmController registerMotionAlarm];
-[SBFMotionAlarmController setMotionAlarmManager:];
-[SBFMotionAlarmController unregisterMotionAlarm];
```
