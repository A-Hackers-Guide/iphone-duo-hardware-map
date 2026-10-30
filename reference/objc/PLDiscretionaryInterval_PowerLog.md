# `PLDiscretionaryInterval`

- Image: [`/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog`](../userland/System__Library__PrivateFrameworks__PowerLog.framework__PowerLog.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSDate" _originalStartDate;
@"NSDate" _currentStartDate;
@"NSDate" _endDate;
@"PLCPUEnergySnapshot" _cpuEnergySnapshot;
@"PLNetworkUsageSnapshot" _networkEnergySnapshot;
d _startCount;
d _openCount;
```

## Properties

```
@property (T@"NSDate",&,V_originalStartDate) originalStartDate;
@property (T@"NSDate",&,V_currentStartDate) currentStartDate;
@property (T@"NSDate",&,V_endDate) endDate;
@property (T@"PLCPUEnergySnapshot",&,V_cpuEnergySnapshot) cpuEnergySnapshot;
@property (T@"PLNetworkUsageSnapshot",&,V_networkEnergySnapshot) networkEnergySnapshot;
@property (Td,V_startCount) startCount;
@property (Td,V_openCount) openCount;
```

## Instance methods

```
-[PLDiscretionaryInterval originalStartDate];
-[PLDiscretionaryInterval isClosed];
-[PLDiscretionaryInterval endDate];
-[PLDiscretionaryInterval setOriginalStartDate:];
-[PLDiscretionaryInterval setStartCount:];
-[PLDiscretionaryInterval setEndDate:];
-[PLDiscretionaryInterval description];
-[PLDiscretionaryInterval startCount];
-[PLDiscretionaryInterval openCount];
-[PLDiscretionaryInterval setOpenCount:];
-[PLDiscretionaryInterval shouldClose];
-[PLDiscretionaryInterval checkOpenIntervalDuration:];
-[PLDiscretionaryInterval closeInterval];
-[PLDiscretionaryInterval cpuEnergySnapshot];
-[PLDiscretionaryInterval currentStartDate];
-[PLDiscretionaryInterval initWithIdentifier:andInfo:andSnapshottingEnabled:andMockData:];
-[PLDiscretionaryInterval networkEnergySnapshot];
-[PLDiscretionaryInterval setCpuEnergySnapshot:];
-[PLDiscretionaryInterval setCurrentStartDate:];
-[PLDiscretionaryInterval setNetworkEnergySnapshot:];
```
