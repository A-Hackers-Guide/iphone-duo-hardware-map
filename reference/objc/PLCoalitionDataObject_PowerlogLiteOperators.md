# `PLCoalitionDataObject`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
{coalition_resource_usage="tasks_started"Q"tasks_exited"Q"time_nonempty"Q"cpu_time"Q"interrupt_wakeups"Q"platform_idle_wakeups"Q"bytesread"Q"byteswritten"Q"gpu_time"Q"cpu_time_billed_to_me"Q"cpu_time_billed_to_others"Q"energy"Q"logical_immediate_writes"Q"logical_deferred_writes"Q"logical_invalidated_writes"Q"logical_metadata_writes"Q"logical_immediate_writes_to_external"Q"logical_deferred_writes_to_external"Q"logical_invalidated_writes_to_external"Q"logical_metadata_writes_to_external"Q"energy_billed_to_me"Q"energy_billed_to_others"Q"cpu_ptime"Q"cpu_time_eqos_len"Q"cpu_time_eqos"[7Q]"cpu_instructions"Q"cpu_cycles"Q"fs_metadata_writes"Q"pm_writes"Q"cpu_pinstructions"Q"cpu_pcycles"Q"conclave_mem"Q"ane_mach_time"Q"ane_energy_nj"Q"phys_footprint"Q"gpu_energy_nj"Q"gpu_energy_nj_billed_to_me"Q"gpu_energy_nj_billed_to_others"Q"swapins"Q"pages_grabbed"Q"pages_grabbed_kern"Q"pages_grabbed_iopl"Q"pages_grabbed_upl"Q"pageins"Q} _coalResourceUsage;
B _isUIKitApp;
@"NSString" _bundleID;
@"NSString" _launchdName;
Q _coalitionID;
@"CoalitionComputeMetrics" _metrics;
```

## Properties

```
@property (T@"NSString",&,V_bundleID) bundleID;
@property (T@"NSString",&,V_launchdName) launchdName;
@property (T^{coalition_resource_usage=QQQQQQQQQQQQQQQQQQQQQQQQ[7Q]QQQQQQQQQQQQQQQQQQQ},R) coalResourceUsage;
@property (TQ,V_coalitionID) coalitionID;
@property (T@"CoalitionComputeMetrics",&,V_metrics) metrics;
@property (TB,V_isUIKitApp) isUIKitApp;
```

## Instance methods

```
-[PLCoalitionDataObject setMetrics:];
-[PLCoalitionDataObject setBundleID:];
-[PLCoalitionDataObject description];
-[PLCoalitionDataObject bundleID];
-[PLCoalitionDataObject metrics];
-[PLCoalitionDataObject setLaunchdName:];
-[PLCoalitionDataObject setCoalitionID:];
-[PLCoalitionDataObject coalitionID];
-[PLCoalitionDataObject launchdName];
-[PLCoalitionDataObject coalResourceUsage];
-[PLCoalitionDataObject isUIKitApp];
-[PLCoalitionDataObject setIsUIKitApp:];
-[PLCoalitionDataObject updateWithResourceUsage:];
```
