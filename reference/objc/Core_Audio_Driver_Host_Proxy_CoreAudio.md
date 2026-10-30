# `Core_Audio_Driver_Host_Proxy`

- Image: [`/System/Library/Frameworks/CoreAudio.framework/CoreAudio`](../userland/System__Library__Frameworks__CoreAudio.framework__CoreAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`
- 7 instance variables, 11 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSXPCConnection" _connection_to_host;
{DictionaryRef="mObject"{ObjectRef<const __CFDictionary *>="mCFObject"^{__CFDictionary}}} _driver_storage;
@"Core_Audio_Driver" _driver;
Q _current_config_change_token;
{shared_ptr<Host_Interface>="__ptr_"^{Host_Interface}"__cntrl_"^{__shared_weak_count}} _host_interface;
{shared_ptr<caulk::mach::unfair_lock>="__ptr_"^{unfair_lock}"__cntrl_"^{__shared_weak_count}} _driver_storage_lock;
{shared_ptr<caulk::mach::unfair_lock>="__ptr_"^{unfair_lock}"__cntrl_"^{__shared_weak_count}} _config_change_lock;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_connection_to_host) connection_to_host;
@property (T{shared_ptr<Host_Interface>=^{Host_Interface}^{__shared_weak_count}},R,N,V_host_interface) host_interface;
@property (T{shared_ptr<caulk::mach::unfair_lock>=^{unfair_lock}^{__shared_weak_count}},R,N,V_driver_storage_lock) driver_storage_lock;
@property (T{DictionaryRef={ObjectRef<const __CFDictionary *>=^{__CFDictionary}}},N,V_driver_storage) driver_storage;
@property (T@"Core_Audio_Driver",&,N,V_driver) driver;
@property (T{shared_ptr<caulk::mach::unfair_lock>=^{unfair_lock}^{__shared_weak_count}},R,N,V_config_change_lock) config_change_lock;
@property (TQ,N,V_current_config_change_token) current_config_change_token;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[Core_Audio_Driver_Host_Proxy driver];
-[Core_Audio_Driver_Host_Proxy init];
-[Core_Audio_Driver_Host_Proxy setDriver:];
-[Core_Audio_Driver_Host_Proxy host_interface];
-[Core_Audio_Driver_Host_Proxy setCurrent_config_change_token:];
-[Core_Audio_Driver_Host_Proxy init_with_host_endpoint:driver:];
-[Core_Audio_Driver_Host_Proxy config_change_lock];
-[Core_Audio_Driver_Host_Proxy connection_to_host];
-[Core_Audio_Driver_Host_Proxy copy_from_driver_storage:];
-[Core_Audio_Driver_Host_Proxy current_config_change_token];
-[Core_Audio_Driver_Host_Proxy delete_from_driver_storage:];
-[Core_Audio_Driver_Host_Proxy driver_properties_changed:properties_data:];
-[Core_Audio_Driver_Host_Proxy driver_request_config_change:change_action:change_info:];
-[Core_Audio_Driver_Host_Proxy driver_storage];
-[Core_Audio_Driver_Host_Proxy driver_storage_lock];
-[Core_Audio_Driver_Host_Proxy get_host_interface];
-[Core_Audio_Driver_Host_Proxy setConnection_to_host:];
-[Core_Audio_Driver_Host_Proxy setDriver_storage:];
-[Core_Audio_Driver_Host_Proxy write_to_driver_storage:property_list:];
```
