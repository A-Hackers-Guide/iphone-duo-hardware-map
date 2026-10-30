# `NWConcrete_nw_protocol_definition`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_protocol_definition`
- 28 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
{nw_protocol_identifier="name"[32c]"level"i"mapping"i} identifier;
[16C] unique_identifier;
i variant;
^{nw_protocol_definition_common_state=^?^?^?^?^?^?^?^?^?^?@?} common_state;
^{nw_protocol_definition_extended_state=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?II} extended_state;
^? allocate_options;
^? copy_options;
^? deallocate_options;
^? check_equality_options;
^? compare_options;
^? serialize_options;
^? deserialize_options;
^? allocate_metadata;
^? deallocate_metadata;
^? compare_metadata;
^? serialize_metadata;
^? deserialize_metadata;
@"NSObject<OS_nw_object>" swift_protocol_identifier;
^? swift_options_creator_function;
b1 framer;
b1 supports_replies;
b1 message_is_stream;
b1 receive_single_message;
b1 multipath;
b1 supports_discontiguous_data;
b1 has_global_definition;
b1 is_proxy;
b1 serialize_in_parameters;
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
-[NWConcrete_nw_protocol_definition init];
-[NWConcrete_nw_protocol_definition dealloc];
-[NWConcrete_nw_protocol_definition description];
```
