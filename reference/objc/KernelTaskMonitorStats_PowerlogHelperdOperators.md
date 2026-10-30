# `KernelTaskMonitorStats`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
d _cpu_time;
Q _cpu_energy_p;
Q _cpu_energy_e;
Q _cpu_energy_m;
Q _thread_id;
@"NSString" _thread_name;
```

## Properties

```
@property (Td,V_cpu_time) cpu_time;
@property (TQ,V_cpu_energy_p) cpu_energy_p;
@property (TQ,V_cpu_energy_e) cpu_energy_e;
@property (TQ,V_cpu_energy_m) cpu_energy_m;
@property (TQ,V_thread_id) thread_id;
@property (T@"NSString",&,V_thread_name) thread_name;
```

## Instance methods

```
-[KernelTaskMonitorStats setThread_name:];
-[KernelTaskMonitorStats cpu_energy_e];
-[KernelTaskMonitorStats cpu_energy_m];
-[KernelTaskMonitorStats cpu_energy_p];
-[KernelTaskMonitorStats cpu_time];
-[KernelTaskMonitorStats setCpu_energy_e:];
-[KernelTaskMonitorStats setCpu_energy_m:];
-[KernelTaskMonitorStats setCpu_energy_p:];
-[KernelTaskMonitorStats setCpu_time:];
-[KernelTaskMonitorStats setThread_id:];
-[KernelTaskMonitorStats thread_id];
-[KernelTaskMonitorStats thread_name];
```
