# `NWConcrete_nw_context`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_context`
- 33 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_workloop>" workloop;
* identifier;
^{nw_context_cache={_cache_entries_head=^{nw_association_cache_entry}^^{nw_association_cache_entry}}{_idle_cache_entries_head=^{nw_association_cache_entry}^^{nw_association_cache_entry}}^{nw_hash_table}^{nw_hash_table}^{nw_hash_table}^vII} cache;
^{nw_context_globals=^v{nw_timer_list_head=^{nw_timer_entry}^^{nw_timer_entry}}^{nw_hash_table}Q{mutex={os_unfair_lock_s=I}}{mutex={os_unfair_lock_s=I}}{mutex={os_unfair_lock_s=I}}^{nw_hash_table}^v^vQQ@@?@@@@^{nw_mem_buffer_manager}^{nw_mem_buffer_manager}^{nw_mem_buffer_manager}^{nw_mem_buffer_manager}^{nw_mem_buffer_manager}^{nw_mem_buffer_manager}^{nw_mem_buffer_manager}} globals;
@"NWConcrete_nw_context" isolated_context;
@"NSObject<OS_nw_resolver_config>" fallback_resolver_config;
@"NSObject<OS_nw_array>" proxy_configs;
@"NSObject<OS_dispatch_queue>" cached_targeted_queue;
@"NSObject<OS_dispatch_queue>" idle_block_queue;
@? idle_block;
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} activate_lock;
I max_cache_entries;
I target_cache_entries;
I max_idle_cache_entries;
q association_dormant_delay;
q context_purge_delay;
AQ inline_tid;
i scheduling_mode;
i privacy_level;
@? tracker_lookup_callback;
@? flow_count_increment_callback;
b1 isolate_protocol_stack;
b1 isolate_protocol_cache;
b1 is_implicit;
b1 is_inline;
b1 is_inline_and_cancelled;
b1 is_isolated_context;
b1 activated;
b1 required_encrypted_resolution;
b1 suppress_kernel_logging;
b1 has_active_instances;
b1 client_set_privacy_level;
b5 _pad_bits;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[NWConcrete_nw_context dealloc];
-[NWConcrete_nw_context redactedDescription];
-[NWConcrete_nw_context description];
```
