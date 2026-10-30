# `CWFNetworkPathMonitor`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 10 properties, 30 instance methods, 0 class methods

## Instance variables

```
B _monitoring;
B _rawPathSatisfied;
B _reportedUnsatisfied;
@"NSObject<OS_dispatch_queue>" _targetQueue;
@? _networkPathStatusChanged;
@"NSObject<OS_dispatch_queue>" _internalQueue;
@"NSObject<OS_nw_path_monitor>" _pathMonitor;
@"NSObject<OS_dispatch_source>" _delayTimer;
Q _monitoringStartTimestamp;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,V_internalQueue) internalQueue;
@property (T@"NSObject<OS_nw_path_monitor>",&,V_pathMonitor) pathMonitor;
@property (T@"NSObject<OS_dispatch_source>",&,V_delayTimer) delayTimer;
@property (TB,V_monitoring) monitoring;
@property (TB,V_rawPathSatisfied) rawPathSatisfied;
@property (TB,V_reportedUnsatisfied) reportedUnsatisfied;
@property (TQ,V_monitoringStartTimestamp) monitoringStartTimestamp;
@property (TB,R) wifiPathSatisfied;
@property (T@"NSObject<OS_dispatch_queue>",&,V_targetQueue) targetQueue;
@property (T@?,C,V_networkPathStatusChanged) networkPathStatusChanged;
```

## Instance methods

```
-[CWFNetworkPathMonitor startMonitoring];
-[CWFNetworkPathMonitor setTargetQueue:];
-[CWFNetworkPathMonitor targetQueue];
-[CWFNetworkPathMonitor init];
-[CWFNetworkPathMonitor stopMonitoring];
-[CWFNetworkPathMonitor pathMonitor];
-[CWFNetworkPathMonitor delayTimer];
-[CWFNetworkPathMonitor invalidate];
-[CWFNetworkPathMonitor activate];
-[CWFNetworkPathMonitor setDelayTimer:];
-[CWFNetworkPathMonitor setInternalQueue:];
-[CWFNetworkPathMonitor setPathMonitor:];
-[CWFNetworkPathMonitor internalQueue];
-[CWFNetworkPathMonitor monitoring];
-[CWFNetworkPathMonitor setMonitoring:];
-[CWFNetworkPathMonitor __cancelDelayTimer];
-[CWFNetworkPathMonitor __reportPathSatisfied];
-[CWFNetworkPathMonitor __reportPathUnsatisfied];
-[CWFNetworkPathMonitor __startDelayTimer];
-[CWFNetworkPathMonitor __stopPathMonitor];
-[CWFNetworkPathMonitor __submitCoreAnalyticsEvent];
-[CWFNetworkPathMonitor monitoringStartTimestamp];
-[CWFNetworkPathMonitor networkPathStatusChanged];
-[CWFNetworkPathMonitor rawPathSatisfied];
-[CWFNetworkPathMonitor reportedUnsatisfied];
-[CWFNetworkPathMonitor setMonitoringStartTimestamp:];
-[CWFNetworkPathMonitor setNetworkPathStatusChanged:];
-[CWFNetworkPathMonitor setRawPathSatisfied:];
-[CWFNetworkPathMonitor setReportedUnsatisfied:];
-[CWFNetworkPathMonitor wifiPathSatisfied];
```
