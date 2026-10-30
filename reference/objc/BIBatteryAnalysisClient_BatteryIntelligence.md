# `BIBatteryAnalysisClient`

- Image: [`/System/Library/PrivateFrameworks/BatteryIntelligence.framework/BatteryIntelligence`](../userland/System__Library__PrivateFrameworks__BatteryIntelligence.framework__BatteryIntelligence.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 32 instance methods, 0 class methods

## Instance variables

```
B _trackAccessoryEstimates;
@"<BIBatteryAnalysisDelegate>" _delegate;
@"NSObject<OS_os_log>" _logger;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSSet" _targets;
@"NSMutableDictionary" _targetOutputs;
@"NSMutableDictionary" _accessoryEstimates;
@"NSError" _accessoryEstimatesFetchError;
@"NSXPCConnection" _connection;
@"NSMutableSet" _notificationTokens;
```

## Properties

```
@property (T@"NSObject<OS_os_log>",&,N,V_logger) logger;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSSet",&,N,V_targets) targets;
@property (T@"NSMutableDictionary",&,N,V_targetOutputs) targetOutputs;
@property (T@"NSMutableDictionary",&,N,V_accessoryEstimates) accessoryEstimates;
@property (T@"NSError",&,N,V_accessoryEstimatesFetchError) accessoryEstimatesFetchError;
@property (TB,N,V_trackAccessoryEstimates) trackAccessoryEstimates;
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (T@"NSMutableSet",&,N,V_notificationTokens) notificationTokens;
@property (T@"<BIBatteryAnalysisDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[BIBatteryAnalysisClient logger];
-[BIBatteryAnalysisClient setLogger:];
-[BIBatteryAnalysisClient dealloc];
-[BIBatteryAnalysisClient queue];
-[BIBatteryAnalysisClient setDelegate:];
-[BIBatteryAnalysisClient connection];
-[BIBatteryAnalysisClient delegate];
-[BIBatteryAnalysisClient targets];
-[BIBatteryAnalysisClient setConnection:];
-[BIBatteryAnalysisClient initWithTargets:];
-[BIBatteryAnalysisClient setQueue:];
-[BIBatteryAnalysisClient setTargets:];
-[BIBatteryAnalysisClient estimateForTarget:withError:];
-[BIBatteryAnalysisClient accessoryEstimates];
-[BIBatteryAnalysisClient accessoryEstimatesFetchError];
-[BIBatteryAnalysisClient accessoryEstimatesFromCache:];
-[BIBatteryAnalysisClient accessoryEstimatesWithError:];
-[BIBatteryAnalysisClient estimateFromCache:withError:];
-[BIBatteryAnalysisClient formattedEstimateForOutput:];
-[BIBatteryAnalysisClient initWithTargets:trackAccessoryEstimates:];
-[BIBatteryAnalysisClient notificationTokens];
-[BIBatteryAnalysisClient registerForAccessoryEstimateUpdates];
-[BIBatteryAnalysisClient registerForUpdatesToTarget:];
-[BIBatteryAnalysisClient setAccessoryEstimates:];
-[BIBatteryAnalysisClient setAccessoryEstimatesFetchError:];
-[BIBatteryAnalysisClient setNotificationTokens:];
-[BIBatteryAnalysisClient setTargetOutputs:];
-[BIBatteryAnalysisClient setTrackAccessoryEstimates:];
-[BIBatteryAnalysisClient targetOutputs];
-[BIBatteryAnalysisClient trackAccessoryEstimates];
-[BIBatteryAnalysisClient updateAccessoryEstimates];
-[BIBatteryAnalysisClient updateEstimateForTarget:];
```
