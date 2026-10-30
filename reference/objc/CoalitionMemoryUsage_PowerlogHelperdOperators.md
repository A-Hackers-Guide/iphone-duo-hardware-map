# `CoalitionMemoryUsage`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 12 properties, 24 instance methods, 0 class methods

## Instance variables

```
i _process_jetsam_priority;
Q _wired_size;
Q _purgeable_size;
Q _phys_footprint_size;
Q _compressed_size;
Q _process_count;
Q _process_phys_footprint_size;
Q _process_peak_phys_footprint;
Q _compressed_lifetime;
q _ledger_swapins;
Q _rss_size;
Q _n_files;
```

## Properties

```
@property (TQ,V_wired_size) wired_size;
@property (TQ,V_purgeable_size) purgeable_size;
@property (TQ,V_phys_footprint_size) phys_footprint_size;
@property (TQ,V_compressed_size) compressed_size;
@property (TQ,V_process_count) process_count;
@property (TQ,V_process_phys_footprint_size) process_phys_footprint_size;
@property (TQ,V_process_peak_phys_footprint) process_peak_phys_footprint;
@property (Ti,V_process_jetsam_priority) process_jetsam_priority;
@property (TQ,V_compressed_lifetime) compressed_lifetime;
@property (Tq,V_ledger_swapins) ledger_swapins;
@property (TQ,V_rss_size) rss_size;
@property (TQ,V_n_files) n_files;
```

## Instance methods

```
-[CoalitionMemoryUsage n_files];
-[CoalitionMemoryUsage setProcess_phys_footprint_size:];
-[CoalitionMemoryUsage compressed_size];
-[CoalitionMemoryUsage setProcess_peak_phys_footprint:];
-[CoalitionMemoryUsage compressed_lifetime];
-[CoalitionMemoryUsage ledger_swapins];
-[CoalitionMemoryUsage phys_footprint_size];
-[CoalitionMemoryUsage process_count];
-[CoalitionMemoryUsage process_jetsam_priority];
-[CoalitionMemoryUsage process_peak_phys_footprint];
-[CoalitionMemoryUsage process_phys_footprint_size];
-[CoalitionMemoryUsage purgeable_size];
-[CoalitionMemoryUsage rss_size];
-[CoalitionMemoryUsage setCompressed_lifetime:];
-[CoalitionMemoryUsage setCompressed_size:];
-[CoalitionMemoryUsage setLedger_swapins:];
-[CoalitionMemoryUsage setN_files:];
-[CoalitionMemoryUsage setPhys_footprint_size:];
-[CoalitionMemoryUsage setProcess_count:];
-[CoalitionMemoryUsage setProcess_jetsam_priority:];
-[CoalitionMemoryUsage setPurgeable_size:];
-[CoalitionMemoryUsage setRss_size:];
-[CoalitionMemoryUsage setWired_size:];
-[CoalitionMemoryUsage wired_size];
```
