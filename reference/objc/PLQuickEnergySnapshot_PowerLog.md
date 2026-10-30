# `PLQuickEnergySnapshot`

- Image: [`/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog`](../userland/System__Library__PrivateFrameworks__PowerLog.framework__PowerLog.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSDate" _timestamp;
d _cpuEnergy;
d _networkEnergy;
```

## Properties

```
@property (T@"NSDate",&,V_timestamp) timestamp;
@property (Td,V_cpuEnergy) cpuEnergy;
@property (Td,V_networkEnergy) networkEnergy;
```

## Instance methods

```
-[PLQuickEnergySnapshot setTimestamp:];
-[PLQuickEnergySnapshot timestamp];
-[PLQuickEnergySnapshot description];
-[PLQuickEnergySnapshot computeEnergyDiff:];
-[PLQuickEnergySnapshot cpuEnergy];
-[PLQuickEnergySnapshot getTotalEnergy];
-[PLQuickEnergySnapshot initWithEnergies:andNetworkEnergy:];
-[PLQuickEnergySnapshot networkEnergy];
-[PLQuickEnergySnapshot setCpuEnergy:];
-[PLQuickEnergySnapshot setNetworkEnergy:];
```
