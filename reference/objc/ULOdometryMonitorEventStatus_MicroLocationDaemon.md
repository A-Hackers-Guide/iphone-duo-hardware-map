# `ULOdometryMonitorEventStatus`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULEvent`
- 5 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"ULOdometryStatus" _odometryStatus;
@"NSError" _error;
@"NSDate" _errorDate;
@"NSUUID" _trajectoryUUID;
@"NSNumber" _isRunning;
```

## Properties

```
@property (T@"ULOdometryStatus",&,N,V_odometryStatus) odometryStatus;
@property (T@"NSError",&,N,V_error) error;
@property (T@"NSDate",&,N,V_errorDate) errorDate;
@property (T@"NSUUID",&,N,V_trajectoryUUID) trajectoryUUID;
@property (T@"NSNumber",&,N,V_isRunning) isRunning;
```

## Instance methods

```
-[ULOdometryMonitorEventStatus isRunning];
-[ULOdometryMonitorEventStatus setError:];
-[ULOdometryMonitorEventStatus error];
-[ULOdometryMonitorEventStatus trajectoryUUID];
-[ULOdometryMonitorEventStatus setIsRunning:];
-[ULOdometryMonitorEventStatus setTrajectoryUUID:];
-[ULOdometryMonitorEventStatus errorDate];
-[ULOdometryMonitorEventStatus odometryStatus];
-[ULOdometryMonitorEventStatus setErrorDate:];
-[ULOdometryMonitorEventStatus setOdometryStatus:];
```
