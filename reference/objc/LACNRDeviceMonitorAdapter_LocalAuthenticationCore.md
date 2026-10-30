# `LACNRDeviceMonitorAdapter`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NRDeviceMonitorDelegate`, `LACNRDeviceMonitorAdapter`
- 6 instance variables, 5 properties, 6 instance methods, 0 class methods

## Instance variables

```
@? _reachableStatusDidChange;
@"NRDeviceMonitor" _deviceMonitor;
B _isMonitoring;
B _isNearby;
B _isConnected;
B _lastReportedReachable;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) isReachable;
```

## Instance methods

```
-[LACNRDeviceMonitorAdapter isReachable];
-[LACNRDeviceMonitorAdapter stopMonitoring];
-[LACNRDeviceMonitorAdapter deviceIsConnectedDidChange:isConnected:];
-[LACNRDeviceMonitorAdapter deviceIsNearbyDidChange:isNearby:];
-[LACNRDeviceMonitorAdapter reportReachableStateIfChanged];
-[LACNRDeviceMonitorAdapter startMonitoringOnQueue:statusDidChange:completion:];
```
