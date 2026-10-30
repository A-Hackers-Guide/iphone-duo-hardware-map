# `CAFValueMonitor`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _signaledReadyToMonitor;
@"NSObject<OS_dispatch_queue>" _monitorQueue;
@"<CAFValueMonitorDelegate>" _delegate;
@"NSMutableSet" _monitoringForValue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_monitorQueue) monitorQueue;
@property (T@"<CAFValueMonitorDelegate>",R,W,N,V_delegate) delegate;
@property (TB,N,V_signaledReadyToMonitor) signaledReadyToMonitor;
@property (T@"NSMutableSet",R,N,V_monitoringForValue) monitoringForValue;
@property (TB,R,N) receivedAllValues;
```

## Instance methods

```
-[CAFValueMonitor initWithDelegate:];
-[CAFValueMonitor delegate];
-[CAFValueMonitor monitorQueue];
-[CAFValueMonitor setMonitorQueue:];
-[CAFValueMonitor receivedAllValues];
-[CAFValueMonitor _locked_receivedAllValues];
-[CAFValueMonitor monitorForValue:];
-[CAFValueMonitor monitoringForValue];
-[CAFValueMonitor setSignaledReadyToMonitor:];
-[CAFValueMonitor signalReadyToMonitor];
-[CAFValueMonitor signaledReadyToMonitor];
-[CAFValueMonitor valueReceivedFor:];
```
