# `NWConcrete_nw_interface_status_monitor`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_interface_status_monitor`
- 10 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_nw_interface>" interface;
@"NSObject<OS_nw_channel>" channel;
@? packet_handler;
@"NSObject<OS_dispatch_queue>" packet_handler_queue;
@? update_handler;
@"NSObject<OS_dispatch_queue>" update_handler_queue;
^v channel_event_source;
^v interface_advisory_source;
b1 cancelled;
b7 __pad_bits;
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
-[NWConcrete_nw_interface_status_monitor init];
-[NWConcrete_nw_interface_status_monitor dealloc];
-[NWConcrete_nw_interface_status_monitor description];
```
