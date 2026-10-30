# `NWConcrete_nw_connection_progress_report`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_connection_progress_report`
- 9 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
i phase;
Q connection_id;
I rtt_estimate;
I completion_estimate;
I elapsed_time_ms;
I last_attempt_started_ms;
S attempt_count;
i stall_reason;
C link_quality;
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
-[NWConcrete_nw_connection_progress_report init];
-[NWConcrete_nw_connection_progress_report dealloc];
-[NWConcrete_nw_connection_progress_report description];
```
