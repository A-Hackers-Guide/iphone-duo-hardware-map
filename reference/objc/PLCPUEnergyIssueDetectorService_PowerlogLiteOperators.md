# `PLCPUEnergyIssueDetectorService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLService`
- 10 instance variables, 10 properties, 33 instance methods, 4 class methods

## Instance variables

```
B _deviceIsPluggedIn;
B _pluggedInBetweenCoalitionSBC;
@"PLEntryNotificationOperatorComposition" _coalitionCallback;
@"PLEntryNotificationOperatorComposition" _batteryCallback;
@"NSString" _entryKeyPLCoalitionAgentEventIntervalCoalition;
@"NSMutableDictionary" _cpuUsage;
@"NSArray" _cpuAllowList;
@"NSDictionary" _cpuThresholds;
@"NSDate" _detectionStartTime;
@"PLXPCListenerOperatorComposition" _detectorListener;
```

## Properties

```
@property (T@"PLEntryNotificationOperatorComposition",&,V_coalitionCallback) coalitionCallback;
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryCallback) batteryCallback;
@property (T@"NSString",R,V_entryKeyPLCoalitionAgentEventIntervalCoalition) entryKeyPLCoalitionAgentEventIntervalCoalition;
@property (TB,V_deviceIsPluggedIn) deviceIsPluggedIn;
@property (TB,V_pluggedInBetweenCoalitionSBC) pluggedInBetweenCoalitionSBC;
@property (T@"NSMutableDictionary",&,V_cpuUsage) cpuUsage;
@property (T@"NSArray",&,V_cpuAllowList) cpuAllowList;
@property (T@"NSDictionary",&,V_cpuThresholds) cpuThresholds;
@property (T@"NSDate",&,V_detectionStartTime) detectionStartTime;
@property (T@"PLXPCListenerOperatorComposition",&,V_detectorListener) detectorListener;
```

## Class methods

```
+[PLCPUEnergyIssueDetectorService load];
+[PLCPUEnergyIssueDetectorService defaults];
+[PLCPUEnergyIssueDetectorService entryAggregateDefinitions];
+[PLCPUEnergyIssueDetectorService entryAggregateDefinitionAppRunTime];
```

## Instance methods

```
-[PLCPUEnergyIssueDetectorService init];
-[PLCPUEnergyIssueDetectorService initOperatorDependancies];
-[PLCPUEnergyIssueDetectorService buildCallBack:withGroup:withHandler:];
-[PLCPUEnergyIssueDetectorService testService];
-[PLCPUEnergyIssueDetectorService cpuUsage];
-[PLCPUEnergyIssueDetectorService setCpuUsage:];
-[PLCPUEnergyIssueDetectorService batteryCallback];
-[PLCPUEnergyIssueDetectorService coalitionCallback];
-[PLCPUEnergyIssueDetectorService detectionStartTime];
-[PLCPUEnergyIssueDetectorService deviceIsPluggedIn];
-[PLCPUEnergyIssueDetectorService entryKeyPLCoalitionAgentEventIntervalCoalition];
-[PLCPUEnergyIssueDetectorService getCPUTime:];
-[PLCPUEnergyIssueDetectorService handleBatteryCallback:];
-[PLCPUEnergyIssueDetectorService handleCoalitionCallback:];
-[PLCPUEnergyIssueDetectorService sendEnergyIssueSignatureNotification:withThreshold:];
-[PLCPUEnergyIssueDetectorService setBatteryCallback:];
-[PLCPUEnergyIssueDetectorService setCoalitionCallback:];
-[PLCPUEnergyIssueDetectorService setDetectionStartTime:];
-[PLCPUEnergyIssueDetectorService setDeviceIsPluggedIn:];
-[PLCPUEnergyIssueDetectorService checkCpuUsage:withNewCoaltionArray:];
-[PLCPUEnergyIssueDetectorService cpuAllowList];
-[PLCPUEnergyIssueDetectorService cpuThresholds];
-[PLCPUEnergyIssueDetectorService customLongTermCPUThreshold];
-[PLCPUEnergyIssueDetectorService detectorListener];
-[PLCPUEnergyIssueDetectorService listAllRunningPidsWithBuffer:withSizeOfBuffer:];
-[PLCPUEnergyIssueDetectorService loadCPUAllowlist];
-[PLCPUEnergyIssueDetectorService loadCpuThresholds];
-[PLCPUEnergyIssueDetectorService matchingPidWithProcessName:withBundleID:];
-[PLCPUEnergyIssueDetectorService pluggedInBetweenCoalitionSBC];
-[PLCPUEnergyIssueDetectorService setCpuAllowList:];
-[PLCPUEnergyIssueDetectorService setCpuThresholds:];
-[PLCPUEnergyIssueDetectorService setDetectorListener:];
-[PLCPUEnergyIssueDetectorService setPluggedInBetweenCoalitionSBC:];
```
