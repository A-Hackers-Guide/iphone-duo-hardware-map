# `BIThermalPredictionClient`

- Image: [`/System/Library/PrivateFrameworks/BatteryIntelligence.framework/BatteryIntelligence`](../userland/System__Library__PrivateFrameworks__BatteryIntelligence.framework__BatteryIntelligence.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BIThermalPredictionClientProtocol`
- 7 instance variables, 11 properties, 21 instance methods, 0 class methods

## Instance variables

```
i _reconnectToken;
@"<BIThermalPredictionDelegate>" _delegate;
@"NSObject<OS_os_log>" _logger;
@"NSObject<OS_dispatch_queue>" _queue;
@"BIThermalPredictionOutput" _cachedPrediction;
@"NSError" _cachedError;
@"NSXPCConnection" _connection;
```

## Properties

```
@property (T@"NSObject<OS_os_log>",&,N,V_logger) logger;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"BIThermalPredictionOutput",&,V_cachedPrediction) cachedPrediction;
@property (T@"NSError",&,V_cachedError) cachedError;
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (Ti,N,V_reconnectToken) reconnectToken;
@property (T@"<BIThermalPredictionDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BIThermalPredictionClient logger];
-[BIThermalPredictionClient setLogger:];
-[BIThermalPredictionClient init];
-[BIThermalPredictionClient dealloc];
-[BIThermalPredictionClient queue];
-[BIThermalPredictionClient setDelegate:];
-[BIThermalPredictionClient connection];
-[BIThermalPredictionClient delegate];
-[BIThermalPredictionClient setConnection:];
-[BIThermalPredictionClient setQueue:];
-[BIThermalPredictionClient registerForUpdates];
-[BIThermalPredictionClient setCachedError:];
-[BIThermalPredictionClient cachedError];
-[BIThermalPredictionClient cachedPrediction];
-[BIThermalPredictionClient didReceivePredictionUpdate:error:];
-[BIThermalPredictionClient predictTLCWithError:];
-[BIThermalPredictionClient reconnectToken];
-[BIThermalPredictionClient respondToReconnect];
-[BIThermalPredictionClient setCachedPrediction:];
-[BIThermalPredictionClient setReconnectToken:];
-[BIThermalPredictionClient updatePrediction];
```
