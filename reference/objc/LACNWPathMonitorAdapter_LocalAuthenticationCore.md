# `LACNWPathMonitorAdapter`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACReachabilityProviding`
- 5 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_nw_path_monitor>" _pathMonitor;
@"NSObject<OS_dispatch_queue>" _monitoringQueue;
@? _statusUpdateHandler;
q _currentStatus;
B _isForwarding;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACNWPathMonitorAdapter init];
-[LACNWPathMonitorAdapter dealloc];
-[LACNWPathMonitorAdapter status];
-[LACNWPathMonitorAdapter stopMonitoring];
-[LACNWPathMonitorAdapter _handlePathUpdate:];
-[LACNWPathMonitorAdapter _networkStatusFromPathStatus:];
-[LACNWPathMonitorAdapter setStatusUpdateHandler:];
-[LACNWPathMonitorAdapter startMonitoringOnQueue:];
```
