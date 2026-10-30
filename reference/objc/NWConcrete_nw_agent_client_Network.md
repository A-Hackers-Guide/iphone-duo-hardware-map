# `NWConcrete_nw_agent_client`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_agent_client`
- 14 instance variables, 4 properties, 1 instance methods, 0 class methods

## Instance variables

```
[16C] client_uuid;
[8c] log_string;
@"NSObject<OS_nw_endpoint>" endpoint;
@"NSObject<OS_nw_parameters>" parameters;
@"NSObject<OS_nw_path>" path;
@"NSObject<OS_nw_advertise_descriptor>" advertise_descriptor;
@"NSObject<OS_nw_browse_descriptor>" browse_descriptor;
@"NSObject<OS_nw_group_descriptor>" group_descriptor;
@"NSObject<OS_nw_channel>" channel;
@"NSObject<OS_nw_context>" client_context;
{retained_ptr<nw_protocol *>="m_obj"^{nw_protocol}"m_should_release"b1"__pad_bits"b7"__pad_bytes"[7C]} framer_protocol;
@"NSObject<OS_nw_path_flow_registration>" flow_registration;
@"NSObject<OS_nw_path_evaluator>" path_evaluator;
I assert_count;
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
-[NWConcrete_nw_agent_client dealloc];
```
