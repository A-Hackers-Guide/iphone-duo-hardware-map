# `NWConcrete_nw_listener`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `nw_listener_inbox_delegate`, `OS_nw_listener`
- 49 instance variables, 4 properties, 15 instance methods, 0 class methods

## Instance variables

```
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} lock;
@"NSObject<OS_nw_parameters>" parameters;
@"NSObject<OS_nw_context>" context;
@"NSObject<OS_nw_group_descriptor>" multicast_descriptor;
S id_value;
[6c] id_str;
@"NWConcrete_nw_connection" join_connection;
* launchd_key;
@"NSObject<OS_dispatch_queue>" client_queue;
I client_qos_class;
@? event_handler;
@? new_connection_handler;
@? new_connection_group_handler;
I new_connection_limit;
@? new_packet_handler;
@? advertised_endpoint_changed_handler;
i state;
@"NSObject<OS_nw_error>" last_error;
@"NSObject<OS_nw_array>" inboxes;
@"NSObject<OS_nw_array>" flow_registrations;
@"NSObject<OS_nw_array>" proxy_connections;
@"NSObject<OS_nw_array>" connected_endpoints;
@"NSObject<OS_nw_path_evaluator>" evaluator;
@"NSObject<OS_nw_path>" path;
@"NSObject<OS_xpc_object>" inactive_agents;
@"NSObject<OS_nw_path>" inactive_agent_path;
@"NSObject<OS_xpc_object>" triggered_agents;
@"NSObject<OS_nw_parameters>" current_derived_parameters;
@"NSArray" authorized_keys;
C preferred_auth_method;
@"NSObject<OS_nw_array>" ids_info;
* device_id;
* device_name;
* device_model;
@"NSObject<OS_nw_txt_record>" device_txt_record;
S awdl_use_count;
^v advertise_new_connection_timer;
@"NWConcrete_nw_listener" internally_retained_object;
@"NSObject<OS_nw_advertise_descriptor>" advertise_descriptor;
@"NSArray" advertisers;
@"NSMutableDictionary" agentGeneration;
@"NSObject<OS_nw_endpoint>" advertised_endpoint;
@"NSObject<OS_nw_endpoint>" local_endpoint;
I defer_socket;
S port;
b1 cancelling;
b1 reported_state;
b1 allow_new_connection_inline;
b1 require_authorized_keys;
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
-[NWConcrete_nw_listener copyPeerDeviceModel];
-[NWConcrete_nw_listener canHandleNewConnection:];
-[NWConcrete_nw_listener copyPeerDeviceID];
-[NWConcrete_nw_listener copyPeerDeviceName];
-[NWConcrete_nw_listener dealloc];
-[NWConcrete_nw_listener handleInbound:addProtocolInbox:peerIdentity:];
-[NWConcrete_nw_listener handleInboxCancelComplete:];
-[NWConcrete_nw_listener updateParametersForNewConnection:];
-[NWConcrete_nw_listener handleInbound:addProtocolInbox:];
-[NWConcrete_nw_listener handleInboxFailed:error:];
-[NWConcrete_nw_listener getIDSInformation];
-[NWConcrete_nw_listener copyPeerTXTRecord];
-[NWConcrete_nw_listener description];
-[NWConcrete_nw_listener applyPeerIdentityToEndpoint:peerIdentity:];
-[NWConcrete_nw_listener handleInboundPacket:length:from:to:interface:socket:ipMetadata:];
```
