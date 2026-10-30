# `ANSystemMonitor`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 2 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"<ANSystemUtilsProtocol>" _systemUtils;
@"ANMetricHeartbeatTimer" _heartbeatMonitor;
@"ANSleepMonitor" _sleepMonitor;
@"ANDataProtectionMonitor" _dataProtectionMonitor;
@"ANReachabilityMonitor" _reachabilityMonitor;
@"ANWifiMonitor" _wifiMonitor;
B _btStreaming;
B _wifiNetworkCritical;
i _isCoexImpacted;
B _isAssociatedTo2GHzWiFi;
i _audioStreamNotificationToken;
@"RTRoutineManager" _routineManager;
@"<ANSystemMonitorDelegate>" _delegate;
```

## Properties

```
@property (T@"<ANSystemMonitorDelegate>",N,V_delegate) delegate;
@property (Ti,R) coexImpactState;
```

## Instance methods

```
-[ANSystemMonitor _registerForNotifications];
-[ANSystemMonitor init];
-[ANSystemMonitor coexImpactState];
-[ANSystemMonitor dealloc];
-[ANSystemMonitor setDelegate:];
-[ANSystemMonitor delegate];
-[ANSystemMonitor _handleSystemWake];
-[ANSystemMonitor _handleSystemSleep];
-[ANSystemMonitor _checkAudioStreamState];
-[ANSystemMonitor _onMetricHeartbeat];
-[ANSystemMonitor _onRTVisit:];
-[ANSystemMonitor _onReachabilityChanged:];
-[ANSystemMonitor _recomputeCoexImpactedStateAndNotifyClients];
-[ANSystemMonitor fetchLOIVisitAtStart];
-[ANSystemMonitor initWithQueue:systemUtils:];
-[ANSystemMonitor setupSystemMonitor];
```
