# `NWConcrete_nw_framer`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_framer`
- 57 instance variables, 4 properties, 2 instance methods, 0 class methods

## Instance variables

```
{nw_protocol_stub_s=} protocol;
@"NSObject<OS_nw_protocol_definition>" parent_definition;
{nw_protocol_callbacks="add_input_handler"^?"remove_input_handler"^?"replace_input_handler"^?"connect"^?"disconnect"^?"connected"^?"disconnected"^?"error"^?"input_available"^?"output_available"^?"get_input_frames"^?"get_output_frames"^?"finalize_output_frames"^?"link_state"^?"get_parameters"^?"get_path"^?"get_local_endpoint"^?"get_remote_endpoint"^?"register_notification"^?"unregister_notification"^?"notify"^?"updated_path"^?"supports_external_data"^?"input_finished"^?"output_finished"^?"get_output_local_endpoint"^?"get_output_interface"^?"waiting_for_output"^?"copy_info"^?"add_listen_handler"^?"remove_listen_handler"^?"get_message_properties"^?"reset"^?"input_flush"^?"log_send_state"^?} callbacks;
^v internal_reference;
@"NSObject<OS_nw_endpoint>" endpoint;
@"NSObject<OS_nw_parameters>" parameters;
@"NSObject<OS_nw_context>" context;
@"NSObject<OS_nw_dictionary>" connection_state;
@"NSObject<OS_nw_protocol_metadata>" pending_inbound_message;
@? start;
@? parse_input;
@? write_output;
@? wakeup;
@? stop;
@? cleanup;
@? copy_metadata;
Q handshake_milliseconds;
Q handshake_rtt_milliseconds;
{nw_frame_array_s="tqh_first"^{nw_frame}"tqh_last"^^{nw_frame}} inbound_frames;
{nw_frame_array_s="tqh_first"^{nw_frame}"tqh_last"^^{nw_frame}} outbound_frames;
Q input_needed;
Q input_body_remaining;
{nw_frame_array_s="tqh_first"^{nw_frame}"tqh_last"^^{nw_frame}} received_input_frames;
{nw_frame_array_s="tqh_first"^{nw_frame}"tqh_last"^^{nw_frame}} pending_input_frames;
I pending_input_frame_count;
@"NSObject<OS_nw_array>" output_data_array;
@? wakeup_block;
{nw_frame_array_s="tqh_first"^{nw_frame}"tqh_last"^^{nw_frame}} received_output_frames;
@"NSObject<OS_nw_protocol_metadata>" pending_output_message;
I pending_output_message_length;
I pending_output_frames;
I pending_output_cursor;
S prepended_log_id_num;
b1 supports_external_data;
b1 output_frame_as_message;
b1 in_start;
b1 called_start;
b1 ready;
b1 flow_controlled;
b1 waiting_for_flow_control;
b1 in_input_callout;
b1 in_input_available;
b1 new_input_available;
b1 in_output_callout;
b1 pending_input_should_mark_complete;
b1 pending_output_message_complete;
b1 pending_output_connection_complete;
b1 pending_output_finished;
b1 failed;
b1 pass_through_input;
b1 pass_through_output;
b1 input_suspended;
b1 wait_for_early_data;
b1 block_lower_metadata;
b1 input_available_unacknowledged;
b1 output_blocked;
[84c] log_str;
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
-[NWConcrete_nw_framer init];
-[NWConcrete_nw_framer destroy];
```
