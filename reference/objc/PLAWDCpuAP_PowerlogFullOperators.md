# `PLAWDCpuAP`

- Image: [`/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators`](../userland/System__Library__PrivateFrameworks__PowerlogFullOperators.framework__PowerlogFullOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAWDAuxMetrics`
- 7 instance variables, 7 properties, 26 instance methods, 4 class methods

## Instance variables

```
B _isIoreportEnergy;
@"PLEntryNotificationOperatorComposition" _monitorEventCallback;
@"PLEntryNotificationOperatorComposition" _wakeEventCallback;
@"PLEntryNotificationOperatorComposition" _ioreportEnergyEventCallback;
@"NSDate" _sleepStartTime;
q _apSubmitCnt;
q _cpuLoadSubmitCnt;
```

## Properties

```
@property (T@"PLEntryNotificationOperatorComposition",&,V_monitorEventCallback) monitorEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_wakeEventCallback) wakeEventCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_ioreportEnergyEventCallback) ioreportEnergyEventCallback;
@property (T@"NSDate",&,V_sleepStartTime) sleepStartTime;
@property (TB,V_isIoreportEnergy) isIoreportEnergy;
@property (Tq,V_apSubmitCnt) apSubmitCnt;
@property (Tq,V_cpuLoadSubmitCnt) cpuLoadSubmitCnt;
```

## Class methods

```
+[PLAWDCpuAP entryAggregateDefinitions];
+[PLAWDCpuAP entryAggregateDefinitionAwdAp];
+[PLAWDCpuAP entryAggregateDefinitionAwdCpu];
+[PLAWDCpuAP getSharedObjWithOperator:];
```

## Instance methods

```
-[PLAWDCpuAP sleepStartTime];
-[PLAWDCpuAP setApSubmitCnt:];
-[PLAWDCpuAP setIoreportEnergyEventCallback:];
-[PLAWDCpuAP addEntryToApMetricsTable:withValue:];
-[PLAWDCpuAP apSubmitCnt];
-[PLAWDCpuAP cpuLoadSubmitCnt];
-[PLAWDCpuAP handleIOReportEnergyCallback:];
-[PLAWDCpuAP handleMonitorCallback:];
-[PLAWDCpuAP handleWakeCallback:];
-[PLAWDCpuAP ioreportEnergyEventCallback];
-[PLAWDCpuAP isIoreportEnergy];
-[PLAWDCpuAP monitorEventCallback];
-[PLAWDCpuAP resetApTable];
-[PLAWDCpuAP setCpuLoadSubmitCnt:];
-[PLAWDCpuAP setIsIoreportEnergy:];
-[PLAWDCpuAP setMonitorEventCallback:];
-[PLAWDCpuAP setSleepStartTime:];
-[PLAWDCpuAP setWakeEventCallback:];
-[PLAWDCpuAP startApMetricCollection:];
-[PLAWDCpuAP startCpuMetricCollection:];
-[PLAWDCpuAP startMetricCollection:];
-[PLAWDCpuAP stopMetricCollection:];
-[PLAWDCpuAP submitApDataToAWDServer:withAwdConn:];
-[PLAWDCpuAP submitCpuDataToAWDServer:withAwdConn:];
-[PLAWDCpuAP submitDataToAWDServer:withAwdConn:];
-[PLAWDCpuAP wakeEventCallback];
```
