# `PLPMUMetricsAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 3 instance variables, 3 properties, 15 instance methods, 3 class methods

## Instance variables

```
I _railEnergyPMUConn;
@"PLTimer" _railEnergyTimer;
@"NSDate" _lastEntryDate;
```

## Properties

```
@property (T@"PLTimer",&,V_railEnergyTimer) railEnergyTimer;
@property (TI,V_railEnergyPMUConn) railEnergyPMUConn;
@property (T@"NSDate",&,V_lastEntryDate) lastEntryDate;
```

## Class methods

```
+[PLPMUMetricsAgent load];
+[PLPMUMetricsAgent isEnabled];
+[PLPMUMetricsAgent buckNames];
```

## Instance methods

```
-[PLPMUMetricsAgent triggerRailEnergyLogging];
-[PLPMUMetricsAgent getTimestamp:withIndex:];
-[PLPMUMetricsAgent init];
-[PLPMUMetricsAgent setRailEnergyTimer:];
-[PLPMUMetricsAgent initOperatorDependancies];
-[PLPMUMetricsAgent railEnergyPMUConn];
-[PLPMUMetricsAgent setRailEnergyPMUConn:];
-[PLPMUMetricsAgent railEnergyTimer];
-[PLPMUMetricsAgent getBuckNameFromProperty:];
-[PLPMUMetricsAgent lastEntryDate];
-[PLPMUMetricsAgent parseAndLogRailEnergyMetrics:withEntryDate:];
-[PLPMUMetricsAgent connectToRailEnergyService];
-[PLPMUMetricsAgent getEnergy:withIndex:];
-[PLPMUMetricsAgent log];
-[PLPMUMetricsAgent setLastEntryDate:];
```
