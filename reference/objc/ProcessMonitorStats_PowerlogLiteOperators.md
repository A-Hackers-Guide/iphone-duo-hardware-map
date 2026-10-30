# `ProcessMonitorStats`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
B _shared_cache_reslid;
Q _cpu_time;
Q _cpu_time_diff;
```

## Properties

```
@property (TQ,V_cpu_time) cpu_time;
@property (TQ,V_cpu_time_diff) cpu_time_diff;
@property (TB,V_shared_cache_reslid) shared_cache_reslid;
```

## Instance methods

```
-[ProcessMonitorStats cpu_time];
-[ProcessMonitorStats cpu_time_diff];
-[ProcessMonitorStats setCpu_time:];
-[ProcessMonitorStats setCpu_time_diff:];
-[ProcessMonitorStats setShared_cache_reslid:];
-[ProcessMonitorStats shared_cache_reslid];
```
