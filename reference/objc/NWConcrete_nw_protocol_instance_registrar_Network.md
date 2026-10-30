# `NWConcrete_nw_protocol_instance_registrar`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_protocol_instance_registrar`
- 4 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} lock;
{nw_protocol_entry_list="lh_first"^{nw_protocol_entry}} instances;
{nw_protocol_identifier="name"[32c]"level"i"mapping"i} identifier;
Q instance_count;
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
-[NWConcrete_nw_protocol_instance_registrar dealloc];
-[NWConcrete_nw_protocol_instance_registrar redactedDescription];
-[NWConcrete_nw_protocol_instance_registrar description];
```
