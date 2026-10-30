# `PLNetworkAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 15 instance variables, 15 properties, 41 instance methods, 12 class methods

## Instance variables

```
i _wakeSocket;
@"PLEntryNotificationOperatorComposition" _batteryLevelChanged;
@"PLEntryNotificationOperatorComposition" _canSleep;
@"PLSemaphore" _canSleepSemaphore;
@"PLXPCListenerOperatorComposition" _downloadAutoAssetDownloadsListener;
@"PLXPCListenerOperatorComposition" _downloadV2AssetDownloadsListener;
@"NSObject<OS_nw_path_monitor>" _nwPathMonitorCellular;
@"NSObject<OS_nw_path_monitor>" _nwPathMonitorWiFi;
@"NSObject<OS_nw_path_monitor>" _nwPathMonitorWired;
@"NSObject<OS_nw_path_monitor>" _nwPathMonitorLoopback;
@"NSObject<OS_nw_path_monitor>" _nwPathMonitorOther;
@"NSObject<OS_dispatch_queue>" _nwPathMonitorQueue;
d _monitorCadence;
@"PLTimer" _monitorTimer;
@"NSMutableDictionary" _metrics;
```

## Properties

```
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryLevelChanged) batteryLevelChanged;
@property (T@"PLEntryNotificationOperatorComposition",&,V_canSleep) canSleep;
@property (T@"PLSemaphore",&,V_canSleepSemaphore) canSleepSemaphore;
@property (T@"PLXPCListenerOperatorComposition",&,V_downloadAutoAssetDownloadsListener) downloadAutoAssetDownloadsListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_downloadV2AssetDownloadsListener) downloadV2AssetDownloadsListener;
@property (Ti,N,V_wakeSocket) wakeSocket;
@property (T@"NSObject<OS_nw_path_monitor>",&,V_nwPathMonitorCellular) nwPathMonitorCellular;
@property (T@"NSObject<OS_nw_path_monitor>",&,V_nwPathMonitorWiFi) nwPathMonitorWiFi;
@property (T@"NSObject<OS_nw_path_monitor>",&,V_nwPathMonitorWired) nwPathMonitorWired;
@property (T@"NSObject<OS_nw_path_monitor>",&,V_nwPathMonitorLoopback) nwPathMonitorLoopback;
@property (T@"NSObject<OS_nw_path_monitor>",&,V_nwPathMonitorOther) nwPathMonitorOther;
@property (T@"NSObject<OS_dispatch_queue>",&,V_nwPathMonitorQueue) nwPathMonitorQueue;
@property (Td,V_monitorCadence) monitorCadence;
@property (T@"PLTimer",&,V_monitorTimer) monitorTimer;
@property (T@"NSMutableDictionary",&,V_metrics) metrics;
```

## Class methods

```
+[PLNetworkAgent entryEventIntervalDefinitions];
+[PLNetworkAgent entryEventPointDefinitions];
+[PLNetworkAgent entryEventForwardDefinitions];
+[PLNetworkAgent entryEventBackwardDefinitions];
+[PLNetworkAgent entryEventNoneDefinitions];
+[PLNetworkAgent load];
+[PLNetworkAgent defaults];
+[PLNetworkAgent accountingGroupDefinitions];
+[PLNetworkAgent railDefinitions];
+[PLNetworkAgent entryEventPointDefinitionWake];
+[PLNetworkAgent entryEventForwardDefinitionNetworkIsExpensive];
+[PLNetworkAgent entryEventPointDefinitionUnattributedWake];
```

## Instance methods

```
-[PLNetworkAgent setMetrics:];
-[PLNetworkAgent nwPathMonitorWiFi];
-[PLNetworkAgent logMobileAssetDownload:withCategory:];
-[PLNetworkAgent setDownloadV2AssetDownloadsListener:];
-[PLNetworkAgent canSleep];
-[PLNetworkAgent setNwPathMonitorWiFi:];
-[PLNetworkAgent setNwPathMonitorLoopback:];
-[PLNetworkAgent logEventBackwardCumulativeNetworkUsage:];
-[PLNetworkAgent setMonitorCadence:];
-[PLNetworkAgent init];
-[PLNetworkAgent setDownloadAutoAssetDownloadsListener:];
-[PLNetworkAgent logOSMetric:];
-[PLNetworkAgent nwPathMonitorWired];
-[PLNetworkAgent setMonitorTimer:];
-[PLNetworkAgent initOperatorDependancies];
-[PLNetworkAgent handleNWPathUpdate:];
-[PLNetworkAgent nwPathMonitorQueue];
-[PLNetworkAgent downloadAutoAssetDownloadsListener];
-[PLNetworkAgent setCanSleepSemaphore:];
-[PLNetworkAgent setNwPathMonitorOther:];
-[PLNetworkAgent setNwPathMonitorWired:];
-[PLNetworkAgent canSleepSemaphore];
-[PLNetworkAgent nwPathMonitorOther];
-[PLNetworkAgent setCanSleep:];
-[PLNetworkAgent downloadV2AssetDownloadsListener];
-[PLNetworkAgent initInterfaceMetrics];
-[PLNetworkAgent NWPathMonitorWithInterface:];
-[PLNetworkAgent setNwPathMonitorCellular:];
-[PLNetworkAgent monitorCadence];
-[PLNetworkAgent setBatteryLevelChanged:];
-[PLNetworkAgent setWakeSocket:];
-[PLNetworkAgent nwPathMonitorLoopback];
-[PLNetworkAgent log];
-[PLNetworkAgent metrics];
-[PLNetworkAgent setNwPathMonitorQueue:];
-[PLNetworkAgent monitorTimer];
-[PLNetworkAgent batteryLevelChanged];
-[PLNetworkAgent nwPathMonitorCellular];
-[PLNetworkAgent logEventPointWake];
-[PLNetworkAgent wakeSocket];
-[PLNetworkAgent initKernelEvent];
```
