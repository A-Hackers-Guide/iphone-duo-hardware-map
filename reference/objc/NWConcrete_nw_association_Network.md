# `NWConcrete_nw_association`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NWDeallocOnQueueObject`
- Protocols: `OS_nw_association`
- 12 instance variables, 0 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_nw_endpoint>" endpoint;
@"NSObject<OS_nw_path_parameters>" path_parameters;
@"NSObject<OS_nw_path_evaluator>" evaluator;
@"NSObject<OS_nw_path>" previous_path;
^{nw_hash_table=} handles;
^{nw_hash_table=} connected_flow_handles;
^{nw_hash_table=} cache_entries;
^v deactivation_timer;
I dry_run_count;
b1 dormant;
b1 in_force_update;
b6 __pad_bits;
```

## Class methods

```
+[NWConcrete_nw_association initialize];
```

## Instance methods

```
-[NWConcrete_nw_association dealloc];
-[NWConcrete_nw_association redactedDescription];
-[NWConcrete_nw_association copyContext];
-[NWConcrete_nw_association description];
```
