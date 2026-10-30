# `Core_Audio_Driver`

- Image: [`/System/Library/Frameworks/CoreAudio.framework/CoreAudio`](../userland/System__Library__Frameworks__CoreAudio.framework__CoreAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`, `Core_Audio_Driver_Protocol`
- 14 instance variables, 18 properties, 58 instance methods, 0 class methods

## Instance variables

```
@"Core_Audio_Driver_Host_Proxy" _driver_host_proxy;
@"NSXPCListener" _listener;
@"NSXPCListenerEndpoint" _endpoint;
^^{AudioServerPlugInDriverInterface} _asp_interface;
^{AudioServerPlugInHostInterface=^?^?^?^?^?} _host_interface;
@"NSObject<OS_dispatch_queue>" _concurrent_queue;
@? _process_boost_reply;
{shared_ptr<caulk::mach::unfair_lock>="__ptr_"^{unfair_lock}"__cntrl_"^{__shared_weak_count}} _config_change_info_lock;
{shared_ptr<std::map<unsigned long long, void *>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} _config_change_info_map;
{shared_ptr<Property_Type_Info>="__ptr_"^{Property_Type_Info}"__cntrl_"^{__shared_weak_count}} _m_custom_property_type_cache;
{shared_ptr<caulk::mach::unfair_lock>="__ptr_"^{unfair_lock}"__cntrl_"^{__shared_weak_count}} _io_receiver_lock;
{shared_ptr<std::unordered_map<AMCP::Portal::IPC::io_messenger_id_t, std::shared_ptr<AMCP::Portal::IPC::IO_Receiver>>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} _io_receivers;
{shared_ptr<std::vector<std::pair<AMCP::Portal::IPC::shared_buffer_info_t, applesauce::xpc::dict>>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} _io_buffer_list;
{function<void ()>="__f_"{__value_func<void ()>="__buf_"(type="__data"[24C])"__f_"^v}} _m_invalidation_handler;
```

## Properties

```
@property (T@"Core_Audio_Driver_Host_Proxy",&,N,V_driver_host_proxy) driver_host_proxy;
@property (T@"NSXPCListener",&,N,V_listener) listener;
@property (T@"NSXPCListenerEndpoint",&,N,V_endpoint) endpoint;
@property (T^^{AudioServerPlugInDriverInterface},N,V_asp_interface) asp_interface;
@property (T^{AudioServerPlugInHostInterface=^?^?^?^?^?},N,V_host_interface) host_interface;
@property (T{shared_ptr<caulk::mach::unfair_lock>=^{unfair_lock}^{__shared_weak_count}},R,N,V_config_change_info_lock) config_change_info_lock;
@property (T{shared_ptr<std::map<unsigned long long, void *>>=^v^{__shared_weak_count}},N,V_config_change_info_map) config_change_info_map;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_concurrent_queue) concurrent_queue;
@property (T{shared_ptr<Property_Type_Info>=^{Property_Type_Info}^{__shared_weak_count}},N,V_m_custom_property_type_cache) m_property_type_info;
@property (T@?,C,N,V_process_boost_reply) process_boost_reply;
@property (T{shared_ptr<std::unordered_map<AMCP::Portal::IPC::io_messenger_id_t, std::shared_ptr<AMCP::Portal::IPC::IO_Receiver>>>=^v^{__shared_weak_count}},N,V_io_receivers) io_receivers;
@property (T{shared_ptr<std::vector<std::pair<AMCP::Portal::IPC::shared_buffer_info_t, applesauce::xpc::dict>>>=^v^{__shared_weak_count}},N,V_io_buffer_list) io_buffer_list;
@property (T{shared_ptr<caulk::mach::unfair_lock>=^{unfair_lock}^{__shared_weak_count}},N,V_io_receiver_lock) io_receiver_lock;
@property (T{function<void ()>={__value_func<void ()>=(type=[24C])^v}},N,V_m_invalidation_handler) m_invalidation_handler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[Core_Audio_Driver setHost_interface:];
-[Core_Audio_Driver abort_device_configuration_change:action:change:reply:];
-[Core_Audio_Driver driver_host_proxy];
-[Core_Audio_Driver setProcess_boost_reply:];
-[Core_Audio_Driver io_buffer_list];
-[Core_Audio_Driver is_property_settable:reply:];
-[Core_Audio_Driver retain_reply_for_process_boost:];
-[Core_Audio_Driver process_boost_reply];
-[Core_Audio_Driver setEndpoint:];
-[Core_Audio_Driver start_io:client_id:reply:];
-[Core_Audio_Driver listener:shouldAcceptNewConnection:];
-[Core_Audio_Driver release_unpacked_cf_objects:qualifier_data:data_type:data:];
-[Core_Audio_Driver init];
-[Core_Audio_Driver io_receiver_lock];
-[Core_Audio_Driver setIo_receiver_lock:];
-[Core_Audio_Driver setConcurrent_queue:];
-[Core_Audio_Driver start_synchronous_messenger:client_id:nominal_sample_rate:io_buffer_frame_size:work_group_port:io_messenger:reply:];
-[Core_Audio_Driver dealloc];
-[Core_Audio_Driver m_invalidation_handler];
-[Core_Audio_Driver setIo_buffer_list:];
-[Core_Audio_Driver unregister_io_buffer:reply:];
-[Core_Audio_Driver setListener:];
-[Core_Audio_Driver get_property_data:qualifier:data_size:reply:];
-[Core_Audio_Driver endpoint];
-[Core_Audio_Driver concurrent_queue];
-[Core_Audio_Driver init_driver_interface:invalidation_handler:];
-[Core_Audio_Driver setDriver_host_proxy:];
-[Core_Audio_Driver destroy_io_receiver:];
-[Core_Audio_Driver setConfig_change_info_map:];
-[Core_Audio_Driver stop_synchronous_messenger:client_id:reply:];
-[Core_Audio_Driver handle_register_buffer:];
-[Core_Audio_Driver listener];
-[Core_Audio_Driver io_receivers];
-[Core_Audio_Driver set_property_data:qualifier:data:reply:];
-[Core_Audio_Driver create_device:client_id:process_id:is_native_endianess:bundle_id:reply:];
-[Core_Audio_Driver stop_io:client_id:reply:];
-[Core_Audio_Driver setM_property_type_info:];
-[Core_Audio_Driver get_property_data_size:qualifier:reply:];
-[Core_Audio_Driver handle_unregister_buffer:];
-[Core_Audio_Driver config_change_info_lock];
-[Core_Audio_Driver has_property:reply:];
-[Core_Audio_Driver add_device_client:client_id:process_id:is_native_endianess:bundle_id:reply:];
-[Core_Audio_Driver destroy_device:reply:];
-[Core_Audio_Driver setAsp_interface:];
-[Core_Audio_Driver destroy_io_receiver:client_id:];
-[Core_Audio_Driver initialize:reply:];
-[Core_Audio_Driver register_io_buffer:reply:];
-[Core_Audio_Driver create_and_start_io_receiver:client_id:nominal_sample_rate:io_buffer_frame_size:work_group_port:io_messenger:];
-[Core_Audio_Driver asp_interface];
-[Core_Audio_Driver host_interface];
-[Core_Audio_Driver remove_device_client:client_id:process_id:is_native_endianess:bundle_id:reply:];
-[Core_Audio_Driver setM_invalidation_handler:];
-[Core_Audio_Driver config_change_info_map];
-[Core_Audio_Driver store_change_info:for_token:];
-[Core_Audio_Driver object_was_destroyed:reply:];
-[Core_Audio_Driver setIo_receivers:];
-[Core_Audio_Driver m_property_type_info];
-[Core_Audio_Driver perform_device_configuration_change:action:change:reply:];
```
