# `SAAlarmTask`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _alarmUUID;
@"NSDate" _fireDate;
@"<SATimeClientProtocol>" _client;
```

## Properties

```
@property (T@"NSUUID",C,N,V_alarmUUID) alarmUUID;
@property (T@"NSDate",C,N,V_fireDate) fireDate;
@property (T@"<SATimeClientProtocol>",W,N,V_client) client;
```

## Instance methods

```
-[SAAlarmTask fireDate];
-[SAAlarmTask setClient:];
-[SAAlarmTask setFireDate:];
-[SAAlarmTask client];
-[SAAlarmTask alarmUUID];
-[SAAlarmTask setAlarmUUID:];
```
