# `CMNetworkActivityMonitor`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
B _networkIsActive;
@"CMNetworkActivityObserver" _cmObserver;
q _showingNetworkActivityCount;
q _monitoringActiveCount;
```

## Properties

```
@property (T@"CMNetworkActivityObserver",&,N,SsetCMObserver:,V_cmObserver) cmObserver;
@property (Tq,N,V_showingNetworkActivityCount) showingNetworkActivityCount;
@property (Tq,N,V_monitoringActiveCount) monitoringActiveCount;
@property (TB,N,V_networkIsActive) networkIsActive;
```

## Class methods

```
+[CMNetworkActivityMonitor sharedActivityMonitor];
```

## Instance methods

```
-[CMNetworkActivityMonitor beginMonitoring];
-[CMNetworkActivityMonitor init];
-[CMNetworkActivityMonitor dealloc];
-[CMNetworkActivityMonitor endMonitoring];
-[CMNetworkActivityMonitor networkIsActive];
-[CMNetworkActivityMonitor setShowingNetworkActivityCount:];
-[CMNetworkActivityMonitor cmObserver];
-[CMNetworkActivityMonitor monitoringActiveCount];
-[CMNetworkActivityMonitor setCMObserver:];
-[CMNetworkActivityMonitor setMonitoringActiveCount:];
-[CMNetworkActivityMonitor setNetworkIsActive:];
-[CMNetworkActivityMonitor showingNetworkActivityCount];
```
