# `Remote_Driver_Host_Delegate`

- Image: [`/System/Library/Frameworks/CoreAudio.framework/CoreAudio`](../userland/System__Library__Frameworks__CoreAudio.framework__CoreAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `Core_Audio_Driver_Host_Callback_Delegate`
- 1 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
{shared_ptr<HALS_UCRemotePlugIn>="__ptr_"^{HALS_UCRemotePlugIn}"__cntrl_"^{__shared_weak_count}} _remote_plugin;
```

## Properties

```
@property (T{shared_ptr<HALS_UCRemotePlugIn>=^{HALS_UCRemotePlugIn}^{__shared_weak_count}},N,V_remote_plugin) remote_plugin;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[Remote_Driver_Host_Delegate teardown];
-[Remote_Driver_Host_Delegate object_properties_changed:data:];
-[Remote_Driver_Host_Delegate copy_storage_settings:];
-[Remote_Driver_Host_Delegate delete_storage_settings:];
-[Remote_Driver_Host_Delegate init_with_remote_plugin:];
-[Remote_Driver_Host_Delegate remote_plugin];
-[Remote_Driver_Host_Delegate request_config_change:change_action:change_token:];
-[Remote_Driver_Host_Delegate setRemote_plugin:];
-[Remote_Driver_Host_Delegate write_storage_settings:storage_data:];
```
