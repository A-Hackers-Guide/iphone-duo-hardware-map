# `NWConcrete_nw_aop2_offload_ring`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_aop2_offload_ring`
- 13 instance variables, 4 properties, 2 instance methods, 0 class methods

## Instance variables

```
{nw_frame_array_s="tqh_first"^{nw_frame}"tqh_last"^^{nw_frame}} free_frame_array;
{nw_frame_array_s="tqh_first"^{nw_frame}"tqh_last"^^{nw_frame}} assigned_output_frame_array;
{nw_frame_array_s="tqh_first"^{nw_frame}"tqh_last"^^{nw_frame}} assigned_input_frame_array;
^{nw_hash_table=} input_clients;
@"NWConcrete_nw_aop2_offload_context_state" parent_context_state;
@"NSObject<OS_nw_interface>" interface;
Q total_allocated_frame_count;
Q num_frames;
I ring_id;
I assigned_output_frame_count;
I assigned_input_frame_count;
I clients_waiting_for_output_buffers;
B detaching;
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
-[NWConcrete_nw_aop2_offload_ring init];
-[NWConcrete_nw_aop2_offload_ring dealloc];
```
