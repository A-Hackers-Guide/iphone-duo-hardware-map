# `Core_Audio_Driver_Host`

- Image: [`/System/Library/Frameworks/CoreAudio.framework/CoreAudio`](../userland/System__Library__Frameworks__CoreAudio.framework__CoreAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`, `Core_Audio_Driver_Host_Protocol`
- 10 instance variables, 14 properties, 50 instance methods, 0 class methods

## Instance variables

```
@"NSXPCConnection" _connection_to_driver;
@"NSXPCConnection" _connection_from_driver;
@"NSXPCListener" _listener;
@"NSXPCListenerEndpoint" _endpoint;
@"<Core_Audio_Driver_Host_Callback_Delegate>" _delegate;
@"Protocol" _driver_protocol;
@"Protocol" _driver_host_protocol;
@"NSXPCListenerEndpoint" _driver_endpoint;
{shared_ptr<Property_Type_Info>="__ptr_"^{Property_Type_Info}"__cntrl_"^{__shared_weak_count}} _m_custom_property_type_cache;
{function<void ()>="__f_"{__value_func<void ()>="__buf_"(type="__data"[24C])"__f_"^v}} _m_invalidation_handler;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_connection_to_driver) connection_to_driver;
@property (T@"NSXPCConnection",&,N,V_connection_from_driver) connection_from_driver;
@property (T@"NSXPCListener",&,N,V_listener) listener;
@property (T@"NSXPCListenerEndpoint",&,N,V_endpoint) endpoint;
@property (T@"NSXPCListenerEndpoint",&,N,V_driver_endpoint) driver_endpoint;
@property (T@"<Core_Audio_Driver_Host_Callback_Delegate>",&,N,V_delegate) delegate;
@property (T@"Protocol",&,N,V_driver_host_protocol) driver_host_protocol;
@property (T@"Protocol",&,N,V_driver_protocol) driver_protocol;
@property (T{shared_ptr<Property_Type_Info>=^{Property_Type_Info}^{__shared_weak_count}},N,V_m_custom_property_type_cache) m_property_type_info;
@property (T{function<void ()>={__value_func<void ()>=(type=[24C])^v}},N,V_m_invalidation_handler) m_invalidation_handler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[Core_Audio_Driver_Host setEndpoint:];
-[Core_Audio_Driver_Host listener:shouldAcceptNewConnection:];
-[Core_Audio_Driver_Host init];
-[Core_Audio_Driver_Host stop_io:client_info:];
-[Core_Audio_Driver_Host dealloc];
-[Core_Audio_Driver_Host m_invalidation_handler];
-[Core_Audio_Driver_Host setListener:];
-[Core_Audio_Driver_Host endpoint];
-[Core_Audio_Driver_Host setConnection_to_driver:];
-[Core_Audio_Driver_Host set_invalidation_handler:];
-[Core_Audio_Driver_Host start_synchronous_messenger:client_id:nominal_sample_rate:io_buffer_frame_size:work_group_port:io_messenger:];
-[Core_Audio_Driver_Host start_io:client_info:];
-[Core_Audio_Driver_Host write_storage_settings:storage_data:reply:];
-[Core_Audio_Driver_Host setConnection_from_driver:];
-[Core_Audio_Driver_Host is_property_settable:out_settable:];
-[Core_Audio_Driver_Host unregister_buffer:];
-[Core_Audio_Driver_Host listener];
-[Core_Audio_Driver_Host remove_device_client:client_info:];
-[Core_Audio_Driver_Host setM_property_type_info:];
-[Core_Audio_Driver_Host object_properties_changed:properties_data:reply:];
-[Core_Audio_Driver_Host setDelegate:];
-[Core_Audio_Driver_Host get_property_data:qualifier_data_size:qualifier_data:data_size:out_data_size:out_data:];
-[Core_Audio_Driver_Host connection_to_driver];
-[Core_Audio_Driver_Host register_buffer:];
-[Core_Audio_Driver_Host setDriver_host_protocol:];
-[Core_Audio_Driver_Host driver_host_protocol];
-[Core_Audio_Driver_Host delegate];
-[Core_Audio_Driver_Host object_was_destroyed:];
-[Core_Audio_Driver_Host retain_reply_for_process_boost];
-[Core_Audio_Driver_Host destroy_device:];
-[Core_Audio_Driver_Host stop_synchronous_messenger:client_id:];
-[Core_Audio_Driver_Host initialize_driver:];
-[Core_Audio_Driver_Host add_device_client:client_info:];
-[Core_Audio_Driver_Host setM_invalidation_handler:];
-[Core_Audio_Driver_Host get_property_data_size:qualifier_data_size:qualifier_data:out_size:];
-[Core_Audio_Driver_Host init_with_delegate:];
-[Core_Audio_Driver_Host connection_from_driver];
-[Core_Audio_Driver_Host request_config_change:change_action:change_token:reply:];
-[Core_Audio_Driver_Host delete_storage_settings:reply:];
-[Core_Audio_Driver_Host perform_device_configuration_change:action:change:];
-[Core_Audio_Driver_Host set_property_data:qualifier_data_size:qualifier_data:data_size:data:];
-[Core_Audio_Driver_Host create_device:client_info:out_object_id:];
-[Core_Audio_Driver_Host copy_storage_settings:reply:];
-[Core_Audio_Driver_Host abort_device_configuration_change:action:change:];
-[Core_Audio_Driver_Host driver_protocol];
-[Core_Audio_Driver_Host setDriver_endpoint:];
-[Core_Audio_Driver_Host has_property:out_has_property:];
-[Core_Audio_Driver_Host driver_endpoint];
-[Core_Audio_Driver_Host m_property_type_info];
-[Core_Audio_Driver_Host setDriver_protocol:];
```
