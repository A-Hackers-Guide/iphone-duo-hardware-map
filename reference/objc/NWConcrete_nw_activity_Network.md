# `NWConcrete_nw_activity`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_activity`
- 22 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
[16C] token;
Q investigation_identifier;
Q start_time;
Q end_time;
Q start_time_unix_nano;
Q end_time_unix_nano;
I fragments_quenched;
{retained_ptr<NWConcrete_nw_activity *>="m_obj"@"NWConcrete_nw_activity""m_should_release"b1"__pad_bits"b7"__pad_bytes"[7C]} parent;
* underlying_error_domain_string;
{unfair_mutex="m_mutex"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} lock;
{description_cache="description"{retained_ptr<NSString *>="m_obj"@"NSString""m_should_release"b1"__pad_bits"b7"__pad_bytes"[7C]}"mutex"{unfair_mutex="m_mutex"{os_unfair_lock_s="_os_unfair_lock_opaque"I}}"__pad"[4C]} description_cache;
I label;
I domain;
I client_metric_count;
i underlying_error_domain;
i underlying_error_code;
i reporting_strategy;
i completion_reason;
b1 is_retry;
b1 is_lightweight;
b1 activated;
b1 completed;
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
-[NWConcrete_nw_activity dealloc];
-[NWConcrete_nw_activity redactedDescription];
-[NWConcrete_nw_activity description];
```
