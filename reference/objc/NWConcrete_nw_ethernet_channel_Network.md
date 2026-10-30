# `NWConcrete_nw_ethernet_channel`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_ethernet_channel`
- 26 instance variables, 4 properties, 1 instance methods, 0 class methods

## Instance variables

```
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} _lock;
S _ether_type;
@"NSObject<OS_nw_interface>" _interface;
r* _interfaceName;
i _state;
@"NSObject<OS_dispatch_queue>" _client_queue;
@? _client_state_handler;
@? _client_receive_handler;
@"NSObject<OS_nw_context>" _context;
@"NSObject<OS_nw_path_evaluator>" _evaluator;
@"NSObject<OS_nw_path_flow_registration>" _registration;
@"NSObject<OS_nw_path_flow>" _flow;
[6C] _flow_local_ethernet_address;
^v _input_source;
B _input_suspended;
B _cancelled;
B _delay_cancel;
[16C] _nexusInstance;
I _nexusPort;
[16C] _flowId;
^{channel=} _channel;
^{channel_attr=} _attributes;
i _channel_fd;
S _slot_size;
^{channel_ring_desc=} _rx_ring;
^{channel_ring_desc=} _tx_ring;
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
-[NWConcrete_nw_ethernet_channel dealloc];
```
