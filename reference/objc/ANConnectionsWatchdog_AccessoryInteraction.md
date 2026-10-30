# `ANConnectionsWatchdog`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 5 properties, 17 instance methods, 0 class methods

## Instance variables

```
@? _connectionTimeoutBlock;
@"NSObject<OS_dispatch_queue>" _queue;
@"CBCentralManager" _centralManager;
@"ANMetricManager" _metricManager;
@"<ANSystemUtilsProtocol>" _systemUtils;
@"NSMutableDictionary" _watchdoggedConnections;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,&,V_queue) queue;
@property (T@"CBCentralManager",R,&,V_centralManager) centralManager;
@property (T@"ANMetricManager",R,&,V_metricManager) metricManager;
@property (T@"<ANSystemUtilsProtocol>",R,&,V_systemUtils) systemUtils;
@property (T@"NSMutableDictionary",R,&,V_watchdoggedConnections) watchdoggedConnections;
```

## Instance methods

```
-[ANConnectionsWatchdog metricManager];
-[ANConnectionsWatchdog centralManager];
-[ANConnectionsWatchdog init];
-[ANConnectionsWatchdog dealloc];
-[ANConnectionsWatchdog queue];
-[ANConnectionsWatchdog cancelPeripheralConnection:];
-[ANConnectionsWatchdog systemUtils];
-[ANConnectionsWatchdog evaluateTimeout];
-[ANConnectionsWatchdog clearConnectionTimeout];
-[ANConnectionsWatchdog connectionTimeoutBlockExists];
-[ANConnectionsWatchdog didConnectPeripheral:shouldWatchdog:accessoryTypeName:];
-[ANConnectionsWatchdog didDisconnectPeripheral:error:];
-[ANConnectionsWatchdog didUpdateConnectionParameters:interval:latency:shouldWatchdog:accessoryTypeName:];
-[ANConnectionsWatchdog evaluateWatchdoggedConnections];
-[ANConnectionsWatchdog initWithQueue:centralManager:metricManager:systemUtils:];
-[ANConnectionsWatchdog scheduleConnectionTimeout:];
-[ANConnectionsWatchdog watchdoggedConnections];
```
