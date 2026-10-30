# `ULSleepWakeMonitor`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULEventMonitor`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
i _sleepWakeState;
@"CUSleepWakeMonitor" _sleepWakeMonitor;
```

## Properties

```
@property (T@"CUSleepWakeMonitor",&,N,V_sleepWakeMonitor) sleepWakeMonitor;
@property (Ti,N,V_sleepWakeState) sleepWakeState;
```

## Class methods

```
+[ULSleepWakeMonitor _internalSleepWakeStateFromCUSleepWakeState:];
```

## Instance methods

```
-[ULSleepWakeMonitor stopMonitoring:];
-[ULSleepWakeMonitor setSleepWakeMonitor:];
-[ULSleepWakeMonitor sleepWakeMonitor];
-[ULSleepWakeMonitor latestEventAfterAddingObserverForEventName:];
-[ULSleepWakeMonitor startMonitoring:];
-[ULSleepWakeMonitor setSleepWakeState:];
-[ULSleepWakeMonitor sleepWakeState];
-[ULSleepWakeMonitor _didUpdateSleepWakeState:];
```
