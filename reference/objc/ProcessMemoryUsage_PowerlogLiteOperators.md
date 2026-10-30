# `ProcessMemoryUsage`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 18 properties, 36 instance methods, 0 class methods

## Instance variables

```
B _isDaemonXPCService;
B _process_active;
B _isLimitHard;
B _isActiveLimit;
B _isLimitIncreased;
i _jetsam_priority;
i _memoryLimitMB;
@"NSString" _processName;
@"NSString" _bundleId;
@"NSString" _bundleVersion;
@"NSString" _processLaunchdName;
Q _phys_footprint_size;
Q _peak_phys_footprint;
Q _interval_peak_phys_footprint;
Q _neural_footprint;
Q _interval_peak_neural_footprint;
Q _conclave_footprint;
Q _timeAtPriorityMATU;
```

## Properties

```
@property (TB,V_isDaemonXPCService) isDaemonXPCService;
@property (T@"NSString",&,V_processName) processName;
@property (T@"NSString",&,V_bundleId) bundleId;
@property (T@"NSString",&,V_bundleVersion) bundleVersion;
@property (T@"NSString",&,V_processLaunchdName) processLaunchdName;
@property (TQ,V_phys_footprint_size) phys_footprint_size;
@property (TQ,V_peak_phys_footprint) peak_phys_footprint;
@property (TQ,V_interval_peak_phys_footprint) interval_peak_phys_footprint;
@property (TQ,V_neural_footprint) neural_footprint;
@property (TQ,V_interval_peak_neural_footprint) interval_peak_neural_footprint;
@property (TQ,V_conclave_footprint) conclave_footprint;
@property (Ti,V_jetsam_priority) jetsam_priority;
@property (TQ,V_timeAtPriorityMATU) timeAtPriorityMATU;
@property (TB,V_process_active) process_active;
@property (Ti,V_memoryLimitMB) memoryLimitMB;
@property (TB,V_isLimitHard) isLimitHard;
@property (TB,V_isActiveLimit) isActiveLimit;
@property (TB,V_isLimitIncreased) isLimitIncreased;
```

## Instance methods

```
-[ProcessMemoryUsage bundleVersion];
-[ProcessMemoryUsage setProcessName:];
-[ProcessMemoryUsage setBundleVersion:];
-[ProcessMemoryUsage setBundleId:];
-[ProcessMemoryUsage processName];
-[ProcessMemoryUsage bundleId];
-[ProcessMemoryUsage memoryLimitMB];
-[ProcessMemoryUsage jetsam_priority];
-[ProcessMemoryUsage setIsLimitHard:];
-[ProcessMemoryUsage conclave_footprint];
-[ProcessMemoryUsage interval_peak_neural_footprint];
-[ProcessMemoryUsage interval_peak_phys_footprint];
-[ProcessMemoryUsage isActiveLimit];
-[ProcessMemoryUsage isDaemonXPCService];
-[ProcessMemoryUsage isLimitHard];
-[ProcessMemoryUsage isLimitIncreased];
-[ProcessMemoryUsage neural_footprint];
-[ProcessMemoryUsage peak_phys_footprint];
-[ProcessMemoryUsage phys_footprint_size];
-[ProcessMemoryUsage processLaunchdName];
-[ProcessMemoryUsage process_active];
-[ProcessMemoryUsage setConclave_footprint:];
-[ProcessMemoryUsage setInterval_peak_neural_footprint:];
-[ProcessMemoryUsage setInterval_peak_phys_footprint:];
-[ProcessMemoryUsage setIsActiveLimit:];
-[ProcessMemoryUsage setIsDaemonXPCService:];
-[ProcessMemoryUsage setIsLimitIncreased:];
-[ProcessMemoryUsage setJetsam_priority:];
-[ProcessMemoryUsage setMemoryLimitMB:];
-[ProcessMemoryUsage setNeural_footprint:];
-[ProcessMemoryUsage setPeak_phys_footprint:];
-[ProcessMemoryUsage setPhys_footprint_size:];
-[ProcessMemoryUsage setProcessLaunchdName:];
-[ProcessMemoryUsage setProcess_active:];
-[ProcessMemoryUsage setTimeAtPriorityMATU:];
-[ProcessMemoryUsage timeAtPriorityMATU];
```
