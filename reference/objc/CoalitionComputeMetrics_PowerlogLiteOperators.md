# `CoalitionComputeMetrics`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 37 instance variables, 37 properties, 75 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_metric_uint64_counter>" _tasks_started;
@"NSObject<OS_os_metric_uint64_counter>" _tasks_exited;
@"NSObject<OS_os_metric_uint64_counter>" _cpu_time;
@"NSObject<OS_os_metric_uint64_counter>" _interrupt_wakeups;
@"NSObject<OS_os_metric_uint64_counter>" _platform_idle_wakeups;
@"NSObject<OS_os_metric_uint64_counter>" _bytesread;
@"NSObject<OS_os_metric_uint64_counter>" _byteswritten;
@"NSObject<OS_os_metric_uint64_counter>" _gpu_time;
@"NSObject<OS_os_metric_uint64_counter>" _cpu_time_billed_to_me;
@"NSObject<OS_os_metric_uint64_counter>" _cpu_time_billed_to_others;
@"NSObject<OS_os_metric_uint64_counter>" _energy;
@"NSObject<OS_os_metric_uint64_counter>" _energy_billed_to_me;
@"NSObject<OS_os_metric_uint64_counter>" _energy_billed_to_others;
@"NSObject<OS_os_metric_uint64_counter>" _cpu_ptime;
@"NSMutableArray" _cpu_time_eqos;
@"NSObject<OS_os_metric_uint64_counter>" _cpu_instructions;
@"NSObject<OS_os_metric_uint64_counter>" _cpu_cycles;
@"NSObject<OS_os_metric_uint64_counter>" _fs_metadata_writes;
@"NSObject<OS_os_metric_uint64_counter>" _pm_writes;
@"NSObject<OS_os_metric_uint64_counter>" _cpu_pinstructions;
@"NSObject<OS_os_metric_uint64_counter>" _cpu_pcycles;
@"NSObject<OS_os_metric_double_gauge>" _conclave_mem;
@"NSObject<OS_os_metric_uint64_counter>" _ane_mach_time;
@"NSObject<OS_os_metric_uint64_counter>" _ane_energy_nj;
@"NSObject<OS_os_metric_double_gauge>" _phys_footprint;
@"NSObject<OS_os_metric_uint64_counter>" _gpu_energy_nj;
@"NSObject<OS_os_metric_uint64_counter>" _gpu_energy_nj_billed_to_me;
@"NSObject<OS_os_metric_uint64_counter>" _gpu_energy_nj_billed_to_others;
@"NSObject<OS_os_metric_uint64_counter>" _swapins;
@"NSObject<OS_os_metric_double_gauge>" _wired_size;
@"NSObject<OS_os_metric_double_gauge>" _purgeable_size;
@"NSObject<OS_os_metric_double_gauge>" _rss_size;
@"NSObject<OS_os_metric_double_gauge>" _anonmem_size;
@"NSObject<OS_os_metric_double_gauge>" _compressed_size;
@"NSObject<OS_os_metric_double_gauge>" _process_count;
@"NSObject<OS_os_metric_double_gauge>" _compressed_lifetime;
@"NSObject<OS_os_metric_double_gauge>" _n_files;
```

## Properties

```
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_tasks_started) tasks_started;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_tasks_exited) tasks_exited;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_cpu_time) cpu_time;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_interrupt_wakeups) interrupt_wakeups;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_platform_idle_wakeups) platform_idle_wakeups;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_bytesread) bytesread;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_byteswritten) byteswritten;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_gpu_time) gpu_time;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_cpu_time_billed_to_me) cpu_time_billed_to_me;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_cpu_time_billed_to_others) cpu_time_billed_to_others;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_energy) energy;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_energy_billed_to_me) energy_billed_to_me;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_energy_billed_to_others) energy_billed_to_others;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_cpu_ptime) cpu_ptime;
@property (T@"NSMutableArray",&,V_cpu_time_eqos) cpu_time_eqos;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_cpu_instructions) cpu_instructions;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_cpu_cycles) cpu_cycles;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_fs_metadata_writes) fs_metadata_writes;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_pm_writes) pm_writes;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_cpu_pinstructions) cpu_pinstructions;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_cpu_pcycles) cpu_pcycles;
@property (T@"NSObject<OS_os_metric_double_gauge>",&,V_conclave_mem) conclave_mem;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_ane_mach_time) ane_mach_time;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_ane_energy_nj) ane_energy_nj;
@property (T@"NSObject<OS_os_metric_double_gauge>",&,V_phys_footprint) phys_footprint;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_gpu_energy_nj) gpu_energy_nj;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_gpu_energy_nj_billed_to_me) gpu_energy_nj_billed_to_me;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_gpu_energy_nj_billed_to_others) gpu_energy_nj_billed_to_others;
@property (T@"NSObject<OS_os_metric_uint64_counter>",&,V_swapins) swapins;
@property (T@"NSObject<OS_os_metric_double_gauge>",&,V_wired_size) wired_size;
@property (T@"NSObject<OS_os_metric_double_gauge>",&,V_purgeable_size) purgeable_size;
@property (T@"NSObject<OS_os_metric_double_gauge>",&,V_rss_size) rss_size;
@property (T@"NSObject<OS_os_metric_double_gauge>",&,V_anonmem_size) anonmem_size;
@property (T@"NSObject<OS_os_metric_double_gauge>",&,V_compressed_size) compressed_size;
@property (T@"NSObject<OS_os_metric_double_gauge>",&,V_process_count) process_count;
@property (T@"NSObject<OS_os_metric_double_gauge>",&,V_compressed_lifetime) compressed_lifetime;
@property (T@"NSObject<OS_os_metric_double_gauge>",&,V_n_files) n_files;
```

## Instance methods

```
-[CoalitionComputeMetrics energy];
-[CoalitionComputeMetrics setEnergy:];
-[CoalitionComputeMetrics n_files];
-[CoalitionComputeMetrics swapins];
-[CoalitionComputeMetrics compressed_size];
-[CoalitionComputeMetrics setCpu_pcycles:];
-[CoalitionComputeMetrics ane_energy_nj];
-[CoalitionComputeMetrics ane_mach_time];
-[CoalitionComputeMetrics anonmem_size];
-[CoalitionComputeMetrics bytesread];
-[CoalitionComputeMetrics byteswritten];
-[CoalitionComputeMetrics compressed_lifetime];
-[CoalitionComputeMetrics conclave_mem];
-[CoalitionComputeMetrics cpu_cycles];
-[CoalitionComputeMetrics cpu_instructions];
-[CoalitionComputeMetrics cpu_pcycles];
-[CoalitionComputeMetrics cpu_pinstructions];
-[CoalitionComputeMetrics cpu_ptime];
-[CoalitionComputeMetrics cpu_time];
-[CoalitionComputeMetrics cpu_time_billed_to_me];
-[CoalitionComputeMetrics cpu_time_billed_to_others];
-[CoalitionComputeMetrics cpu_time_eqos];
-[CoalitionComputeMetrics energy_billed_to_me];
-[CoalitionComputeMetrics energy_billed_to_others];
-[CoalitionComputeMetrics fs_metadata_writes];
-[CoalitionComputeMetrics gpu_energy_nj];
-[CoalitionComputeMetrics gpu_energy_nj_billed_to_me];
-[CoalitionComputeMetrics gpu_energy_nj_billed_to_others];
-[CoalitionComputeMetrics gpu_time];
-[CoalitionComputeMetrics initWithCoalitionId:withBundleId:withLaunchDName:];
-[CoalitionComputeMetrics interrupt_wakeups];
-[CoalitionComputeMetrics phys_footprint];
-[CoalitionComputeMetrics platform_idle_wakeups];
-[CoalitionComputeMetrics pm_writes];
-[CoalitionComputeMetrics process_count];
-[CoalitionComputeMetrics purgeable_size];
-[CoalitionComputeMetrics rss_size];
-[CoalitionComputeMetrics setAne_energy_nj:];
-[CoalitionComputeMetrics setAne_mach_time:];
-[CoalitionComputeMetrics setAnonmem_size:];
-[CoalitionComputeMetrics setBytesread:];
-[CoalitionComputeMetrics setByteswritten:];
-[CoalitionComputeMetrics setCompressed_lifetime:];
-[CoalitionComputeMetrics setCompressed_size:];
-[CoalitionComputeMetrics setConclave_mem:];
-[CoalitionComputeMetrics setCpu_cycles:];
-[CoalitionComputeMetrics setCpu_instructions:];
-[CoalitionComputeMetrics setCpu_pinstructions:];
-[CoalitionComputeMetrics setCpu_ptime:];
-[CoalitionComputeMetrics setCpu_time:];
-[CoalitionComputeMetrics setCpu_time_billed_to_me:];
-[CoalitionComputeMetrics setCpu_time_billed_to_others:];
-[CoalitionComputeMetrics setCpu_time_eqos:];
-[CoalitionComputeMetrics setEnergy_billed_to_me:];
-[CoalitionComputeMetrics setEnergy_billed_to_others:];
-[CoalitionComputeMetrics setFs_metadata_writes:];
-[CoalitionComputeMetrics setGpu_energy_nj:];
-[CoalitionComputeMetrics setGpu_energy_nj_billed_to_me:];
-[CoalitionComputeMetrics setGpu_energy_nj_billed_to_others:];
-[CoalitionComputeMetrics setGpu_time:];
-[CoalitionComputeMetrics setInterrupt_wakeups:];
-[CoalitionComputeMetrics setN_files:];
-[CoalitionComputeMetrics setPhys_footprint:];
-[CoalitionComputeMetrics setPlatform_idle_wakeups:];
-[CoalitionComputeMetrics setPm_writes:];
-[CoalitionComputeMetrics setProcess_count:];
-[CoalitionComputeMetrics setPurgeable_size:];
-[CoalitionComputeMetrics setRss_size:];
-[CoalitionComputeMetrics setSwapins:];
-[CoalitionComputeMetrics setTasks_exited:];
-[CoalitionComputeMetrics setTasks_started:];
-[CoalitionComputeMetrics setWired_size:];
-[CoalitionComputeMetrics tasks_exited];
-[CoalitionComputeMetrics tasks_started];
-[CoalitionComputeMetrics wired_size];
```
