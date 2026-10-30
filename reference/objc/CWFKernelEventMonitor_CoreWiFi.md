# `CWFKernelEventMonitor`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 1 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _mutexQueue;
@"NSObject<OS_dispatch_queue>" _eventQueue;
@"NSObject<OS_dispatch_source>" _keventSource;
B _isMonitoringEvents;
@? _eventHandler;
```

## Properties

```
@property (T@?,C,V_eventHandler) eventHandler;
```

## Class methods

```
+[CWFKernelEventMonitor descriptionForKernelEventCode:];
```

## Instance methods

```
-[CWFKernelEventMonitor eventHandler];
-[CWFKernelEventMonitor setEventHandler:];
-[CWFKernelEventMonitor startEventMonitoring];
-[CWFKernelEventMonitor isMonitoringEvents];
-[CWFKernelEventMonitor init];
-[CWFKernelEventMonitor dealloc];
-[CWFKernelEventMonitor stopEventMonitoring];
-[CWFKernelEventMonitor interfaceFlagsWithInterfaceName:];
```
