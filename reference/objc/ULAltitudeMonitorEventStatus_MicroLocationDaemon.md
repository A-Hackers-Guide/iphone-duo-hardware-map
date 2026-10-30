# `ULAltitudeMonitorEventStatus`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULEvent`
- 5 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"ULAltitudeStatus" _altitudeStatus;
@"NSError" _error;
@"NSDate" _errorDate;
@"NSUUID" _altitudeSessionUUID;
@"NSNumber" _isRunning;
```

## Properties

```
@property (T@"ULAltitudeStatus",&,N,V_altitudeStatus) altitudeStatus;
@property (T@"NSError",&,N,V_error) error;
@property (T@"NSDate",&,N,V_errorDate) errorDate;
@property (T@"NSUUID",&,N,V_altitudeSessionUUID) altitudeSessionUUID;
@property (T@"NSNumber",&,N,V_isRunning) isRunning;
```

## Instance methods

```
-[ULAltitudeMonitorEventStatus isRunning];
-[ULAltitudeMonitorEventStatus setError:];
-[ULAltitudeMonitorEventStatus error];
-[ULAltitudeMonitorEventStatus setAltitudeSessionUUID:];
-[ULAltitudeMonitorEventStatus altitudeSessionUUID];
-[ULAltitudeMonitorEventStatus setIsRunning:];
-[ULAltitudeMonitorEventStatus altitudeStatus];
-[ULAltitudeMonitorEventStatus errorDate];
-[ULAltitudeMonitorEventStatus setAltitudeStatus:];
-[ULAltitudeMonitorEventStatus setErrorDate:];
```
