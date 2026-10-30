# `NWConcrete_nw_content_context`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_content_context`
- 21 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
[16C] packet_id;
[32c] identifier;
@"NWConcrete_nw_content_context" antecedent;
Q expiration_milliseconds;
Q enqueue_time;
d relative_priority;
@"NSObject<OS_nw_array>" protocol_metadatas;
@"NSObject<OS_nw_error>" error;
@"NSObject<OS_nw_array>" connection_group_info;
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} lock;
C app_type;
C app_metadata;
b1 is_final;
b1 expiration_checked;
b1 completed_send;
b1 has_packet_id;
b1 connection_group_connection;
b1 connection_group_multicast;
b1 supports_replies;
b1 is_wake_packet;
b1 has_app_metadata;
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
-[NWConcrete_nw_content_context dealloc];
-[NWConcrete_nw_content_context redactedDescription];
-[NWConcrete_nw_content_context description];
```
