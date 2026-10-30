# `SampleAlgorithm`

- Image: [`/System/Library/PrivateFrameworks/BatteryAlgorithms.framework/BatteryAlgorithms`](../userland/System__Library__PrivateFrameworks__BatteryAlgorithms.framework__BatteryAlgorithms.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BAProtocol`
- 8 instance variables, 12 properties, 16 instance methods, 1 class methods

## Instance variables

```
B dataOnDemand;
B _freshInitNeeded;
@"NSString" _name;
@"NSString" _version;
@"NSString" _algoDescription;
@"NSNumber" _runPeriod;
^Q _runType;
@"NSObject<OS_os_log>" _logger;
```

## Properties

```
@property (T@"NSObject<OS_os_log>",&,N,V_logger) logger;
@property (T@"NSString",R,N,V_name) name;
@property (T@"NSString",R,N,V_version) version;
@property (T@"NSString",R,N,V_algoDescription) algoDescription;
@property (T@"NSNumber",R,N,V_runPeriod) runPeriod;
@property (T^Q,R,N,V_runType) runType;
@property (TB,R,N,V_freshInitNeeded) freshInitNeeded;
@property (TB,R,N,VdataOnDemand) dataOnDemand;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SampleAlgorithm algorithmWithData:];
```

## Instance methods

```
-[SampleAlgorithm logger];
-[SampleAlgorithm setLogger:];
-[SampleAlgorithm version];
-[SampleAlgorithm output];
-[SampleAlgorithm name];
-[SampleAlgorithm runWithData:];
-[SampleAlgorithm runType];
-[SampleAlgorithm algoDescription];
-[SampleAlgorithm freshInitNeeded];
-[SampleAlgorithm preRun:];
-[SampleAlgorithm dataOnDemand];
-[SampleAlgorithm freshInitWithData:];
-[SampleAlgorithm getWithSpecifier:];
-[SampleAlgorithm initWithSMCKeys:withSystemState:withSavedAlgoState:];
-[SampleAlgorithm runPeriod];
-[SampleAlgorithm updateWithSpecifier:];
```
