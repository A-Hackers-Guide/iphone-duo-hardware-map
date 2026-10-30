# `NWConcrete_nw_write_request`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_write_request`
- 21 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NWConcrete_nw_write_request" next;
@"NWConcrete_nw_write_request" tail;
@? completion;
@? file_handler;
@"NWConcrete_nw_connection" connection;
I qos_class;
@"NSObject<OS_dispatch_data>" data;
@"NSObject<OS_nw_content_context>" context;
@"NSObject<OS_nw_fd_wrapper>" fd;
^v progress_timer_source;
I progress_msecs;
Q num_bytes;
@"NSObject<OS_nw_content_context>" original_message;
Q consumed_bytes;
d relative_priority;
b1 complete;
b1 reported;
b1 idempotent;
b1 write_close;
b1 file_finished;
b1 file_progress_started;
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
-[NWConcrete_nw_write_request init];
-[NWConcrete_nw_write_request dealloc];
-[NWConcrete_nw_write_request description];
```
