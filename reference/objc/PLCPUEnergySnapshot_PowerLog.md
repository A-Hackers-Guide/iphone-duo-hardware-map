# `PLCPUEnergySnapshot`

- Image: [`/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog`](../userland/System__Library__PrivateFrameworks__PowerLog.framework__PowerLog.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 17 instance methods, 6 class methods

## Instance variables

```
Q _cpuEnergy;
Q _cpuEnergyBilledToMe;
Q _cpuEnergyBilledToOthers;
@"NSMutableDictionary" _mockData;
```

## Properties

```
@property (TQ,V_cpuEnergy) cpuEnergy;
@property (TQ,V_cpuEnergyBilledToMe) cpuEnergyBilledToMe;
@property (TQ,V_cpuEnergyBilledToOthers) cpuEnergyBilledToOthers;
@property (T@"NSMutableDictionary",&,V_mockData) mockData;
```

## Class methods

```
+[PLCPUEnergySnapshot coalitionIDToCoalitionNameMapping];
+[PLCPUEnergySnapshot identifierToAccountingName];
+[PLCPUEnergySnapshot identifierToCoalitionID];
+[PLCPUEnergySnapshot setCoalitionIDToCoalitionNameMapping:];
+[PLCPUEnergySnapshot setIdentifierToAccountingName:];
+[PLCPUEnergySnapshot setIdentifierToCoalitionID:];
```

## Instance methods

```
-[PLCPUEnergySnapshot isValid];
-[PLCPUEnergySnapshot description];
-[PLCPUEnergySnapshot mockData];
-[PLCPUEnergySnapshot setMockData:];
-[PLCPUEnergySnapshot initWithIdentifier:andMockData:];
-[PLCPUEnergySnapshot computeEnergyDiff:];
-[PLCPUEnergySnapshot computeEnergyDiffUntilNow:andAdjustSnapshotToNow:];
-[PLCPUEnergySnapshot cpuEnergy];
-[PLCPUEnergySnapshot cpuEnergyBilledToMe];
-[PLCPUEnergySnapshot cpuEnergyBilledToOthers];
-[PLCPUEnergySnapshot getCoalitionIDForIdentifier:];
-[PLCPUEnergySnapshot refreshCoalitionIDMapping];
-[PLCPUEnergySnapshot searchCoalitionsCacheForID:];
-[PLCPUEnergySnapshot setCpuEnergy:];
-[PLCPUEnergySnapshot setCpuEnergyBilledToMe:];
-[PLCPUEnergySnapshot setCpuEnergyBilledToOthers:];
-[PLCPUEnergySnapshot snapshotCPUEnergy:];
```
