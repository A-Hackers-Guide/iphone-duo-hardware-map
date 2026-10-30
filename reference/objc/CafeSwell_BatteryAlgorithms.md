# `CafeSwell`

- Image: [`/System/Library/PrivateFrameworks/BatteryAlgorithms.framework/BatteryAlgorithms`](../userland/System__Library__PrivateFrameworks__BatteryAlgorithms.framework__BatteryAlgorithms.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BAProtocol`
- 12 instance variables, 16 properties, 26 instance methods, 1 class methods

## Instance variables

```
B _freshInitNeeded;
B _dataOnDemand;
@"NSString" _name;
@"NSString" _version;
@"NSString" _algoDescription;
@"NSNumber" _runPeriod;
^Q _runType;
@"NSObject<OS_os_log>" _logger;
^v _model;
d _previousACAMInitializationTime;
d _previousFreshInitializationTime;
@"NSMutableArray" _runningInfo;
```

## Properties

```
@property (T@"NSObject<OS_os_log>",&,N,V_logger) logger;
@property (T^v,N,V_model) model;
@property (Td,N,V_previousACAMInitializationTime) previousACAMInitializationTime;
@property (Td,N,V_previousFreshInitializationTime) previousFreshInitializationTime;
@property (T@"NSMutableArray",&,V_runningInfo) runningInfo;
@property (T@"NSString",R,N,V_name) name;
@property (T@"NSString",R,N,V_version) version;
@property (T@"NSString",R,N,V_algoDescription) algoDescription;
@property (T@"NSNumber",R,N,V_runPeriod) runPeriod;
@property (T^Q,R,N,V_runType) runType;
@property (TB,R,N,V_freshInitNeeded) freshInitNeeded;
@property (TB,R,N,V_dataOnDemand) dataOnDemand;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CafeSwell algorithmWithData:];
```

## Instance methods

```
-[CafeSwell model];
-[CafeSwell logger];
-[CafeSwell setLogger:];
-[CafeSwell setModel:];
-[CafeSwell version];
-[CafeSwell init:];
-[CafeSwell output];
-[CafeSwell name];
-[CafeSwell runWithData:];
-[CafeSwell previousFreshInitializationTime];
-[CafeSwell runType];
-[CafeSwell algoDescription];
-[CafeSwell freshInitNeeded];
-[CafeSwell preRun:];
-[CafeSwell setRunningInfo:];
-[CafeSwell dataOnDemand];
-[CafeSwell freshInitWithData:];
-[CafeSwell getCafeSwellConfig];
-[CafeSwell getWithSpecifier:];
-[CafeSwell multiLog:];
-[CafeSwell previousACAMInitializationTime];
-[CafeSwell runPeriod];
-[CafeSwell runningInfo];
-[CafeSwell setPreviousACAMInitializationTime:];
-[CafeSwell setPreviousFreshInitializationTime:];
-[CafeSwell updateWithSpecifier:];
```
