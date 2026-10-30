# `NWConcrete_nw_browser`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_browser`
- 29 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} lock;
@"NSObject<OS_dispatch_queue>" client_queue;
i type;
@"NSObject<OS_nw_browse_descriptor>" descriptor;
@"NSObject<OS_nw_parameters>" parameters;
@"NWConcrete_nw_browser" internally_retained_object;
@? browse_results_changed_handler;
@? no_results_handler;
@? state_changed_handler;
i state;
@"NSObject<OS_nw_error>" error;
@"NSObject<OS_nw_path_evaluator>" browse_evaluator;
@"NSObject<OS_nw_path>" current_browse_path;
@"NSObject<OS_nw_dictionary>" browse_flow_registrations;
@"NSObject<OS_nw_array>" path_endpoint_array;
^{_DNSServiceRef_t=} main_dns_ref;
^{_DNSServiceRef_t=} secondary_dns_ref;
@"NSObject<OS_nw_array>" old_results;
@"NSObject<OS_nw_array>" new_results;
@"NSObject<OS_xpc_object>" dns_ref_map;
@"NSObject<OS_xpc_object>" changes_map;
@"NSObject<OS_nw_dictionary>" txt_record_map;
* description;
* logging_description;
I log_id;
B include_txt_record;
B sign_results;
B redact_logs;
B delivered_first_browse_result;
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
-[NWConcrete_nw_browser dealloc];
-[NWConcrete_nw_browser redactedDescription];
-[NWConcrete_nw_browser description];
```
