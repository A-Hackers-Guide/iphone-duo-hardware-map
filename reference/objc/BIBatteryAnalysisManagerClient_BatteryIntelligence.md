# `BIBatteryAnalysisManagerClient`

- Image: [`/System/Library/PrivateFrameworks/BatteryIntelligence.framework/BatteryIntelligence`](../userland/System__Library__PrivateFrameworks__BatteryIntelligence.framework__BatteryIntelligence.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logger;
@"NSXPCConnection" _connection;
```

## Properties

```
@property (T@"NSObject<OS_os_log>",&,N,V_logger) logger;
@property (T@"NSXPCConnection",&,N,V_connection) connection;
```

## Instance methods

```
-[BIBatteryAnalysisManagerClient logger];
-[BIBatteryAnalysisManagerClient setLogger:];
-[BIBatteryAnalysisManagerClient init];
-[BIBatteryAnalysisManagerClient dealloc];
-[BIBatteryAnalysisManagerClient connection];
-[BIBatteryAnalysisManagerClient setConnection:];
-[BIBatteryAnalysisManagerClient adHocRunWithError:];
-[BIBatteryAnalysisManagerClient updateTarget:withEstimate:withError:];
```
