# `Core_Audio_Driver_Registrar`

- Image: [`/System/Library/Frameworks/CoreAudio.framework/CoreAudio`](../userland/System__Library__Frameworks__CoreAudio.framework__CoreAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`, `Core_Audio_Driver_Registrar_Protocol`
- 2 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
^v _registrar;
{shared_ptr<std::vector<Registrar_Connection_Info>>="__ptr_"^v"__cntrl_"^{__shared_weak_count}} _connection_infos;
```

## Properties

```
@property (T^v,N,V_registrar) registrar;
@property (T{shared_ptr<std::vector<Registrar_Connection_Info>>=^v^{__shared_weak_count}},N,V_connection_infos) connection_infos;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[Core_Audio_Driver_Registrar listener:shouldAcceptNewConnection:];
-[Core_Audio_Driver_Registrar init];
-[Core_Audio_Driver_Registrar registrar];
-[Core_Audio_Driver_Registrar connection_infos];
-[Core_Audio_Driver_Registrar register_driver:bundle_url:bundle_id:cpu_type:driver_type:reply:];
-[Core_Audio_Driver_Registrar setConnection_infos:];
-[Core_Audio_Driver_Registrar setRegistrar:];
```
