# `SAScanSessionTracker`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSDate" _sessionStartTime;
@"NSMutableSet" _devicesConnectedDuringSession;
```

## Properties

```
@property (T@"NSDate",&,N,V_sessionStartTime) sessionStartTime;
@property (T@"NSMutableSet",&,N,V_devicesConnectedDuringSession) devicesConnectedDuringSession;
@property (TB,R,N) hasActiveSession;
@property (T@"NSDate",R,N) scanStartTime;
```

## Instance methods

```
-[SAScanSessionTracker init];
-[SAScanSessionTracker reset];
-[SAScanSessionTracker hasActiveSession];
-[SAScanSessionTracker sessionStartTime];
-[SAScanSessionTracker setSessionStartTime:];
-[SAScanSessionTracker beginScanSessionAt:withCurrentlyConnectedDevices:];
-[SAScanSessionTracker deviceConnectedDuringScan:atTime:];
-[SAScanSessionTracker devicesConnectedDuringSession];
-[SAScanSessionTracker endScanSession];
-[SAScanSessionTracker scanStartTime];
-[SAScanSessionTracker setDevicesConnectedDuringSession:];
-[SAScanSessionTracker wasDeviceConnectedDuringSession:];
```
