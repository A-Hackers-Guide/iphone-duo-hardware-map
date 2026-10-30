# `Core_Audio_Driver_Service_Client`

- Image: [`/System/Library/Frameworks/CoreAudio.framework/CoreAudio`](../userland/System__Library__Frameworks__CoreAudio.framework__CoreAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`, `Core_Audio_Driver_Service_Client_Protocol`
- 8 instance variables, 12 properties, 27 instance methods, 1 class methods

## Instance variables

```
@"NSXPCConnection" _connection_to_driver_service;
@"<Core_Audio_Driver_Service_Client_Callback_Delegate>" _delegate;
@"NSXPCListener" _listener;
@"NSXPCListenerEndpoint" _endpoint;
@"NSXPCConnection" _connection_from_driver_service;
{shared_ptr<std::function<void (std::shared_ptr<Driver_File>)>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} _driver_service_undertaker;
{shared_ptr<Driver_File>="__ptr_"^{Driver_File}"__cntrl_"^{__shared_weak_count}} _driver_file;
{Dispatch_Queue="fObj"{object="fObj"@"NSObject<OS_dispatch_object>"}"__weak_this_"{weak_ptr<AMCP::Utility::Dispatch_Queue>="__ptr_"^{Dispatch_Queue}"__cntrl_"^{__shared_weak_count}}"m_workloop"{Workloop="fObj"{object="fObj"@"NSObject<OS_dispatch_object>"}}"m_flush_started"{atomic<bool>="__a_"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>="__a_value"AB}}"m_something_dispatched_after_flush"{atomic<bool>="__a_"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>="__a_value"AB}}"m_port_death_list"{vector<AMCP::Utility::Dispatch_Queue::Event_Source, std::allocator<AMCP::Utility::Dispatch_Queue::Event_Source>>="__begin_"^{Event_Source}"__end_"^{Event_Source}""{?="__cap_"^{Event_Source}}}"m_port_death_list_mutex"{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}}"m_mach_port_receiver_list"{vector<AMCP::Utility::Dispatch_Queue::Event_Source, std::allocator<AMCP::Utility::Dispatch_Queue::Event_Source>>="__begin_"^{Event_Source}"__end_"^{Event_Source}""{?="__cap_"^{Event_Source}}}"m_mach_port_receiver_list_mutex"{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}}"m_mig_server_list"{vector<AMCP::Utility::Dispatch_Queue::Event_Source, std::allocator<AMCP::Utility::Dispatch_Queue::Event_Source>>="__begin_"^{Event_Source}"__end_"^{Event_Source}""{?="__cap_"^{Event_Source}}}"m_mig_server_list_mutex"{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}}"m_after_count"{atomic<long long>="__a_"{__cxx_atomic_impl<long long, std::__cxx_atomic_base_impl<long long>>="__a_value"Aq}}"m_after_count_semaphore"@"NSObject<OS_dispatch_semaphore>""m_dispatch_group"{optional<applesauce::dispatch::group>=""(?="__null_state_"c"__val_"{group="fObj"{object="fObj"@"NSObject<OS_dispatch_object>"}})"__engaged_"B}} _queue;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_connection_to_driver_service) connection_to_driver_service;
@property (T@"NSXPCConnection",&,N,V_connection_from_driver_service) connection_from_driver_service;
@property (T@"NSXPCListener",&,N,V_listener) listener;
@property (T@"NSXPCListenerEndpoint",&,N,V_endpoint) endpoint;
@property (T{Dispatch_Queue={object=@}{weak_ptr<AMCP::Utility::Dispatch_Queue>=^{Dispatch_Queue}^{__shared_weak_count}}{Workloop={object=@}}{atomic<bool>={__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>=AB}}{atomic<bool>={__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>=AB}}{vector<AMCP::Utility::Dispatch_Queue::Event_Source, std::allocator<AMCP::Utility::Dispatch_Queue::Event_Source>>=^{Event_Source}^{Event_Source}{?=^{Event_Source}}}{mutex={_opaque_pthread_mutex_t=q[56c]}}{vector<AMCP::Utility::Dispatch_Queue::Event_Source, std::allocator<AMCP::Utility::Dispatch_Queue::Event_Source>>=^{Event_Source}^{Event_Source}{?=^{Event_Source}}}{mutex={_opaque_pthread_mutex_t=q[56c]}}{vector<AMCP::Utility::Dispatch_Queue::Event_Source, std::allocator<AMCP::Utility::Dispatch_Queue::Event_Source>>=^{Event_Source}^{Event_Source}{?=^{Event_Source}}}{mutex={_opaque_pthread_mutex_t=q[56c]}}{atomic<long long>={__cxx_atomic_impl<long long, std::__cxx_atomic_base_impl<long long>>=Aq}}@{optional<applesauce::dispatch::group>=(?=c{group={object=@}})B}},N,V_queue) queue;
@property (T@"<Core_Audio_Driver_Service_Client_Callback_Delegate>",&,N,V_delegate) delegate;
@property (T{shared_ptr<std::function<void (std::shared_ptr<Driver_File>)>>=^v^{__shared_weak_count}},N,V_driver_service_undertaker) driver_service_undertaker;
@property (T{shared_ptr<Driver_File>=^{Driver_File}^{__shared_weak_count}},N,V_driver_file) driver_file;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[Core_Audio_Driver_Service_Client get_driver_name_list:];
```

## Instance methods

```
-[Core_Audio_Driver_Service_Client setEndpoint:];
-[Core_Audio_Driver_Service_Client listener:shouldAcceptNewConnection:];
-[Core_Audio_Driver_Service_Client init];
-[Core_Audio_Driver_Service_Client dealloc];
-[Core_Audio_Driver_Service_Client setListener:];
-[Core_Audio_Driver_Service_Client endpoint];
-[Core_Audio_Driver_Service_Client queue];
-[Core_Audio_Driver_Service_Client listener];
-[Core_Audio_Driver_Service_Client invalidate];
-[Core_Audio_Driver_Service_Client setDelegate:];
-[Core_Audio_Driver_Service_Client delegate];
-[Core_Audio_Driver_Service_Client setQueue:];
-[Core_Audio_Driver_Service_Client send_endpoint_to_driver_service];
-[Core_Audio_Driver_Service_Client setDriver_file:];
-[Core_Audio_Driver_Service_Client connect_to_driver_service:];
-[Core_Audio_Driver_Service_Client connection_from_driver_service];
-[Core_Audio_Driver_Service_Client connection_to_driver_service];
-[Core_Audio_Driver_Service_Client deferred_driver_loaded:reply:];
-[Core_Audio_Driver_Service_Client driver_file];
-[Core_Audio_Driver_Service_Client driver_service_undertaker];
-[Core_Audio_Driver_Service_Client get_lazy_connection:];
-[Core_Audio_Driver_Service_Client init_with_driver_service_undertaker:];
-[Core_Audio_Driver_Service_Client load_driver:driver_endpoint:];
-[Core_Audio_Driver_Service_Client setConnection_from_driver_service:];
-[Core_Audio_Driver_Service_Client setConnection_to_driver_service:];
-[Core_Audio_Driver_Service_Client setDriver_service_undertaker:];
-[Core_Audio_Driver_Service_Client tell_driver_service_to_exit];
```
