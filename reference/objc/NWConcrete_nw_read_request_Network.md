# `NWConcrete_nw_read_request`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_read_request`
- 26 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NWConcrete_nw_read_request" next;
@"NWConcrete_nw_read_request" tail;
@? data_completion;
@? file_handler;
@? data_multiple_completion;
@? buffer_completion;
@"NWConcrete_nw_connection" connection;
I qos_class;
i variant;
Q min;
Q max;
Q progress;
@"NSObject<OS_nw_fd_wrapper>" fd;
^v progress_timer_source;
I progress_msecs;
* buffer;
@"NSObject<OS_dispatch_data>" data;
@"NSObject<OS_nw_content_context>" context;
@"NSObject<OS_nw_content_context>" repliable_message;
@"NSObject<OS_nw_error>" error;
@"NSObject<OS_nw_array>" read_array;
@"NSObject<OS_nw_array>" context_array;
b1 reported;
b1 is_complete;
b1 file_progress_started;
b1 file_finished;
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
-[NWConcrete_nw_read_request init];
-[NWConcrete_nw_read_request dealloc];
-[NWConcrete_nw_read_request description];
```
