# `WFPersonalHotspotStateMonitor`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"WFClient" _client;
@"NSObject<OS_dispatch_queue>" _internalQueue;
@"NSRunLoop" _callbackRunLoop;
@"NSThread" _callbackThread;
^{NETRBClient=} _netrbClient;
```

## Properties

```
@property (T@"WFClient",&,N,V_client) client;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_internalQueue) internalQueue;
@property (T@"NSRunLoop",V_callbackRunLoop) callbackRunLoop;
@property (T@"NSThread",&,N,V_callbackThread) callbackThread;
@property (T^{NETRBClient=},N,V_netrbClient) netrbClient;
```

## Instance methods

```
-[WFPersonalHotspotStateMonitor setMISDiscoveryState:immediateDisable:];
-[WFPersonalHotspotStateMonitor setCallbackThread:];
-[WFPersonalHotspotStateMonitor init];
-[WFPersonalHotspotStateMonitor setCallbackRunLoop:];
-[WFPersonalHotspotStateMonitor dealloc];
-[WFPersonalHotspotStateMonitor setClient:];
-[WFPersonalHotspotStateMonitor _runManagerCallbackThread];
-[WFPersonalHotspotStateMonitor asyncMISDiscoveryState:];
-[WFPersonalHotspotStateMonitor callbackThread];
-[WFPersonalHotspotStateMonitor setInternalQueue:];
-[WFPersonalHotspotStateMonitor callbackRunLoop];
-[WFPersonalHotspotStateMonitor client];
-[WFPersonalHotspotStateMonitor internalQueue];
-[WFPersonalHotspotStateMonitor clientConnections];
-[WFPersonalHotspotStateMonitor setNetrbClient:];
-[WFPersonalHotspotStateMonitor _spawnManagerCallbackThread];
-[WFPersonalHotspotStateMonitor _startMonitoringNETRBState];
-[WFPersonalHotspotStateMonitor netrbClient];
```
